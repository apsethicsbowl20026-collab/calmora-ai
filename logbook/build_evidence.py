#!/usr/bin/env python3
"""Export the evidence supplement without overwriting the original logbook.
Install python-docx and reportlab, then run: python logbook/build_evidence.py
The Markdown remains the editable source; raw evidence files are never rewritten.
"""
from pathlib import Path
from docx import Document
from docx.shared import Cm, Pt, RGBColor
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from build import parse, add_inline_runs, pdf_inline  # shared Markdown grammar + licensed system fonts

HERE = Path(__file__).resolve().parent
BASE = HERE / 'PRIMOSHU-Test-Logs-and-Interview-Notes'
TITLE = 'PRIMØSHU by Calmora | Logbook evidence'
INK = '#20382B'
ACCENT = '#426B50'


def word(blocks):
    doc = Document()
    section = doc.sections[0]
    section.page_width, section.page_height = Cm(21), Cm(29.7)
    section.top_margin, section.bottom_margin = Cm(2), Cm(1.8)
    section.left_margin = section.right_margin = Cm(1.8)
    style = doc.styles['Normal']
    style.font.name, style.font.size = 'Calibri', Pt(10)
    style.paragraph_format.space_after = Pt(6)
    for name, size in [('Title', 24), ('Heading 1', 18), ('Heading 2', 15), ('Heading 3', 12)]:
        doc.styles[name].font.size = Pt(size)
        doc.styles[name].font.color.rgb = RGBColor.from_string('20382B')
    header = section.header.paragraphs[0]
    header.add_run(TITLE).font.size = Pt(8)
    footer = section.footer.paragraphs[0]
    footer.add_run('Evidence supplement • 4 November 2026 • Page ').font.size = Pt(8)
    field = OxmlElement('w:fldSimple'); field.set(qn('w:instr'), 'PAGE'); footer._p.append(field)
    doc.core_properties.title = TITLE
    doc.core_properties.subject = 'Executed technical test log and recorded stakeholder feedback; interview templates are unfilled.'
    for block in blocks:
        kind = block['t']
        if kind == 'pagebreak':
            doc.add_page_break()
        elif kind == 'h':
            p = doc.add_paragraph(style='Title' if block['lvl'] == 1 else f"Heading {min(block['lvl'] - 1, 3)}")
            add_inline_runs(p, block['text'])
        elif kind == 'table':
            rows = block['rows']
            table = doc.add_table(rows=0, cols=len(rows[0])); table.style = 'Light Shading Accent 1'
            for index, row in enumerate(rows):
                cells = table.add_row().cells
                for cell, text in zip(cells, row):
                    add_inline_runs(cell.paragraphs[0], text, base=9)
                    if index == 0:
                        for run in cell.paragraphs[0].runs: run.bold = True
                if index == 0:
                    repeat = OxmlElement('w:tblHeader'); table.rows[0]._tr.get_or_add_trPr().append(repeat)
            doc.add_paragraph()
        else:
            prefix = '• ' if kind == 'bullet' else block.get('num', '') + ' ' if kind == 'number' else ''
            p = doc.add_paragraph(); add_inline_runs(p, prefix + block['text'])
    doc.save(str(BASE.with_suffix('.docx')))


def pdf(blocks):
    body = ParagraphStyle('body', fontName='DJ', fontSize=9, leading=12, spaceAfter=7, textColor=colors.HexColor(INK))
    small = ParagraphStyle('small', parent=body, fontSize=8, leading=10, spaceAfter=0)
    styles = {level: ParagraphStyle(f'h{level}', parent=body, fontName='DJ-Bold', fontSize={1:23, 2:17, 3:11, 4:10}[level], leading={1:29, 2:23, 3:16, 4:14}[level], spaceBefore=8, spaceAfter=11, keepWithNext=True) for level in range(1,5)}
    story = []
    width = A4[0] - 100
    for block in blocks:
        kind = block['t']
        if kind == 'pagebreak': story.append(PageBreak())
        elif kind == 'h': story.append(Paragraph(pdf_inline(block['text']), styles[min(block['lvl'],4)]))
        elif kind == 'table':
            rows = [[Paragraph(pdf_inline(text), small) for text in row] for row in block['rows']]
            count = len(rows[0])
            widths = [width * .23, width * .62, width * .15] if count == 3 else [width / count] * count
            # Wide middle columns make the test matrix and feedback tables readable.
            if count == 3 and len(block['rows']) < 10: widths = [width*.2,width*.45,width*.35]
            if count == 2: widths = [width*.36,width*.64]
            table = Table(rows, colWidths=widths, repeatRows=1, hAlign='LEFT')
            table.setStyle(TableStyle([
                ('BACKGROUND',(0,0),(-1,0),colors.HexColor('#DBE9DC')),
                ('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.HexColor('#F3F7F1'),colors.white]),
                ('GRID',(0,0),(-1,-1),.4,colors.HexColor('#CBD8C7')),
                ('VALIGN',(0,0),(-1,-1),'TOP'),
                ('LEFTPADDING',(0,0),(-1,-1),7),('RIGHTPADDING',(0,0),(-1,-1),7),
                ('TOPPADDING',(0,0),(-1,-1),5.5),('BOTTOMPADDING',(0,0),(-1,-1),5.5),
            ]))
            story.extend([table,Spacer(1,10)])
        else:
            prefix = '• ' if kind == 'bullet' else block.get('num','')+' ' if kind == 'number' else ''
            story.append(Paragraph(pdf_inline(prefix+block['text']),body))
    def decorate(canvas, doc):
        canvas.saveState();canvas.setFont('DJ',8);canvas.setFillColor(colors.HexColor(ACCENT))
        canvas.drawString(50,A4[1]-32,TITLE)
        canvas.drawString(50,26,'Evidence supplement • 4 November 2026')
        canvas.drawRightString(A4[0]-50,26,f'Page {doc.page}')
        canvas.restoreState()
    doc = SimpleDocTemplate(str(BASE.with_suffix('.pdf')), pagesize=A4, leftMargin=50,rightMargin=50,topMargin=52,bottomMargin=46,title=TITLE,author='Project evidence supplement')
    doc.build(story,onFirstPage=decorate,onLaterPages=decorate)


if __name__ == '__main__':
    blocks = parse(BASE.with_suffix('.md').read_text().splitlines())
    word(blocks);pdf(blocks)
    for suffix in ['.docx','.pdf']: print(BASE.with_suffix(suffix))
