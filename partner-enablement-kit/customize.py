#!/usr/bin/env python3
"""Stamp the Constitutional Enablement Kit with an organization's branding.

This script reads ``brand.yaml`` and produces a branded copy of the kit in
``dist/``. The kit's source files are never modified, which keeps a fork cleanly
mergeable with upstream constitution updates: pull the update, re-run this
script, and your branding is re-applied on top.

What it does to each Markdown document:
  1. Resolves ``{{TOKEN}}`` placeholders from the brand config.
  2. Applies whole-word ``term_swaps`` from the brand config.
  3. Injects a branded header (framework, organization, version) and a footer.

Usage:
    python3 customize.py                 # build branded copy into ./dist
    python3 customize.py --out build     # build into ./build instead
    python3 customize.py --check         # verify no unresolved {{TOKENS}} remain
    python3 customize.py --no-header     # skip header/footer injection

No third-party libraries are required; ``brand.yaml`` is parsed directly as a
small, flat YAML subset (scalars, simple lists, and one-level maps).
"""

from __future__ import annotations

import argparse
import re
import shutil
import sys
from pathlib import Path

KIT_ROOT = Path(__file__).resolve().parent
BRAND_FILE = KIT_ROOT / "brand.yaml"
DEFAULT_OUT = KIT_ROOT / "dist"

# Directories that are tooling/output rather than kit content.
EXCLUDED_DIRS = {"dist", "build", "assets", "__pycache__", ".git"}

TOKEN_RE = re.compile(r"\{\{\s*([A-Z0-9_]+)\s*\}\}")


# ── brand.yaml parsing (flat YAML subset, stdlib only) ──────────────────────

