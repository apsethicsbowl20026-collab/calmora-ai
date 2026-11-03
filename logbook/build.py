#!/usr/bin/env python3
"""
Build the Calmora AI Project Logbook deliverables from a single source file.

    python3 logbook/build.py

Reads   : logbook/CALMORA-AI-Project-Logbook.md
Writes  : CALMORA-AI-Project-Logbook.docx   (editable, for the shared drive)
          CALMORA-AI-Project-Logbook.pdf    (submission-ready, mirrors the template)

The Markdown is deliberately simple. Supported block syntax:
  # / ## / ###              headings
  plain line                 a paragraph
  - item, "  - item"         bullet (one level per two leading spaces)
  1. item                    numbered item
  | a | b |                 table (first row = header, second row = |---|---|)
  > quoted line              callout box
  [PAGEBREAK]                page break

Inline syntax: **bold**, *italic*, `code`, [label](url), [[highlighted field]].
`[[...]]` fields are rendered with a yellow highlight in both documents so the
team can spot everything that still needs their real details.
"""

from __future__ import annotations

import os
import re
import xml.sax.saxutils as sax
from pathlib import Path

from docx import Document
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_COLOR_INDEX
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate, Frame, HRFlowable, KeepTogether, PageBreak, PageTemplate,
    Paragraph, Spacer, Table, TableStyle,
)

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
SRC = HERE / "CALMORA-AI-Project-Logbook.md"
DOCX = ROOT / "CALMORA-AI-Project-Logbook.docx"
PDF = ROOT / "CALMORA-AI-Project-Logbook.pdf"

INK = colors.HexColor("#142A22")
TEAL = colors.HexColor("#0E6A50")
MINT = colors.HexColor("#1FA879")
PALE = colors.HexColor("#EAF6F0")
PALE2 = colors.HexColor("#F5FAF7")
LINE = colors.HexColor("#C9DED3")
GREY = colors.HexColor("#5B6F66")
HIGHLIGHT = colors.HexColor("#FFF2A8")

FONT_DIR = Path("/usr/share/fonts/truetype/dejavu")
REG = FONT_DIR / "DejaVuSans.ttf"
BOLD = FONT_DIR / "DejaVuSans-Bold.ttf"
ITAL = FONT_DIR / "DejaVuSerif-Italic.ttf"

# ---------------------------------------------------------------------------
# 1. Parse the markdown into blocks
# ---------------------------------------------------------------------------

INLINE_RE = re.compile(
    r"\[\[(.+?)\]\]"          # 1: highlighted placeholder
    r"|\*\*(.+?)\*\*"        # 2: bold
    r"|\*(.+?)\*"            # 3: italic
    r"|`(.+?)`"              # 4: code
    r"|\[([^\]]+)\]\(([^)]+)\)"  # 5,6: link
)


def inline(text: str):
    """Return a list of (kind, text, extra) tokens."""
    out, pos = [], 0
    for m in INLINE_RE.finditer(text):
        if m.start() > pos:
            out.append(("plain", text[pos:m.start()], None))
        if m.group(1) is not None:
            out.append(("hl", "[[" + m.group(1) + "]]", None))
        elif m.group(2) is not None:
            out.append(("bold", m.group(2), None))
        elif m.group(3) is not None:
            out.append(("italic", m.group(3), None))
        elif m.group(4) is not None:
            out.append(("code", m.group(4), None))
        else:
            out.append(("link", m.group(5), m.group(6)))
        pos = m.end()
    if pos < len(text):
        out.append(("plain", text[pos:], None))
    return out or [("plain", text, None)]


