import docx
from docx.shared import Pt, RGBColor, Mm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

def set_cell_shd(cell, hex_color):
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hex_color}"/>')
    cell._tc.get_or_add_tcPr().append(shd)

def set_cell_pad(cell, top=30, bottom=30, left=50, right=50):
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

def make_3column_single_page(output_file):
    doc = docx.Document()
    
    # Precise A4 page dimensions
    section = doc.sections[0]
    section.page_width = Mm(210)
    section.page_height = Mm(297)
    section.top_margin = Mm(8)
    section.bottom_margin = Mm(6)
    section.left_margin = Mm(8)
    section.right_margin = Mm(8)
    
    normal = doc.styles['Normal']
    normal.font.name = 'Calibri'
    normal.font.size = Pt(8)
    normal.font.color.rgb = RGBColor(15, 23, 42)

    # 1. Header Banner
    title_p = doc.add_paragraph()
    title_p.paragraph_format.space_before = Pt(0)
    title_p.paragraph_format.space_after = Pt(1)
    title_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_title = title_p.add_run("BEERBOX MIDRAND • OFFICIAL PUB QUIZ ANSWER SHEET")
    r_title.font.bold = True
    r_title.font.size = Pt(12)
    r_title.font.color.rgb = RGBColor(180, 83, 9)

    sub_p = doc.add_paragraph()
    sub_p.paragraph_format.space_before = Pt(0)
    sub_p.paragraph_format.space_after = Pt(3)
    sub_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_sub = sub_p.add_run("Hosted by DJ JC • Circle or tick your answers • Strictly No Shazam or Google!")
    r_sub.font.size = Pt(7.5)
    r_sub.font.color.rgb = RGBColor(100, 116, 139)

    # 2. Team Info Bar
    team_tbl = doc.add_table(rows=1, cols=4)
    team_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_tbl_borders(team_tbl, color="CBD5E1", sz="5")
    for i, w in enumerate([Mm(65), Mm(26), Mm(55), Mm(48)]):
        team_tbl.cell(0, i).width = w

    c0 = team_tbl.cell(0, 0)
    set_cell_pad(c0, 40, 40, 60, 60)
    p0 = c0.paragraphs[0]
    p0.paragraph_format.space_after = Pt(0)
    p0.add_run("Team: ").font.bold = True
    p0.add_run("________________________")

    c1 = team_tbl.cell(0, 1)
    set_cell_pad(c1, 40, 40, 60, 60)
    p1 = c1.paragraphs[0]
    p1.paragraph_format.space_after = Pt(0)
    p1.add_run("Table: ").font.bold = True
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

    # Spacing before 3-column table
    sp = doc.add_paragraph()
    sp.paragraph_format.space_before = Pt(2)
    sp.paragraph_format.space_after = Pt(2)

    # 3. Main 3-Column Layout Container
    main_tbl = doc.add_table(rows=1, cols=3)
    main_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    # 194 mm total printable width / 3 = ~64mm each
    col_w = Mm(64)
    for idx in range(3):
        main_tbl.cell(0, idx).width = col_w
        set_cell_pad(main_tbl.cell(0, idx), 0, 0, 30, 30)

    # Remove outer borders
    set_tbl_borders(main_tbl, color="FFFFFF", sz="0")

    def make_round_card(cell, round_num, round_title, badge_text):
        # Banner
        b_tbl = cell.add_table(rows=1, cols=2)
        b_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        b_tbl.cell(0, 0).width = Mm(46)
        b_tbl.cell(0, 1).width = Mm(18)
        set_cell_shd(b_tbl.cell(0, 0), "1E293B")
        set_cell_shd(b_tbl.cell(0, 1), "1E293B")
        set_cell_pad(b_tbl.cell(0, 0), 25, 25, 40, 40)
        set_cell_pad(b_tbl.cell(0, 1), 25, 25, 40, 40)
        
        p_l = b_tbl.cell(0, 0).paragraphs[0]
        p_l.paragraph_format.space_after = Pt(0)
        r1 = p_l.add_run(f"ROUND {round_num}: {round_title.upper()}")
        r1.font.bold = True
        r1.font.size = Pt(7.5)
        r1.font.color.rgb = RGBColor(254, 243, 199)

        p_r = b_tbl.cell(0, 1).paragraphs[0]
        p_r.paragraph_format.space_after = Pt(0)
        p_r.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        r2 = p_r.add_run(badge_text)
        r2.font.bold = True
        r2.font.size = Pt(7)
        r2.font.color.rgb = RGBColor(251, 191, 36)

        # 10 Questions
        q_tbl = cell.add_table(rows=11, cols=3)
        q_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        set_tbl_borders(q_tbl, color="CBD5E1", sz="3")
        
        for row in q_tbl.rows:
            row.cells[0].width = Mm(8)
            row.cells[1].width = Mm(43)
            row.cells[2].width = Mm(13)

        # Header
        hdr = q_tbl.rows[0]
        for i, (txt, aln) in enumerate([("#", WD_ALIGN_PARAGRAPH.CENTER), ("Select Answer", WD_ALIGN_PARAGRAPH.CENTER), ("Pick", WD_ALIGN_PARAGRAPH.CENTER)]):
            c = hdr.cells[i]
            set_cell_shd(c, "F1F5F9")
            set_cell_pad(c, 20, 20, 20, 20)
            p = c.paragraphs[0]
            p.paragraph_format.space_after = Pt(0)
            p.alignment = aln
            r = p.add_run(txt)
            r.font.bold = True
            r.font.size = Pt(7)
            r.font.color.rgb = RGBColor(71, 85, 105)

        for q in range(1, 11):
            row = q_tbl.rows[q]
            # Q#
            c0 = row.cells[0]
            set_cell_pad(c0, 15, 15, 20, 20)
            p0 = c0.paragraphs[0]
            p0.paragraph_format.space_after = Pt(0)
            p0.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p0.add_run(f"Q{q}").font.bold = True
            p0.runs[0].font.size = Pt(7.5)

            # ABCD blocks
            c1 = row.cells[1]
            set_cell_pad(c1, 15, 15, 20, 20)
            p1 = c1.paragraphs[0]
            p1.paragraph_format.space_after = Pt(0)
            p1.alignment = WD_ALIGN_PARAGRAPH.CENTER
            r_opt = p1.add_run("[A]   [B]   [C]   [D]")
            r_opt.font.bold = True
            r_opt.font.size = Pt(7.5)
            r_opt.font.color.rgb = RGBColor(30, 41, 59)

            # Pick
            c2 = row.cells[2]
            set_cell_pad(c2, 15, 15, 20, 20)
            p2 = c2.paragraphs[0]
            p2.paragraph_format.space_after = Pt(0)
            p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
            r_pk = p2.add_run("[   ]")
            r_pk.font.bold = True
            r_pk.font.size = Pt(7.5)
            r_pk.font.color.rgb = RGBColor(148, 163, 184)

        # Subtotal Row
        sub_tbl = cell.add_table(rows=1, cols=2)
        sub_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        set_tbl_borders(sub_tbl, color="CBD5E1", sz="5")
        sub_tbl.cell(0, 0).width = Mm(36)
        sub_tbl.cell(0, 1).width = Mm(28)

        cs0 = sub_tbl.cell(0, 0)
        set_cell_shd(cs0, "FEF3C7")
        set_cell_pad(cs0, 25, 25, 30, 30)
        ps0 = cs0.paragraphs[0]
        ps0.paragraph_format.space_after = Pt(0)
        rs0 = ps0.add_run(f"R{round_num}: [ ___ / 10 ]")
        rs0.font.bold = True
        rs0.font.size = Pt(7.5)

        cs1 = sub_tbl.cell(0, 1)
        set_cell_shd(cs1, "FDE68A")
        set_cell_pad(cs1, 25, 25, 30, 30)
        ps1 = cs1.paragraphs[0]
        ps1.paragraph_format.space_after = Pt(0)
        ps1.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        rs1 = ps1.add_run(f"Total: [ ____ ]")
        rs1.font.bold = True
        rs1.font.size = Pt(7.5)
        rs1.font.color.rgb = RGBColor(146, 64, 14)

        # Gap
        pg = cell.add_paragraph()
        pg.paragraph_format.space_before = Pt(0)
        pg.paragraph_format.space_after = Pt(4)

    # Column 1: Round 1 & Round 2
    c_col1 = main_tbl.cell(0, 0)
    make_round_card(c_col1, 1, "Bar Warm-Up", "10 Pts")
    make_round_card(c_col1, 2, "Beat & Screen", "10 Pts")

    # Column 2: Round 3 & Round 4
    c_col2 = main_tbl.cell(0, 1)
    make_round_card(c_col2, 3, "Rugby & Sports", "10 Pts")
    make_round_card(c_col2, 4, "World & Science", "10 Pts")

    # Column 3: Round 5 + Tie-Breakers + Master Grand Total Scorecard
    c_col3 = main_tbl.cell(0, 2)
    make_round_card(c_col3, 5, "Mastermind", "10 Pts")

    # Tie-Breakers
    tb_b = c_col3.add_table(rows=1, cols=2)
    tb_b.alignment = WD_TABLE_ALIGNMENT.CENTER
    tb_b.cell(0, 0).width = Mm(46)
    tb_b.cell(0, 1).width = Mm(18)
    set_cell_shd(tb_b.cell(0, 0), "581C87")
    set_cell_shd(tb_b.cell(0, 1), "581C87")
    set_cell_pad(tb_b.cell(0, 0), 20, 20, 30, 30)
    set_cell_pad(tb_b.cell(0, 1), 20, 20, 30, 30)
    
    ptb = tb_b.cell(0, 0).paragraphs[0]
    ptb.paragraph_format.space_after = Pt(0)
    rtb = ptb.add_run("TIE-BREAKERS")
    rtb.font.bold = True
    rtb.font.size = Pt(7.5)
    rtb.font.color.rgb = RGBColor(243, 232, 255)

    ptbr = tb_b.cell(0, 1).paragraphs[0]
    ptbr.paragraph_format.space_after = Pt(0)
    ptbr.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    rtbr = ptbr.add_run("Closest")
    rtbr.font.bold = True
    rtbr.font.size = Pt(7)
    rtbr.font.color.rgb = RGBColor(216, 180, 254)

    tb_tbl = c_col3.add_table(rows=4, cols=3)
    tb_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_tbl_borders(tb_tbl, color="CBD5E1", sz="3")
    for row in tb_tbl.rows:
        row.cells[0].width = Mm(8)
        row.cells[1].width = Mm(43)
        row.cells[2].width = Mm(13)

    tb_hdr = tb_tbl.rows[0]
    for i, (txt, aln) in enumerate([("#", WD_ALIGN_PARAGRAPH.CENTER), ("Estimate / Pick", WD_ALIGN_PARAGRAPH.CENTER), ("Mark", WD_ALIGN_PARAGRAPH.CENTER)]):
        c = tb_hdr.cells[i]
        set_cell_shd(c, "FAF5FF")
        set_cell_pad(c, 20, 20, 20, 20)
        p = c.paragraphs[0]
        p.paragraph_format.space_after = Pt(0)
        p.alignment = aln
        r = p.add_run(txt)
        r.font.bold = True
        r.font.size = Pt(7)
        r.font.color.rgb = RGBColor(107, 33, 168)

    for q in range(1, 4):
        row = tb_tbl.rows[q]
        c0 = row.cells[0]
        set_cell_pad(c0, 15, 15, 20, 20)
        p0 = c0.paragraphs[0]
        p0.paragraph_format.space_after = Pt(0)
        p0.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p0.add_run(f"T{q}").font.bold = True
        p0.runs[0].font.size = Pt(7.5)

        c1 = row.cells[1]
        set_cell_pad(c1, 15, 15, 20, 20)
        p1 = c1.paragraphs[0]
        p1.paragraph_format.space_after = Pt(0)
        p1.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p1.add_run("[A]   [B]   [C]   [D]").font.bold = True
        p1.runs[0].font.size = Pt(7.5)

        c2 = row.cells[2]
        set_cell_pad(c2, 15, 15, 20, 20)
        p2 = c2.paragraphs[0]
        p2.paragraph_format.space_after = Pt(0)
        p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p2.add_run("[   ]").font.bold = True
        p2.runs[0].font.size = Pt(7.5)

    # Gap
    pg_gt = c_col3.add_paragraph()
    pg_gt.paragraph_format.space_before = Pt(0)
    pg_gt.paragraph_format.space_after = Pt(4)

    # Grand Total Box
    gt_b = c_col3.add_table(rows=1, cols=1)
    gt_b.alignment = WD_TABLE_ALIGNMENT.CENTER
    c_gtb = gt_b.cell(0, 0)
    c_gtb.width = Mm(64)
    set_cell_shd(c_gtb, "0F172A")
    set_cell_pad(c_gtb, 25, 25, 30, 30)
    p_gtb = c_gtb.paragraphs[0]
    p_gtb.paragraph_format.space_after = Pt(0)
    p_gtb.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_gtb = p_gtb.add_run("★ GRAND TOTAL SCORECARD ★")
    r_gtb.font.bold = True
    r_gtb.font.size = Pt(7.5)
    r_gtb.font.color.rgb = RGBColor(251, 191, 36)

    gt_grid = c_col3.add_table(rows=3, cols=6)
    gt_grid.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_tbl_borders(gt_grid, color="CBD5E1", sz="5")
    for row in gt_grid.rows:
        for idx in range(6):
            row.cells[idx].width = Mm(64 / 6)

    for i, lbl in enumerate(["R1", "R2", "R3", "R4", "R5", "Joker"]):
        c = gt_grid.cell(0, i)
        set_cell_shd(c, "F1F5F9")
        set_cell_pad(c, 15, 15, 10, 10)
        p = c.paragraphs[0]
        p.paragraph_format.space_after = Pt(0)
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.add_run(lbl).font.bold = True
        p.runs[0].font.size = Pt(6.5)

    for i in range(5):
        c = gt_grid.cell(1, i)
        set_cell_pad(c, 25, 25, 10, 10)
        p = c.paragraphs[0]
        p.paragraph_format.space_after = Pt(0)
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.add_run("[  ]").font.bold = True
        p.runs[0].font.size = Pt(7)

    c_j = gt_grid.cell(1, 5)
    set_cell_shd(c_j, "FEF3C7")
    set_cell_pad(c_j, 25, 25, 10, 10)
    p = c_j.paragraphs[0]
    p.paragraph_format.space_after = Pt(0)
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.add_run("[+ ]").font.bold = True
    p.runs[0].font.size = Pt(7)
    p.runs[0].font.color.rgb = RGBColor(180, 83, 9)

    row2 = gt_grid.rows[2]
    c_f1 = row2.cells[0]
    c_f1.merge(row2.cells[3])
    set_cell_shd(c_f1, "FEF3C7")
    set_cell_pad(c_f1, 30, 30, 20, 20)
    p_f1 = c_f1.paragraphs[0]
    p_f1.paragraph_format.space_after = Pt(0)
    r_f1 = p_f1.add_run("TOTAL: [ ___ / 50 ]")
    r_f1.font.bold = True
    r_f1.font.size = Pt(7.5)
    r_f1.font.color.rgb = RGBColor(146, 64, 14)

    c_f2 = row2.cells[1]
    c_f2.merge(row2.cells[2])
    set_cell_shd(c_f2, "FDE68A")
    set_cell_pad(c_f2, 30, 30, 20, 20)
    p_f2 = c_f2.paragraphs[0]
    p_f2.paragraph_format.space_after = Pt(0)
    p_f2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_f2 = p_f2.add_run("RANK: #[ __ ]")
    r_f2.font.bold = True
    r_f2.font.size = Pt(7.5)
    r_f2.font.color.rgb = RGBColor(146, 64, 14)

    doc.save(output_file)
    print(f"Generated 3-column single-page document: {output_file}")

if __name__ == "__main__":
    out_file = "/home/jakes/repos/quiznight/Beerbox_Pub_Quiz_Single_Page_A4.docx"
    make_3column_single_page(out_file)
