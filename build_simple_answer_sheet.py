import docx
from docx.shared import Pt, RGBColor, Mm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls
from pathlib import Path

def set_cell_shd(cell, hex_color):
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hex_color}"/>')
    cell._tc.get_or_add_tcPr().append(shd)

def set_cell_pad(cell, top=60, bottom=60, left=80, right=80):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)

def set_tbl_borders(table, color="D1D5DB", sz="4"):
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

def make_answer_sheet(output_file):
    doc = docx.Document()
    
    # Configure A4 Margins - compact single page
    section = doc.sections[0]
    section.page_width = Mm(210)
    section.page_height = Mm(297)
    section.top_margin = Mm(8)
    section.bottom_margin = Mm(8)
    section.left_margin = Mm(10)
    section.right_margin = Mm(10)
    
    normal = doc.styles['Normal']
    normal.font.name = 'Calibri'
    normal.font.size = Pt(8.5)
    normal.font.color.rgb = RGBColor(15, 23, 42)

    # 1. Header Banner
    title_p = doc.add_paragraph()
    title_p.paragraph_format.space_before = Pt(0)
    title_p.paragraph_format.space_after = Pt(1)
    title_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_title = title_p.add_run("BEERBOX MIDRAND • OFFICIAL PUB QUIZ ANSWER SHEET")
    r_title.font.bold = True
    r_title.font.size = Pt(13)
    r_title.font.color.rgb = RGBColor(180, 83, 9)

    sub_p = doc.add_paragraph()
    sub_p.paragraph_format.space_before = Pt(0)
    sub_p.paragraph_format.space_after = Pt(4)
    sub_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_sub = sub_p.add_run("Hosted by TJ Entertainment • Mark answers clearly in the A B C D boxes • Swapped for marking after each round")
    r_sub.font.size = Pt(8)
    r_sub.font.color.rgb = RGBColor(100, 116, 139)

    # 2. Team Details Bar Table
    team_tbl = doc.add_table(rows=1, cols=4)
    team_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_tbl_borders(team_tbl, color="CBD5E1", sz="6")
    col_w = [Mm(65), Mm(30), Mm(50), Mm(45)]
    for i, w in enumerate(col_w):
        team_tbl.cell(0, i).width = w

    c0 = team_tbl.cell(0, 0)
    set_cell_pad(c0, 60, 60, 80, 80)
    p0 = c0.paragraphs[0]
    p0.paragraph_format.space_after = Pt(0)
    p0.add_run("Team Name: ").font.bold = True
    p0.add_run("_______________________")

    c1 = team_tbl.cell(0, 1)
    set_cell_pad(c1, 60, 60, 80, 80)
    p1 = c1.paragraphs[0]
    p1.paragraph_format.space_after = Pt(0)
    p1.add_run("Table #: ").font.bold = True
    p1.add_run("____")

    c2 = team_tbl.cell(0, 2)
    set_cell_pad(c2, 60, 60, 80, 80)
    p2 = c2.paragraphs[0]
    p2.paragraph_format.space_after = Pt(0)
    p2.add_run("Captain: ").font.bold = True
    p2.add_run("___________________")

    c3 = team_tbl.cell(0, 3)
    set_cell_shd(c3, "FEF3C7")
    set_cell_pad(c3, 60, 60, 80, 80)
    p3 = c3.paragraphs[0]
    p3.paragraph_format.space_after = Pt(0)
    r_j = p3.add_run("★ JOKER (x2): ")
    r_j.font.bold = True
    r_j.font.color.rgb = RGBColor(180, 83, 9)
    p3.add_run("R1 [ ] R2 [ ] R3 [ ] R4 [ ] R5 [ ]").font.bold = True

    # Spacing
    sp = doc.add_paragraph()
    sp.paragraph_format.space_before = Pt(3)
    sp.paragraph_format.space_after = Pt(3)

    # 3. Two-Column Layout for Rounds 1-4
    # We will use an outer container table with 2 columns: Left Col (R1, R2), Right Col (R3, R4)
    main_tbl = doc.add_table(rows=1, cols=2)
    main_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    main_tbl.cell(0, 0).width = Mm(93)
    main_tbl.cell(0, 1).width = Mm(93)
    
    # Remove outer table borders
    set_tbl_borders(main_tbl, color="FFFFFF", sz="0")
    set_cell_pad(main_tbl.cell(0, 0), 0, 0, 0, 60)
    set_cell_pad(main_tbl.cell(0, 1), 0, 0, 60, 0)

    def build_round_block(container_cell, round_num, round_title, badge_text):
        # Banner Table
        b_tbl = container_cell.add_table(rows=1, cols=2)
        b_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        b_tbl.cell(0, 0).width = Mm(68)
        b_tbl.cell(0, 1).width = Mm(25)
        set_cell_shd(b_tbl.cell(0, 0), "1E293B")
        set_cell_shd(b_tbl.cell(0, 1), "1E293B")
        set_cell_pad(b_tbl.cell(0, 0), 40, 40, 60, 60)
        set_cell_pad(b_tbl.cell(0, 1), 40, 40, 60, 60)
        
        p_l = b_tbl.cell(0, 0).paragraphs[0]
        p_l.paragraph_format.space_after = Pt(0)
        r_bt = p_l.add_run(f"ROUND {round_num}: {round_title.upper()}")
        r_bt.font.bold = True
        r_bt.font.size = Pt(8.5)
        r_bt.font.color.rgb = RGBColor(254, 243, 199)

        p_r = b_tbl.cell(0, 1).paragraphs[0]
        p_r.paragraph_format.space_after = Pt(0)
        p_r.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        r_bb = p_r.add_run(badge_text)
        r_bb.font.bold = True
        r_bb.font.size = Pt(7.5)
        r_bb.font.color.rgb = RGBColor(251, 191, 36)

        # 10 Questions Grid Table
        q_tbl = container_cell.add_table(rows=11, cols=4)
        q_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        set_tbl_borders(q_tbl, color="CBD5E1", sz="4")
        
        q_widths = [Mm(9), Mm(54), Mm(16), Mm(14)]
        for row in q_tbl.rows:
            for idx, w in enumerate(q_widths):
                row.cells[idx].width = w

        # Header Row
        hdr = q_tbl.rows[0]
        hdr_labels = ["#", "Select Answer (Tick / Circle)", "Pick", "Mark"]
        hdr_aligns = [WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.CENTER]
        for idx, text in enumerate(hdr_labels):
            c = hdr.cells[idx]
            set_cell_shd(c, "F1F5F9")
            set_cell_pad(c, 30, 30, 40, 40)
            p = c.paragraphs[0]
            p.paragraph_format.space_after = Pt(0)
            p.alignment = hdr_aligns[idx]
            r = p.add_run(text)
            r.font.bold = True
            r.font.size = Pt(7.5)
            r.font.color.rgb = RGBColor(71, 85, 105)

        # Rows 1 to 10
        for q in range(1, 11):
            row = q_tbl.rows[q]
            
            # Col 0: Q Number
            c0 = row.cells[0]
            set_cell_pad(c0, 25, 25, 30, 30)
            p0 = c0.paragraphs[0]
            p0.paragraph_format.space_after = Pt(0)
            p0.alignment = WD_ALIGN_PARAGRAPH.CENTER
            r0 = p0.add_run(f"Q{q}")
            r0.font.bold = True
            r0.font.size = Pt(8)
            r0.font.color.rgb = RGBColor(100, 116, 139)

            # Col 1: ABCD Blocks
            c1 = row.cells[1]
            set_cell_pad(c1, 25, 25, 40, 40)
            p1 = c1.paragraphs[0]
            p1.paragraph_format.space_after = Pt(0)
            r1 = p1.add_run("[ A ]    [ B ]    [ C ]    [ D ]")
            r1.font.bold = True
            r1.font.size = Pt(8)
            r1.font.color.rgb = RGBColor(30, 41, 59)

            # Col 2: Your Pick write-in
            c2 = row.cells[2]
            set_cell_pad(c2, 25, 25, 30, 30)
            p2 = c2.paragraphs[0]
            p2.paragraph_format.space_after = Pt(0)
            p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
            r2 = p2.add_run("[    ]")
            r2.font.bold = True
            r2.font.size = Pt(8.5)
            r2.font.color.rgb = RGBColor(148, 163, 184)

            # Col 3: Score tick
            c3 = row.cells[3]
            set_cell_pad(c3, 25, 25, 30, 30)
            p3 = c3.paragraphs[0]
            p3.paragraph_format.space_after = Pt(0)
            p3.alignment = WD_ALIGN_PARAGRAPH.CENTER
            r3 = p3.add_run("[  ]")
            r3.font.size = Pt(8)
            r3.font.color.rgb = RGBColor(203, 213, 225)

        # Subtotal Row at bottom of round
        sub_tbl = container_cell.add_table(rows=1, cols=2)
        sub_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        set_tbl_borders(sub_tbl, color="CBD5E1", sz="6")
        sub_tbl.cell(0, 0).width = Mm(52)
        sub_tbl.cell(0, 1).width = Mm(41)

        c_s0 = sub_tbl.cell(0, 0)
        set_cell_shd(c_s0, "FEF3C7")
        set_cell_pad(c_s0, 40, 40, 60, 60)
        ps0 = c_s0.paragraphs[0]
        ps0.paragraph_format.space_after = Pt(0)
        rs0 = ps0.add_run(f"R{round_num} Subtotal: [ ___ / 10 ]")
        rs0.font.bold = True
        rs0.font.size = Pt(8)

        c_s1 = sub_tbl.cell(0, 1)
        set_cell_shd(c_s1, "FDE68A")
        set_cell_pad(c_s1, 40, 40, 60, 60)
        ps1 = c_s1.paragraphs[0]
        ps1.paragraph_format.space_after = Pt(0)
        ps1.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        rs1 = ps1.add_run(f"Round {round_num} Total: [ _____ ]")
        rs1.font.bold = True
        rs1.font.size = Pt(8.5)
        rs1.font.color.rgb = RGBColor(146, 64, 14)

        # Gap paragraph
        p_gap = container_cell.add_paragraph()
        p_gap.paragraph_format.space_before = Pt(0)
        p_gap.paragraph_format.space_after = Pt(5)

    # Build Left Column: Round 1 & Round 2
    cell_left = main_tbl.cell(0, 0)
    build_round_block(cell_left, 1, "Bar Warm-Up", "10 Pts")
    build_round_block(cell_left, 2, "Beat & Screen", "10 Pts")

    # Build Right Column: Round 3 & Round 4
    cell_right = main_tbl.cell(0, 1)
    build_round_block(cell_right, 3, "Rugby, Cricket & Sports", "10 Pts")
    build_round_block(cell_right, 4, "World & Bar Science", "10 Pts")

    # 4. Bottom Section: Round 5 (Left) + Tie-Breaker & Grand Total (Right)
    bot_tbl = doc.add_table(rows=1, cols=2)
    bot_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    bot_tbl.cell(0, 0).width = Mm(93)
    bot_tbl.cell(0, 1).width = Mm(93)
    set_tbl_borders(bot_tbl, color="FFFFFF", sz="0")
    set_cell_pad(bot_tbl.cell(0, 0), 0, 0, 0, 60)
    set_cell_pad(bot_tbl.cell(0, 1), 0, 0, 60, 0)

    # Left: Round 5
    build_round_block(bot_tbl.cell(0, 0), 5, "Pub Mastermind", "10 Pts")

    # Right: Tie-Breakers + Grand Total Scorecard
    cell_br = bot_tbl.cell(0, 1)
    
    # Tie-Breaker Table
    tb_b = cell_br.add_table(rows=1, cols=2)
    tb_b.alignment = WD_TABLE_ALIGNMENT.CENTER
    tb_b.cell(0, 0).width = Mm(68)
    tb_b.cell(0, 1).width = Mm(25)
    set_cell_shd(tb_b.cell(0, 0), "581C87") # Deep Purple
    set_cell_shd(tb_b.cell(0, 1), "581C87")
    set_cell_pad(tb_b.cell(0, 0), 40, 40, 60, 60)
    set_cell_pad(tb_b.cell(0, 1), 40, 40, 60, 60)
    
    ptb = tb_b.cell(0, 0).paragraphs[0]
    ptb.paragraph_format.space_after = Pt(0)
    rtb = ptb.add_run("SUDDEN-DEATH TIE-BREAKERS")
    rtb.font.bold = True
    rtb.font.size = Pt(8.5)
    rtb.font.color.rgb = RGBColor(243, 232, 255)

    ptb_r = tb_b.cell(0, 1).paragraphs[0]
    ptb_r.paragraph_format.space_after = Pt(0)
    ptb_r.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    rtbr = ptb_r.add_run("Closest Win")
    rtbr.font.bold = True
    rtbr.font.size = Pt(7.5)
    rtbr.font.color.rgb = RGBColor(216, 180, 254)

    # 3 Tie-Breaker rows
    tb_grid = cell_br.add_table(rows=4, cols=4)
    tb_grid.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_tbl_borders(tb_grid, color="CBD5E1", sz="4")
    for row in tb_grid.rows:
        for idx, w in enumerate([Mm(9), Mm(54), Mm(16), Mm(14)]):
            row.cells[idx].width = w

    # Header
    tb_hdr = tb_grid.rows[0]
    for idx, text in enumerate(["#", "Tie-Breaker Options / Guess", "Estimate", "Mark"]):
        c = tb_hdr.cells[idx]
        set_cell_shd(c, "FAF5FF")
        set_cell_pad(c, 30, 30, 40, 40)
        p = c.paragraphs[0]
        p.paragraph_format.space_after = Pt(0)
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER if idx != 1 else WD_ALIGN_PARAGRAPH.LEFT
        r = p.add_run(text)
        r.font.bold = True
        r.font.size = Pt(7.5)
        r.font.color.rgb = RGBColor(107, 33, 168)

    for q in range(1, 4):
        row = tb_grid.rows[q]
        c0 = row.cells[0]
        set_cell_pad(c0, 25, 25, 30, 30)
        p0 = c0.paragraphs[0]
        p0.paragraph_format.space_after = Pt(0)
        p0.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p0.add_run(f"TB{q}").font.bold = True
        p0.runs[0].font.size = Pt(8)

        c1 = row.cells[1]
        set_cell_pad(c1, 25, 25, 40, 40)
        p1 = c1.paragraphs[0]
        p1.paragraph_format.space_after = Pt(0)
        p1.add_run("[ A ]    [ B ]    [ C ]    [ D ]").font.bold = True
        p1.runs[0].font.size = Pt(8)

        c2 = row.cells[2]
        set_cell_pad(c2, 25, 25, 30, 30)
        p2 = c2.paragraphs[0]
        p2.paragraph_format.space_after = Pt(0)
        p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p2.add_run("[    ]").font.bold = True
        p2.runs[0].font.size = Pt(8.5)

        c3 = row.cells[3]
        set_cell_pad(c3, 25, 25, 30, 30)
        p3 = c3.paragraphs[0]
        p3.paragraph_format.space_after = Pt(0)
        p3.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p3.add_run("[  ]").font.size = Pt(8)

    # Spacing before Grand Total
    p_sp_gt = cell_br.add_paragraph()
    p_sp_gt.paragraph_format.space_before = Pt(4)
    p_sp_gt.paragraph_format.space_after = Pt(2)

    # Master Grand Total Scorecard Box
    gt_hdr = cell_br.add_table(rows=1, cols=1)
    gt_hdr.alignment = WD_TABLE_ALIGNMENT.CENTER
    c_gth = gt_hdr.cell(0, 0)
    c_gth.width = Mm(93)
    set_cell_shd(c_gth, "0F172A")
    set_cell_pad(c_gth, 40, 40, 60, 60)
    p_gth = c_gth.paragraphs[0]
    p_gth.paragraph_format.space_after = Pt(0)
    p_gth.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_gth = p_gth.add_run("★ OFFICIAL GRAND TOTAL SCORECARD ★")
    r_gth.font.bold = True
    r_gth.font.size = Pt(8.5)
    r_gth.font.color.rgb = RGBColor(251, 191, 36)

    # 6 columns for rounds 1-5 + joker
    gt_grid = cell_br.add_table(rows=3, cols=6)
    gt_grid.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_tbl_borders(gt_grid, color="CBD5E1", sz="6")
    gt_w = Mm(93 / 6)
    for row in gt_grid.rows:
        for idx in range(6):
            row.cells[idx].width = gt_w

    # Row 0: Labels
    r_lbls = ["R1", "R2", "R3", "R4", "R5", "Joker"]
    for idx, lbl in enumerate(r_lbls):
        c = gt_grid.cell(0, idx)
        set_cell_shd(c, "F1F5F9")
        set_cell_pad(c, 25, 25, 20, 20)
        p = c.paragraphs[0]
        p.paragraph_format.space_after = Pt(0)
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(lbl)
        r.font.bold = True
        r.font.size = Pt(7.5)

    # Row 1: Score boxes
    for idx in range(5):
        c = gt_grid.cell(1, idx)
        set_cell_pad(c, 40, 40, 20, 20)
        p = c.paragraphs[0]
        p.paragraph_format.space_after = Pt(0)
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run("[   ]")
        r.font.bold = True
        r.font.size = Pt(8)

    c_jk = gt_grid.cell(1, 5)
    set_cell_shd(c_jk, "FEF3C7")
    set_cell_pad(c_jk, 40, 40, 20, 20)
    p = c_jk.paragraphs[0]
    p.paragraph_format.space_after = Pt(0)
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run("[ +  ]")
    r.font.bold = True
    r.font.size = Pt(8)
    r.font.color.rgb = RGBColor(180, 83, 9)

    # Row 2: Final Grand Total spanning across
    row2 = gt_grid.rows[2]
    c_fin = row2.cells[0]
    c_fin.merge(row2.cells[3])
    set_cell_shd(c_fin, "FEF3C7")
    set_cell_pad(c_fin, 50, 50, 40, 40)
    p_fin = c_fin.paragraphs[0]
    p_fin.paragraph_format.space_after = Pt(0)
    r_fin = p_fin.add_run("GRAND TOTAL:  [ ______ / 50 ]")
    r_fin.font.bold = True
    r_fin.font.size = Pt(8.5)
    r_fin.font.color.rgb = RGBColor(146, 64, 14)

    c_rnk = row2.cells[1]
    c_rnk.merge(row2.cells[2])
    set_cell_shd(c_rnk, "FDE68A")
    set_cell_pad(c_rnk, 50, 50, 40, 40)
    p_rnk = c_rnk.paragraphs[0]
    p_rnk.paragraph_format.space_after = Pt(0)
    p_rnk.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_rnk = p_rnk.add_run("RANK: # [ ___ ]")
    r_rnk.font.bold = True
    r_rnk.font.size = Pt(8.5)
    r_rnk.font.color.rgb = RGBColor(146, 64, 14)

    # Signoff footer line
    p_so = cell_br.add_paragraph()
    p_so.paragraph_format.space_before = Pt(3)
    p_so.paragraph_format.space_after = Pt(0)
    p_so.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_so = p_so.add_run("Marker: __________________   TJ Entertainment Verified: [  ✓  ]")
    r_so.font.size = Pt(7.5)
    r_so.font.italic = True
    r_so.font.color.rgb = RGBColor(100, 116, 139)

    doc.save(output_file)
    print(f"Successfully generated clean 1-page A4 answer sheet: {output_file}")

if __name__ == "__main__":
    out_path = "/home/jakes/repos/quiznight/Beerbox_Pub_Quiz_A4_Answer_Sheet_Simple.docx"
    make_answer_sheet(out_path)