def parse(lines):
    blocks, i, n = [], 0, len(lines)
    while i < n:
        raw = lines[i].rstrip("\n").rstrip()
        if not raw.strip():
            i += 1
            continue
        if raw.strip() == "[PAGEBREAK]":
            blocks.append({"t": "pagebreak"})
            i += 1
            continue
        if raw.strip() == "---":
            blocks.append({"t": "hr"})
            i += 1
            continue
        m = re.match(r"^(#{1,4})\s+(.*)$", raw)
        if m:
            blocks.append({"t": "h", "lvl": len(m.group(1)), "text": m.group(2)})
            i += 1
            continue
        if raw.lstrip().startswith("|"):
            rows = []
            while i < n and lines[i].rstrip("\n").rstrip().lstrip().startswith("|"):
                cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                if not all(re.fullmatch(r":?-{2,}:?", c or "") for c in cells):
                    rows.append(cells)
                i += 1
            blocks.append({"t": "table", "rows": rows})
            continue
        if raw.lstrip().startswith("> "):
            parts = []
            while i < n and lines[i].rstrip("\n").rstrip().lstrip().startswith(">"):
                parts.append(lines[i].strip().lstrip(">").strip())
                i += 1
            blocks.append({"t": "callout", "text": " ".join(parts)})
            continue
        bm = re.match(r"^(\s*)-\s+(.*)$", raw)
        if bm:
            blocks.append({"t": "bullet", "lvl": len(bm.group(1)) // 2, "text": bm.group(2)})
            i += 1
            continue
        nm = re.match(r"^\s*(\d+)\.\s+(.*)$", raw)
        if nm:
            blocks.append({"t": "number", "num": nm.group(1) + ".", "text": nm.group(2)})
            i += 1
            continue
        blocks.append({"t": "para", "text": raw.strip()})
        i += 1
    return blocks


# ---------------------------------------------------------------------------
# 2. Word (.docx)
# ---------------------------------------------------------------------------

def docx_shade(cell, fill):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), fill)
    tcPr.append(shd)


def docx_para_shade(p, fill):
    pPr = p._p.get_or_add_pPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:fill"), fill)
    pPr.append(shd)


def add_inline_runs(p, text, base=None, italic=False):
    for kind, val, extra in inline(text):
        r = p.add_run(val)
        if base:
            r.font.size = Pt(base)
        if kind == "bold":
            r.bold = True
        elif kind == "italic":
            r.italic = True
        elif kind == "code":
            r.font.name = "Consolas"
            r.font.size = Pt((base or 10.5) - 0.5)
            r.font.color.rgb = RGBColor(0x0E, 0x6A, 0x50)
        elif kind == "hl":
            r.font.highlight_color = WD_COLOR_INDEX.YELLOW
            r.bold = True
            r.font.color.rgb = RGBColor(0x8A, 0x5A, 0x00)
        elif kind == "link":
            r.font.color.rgb = RGBColor(0x0E, 0x6A, 0x50)
            r.underline = True
        if italic and kind == "plain":
            r.italic = True
    return p