def _strip_quotes(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
        return value[1:-1]
    return value


def _strip_comment(raw: str) -> str:
    """Remove a trailing ``#`` comment, but not a ``#`` inside quotes (e.g. hex colors)."""
    quote = None
    for i, ch in enumerate(raw):
        if quote:
            if ch == quote:
                quote = None
        elif ch in "\"'":
            quote = ch
        elif ch == "#":
            return raw[:i]
    return raw


def parse_brand(path: Path) -> dict:
    """Parse the supported flat-YAML subset: scalars, simple lists, 1-level maps."""
    if not path.exists():
        raise FileNotFoundError(f"Brand config not found: {path}")

    data: dict = {}
    current_key: str | None = None
    current_kind: str | None = None  # "list" or "map"

    for raw in path.read_text(encoding="utf-8").splitlines():
        # Drop comments (quote-aware, so hex colors survive) and blank lines.
        line = _strip_comment(raw).rstrip()
        if not line.strip():
            continue

        indented = line[0] in " \t"
        stripped = line.strip()

        if indented and current_key is not None:
            # Continuation of a list or map under current_key.
            if stripped.startswith("- "):
                data.setdefault(current_key, [])
                if not isinstance(data[current_key], list):
                    data[current_key] = []
                data[current_key].append(_strip_quotes(stripped[2:]))
                current_kind = "list"
            elif ":" in stripped:
                k, v = stripped.split(":", 1)
                if not isinstance(data.get(current_key), dict):
                    data[current_key] = {}
                data[current_key][k.strip()] = _strip_quotes(v)
                current_kind = "map"
            continue

        # Top-level key.
        if ":" not in stripped:
            continue
        key, value = stripped.split(":", 1)
        key = key.strip()
        value = value.strip()
        current_key = key
        current_kind = None
        if value == "":
            # A nested list/map will follow on indented lines.
            data[key] = None
        else:
            data[key] = _strip_quotes(value)

    # Normalize empty containers left as None.
    for k, v in list(data.items()):
        if v is None:
            data[k] = ""
    return data


# ── transformation ──────────────────────────────────────────────────────────

def build_token_map(brand: dict) -> dict:
    """Map {{TOKEN}} names to their resolved values from the brand config."""
    examples = brand.get("product_examples") or []
    first_example = examples[0] if isinstance(examples, list) and examples else ""
    return {
        "FRAMEWORK_NAME": brand.get("framework_name", ""),
        "ORG_NAME": brand.get("org_name", ""),
        "ACCELERATOR_NAME": brand.get("accelerator_name", ""),
        "ACCENT_COLOR": brand.get("accent_color", ""),
        "SECONDARY_COLOR": brand.get("secondary_color", ""),
        "VOICE": brand.get("voice", ""),
        "PRODUCT_EXAMPLE": first_example,
        "FOOTER": brand.get("footer", ""),
    }


def apply_tokens(text: str, token_map: dict) -> str:
    def repl(match: re.Match) -> str:
        name = match.group(1)
        return token_map.get(name, match.group(0))

    return TOKEN_RE.sub(repl, text)


def apply_term_swaps(text: str, swaps: dict) -> str:
    """Whole-word, case-preserving-ish replacement for vocabulary alignment."""
    if not swaps:
        return text
    for src, dst in swaps.items():
        if not src or src == dst:
            continue
        # Whole-word, case-insensitive; preserve capitalization of first letter.
        def repl(m: re.Match, dst=dst) -> str:
            word = m.group(0)
            if word[:1].isupper():
                return dst[:1].upper() + dst[1:]
            return dst
        text = re.sub(rf"\b{re.escape(src)}\b", repl, text, flags=re.IGNORECASE)
    return text


def header_block(brand: dict, version: str) -> str:
    fw = brand.get("framework_name", "Constitutional Enablement")
    org = brand.get("org_name", "")
    accent = brand.get("accent_color", "")
    logo = brand.get("logo_path", "")
    bits = [f"**{fw}**"]
    if org:
        bits.append(org)
    line = " — ".join(bits)
    note = []
    if version:
        note.append(f"Constitution {version}")
    if accent:
        note.append(f"`{accent}`")
    sub = " · ".join(note)
    logo_md = f"![logo]({logo})\n\n" if logo else ""
    return f"<!-- branded by customize.py -->\n{logo_md}{line}  \n*{sub}*\n\n---\n\n"


def footer_block(brand: dict) -> str:
    footer = brand.get("footer", "")
    return f"\n\n---\n\n*{footer}*\n" if footer else ""


def read_version() -> str:
    changelog = KIT_ROOT / "CHANGELOG.md"
    if not changelog.exists():
        return ""
    m = re.search(r"\[(\d+\.\d+\.\d+)\]", changelog.read_text(encoding="utf-8"))
    return f"v{m.group(1)}" if m else ""


def iter_markdown_files() -> list[Path]:
    files = []
    for path in KIT_ROOT.rglob("*.md"):
        if any(part in EXCLUDED_DIRS for part in path.relative_to(KIT_ROOT).parts):
            continue
        files.append(path)
    return sorted(files)


# ── commands ────────────────────────────────────────────────────────────────

def cmd_check(brand: dict) -> int:
    token_map = build_token_map(brand)
    orphans: list[str] = []
    for path in iter_markdown_files():
        text = path.read_text(encoding="utf-8")
        resolved = apply_tokens(text, token_map)
        for m in TOKEN_RE.finditer(resolved):
            rel = path.relative_to(KIT_ROOT)
            orphans.append(f"  {rel}: {{{{{m.group(1)}}}}}")
    if orphans:
        print("Unresolved tokens found:")
        print("\n".join(orphans))
        return 1
    print(f"OK — no unresolved tokens across {len(iter_markdown_files())} document(s).")
    return 0


def cmd_build(brand: dict, out_dir: Path, inject: bool) -> int:
    token_map = build_token_map(brand)
    swaps = brand.get("term_swaps") or {}
    version = read_version()

    if out_dir.exists():
        shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True)

    count = 0
    for path in iter_markdown_files():
        rel = path.relative_to(KIT_ROOT)
        text = path.read_text(encoding="utf-8")
        text = apply_tokens(text, token_map)
        text = apply_term_swaps(text, swaps)
        if inject:
            text = header_block(brand, version) + text + footer_block(brand)
        dest = out_dir / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(text, encoding="utf-8")
        count += 1

    # Copy assets (e.g., logo) if present so the branded copy is self-contained.
    assets = KIT_ROOT / "assets"
    if assets.exists():
        shutil.copytree(assets, out_dir / "assets", dirs_exist_ok=True)

    print(f"Built branded kit → {out_dir} ({count} document(s)).")
    if version:
        print(f"Constitution version: {version}")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--out", default=str(DEFAULT_OUT),
                        help="output directory for the branded copy (default: ./dist)")
    parser.add_argument("--check", action="store_true",
                        help="verify no unresolved {{TOKENS}} remain; do not build")
    parser.add_argument("--no-header", action="store_true",
                        help="do not inject the branded header/footer")
    parser.add_argument("--brand", default=str(BRAND_FILE),
                        help="path to brand config (default: ./brand.yaml)")
    args = parser.parse_args(argv)

    try:
        brand = parse_brand(Path(args.brand))
    except FileNotFoundError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    if args.check:
        return cmd_check(brand)
    return cmd_build(brand, Path(args.out), inject=not args.no_header)


if __name__ == "__main__":
    raise SystemExit(main())
