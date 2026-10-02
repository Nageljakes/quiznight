import docx
from docx.shared import Pt, RGBColor, Mm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

def set_cell_shd(cell, hex_color):
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hex_color}"/>')
    cell._tc.get_or_add_tcPr().append(shd)

def set_cell_pad(cell, top=45, bottom=45, left=60, right=60):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)

def set_tbl_borders(table, color="CBD5E1", sz="4"):
    tblPr = table._tbl.tblPr
    borders = parse_xml(f'''
        <w:tblBorders {nsdecls("w")}>
            <w:top w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>
            <w:bottom w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>
            <w:left w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>
            <w:right w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>
            <w:insideH w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>
            <w:insideV w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>
        </w:tblBorders>
    ''')
    tblPr.append(borders)

def make_matrix_single_page(output_file):
    doc = docx.Document()
    
    # A4 Margins - very comfortable single page fit
    section = doc.sections[0]
    section.page_width = Mm(210)
    section.page_height = Mm(297)
    section.top_margin = Mm(10)
    section.bottom_margin = Mm(10)
    section.left_margin = Mm(10)
    section.right_margin = Mm(10)
    
    normal = doc.styles['Normal']
    normal.font.name = 'Calibri'
    normal.font.size = Pt(9)
    normal.font.color.rgb = RGBColor(15, 23, 42)

    # 1. Title Banner
    p_title = doc.add_paragraph()
    p_title.paragraph_format.space_before = Pt(0)
    p_title.paragraph_format.space_after = Pt(1)
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_t = p_title.add_run("BEERBOX MIDRAND • PUB QUIZ MASTER ANSWER SHEET")
    r_t.font.bold = True
    r_t.font.size = Pt(14)
    r_t.font.color.rgb = RGBColor(180, 83, 9)

    p_sub = doc.add_paragraph()
    p_sub.paragraph_format.space_before = Pt(0)
    p_sub.paragraph_format.space_after = Pt(4)
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_s = p_sub.add_run("Hosted by DJ JC • Circle your chosen answer (A, B, C, or D) for each question • Swapped for marking after each round")
    r_s.font.size = Pt(8.5)
    r_s.font.color.rgb = RGBColor(100, 116, 139)

    # 2. Team Details Table
    team_tbl = doc.add_table(rows=1, cols=4)
    team_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_tbl_borders(team_tbl, color="CBD5E1", sz="6")
    for i, w in enumerate([Mm(65), Mm(26), Mm(54), Mm(45)]):
        team_tbl.cell(0, i).width = w

    c0 = team_tbl.cell(0, 0)
    set_cell_pad(c0, 40, 40, 60, 60)
    p0 = c0.paragraphs[0]
    p0.paragraph_format.space_after = Pt(0)
    p0.add_run("Team Name: ").font.bold = True
    p0.add_run("________________________")

    c1 = team_tbl.cell(0, 1)
    set_cell_pad(c1, 40, 40, 60, 60)
    p1 = c1.paragraphs[0]
    p1.paragraph_format.space_after = Pt(0)
    p1.add_run("Table #: ").font.bold = True
    p1.add_run("____")

    c2 = team_tbl.cell(0, 2)
    set_cell_pad(c2, 40, 40, 60, 60)
    p2 = c2.paragraphs[0]
    p2.paragraph_format.space_after = Pt(0)
    p2.add_run("Captain: ").font.bold = True
    p2.add_run("__________________")

    c3 = team_tbl.cell(0, 3)
    set_cell_shd(c3, "FEF3C7")
    set_cell_pad(c3, 40, 40, 60, 60)
    p3 = c3.paragraphs[0]
    p3.paragraph_format.space_after = Pt(0)
    r_j = p3.add_run("★ JOKER (x2): ")
    r_j.font.bold = True
    r_j.font.color.rgb = RGBColor(180, 83, 9)
    p3.add_run("R1 [ ] R2 [ ] R3 [ ] R4 [ ] R5 [ ]").font.bold = True
    p3.runs[1].font.size = Pt(8)

    # Spacing
    p_sp = doc.add_paragraph()
    p_sp.paragraph_format.space_before = Pt(3)
    p_sp.paragraph_format.space_after = Pt(3)

    # 3. Master Answer Matrix Table (6 Columns: Q# + Rounds 1-5)
    # Total printable width = 190 mm.
    # Col 0: 12 mm
    # Cols 1-5: 35.6 mm each -> 12 + (35.6 * 5) = 190 mm
    matrix = doc.add_table(rows=14, cols=6)
    matrix.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_tbl_borders(matrix, color="CBD5E1", sz="5")
    
    col_widths = [Mm(12), Mm(35.6), Mm(35.6), Mm(35.6), Mm(35.6), Mm(35.6)]
    for row in matrix.rows:
        for idx, w in enumerate(col_widths):
            row.cells[idx].width = w

    # Row 0: Headers
    r_headers = [
        ("#", "F1F5F9", RGBColor(71, 85, 105)),
        ("ROUND 1\nBar Warm-Up", "1E293B", RGBColor(254, 243, 199)),
        ("ROUND 2\nBeat & Screen", "1E293B", RGBColor(254, 243, 199)),
        ("ROUND 3\nRugby & Sports", "1E293B", RGBColor(254, 243, 199)),
        ("ROUND 4\nWorld & Science", "1E293B", RGBColor(254, 243, 199)),
        ("ROUND 5\nMastermind", "1E293B", RGBColor(254, 243, 199))
    ]
    
    for idx, (txt, bg, col) in enumerate(r_headers):
        cell = matrix.cell(0, idx)
        set_cell_shd(cell, bg)
        set_cell_pad(cell, 35, 35, 30, 30)
        p = cell.paragraphs[0]
        p.paragraph_format.space_after = Pt(0)
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(txt)
        r.font.bold = True
        r.font.size = Pt(8)
        r.font.color.rgb = col

    # Rows 1 to 10: Questions 1 to 10
    for q in range(1, 11):
        row = matrix.rows[q]
        # Col 0: Q Number
        c0 = row.cells[0]
        set_cell_shd(c0, "F8FAFC")
        set_cell_pad(c0, 25, 25, 20, 20)
        p0 = c0.paragraphs[0]
        p0.paragraph_format.space_after = Pt(0)
        p0.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r0 = p0.add_run(f"Q{q}")
        r0.font.bold = True
        r0.font.size = Pt(8.5)
        r0.font.color.rgb = RGBColor(100, 116, 139)

        # Cols 1 to 5: ABCD bubbles
        for c_idx in range(1, 6):
            cell = row.cells[c_idx]
            set_cell_pad(cell, 25, 25, 20, 20)
            p = cell.paragraphs[0]
            p.paragraph_format.space_after = Pt(0)
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            r = p.add_run("[ A ]   [ B ]   [ C ]   [ D ]")
            r.font.bold = True
            r.font.size = Pt(8)
            r.font.color.rgb = RGBColor(30, 41, 59)

    # Row 11: Base Score
    r11 = matrix.rows[11]
    c11_0 = r11.cells[0]
    set_cell_shd(c11_0, "FEF3C7")
    set_cell_pad(c11_0, 30, 30, 20, 20)
    p = c11_0.paragraphs[0]
    p.paragraph_format.space_after = Pt(0)
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run("Score")
    r.font.bold = True
    r.font.size = Pt(7.5)

    for c_idx in range(1, 6):
        cell = r11.cells[c_idx]
        set_cell_shd(cell, "FEF3C7")
        set_cell_pad(cell, 30, 30, 20, 20)
        p = cell.paragraphs[0]
        p.paragraph_format.space_after = Pt(0)
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run("[ _____ / 10 ]")
        r.font.bold = True
        r.font.size = Pt(8.5)

    # Row 12: Joker Row
    r12 = matrix.rows[12]
    c12_0 = r12.cells[0]
    set_cell_shd(c12_0, "FFFBEB")
    set_cell_pad(c12_0, 25, 25, 20, 20)
    p = c12_0.paragraphs[0]
    p.paragraph_format.space_after = Pt(0)
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run("Joker")
    r.font.bold = True
    r.font.size = Pt(7.5)

    for c_idx in range(1, 6):
        cell = r12.cells[c_idx]
        set_cell_shd(cell, "FFFBEB")
        set_cell_pad(cell, 25, 25, 20, 20)
        p = cell.paragraphs[0]
        p.paragraph_format.space_after = Pt(0)
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run("x2 Active? [ ] YES")
        r.font.size = Pt(7.5)
        r.font.bold = True
        r.font.color.rgb = RGBColor(180, 83, 9)

    # Row 13: Official Round Total
    r13 = matrix.rows[13]
    c13_0 = r13.cells[0]
    set_cell_shd(c13_0, "FDE68A")
    set_cell_pad(c13_0, 30, 30, 20, 20)
    p = c13_0.paragraphs[0]
    p.paragraph_format.space_after = Pt(0)
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run("Total")
    r.font.bold = True
    r.font.size = Pt(7.5)
    r.font.color.rgb = RGBColor(146, 64, 14)

    for c_idx in range(1, 6):
        cell = r13.cells[c_idx]
        set_cell_shd(cell, "FDE68A")
        set_cell_pad(cell, 30, 30, 20, 20)
        p = cell.paragraphs[0]
        p.paragraph_format.space_after = Pt(0)
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run("TOTAL: [ _____ ]")
        r.font.bold = True
        r.font.size = Pt(8.5)
        r.font.color.rgb = RGBColor(146, 64, 14)

    # Spacing
    p_sp2 = doc.add_paragraph()
    p_sp2.paragraph_format.space_before = Pt(4)
    p_sp2.paragraph_format.space_after = Pt(2)

    # 4. Tie-Breaker Bar (Table across width)
    tb_tbl = doc.add_table(rows=1, cols=4)
    tb_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_tbl_borders(tb_tbl, color="CBD5E1", sz="5")
    # Widths: 40mm, 50mm, 50mm, 50mm = 190mm
    for i, w in enumerate([Mm(40), Mm(50), Mm(50), Mm(50)]):
        tb_tbl.cell(0, i).width = w

    c_tb0 = tb_tbl.cell(0, 0)
    set_cell_shd(c_tb0, "581C87")
    set_cell_pad(c_tb0, 30, 30, 40, 40)
    p = c_tb0.paragraphs[0]
    p.paragraph_format.space_after = Pt(0)
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run("SUDDEN-DEATH\nTIE-BREAKERS")
    r.font.bold = True
    r.font.size = Pt(7.5)
    r.font.color.rgb = RGBColor(243, 232, 255)

    for idx, t_num in enumerate(["TB 1", "TB 2", "TB 3"]):
        c = tb_tbl.cell(0, idx + 1)
        set_cell_shd(c, "FAF5FF")
        set_cell_pad(c, 30, 30, 40, 40)
        p = c.paragraphs[0]
        p.paragraph_format.space_after = Pt(0)
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(f"{t_num}: [ A ] [ B ] [ C ] [ D ]\nGuess / Num: [ ____________ ]")
        r.font.bold = True
        r.font.size = Pt(7.5)
        r.font.color.rgb = RGBColor(107, 33, 168)

    # Spacing
    p_sp3 = doc.add_paragraph()
    p_sp3.paragraph_format.space_before = Pt(4)
    p_sp3.paragraph_format.space_after = Pt(2)

    # 5. Master Grand Total Scorecard Banner
    gt_tbl = doc.add_table(rows=2, cols=6)
    gt_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_tbl_borders(gt_tbl, color="CBD5E1", sz="6")
    gt_col_w = Mm(190 / 6)
    for row in gt_tbl.rows:
        for idx in range(6):
            row.cells[idx].width = gt_col_w

    # Row 0: Labels
    gt_lbls = ["Round 1", "Round 2", "Round 3", "Round 4", "Round 5", "Joker Bonus"]
    for idx, lbl in enumerate(gt_lbls):
        c = gt_tbl.cell(0, idx)
        set_cell_shd(c, "F1F5F9")
        set_cell_pad(c, 25, 25, 20, 20)
        p = c.paragraphs[0]
        p.paragraph_format.space_after = Pt(0)
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(lbl)
        r.font.bold = True
        r.font.size = Pt(7.5)

    # Row 1: Values
    for idx in range(5):
        c = gt_tbl.cell(1, idx)
        set_cell_pad(c, 35, 35, 20, 20)
        p = c.paragraphs[0]
        p.paragraph_format.space_after = Pt(0)
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run("[   / 10 ]")
        r.font.bold = True
        r.font.size = Pt(8.5)

    c_jb = gt_tbl.cell(1, 5)
    set_cell_shd(c_jb, "FEF3C7")
    set_cell_pad(c_jb, 35, 35, 20, 20)
    p = c_jb.paragraphs[0]
    p.paragraph_format.space_after = Pt(0)
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run("[ + _____ ]")
    r.font.bold = True
    r.font.size = Pt(8.5)
    r.font.color.rgb = RGBColor(180, 83, 9)

    # Final Summary Row
    fin_tbl = doc.add_table(rows=1, cols=3)
    fin_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_tbl_borders(fin_tbl, color="CBD5E1", sz="6")
    for i, w in enumerate([Mm(85), Mm(55), Mm(50)]):
        fin_tbl.cell(0, i).width = w

    c_f0 = fin_tbl.cell(0, 0)
    set_cell_shd(c_f0, "FEF3C7")
    set_cell_pad(c_f0, 40, 40, 60, 60)
    p = c_f0.paragraphs[0]
    p.paragraph_format.space_after = Pt(0)
    r = p.add_run("★ FINAL TOURNAMENT SCORE: [ _______ / 50 ]")
    r.font.bold = True
    r.font.size = Pt(9)
    r.font.color.rgb = RGBColor(146, 64, 14)

    c_f1 = fin_tbl.cell(0, 1)
    set_cell_shd(c_f1, "FDE68A")
    set_cell_pad(c_f1, 40, 40, 60, 60)
    p = c_f1.paragraphs[0]
    p.paragraph_format.space_after = Pt(0)
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run("FINAL RANK:  # [ ______ ]")
    r.font.bold = True
    r.font.size = Pt(9)
    r.font.color.rgb = RGBColor(146, 64, 14)

    c_f2 = fin_tbl.cell(0, 2)
    set_cell_shd(c_f2, "F1F5F9")
    set_cell_pad(c_f2, 40, 40, 60, 60)
    p = c_f2.paragraphs[0]
    p.paragraph_format.space_after = Pt(0)
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run("Marker Verified: [  ✓  ]")
    r.font.bold = True
    r.font.size = Pt(8)
    r.font.color.rgb = RGBColor(100, 116, 139)

    doc.save(output_file)
    print(f"Generated Master Matrix single-page document: {output_file}")

if __name__ == "__main__":
    out_file = "/home/jakes/repos/quiznight/Beerbox_Pub_Quiz_Single_Page_Matrix_A4.docx"
    make_matrix_single_page(out_file)