def build_docx(blocks):
    doc = Document()
    sec = doc.sections[0]
    sec.top_margin = Cm(1.9)
    sec.bottom_margin = Cm(1.8)
    sec.left_margin = Cm(2.0)
    sec.right_margin = Cm(2.0)

    normal = doc.styles["Normal"]
    normal.font.name = "Calibri"
    normal.font.size = Pt(10.5)
    normal.font.color.rgb = RGBColor(0x14, 0x2A, 0x22)
    normal.paragraph_format.space_after = Pt(6)
    normal.paragraph_format.line_spacing = 1.12

    for name, size, color in (("Title", 30, 0x0E6A50), ("Heading 1", 18, 0x0E6A50),
                              ("Heading 2", 13.5, 0x145B45), ("Heading 3", 11.5, 0x1FA879)):
        st = doc.styles[name]
        st.font.name = "Calibri"
        st.font.size = Pt(size)
        st.font.bold = True
        st.font.color.rgb = RGBColor((color >> 16) & 255, (color >> 8) & 255, color & 255)
        st.paragraph_format.space_before = Pt(14 if name != "Title" else 0)
        st.paragraph_format.space_after = Pt(6)
        st.paragraph_format.keep_with_next = True

    # header / footer with page number field
    hp = sec.header.paragraphs[0]
    hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    hr = hp.add_run("CALMORA  ·  AI PROJECT LOGBOOK")
    hr.font.size = Pt(8)
    hr.font.bold = True
    hr.font.color.rgb = RGBColor(0x5B, 0x6F, 0x66)
    fp = sec.footer.paragraphs[0]
    fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
    fr = fp.add_run("Calmora — a quiet place to think out loud   |   Page ")
    fr.font.size = Pt(8)
    fr.font.color.rgb = RGBColor(0x5B, 0x6F, 0x66)
    fld = OxmlElement("w:fldSimple")
    fld.set(qn("w:instr"), "PAGE")
    fp._p.append(fld)

    first_h2 = True
    for b in blocks:
        t = b["t"]
        if t == "pagebreak":
            doc.add_page_break()
            continue
        if t == "hr":
            p = doc.add_paragraph()
            pPr = p._p.get_or_add_pPr()
            pbdr = OxmlElement("w:pBdr")
            bottom = OxmlElement("w:bottom")
            bottom.set(qn("w:val"), "single")
            bottom.set(qn("w:sz"), "6")
            bottom.set(qn("w:color"), "1FA879")
            pbdr.append(bottom)
            pPr.append(pbdr)
            continue
        if t == "h":
            lvl = b["lvl"]
            if lvl == 1:
                p = doc.add_paragraph(style="Title")
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                add_inline_runs(p, b["text"])
            elif lvl == 2:
                if first_h2:
                    # Cover subtitle — centred, no section rule, no page break.
                    first_h2 = False
                    p = doc.add_paragraph(style="Heading 2")
                    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                    add_inline_runs(p, b["text"])
                    continue
                p = doc.add_paragraph(style="Heading 1")
                add_inline_runs(p, b["text"])
                pPr = p._p.get_or_add_pPr()
                pbdr = OxmlElement("w:pBdr")
                bt = OxmlElement("w:bottom")
                bt.set(qn("w:val"), "single")
                bt.set(qn("w:sz"), "10")
                bt.set(qn("w:color"), "1FA879")
                bt.set(qn("w:space"), "4")
                pbdr.append(bt)
                pPr.append(pbdr)
            else:
                p = doc.add_paragraph(style="Heading 2" if lvl == 3 else "Heading 3")
                add_inline_runs(p, b["text"])
            continue
        if t == "para":
            p = doc.add_paragraph()
            add_inline_runs(p, b["text"])
            continue
        if t == "bullet":
            p = doc.add_paragraph(style="List Bullet" if b["lvl"] == 0 else "List Bullet 2")
            p.paragraph_format.space_after = Pt(3)
            add_inline_runs(p, b["text"])
            continue
        if t == "number":
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Cm(0.6)
            p.paragraph_format.first_line_indent = Cm(-0.6)
            p.paragraph_format.space_after = Pt(4)
            lead = p.add_run(b["num"] + "  ")
            lead.bold = True
            lead.font.color.rgb = RGBColor(0x0E, 0x6A, 0x50)
            add_inline_runs(p, b["text"])
            continue
        if t == "callout":
            tbl = doc.add_table(rows=1, cols=1)
            tbl.autofit = True
            cell = tbl.cell(0, 0)
            docx_shade(cell, "EAF6F0")
            p = cell.paragraphs[0]
            p.paragraph_format.space_before = Pt(4)
            p.paragraph_format.space_after = Pt(4)
            add_inline_runs(p, b["text"], italic=False)
            doc.add_paragraph().paragraph_format.space_after = Pt(2)
            continue
        if t == "table":
            rows = b["rows"]
            if not rows:
                continue
            ncols = max(len(r) for r in rows)
            tbl = doc.add_table(rows=len(rows), cols=ncols)
            tbl.style = "Table Grid"
            tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
            tbl.autofit = True
            for ri, row in enumerate(rows):
                for ci in range(ncols):
                    cell = tbl.cell(ri, ci)
                    if ri == 0:
                        docx_shade(cell, "0E6A50")
                    elif ri % 2 == 0:
                        docx_shade(cell, "F5FAF7")
                    p = cell.paragraphs[0]
                    p.paragraph_format.space_after = Pt(2)
                    p.paragraph_format.space_before = Pt(2)
                    txt = row[ci] if ci < len(row) else ""
                    add_inline_runs(p, txt, base=9)
                    if ri == 0:
                        for r in p.runs:
                            r.bold = True
                            r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
            # repeat header row on later pages
            trPr = tbl.rows[0]._tr.get_or_add_trPr()
            hdr = OxmlElement("w:tblHeader")
            hdr.set(qn("w:val"), "true")
            trPr.append(hdr)
            doc.add_paragraph().paragraph_format.space_after = Pt(2)
            continue

    cp = doc.core_properties
    cp.title = "AI Project Logbook — CALMORA"
    cp.subject = "Completed AI Project Logbook for the Calmora wellbeing companion"
    cp.author = "Calmora project team"
    cp.keywords = "AI project logbook, Calmora, wellbeing, IBM EdTech Youth Challenge"
    doc.save(DOCX)


# ---------------------------------------------------------------------------
# 3. PDF
# ---------------------------------------------------------------------------

pdfmetrics.registerFont(TTFont("DJ", str(REG)))
pdfmetrics.registerFont(TTFont("DJ-Bold", str(BOLD)))
if ITAL.exists():
    pdfmetrics.registerFont(TTFont("DJ-Italic", str(ITAL)))
    ITAL_NAME = "DJ-Italic"
else:
    ITAL_NAME = "DJ"
pdfmetrics.registerFontFamily("DJ", normal="DJ", bold="DJ-Bold", italic=ITAL_NAME, boldItalic="DJ-Bold")


