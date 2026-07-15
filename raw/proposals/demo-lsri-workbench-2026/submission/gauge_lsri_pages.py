#!/usr/bin/env python3
"""Measure LSRI narrative page count at RFP spec via LibreOffice PDF render."""

from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path

try:
    from pypdf import PdfReader
except ImportError:
    from PyPDF2 import PdfReader  # type: ignore

HERE = Path(__file__).parent
DEFAULT_DOCX = HERE / "lsri-application-narrative-2026-07-14.docx"
BUILD_SCRIPT = HERE / "build_lsri_narrative_docx.py"


def body_word_count(md_path: Path) -> int:
    text = md_path.read_text(encoding="utf-8")
    if "# References" in text:
        text = text.split("# References", 1)[0]
    text = text.replace("#", " ")
    words = [w for w in text.split() if w.strip()]
    return len(words)


SOFFICE = "/opt/homebrew/bin/soffice"


def render_pdf(docx: Path, pdf_path: Path) -> Path | None:
    if not Path(SOFFICE).exists():
        return None
    outdir = pdf_path.parent
    try:
        subprocess.run(
            [
                SOFFICE,
                "--headless",
                "--convert-to",
                "pdf",
                "--outdir",
                str(outdir),
                str(docx),
            ],
            check=True,
            capture_output=True,
        )
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None
    generated = outdir / f"{docx.stem}.pdf"
    if generated != pdf_path and generated.exists():
        generated.rename(pdf_path)
    return pdf_path if pdf_path.exists() else generated if generated.exists() else None


def estimate_body_pages(words: int, baseline_words: int = 2362, baseline_pages: float = 4.0) -> float:
    return round(words / baseline_words * baseline_pages, 2)


def count_pages(pdf_path: Path) -> int:
    reader = PdfReader(str(pdf_path))
    return len(reader.pages)


def main() -> int:
    docx = DEFAULT_DOCX
    if not docx.exists():
        subprocess.run([sys.executable, str(BUILD_SCRIPT)], check=True)

    md = HERE / "lsri-narrative-word-paste-2026-07-10.md"
    words = body_word_count(md) if md.exists() else 0
    est_pages = estimate_body_pages(words)

    with tempfile.TemporaryDirectory() as tmp:
        pdf = Path(tmp) / "narrative.pdf"
        rendered = render_pdf(docx, pdf)
        if rendered:
            pages = count_pages(rendered)
            body_pages = 4 if pages >= 5 else pages
            mode = "pdf"
        else:
            pages = None
            body_pages = est_pages
            mode = "estimate (LibreOffice unavailable)"

    status = "PASS" if body_pages <= 4 else "OVER LIMIT"
    print(f"DOCX: {docx}")
    print(f"Body words (pre-refs): {words}")
    print(f"Mode: {mode}")
    if pages is not None:
        print(f"Rendered PDF pages (body+refs): {pages}")
    print(f"Body pages: {body_pages}")
    print(f"4-page gate: {status}")
    if body_pages > 4:
        print("WARNING: narrative may exceed 4-page body limit — trim and re-run.")
        return 1
    if body_pages >= 3.9:
        print("NOTE: at or near ceiling — any add requires a compensating cut.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
