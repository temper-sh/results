#!/usr/bin/env python3
"""Validate the publication-facing results repository."""

from __future__ import annotations

import csv
import hashlib
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
REQUIRED = (
    "README.md",
    "PHILOSOPHY.md",
    "GUIDE.md",
    "CURRENT.md",
    "CONSIDERED.md",
    "METHOD.md",
    "machines/README.md",
    "details/README.md",
)
EXPECTED_EVIDENCE_HASHES = {
    "details/2026-08-20-qwen38-qualified-profiles/context-evidence.json":
        "203b9c4820c9d7e954c9b2062068ea92d48b9538672d0a0d993d31eda338fda5",
    "details/2026-08-20-qwen38-qualified-profiles/dynamic-evidence.json":
        "bdbf830f7adc22c707c825c6e202fb9ed6b76f14ddc358016e5a05a82d1cb573",
    "details/2026-08-20-qwen38-qualified-profiles/engine-evidence.json":
        "ec1616590c875c578358976ec99d262172bb5f897c463cb8e78b8f1778194560",
    "details/2026-08-21-muse-glimmer-lab/evidence.json":
        "004c479202abca803ba14b733db17df927ca66329b2404cae2aa7bc721d0a862",
}
PRIVATE_PATH_PATTERNS = (
    "/Users/",
    "/home/",
    "file://",
    "C:\\Users\\",
)


def check_required(errors: list[str]) -> None:
    for relative in REQUIRED:
        if not (ROOT / relative).is_file():
            errors.append(f"missing required file: {relative}")


def check_json(errors: list[str]) -> None:
    for path in sorted(ROOT.rglob("*.json")):
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
            errors.append(f"{path.relative_to(ROOT)}: invalid JSON: {exc}")

    for relative, expected in EXPECTED_EVIDENCE_HASHES.items():
        path = ROOT / relative
        if not path.is_file():
            errors.append(f"missing hashed evidence: {relative}")
            continue
        actual = hashlib.sha256(path.read_bytes()).hexdigest()
        if actual != expected:
            errors.append(
                f"{relative}: SHA-256 {actual}, expected {expected}"
            )


def check_tsv(errors: list[str]) -> None:
    for path in sorted(ROOT.rglob("*.tsv")):
        with path.open(encoding="utf-8", newline="") as handle:
            rows = list(csv.reader(handle, delimiter="\t"))
        relative = path.relative_to(ROOT)
        if len(rows) < 2:
            errors.append(f"{relative}: needs a header and at least one row")
            continue
        width = len(rows[0])
        if width < 2 or len(set(rows[0])) != width:
            errors.append(f"{relative}: invalid or duplicate header columns")
        for line_number, row in enumerate(rows[1:], start=2):
            if len(row) != width:
                errors.append(
                    f"{relative}:{line_number}: {len(row)} columns, expected {width}"
                )


def check_markdown(errors: list[str]) -> None:
    for path in sorted(ROOT.rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        relative = path.relative_to(ROOT)

        for marker in PRIVATE_PATH_PATTERNS:
            if marker in text:
                errors.append(f"{relative}: publication-private path marker {marker!r}")

        for match in LINK.finditer(text):
            target = match.group(1).strip()
            if target.startswith("<") and target.endswith(">"):
                target = target[1:-1]
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            target = unquote(target.split("#", 1)[0])
            if not target:
                continue
            destination = (path.parent / target).resolve()
            try:
                destination.relative_to(ROOT)
            except ValueError:
                errors.append(f"{relative}: link escapes repository: {target}")
                continue
            if not destination.exists():
                errors.append(f"{relative}: broken local link: {target}")


def check_tldr(path: Path, errors: list[str]) -> None:
    lines = path.read_text(encoding="utf-8").splitlines()
    relative = path.relative_to(ROOT)
    try:
        line_number = lines.index("## TL;DR") + 1
    except ValueError:
        errors.append(f"{relative}: missing plain-language ## TL;DR")
        return
    if line_number > 15:
        errors.append(
            f"{relative}:{line_number}: TL;DR must appear within first 15 lines"
        )


def check_reader_contract(errors: list[str]) -> None:
    detail_pages = sorted((ROOT / "details").glob("*/README.md"))
    machine_pages = sorted(
        path for path in (ROOT / "machines").glob("*.md")
        if path.name != "README.md"
    )
    for path in detail_pages + machine_pages:
        check_tldr(path, errors)


def main() -> int:
    errors: list[str] = []
    check_required(errors)
    check_json(errors)
    check_tsv(errors)
    check_markdown(errors)
    check_reader_contract(errors)

    if errors:
        for error in errors:
            print(f"FAIL {error}")
        print(f"\n{len(errors)} validation error(s)")
        return 1

    markdown_count = sum(1 for _ in ROOT.rglob("*.md"))
    tsv_count = sum(1 for _ in ROOT.rglob("*.tsv"))
    json_count = sum(1 for _ in ROOT.rglob("*.json"))
    print(
        f"PASS {markdown_count} Markdown, {tsv_count} TSV, "
        f"{json_count} JSON files"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