def pdf_inline(text):
    """Convert inline tokens to a reportlab Paragraph-safe string."""
    out = []
    for kind, val, extra in inline(text):
        e = sax.escape(val)
        if kind == "bold":
            out.append(f'<b>{e}</b>')
        elif kind == "italic":
            out.append(f'<i>{e}</i>')
        elif kind == "code":
            out.append(f'<font name="DJ-Bold" color="#0E6A50">{e}</font>')
        elif kind == "hl":
            out.append(f'<font backColor="#FFF2A8" color="#7A5200"><b>{e}</b></font>')
        elif kind == "link":
            out.append(f'<link href="{sax.escape(extra)}" color="#0E6A50"><u>{e}</u></link>')
        else:
            out.append(e)
    return "".join(out)


def pstyle(name, **kw):
    base = dict(fontName="DJ", fontSize=9.4, leading=13.2, textColor=INK,
                spaceAfter=5, alignment=TA_LEFT)
    base.update(kw)
    return ParagraphStyle(name, **base)


S = {
    "body": pstyle("body"),
    "small": pstyle("small", fontSize=8.2, leading=11, textColor=GREY),
    "h1": pstyle("h1", fontName="DJ-Bold", fontSize=27, leading=32,
                 textColor=TEAL, alignment=TA_CENTER, spaceAfter=10),
    "h2": pstyle("h2", fontName="DJ-Bold", fontSize=17, leading=21,
                 textColor=TEAL, spaceBefore=2, spaceAfter=8, keepWithNext=1),
    "subtitle": pstyle("subtitle", fontName="DJ-Bold", fontSize=14, leading=18,
                       textColor=colors.HexColor("#145B45"), alignment=TA_CENTER,
                       spaceAfter=14, keepWithNext=1),
    "h3": pstyle("h3", fontName="DJ-Bold", fontSize=12, leading=15.5,
                 textColor=colors.HexColor("#145B45"), spaceBefore=11,
                 spaceAfter=5, keepWithNext=1),
    "h4": pstyle("h4", fontName="DJ-Bold", fontSize=10.2, leading=13,
                 textColor=MINT, spaceBefore=8, spaceAfter=4, keepWithNext=1),
    "bullet": pstyle("bullet", fontSize=9.2, leading=12.8, spaceAfter=2.5),
    "number": pstyle("number", fontSize=9.2, leading=12.8, spaceAfter=3),
    "cell": pstyle("cell", fontSize=7.8, leading=10.2, spaceAfter=0),
    "cellh": pstyle("cellh", fontName="DJ-Bold", fontSize=7.8, leading=10.2,
                    textColor=colors.white, spaceAfter=0),
    "callout": pstyle("callout", fontSize=9.2, leading=13, spaceAfter=0),
    "cover": pstyle("cover", fontSize=11, leading=16, alignment=TA_CENTER, textColor=GREY),
}


def col_widths(rows, avail):
    ncols = max(len(r) for r in rows)
    weights = []
    for c in range(ncols):
        vals = [len(r[c]) for r in rows if c < len(r) and r[c]]
        weights.append(max(6, (sum(vals) / max(1, len(vals))) ** 0.55))
    total = sum(weights)
    return [avail * w / total for w in weights]


def make_table(rows, avail):
    widths = col_widths(rows, avail)
    data = []
    for ri, row in enumerate(rows):
        cells = []
        for ci in range(len(widths)):
            txt = row[ci] if ci < len(row) else ""
            style = S["cellh"] if ri == 0 else S["cell"]
            cells.append(Paragraph(pdf_inline(txt), style))
        data.append(cells)
    tbl = Table(data, colWidths=widths, repeatRows=1, hAlign="LEFT")
    cmds = [
        ("BACKGROUND", (0, 0), (-1, 0), TEAL),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("GRID", (0, 0), (-1, -1), 0.4, LINE),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]
    for ri in range(1, len(rows)):
        if ri % 2 == 0:
            cmds.append(("BACKGROUND", (0, ri), (-1, ri), PALE2))
    tbl.setStyle(TableStyle(cmds))
    return tbl


def build_pdf(blocks):
    doc = BaseDocTemplate(
        str(PDF), pagesize=A4,
        leftMargin=1.7 * cm, rightMargin=1.7 * cm,
        topMargin=1.9 * cm, bottomMargin=1.7 * cm,
        title="AI Project Logbook — CALMORA", author="Calmora project team",
        subject="Completed AI Project Logbook for the Calmora wellbeing companion",
    )
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="body")

    def decorate(canvas, d):
        canvas.saveState()
        w, h = A4
        canvas.setFont("DJ-Bold", 7.5)
        canvas.setFillColor(GREY)
        canvas.drawString(doc.leftMargin, h - 1.15 * cm, "CALMORA   ·   AI PROJECT LOGBOOK")
        canvas.drawRightString(w - doc.rightMargin, h - 1.15 * cm, "A quiet place to think out loud")
        canvas.setStrokeColor(LINE)
        canvas.setLineWidth(0.5)
        canvas.line(doc.leftMargin, h - 1.35 * cm, w - doc.rightMargin, h - 1.35 * cm)
        canvas.line(doc.leftMargin, 1.25 * cm, w - doc.rightMargin, 1.25 * cm)
        canvas.setFont("DJ", 7.5)
        canvas.drawCentredString(w / 2, 0.85 * cm, "Page %d" % canvas.getPageNumber())
        canvas.restoreState()

    doc.addPageTemplates([PageTemplate(id="main", frames=[frame], onPage=decorate)])
    avail = doc.width
    story = []
    first_h2 = True

    for b in blocks:
        t = b["t"]
        if t == "pagebreak":
            story.append(PageBreak())
        elif t == "hr":
            story.append(HRFlowable(width="100%", thickness=0.8, color=MINT, spaceBefore=4, spaceAfter=8))
        elif t == "h":
            lvl, text = b["lvl"], pdf_inline(b["text"])
            if lvl == 1:
                story.append(Spacer(1, 1.2 * cm))
                story.append(Paragraph(text, S["h1"]))
                story.append(Paragraph("Completed logbook for the Calmora project", S["cover"]))
                story.append(Spacer(1, 0.7 * cm))
                story.append(HRFlowable(width="45%", thickness=2, color=MINT, hAlign="CENTER"))
                story.append(Spacer(1, 0.8 * cm))
            elif lvl == 2:
                if first_h2:
                    first_h2 = False
                    story.append(Paragraph(text, S["subtitle"]))
                    continue
                story.append(Paragraph(text, S["h2"]))
                story.append(HRFlowable(width="100%", thickness=1.4, color=MINT, spaceAfter=10))
            elif lvl == 3:
                story.append(Paragraph(text, S["h3"]))
            else:
                story.append(Paragraph(text, S["h4"]))
        elif t == "para":
            story.append(Paragraph(pdf_inline(b["text"]), S["body"]))
        elif t == "bullet":
            lvl = min(b["lvl"], 2)
            st = pstyle("b%d" % lvl, fontSize=9.2, leading=12.8, spaceAfter=2.5,
                        leftIndent=12 + 14 * lvl, bulletIndent=2 + 14 * lvl)
            mark = "•" if lvl == 0 else ("–" if lvl == 1 else "·")
            story.append(Paragraph(pdf_inline(b["text"]), st, bulletText=mark))
        elif t == "number":
            st = pstyle("num", fontSize=9.2, leading=12.8, spaceAfter=3,
                        leftIndent=16, bulletIndent=2)
            story.append(Paragraph(pdf_inline(b["text"]), st, bulletText=b["num"]))
        elif t == "callout":
            inner = Paragraph(pdf_inline(b["text"]), S["callout"])
            tbl = Table([[inner]], colWidths=[avail], hAlign="LEFT")
            tbl.setStyle(TableStyle([
                ("BACKGROUND", (0, 0), (-1, -1), PALE),
                ("LINEBEFORE", (0, 0), (0, -1), 3, MINT),
                ("BOX", (0, 0), (-1, -1), 0.4, LINE),
                ("LEFTPADDING", (0, 0), (-1, -1), 10),
                ("RIGHTPADDING", (0, 0), (-1, -1), 10),
                ("TOPPADDING", (0, 0), (-1, -1), 8),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
            ]))
            story.append(KeepTogether([tbl, Spacer(1, 8)]))
        elif t == "table":
            rows = b["rows"]
            if rows:
                story.append(make_table(rows, avail))
                story.append(Spacer(1, 9))

    doc.build(story)


def main():
    lines = SRC.read_text(encoding="utf-8").splitlines()
    blocks = parse(lines)
    build_docx(blocks)
    build_pdf(blocks)
    print("Blocks parsed :", len(blocks))
    print("DOCX          :", DOCX, f"({DOCX.stat().st_size:,} bytes)")
    print("PDF           :", PDF, f"({PDF.stat().st_size:,} bytes)")


if __name__ == "__main__":
    main()
