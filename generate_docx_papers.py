import json
from pathlib import Path
import docx
from docx.shared import Inches, Pt, RGBColor, Mm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn

def set_cell_shading(cell, color_hex):
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{color_hex}"/>')
    cell._tc.get_or_add_tcPr().append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)

def set_table_borders(table, color="D1D5DB", sz="4"):
    tblPr = table._tbl.tblPr
    borders = parse_xml(f'''
        <w:tblBorders {nsdecls("w")}>
            <w:top w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>
            <w:bottom w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>
            <w:left w:val="none"/>
            <w:right w:val="none"/>
            <w:insideH w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>
            <w:insideV w:val="none"/>
        </w:tblBorders>
    ''')
    tblPr.append(borders)

def build_team_question_paper(quiz_data, output_path):
    doc = docx.Document()
    
    # Configure A4 Margins
    for section in doc.sections:
        section.page_width = Mm(210)
        section.page_height = Mm(297)
        section.top_margin = Mm(12)
        section.bottom_margin = Mm(12)
        section.left_margin = Mm(12)
        section.right_margin = Mm(12)
        
    # Styles
    normal_style = doc.styles['Normal']
    normal_style.font.name = 'Calibri'
    normal_style.font.size = Pt(9.5)
    normal_style.font.color.rgb = RGBColor(30, 41, 59) # Slate 800

    # 1. Header Title
    title_p = doc.add_paragraph()
    title_p.paragraph_format.space_before = Pt(0)
    title_p.paragraph_format.space_after = Pt(2)
    title_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run_brand = title_p.add_run("BEERBOX MIDRAND • LIVE PUB QUIZ NIGHT")
    run_brand.font.size = Pt(16)
    run_brand.font.bold = True
    run_brand.font.color.rgb = RGBColor(180, 83, 9) # Amber 700

    sub_p = doc.add_paragraph()
    sub_p.paragraph_format.space_before = Pt(0)
    sub_p.paragraph_format.space_after = Pt(6)
    sub_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run_sub = sub_p.add_run("Hosted by DJ JC • Official Team Question & Answer Paper")
    run_sub.font.size = Pt(10)
    run_sub.font.bold = True
    run_sub.font.color.rgb = RGBColor(71, 85, 105)

    # 2. Team Info Table
    team_tbl = doc.add_table(rows=2, cols=4)
    team_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(team_tbl, color="CBD5E1", sz="6")
    
    # Widths: Col 0: 20mm, Col 1: 85mm, Col 2: 25mm, Col 3: 56mm
    widths = [Mm(25), Mm(80), Mm(30), Mm(51)]
    for r in team_tbl.rows:
        for idx, width in enumerate(widths):
            r.cells[idx].width = width

    # Row 0: Team Name & Table Number
    cell_t0 = team_tbl.cell(0, 0)
    set_cell_shading(cell_t0, "F8FAFC")
    set_cell_margins(cell_t0, top=80, bottom=80, left=100, right=100)
    p = cell_t0.paragraphs[0]
    p.paragraph_format.space_after = Pt(0)
    r_lbl = p.add_run("Team Name:")
    r_lbl.font.bold = True
    r_lbl.font.size = Pt(9.5)

    cell_t1 = team_tbl.cell(0, 1)
    set_cell_margins(cell_t1, top=80, bottom=80, left=100, right=100)
    p = cell_t1.paragraphs[0]
    p.paragraph_format.space_after = Pt(0)
    p.add_run("________________________________________")

    cell_t2 = team_tbl.cell(0, 2)
    set_cell_shading(cell_t2, "F8FAFC")
    set_cell_margins(cell_t2, top=80, bottom=80, left=100, right=100)
    p = cell_t2.paragraphs[0]
    p.paragraph_format.space_after = Pt(0)
    r_lbl = p.add_run("Table No:")
    r_lbl.font.bold = True
    r_lbl.font.size = Pt(9.5)

    cell_t3 = team_tbl.cell(0, 3)
    set_cell_margins(cell_t3, top=80, bottom=80, left=100, right=100)
    p = cell_t3.paragraphs[0]
    p.paragraph_format.space_after = Pt(0)
    p.add_run("Table # [ _______ ]")

    # Row 1: Captain & Joker Round
    cell_c0 = team_tbl.cell(1, 0)
    set_cell_shading(cell_c0, "F8FAFC")
    set_cell_margins(cell_c0, top=80, bottom=80, left=100, right=100)
    p = cell_c0.paragraphs[0]
    p.paragraph_format.space_after = Pt(0)
    r_lbl = p.add_run("Captain:")
    r_lbl.font.bold = True
    r_lbl.font.size = Pt(9.5)

    cell_c1 = team_tbl.cell(1, 1)
    set_cell_margins(cell_c1, top=80, bottom=80, left=100, right=100)
    p = cell_c1.paragraphs[0]
    p.paragraph_format.space_after = Pt(0)
    p.add_run("________________________________________")

    cell_c2 = team_tbl.cell(1, 2)
    set_cell_shading(cell_c2, "FEF3C7") # Warm yellow for Joker
    set_cell_margins(cell_c2, top=80, bottom=80, left=100, right=100)
    p = cell_c2.paragraphs[0]
    p.paragraph_format.space_after = Pt(0)
    r_lbl = p.add_run("★ JOKER (x2):")
    r_lbl.font.bold = True
    r_lbl.font.size = Pt(9)
    r_lbl.font.color.rgb = RGBColor(180, 83, 9)

    cell_c3 = team_tbl.cell(1, 3)
    set_cell_shading(cell_c3, "FFFBEB")
    set_cell_margins(cell_c3, top=80, bottom=80, left=100, right=100)
    p = cell_c3.paragraphs[0]
    p.paragraph_format.space_after = Pt(0)
    p.add_run("[ ] R1  [ ] R2  [ ] R3  [ ] R4  [ ] R5")
    p.runs[0].font.size = Pt(8.5)
    p.runs[0].font.bold = True

    # Instructions line
    inst_p = doc.add_paragraph()
    inst_p.paragraph_format.space_before = Pt(4)
    inst_p.paragraph_format.space_after = Pt(8)
    inst_run = inst_p.add_run("Instructions: Circle your chosen letter (A, B, C, or D) and write it in the 'Your Pick' box. Papers are swapped for marking at the end of each round. Strictly No Shazam / Google!")
    inst_run.font.italic = True
    inst_run.font.size = Pt(8)
    inst_run.font.color.rgb = RGBColor(100, 116, 139)

    # 3. Render Each Round
    for r_idx, r in enumerate(quiz_data):
        is_tiebreaker = (r["roundId"] == 6)
        
        # Round Header Table / Banner
        banner_tbl = doc.add_table(rows=1, cols=2)
        banner_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        banner_cell_left = banner_tbl.cell(0, 0)
        banner_cell_right = banner_tbl.cell(0, 1)
        banner_cell_left.width = Mm(140)
        banner_cell_right.width = Mm(46)
        
        bg_color = "7E22CE" if is_tiebreaker else "1E293B" # Purple for tiebreaker, Slate for rounds
        set_cell_shading(banner_cell_left, bg_color)
        set_cell_shading(banner_cell_right, bg_color)
        set_cell_margins(banner_cell_left, top=90, bottom=90, left=120, right=120)
        set_cell_margins(banner_cell_right, top=90, bottom=90, left=120, right=120)
        
        p_left = banner_cell_left.paragraphs[0]
        p_left.paragraph_format.space_after = Pt(0)
        r_title = p_left.add_run(f"{r['title'].upper()}")
        r_title.font.bold = True
        r_title.font.size = Pt(10)
        r_title.font.color.rgb = RGBColor(254, 243, 199) # Warm cream
        
        p_sub = banner_cell_left.add_paragraph()
        p_sub.paragraph_format.space_before = Pt(1)
        p_sub.paragraph_format.space_after = Pt(0)
        r_theme = p_sub.add_run(r['theme'])
        r_theme.font.size = Pt(8)
        r_theme.font.color.rgb = RGBColor(203, 213, 225)
        
        p_right = banner_cell_right.paragraphs[0]
        p_right.paragraph_format.space_after = Pt(0)
        p_right.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        r_badge = p_right.add_run(r['badge'])
        r_badge.font.bold = True
        r_badge.font.size = Pt(9)
        r_badge.font.color.rgb = RGBColor(251, 191, 36) # Amber gold

        # Question Table
        q_count = len(r['questions'])
        q_tbl = doc.add_table(rows=q_count + 1, cols=4)
        q_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        set_table_borders(q_tbl, color="E2E8F0", sz="4")
        
        col_widths = [Mm(10), Mm(136), Mm(22), Mm(18)]
        for row in q_tbl.rows:
            for idx, w in enumerate(col_widths):
                row.cells[idx].width = w

        # Header Row
        hdr_row = q_tbl.rows[0]
        headers = ["#", "Question & Multiple-Choice Options", "Your Pick", "Score"]
        aligns = [WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.CENTER]
        
        for idx, text in enumerate(headers):
            cell = hdr_row.cells[idx]
            set_cell_shading(cell, "F1F5F9")
            set_cell_margins(cell, top=60, bottom=60, left=80, right=80)
            p = cell.paragraphs[0]
            p.paragraph_format.space_after = Pt(0)
            p.alignment = aligns[idx]
            run = p.add_run(text)
            run.font.bold = True
            run.font.size = Pt(8.5)
            run.font.color.rgb = RGBColor(51, 65, 85)

        # Questions Rows
        for q_idx, q in enumerate(r['questions']):
            row = q_tbl.rows[q_idx + 1]
            
            # Col 0: Q Number
            c0 = row.cells[0]
            set_cell_margins(c0, top=50, bottom=50, left=60, right=60)
            c0.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
            p0 = c0.paragraphs[0]
            p0.paragraph_format.space_after = Pt(0)
            p0.alignment = WD_ALIGN_PARAGRAPH.CENTER
            run0 = p0.add_run(f"Q{q_idx + 1}")
            run0.font.bold = True
            run0.font.size = Pt(9)
            run0.font.color.rgb = RGBColor(100, 116, 139)
            
            # Col 1: Question Text & Options
            c1 = row.cells[1]
            set_cell_margins(c1, top=60, bottom=60, left=80, right=80)
            p1 = c1.paragraphs[0]
            p1.paragraph_format.space_after = Pt(2)
            run_q = p1.add_run(q['q'])
            run_q.font.bold = True
            run_q.font.size = Pt(9)
            run_q.font.color.rgb = RGBColor(15, 23, 42)
            
            # Options formatting
            if 'options' in q and q['options']:
                p_opts = c1.add_paragraph()
                p_opts.paragraph_format.space_before = Pt(0)
                p_opts.paragraph_format.space_after = Pt(0)
                opts_text = "     ".join([f"○ {opt}" for opt in q['options']])
                run_opts = p_opts.add_run(opts_text)
                run_opts.font.size = Pt(8)
                run_opts.font.color.rgb = RGBColor(71, 85, 105)

            # Col 2: Your Pick
            c2 = row.cells[2]
            set_cell_margins(c2, top=60, bottom=60, left=60, right=60)
            c2.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
            p2 = c2.paragraphs[0]
            p2.paragraph_format.space_after = Pt(0)
            p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
            run_box = p2.add_run("[       ]")
            run_box.font.bold = True
            run_box.font.size = Pt(10)
            run_box.font.color.rgb = RGBColor(148, 163, 184)
            
            # Col 3: Score
            c3 = row.cells[3]
            set_cell_margins(c3, top=60, bottom=60, left=60, right=60)
            c3.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
            p3 = c3.paragraphs[0]
            p3.paragraph_format.space_after = Pt(0)
            p3.alignment = WD_ALIGN_PARAGRAPH.CENTER
            run_s = p3.add_run("[   ]")
            run_s.font.size = Pt(9.5)
            run_s.font.color.rgb = RGBColor(203, 213, 225)

        # Round Subtotal Bar
        subtotal_tbl = doc.add_table(rows=1, cols=3)
        subtotal_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        set_table_borders(subtotal_tbl, color="CBD5E1", sz="6")
        
        st_widths = [Mm(60), Mm(66), Mm(60)]
        for idx, w in enumerate(st_widths):
            subtotal_tbl.cell(0, idx).width = w

        c_st0 = subtotal_tbl.cell(0, 0)
        set_cell_shading(c_st0, "FEF3C7") # Light amber
        set_cell_margins(c_st0, top=70, bottom=70, left=100, right=100)
        p = c_st0.paragraphs[0]
        p.paragraph_format.space_after = Pt(0)
        r1 = p.add_run(f"Round {r['roundId']} Base Score:  [ ____ / {q_count} ]")
        r1.font.bold = True
        r1.font.size = Pt(8.5)

        c_st1 = subtotal_tbl.cell(0, 1)
        set_cell_shading(c_st1, "FFFBEB")
        set_cell_margins(c_st1, top=70, bottom=70, left=100, right=100)
        p = c_st1.paragraphs[0]
        p.paragraph_format.space_after = Pt(0)
        if not is_tiebreaker:
            r2 = p.add_run("Joker Active?  [ ] YES (x2)   [ ] NO")
        else:
            r2 = p.add_run("Tie-Breaker: Closest Estimate")
        r2.font.bold = True
        r2.font.size = Pt(8.5)

        c_st2 = subtotal_tbl.cell(0, 2)
        set_cell_shading(c_st2, "FDE68A") # Darker warm amber
        set_cell_margins(c_st2, top=70, bottom=70, left=100, right=100)
        p = c_st2.paragraphs[0]
        p.paragraph_format.space_after = Pt(0)
        p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        r3 = p.add_run(f"Round {r['roundId']} Official Total:  [ _______ ]")
        r3.font.bold = True
        r3.font.size = Pt(9)
        r3.font.color.rgb = RGBColor(146, 64, 14)

        # Spacing after round
        sp_p = doc.add_paragraph()
        sp_p.paragraph_format.space_before = Pt(0)
        sp_p.paragraph_format.space_after = Pt(6)

        # Add page break after Round 2 and Round 4 to keep A4 printout organized
        if r['roundId'] == 2:
            doc.add_page_break()
        elif r['roundId'] == 4:
            doc.add_page_break()

    # 4. Master Grand Total Calculation Scorecard
    doc.add_paragraph()
    gt_banner = doc.add_table(rows=1, cols=1)
    gt_banner.alignment = WD_TABLE_ALIGNMENT.CENTER
    c = gt_banner.cell(0, 0)
    c.width = Mm(186)
    set_cell_shading(c, "0F172A") # Midnight
    set_cell_margins(c, top=100, bottom=100, left=120, right=120)
    p = c.paragraphs[0]
    p.paragraph_format.space_after = Pt(0)
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_gt = p.add_run("★ OFFICIAL GRAND TOTAL SCORECARD (END OF GAME) ★")
    r_gt.font.bold = True
    r_gt.font.size = Pt(11)
    r_gt.font.color.rgb = RGBColor(251, 191, 36)

    gt_tbl = doc.add_table(rows=3, cols=6)
    gt_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(gt_tbl, color="CBD5E1", sz="6")
    
    gt_col_w = Mm(31)
    for row in gt_tbl.rows:
        for idx in range(6):
            row.cells[idx].width = gt_col_w

    # Row 0: Labels
    round_labels = ["Round 1", "Round 2", "Round 3", "Round 4", "Round 5", "Joker Bonus"]
    for idx, lbl in enumerate(round_labels):
        cell = gt_tbl.cell(0, idx)
        set_cell_shading(cell, "F1F5F9")
        set_cell_margins(cell, top=70, bottom=70, left=80, right=80)
        p = cell.paragraphs[0]
        p.paragraph_format.space_after = Pt(0)
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(lbl)
        r.font.bold = True
        r.font.size = Pt(9)

    # Row 1: Score Inputs
    for idx in range(5):
        cell = gt_tbl.cell(1, idx)
        set_cell_margins(cell, top=90, bottom=90, left=80, right=80)
        p = cell.paragraphs[0]
        p.paragraph_format.space_after = Pt(0)
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run("[   / 10 ]")
        r.font.bold = True
        r.font.size = Pt(10)

    cell_jb = gt_tbl.cell(1, 5)
    set_cell_shading(cell_jb, "FEF3C7")
    set_cell_margins(cell_jb, top=90, bottom=90, left=80, right=80)
    p = cell_jb.paragraphs[0]
    p.paragraph_format.space_after = Pt(0)
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run("[ + ____ ]")
    r.font.bold = True
    r.font.size = Pt(10)
    r.font.color.rgb = RGBColor(180, 83, 9)

    # Row 2: Final Grand Total spanning across
    row2 = gt_tbl.rows[2]
    # Merge cells 0 to 3 for final total text, 4 to 5 for rank
    c_final = row2.cells[0]
    c_final.merge(row2.cells[3])
    set_cell_shading(c_final, "FEF3C7")
    set_cell_margins(c_final, top=100, bottom=100, left=120, right=120)
    p = c_final.paragraphs[0]
    p.paragraph_format.space_after = Pt(0)
    r = p.add_run("FINAL TOURNAMENT SCORE:   [ ____________ / 50 ]")
    r.font.bold = True
    r.font.size = Pt(11)
    r.font.color.rgb = RGBColor(146, 64, 14)

    c_rank = row2.cells[1] # Merged cell index
    c_rank.merge(row2.cells[2])
    set_cell_shading(c_rank, "FDE68A")
    set_cell_margins(c_rank, top=100, bottom=100, left=120, right=120)
    p = c_rank.paragraphs[0]
    p.paragraph_format.space_after = Pt(0)
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run("FINAL RANK:  # [ ______ ]")
    r.font.bold = True
    r.font.size = Pt(11)
    r.font.color.rgb = RGBColor(146, 64, 14)

    # Signoff line
    so_p = doc.add_paragraph()
    so_p.paragraph_format.space_before = Pt(8)
    so_p.paragraph_format.space_after = Pt(0)
    so_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_so = so_p.add_run("Official Marker Signature: _______________________      DJ JC Verified: [  ✓  ]")
    r_so.font.size = Pt(8.5)
    r_so.font.italic = True
    r_so.font.color.rgb = RGBColor(100, 116, 139)

    doc.save(str(output_path))
    print(f"Successfully generated Question Paper: {output_path}")

def build_host_answer_key(quiz_data, output_path):
    doc = docx.Document()
    
    # Configure A4 Margins
    for section in doc.sections:
        section.page_width = Mm(210)
        section.page_height = Mm(297)
        section.top_margin = Mm(12)
        section.bottom_margin = Mm(12)
        section.left_margin = Mm(12)
        section.right_margin = Mm(12)
        
    normal_style = doc.styles['Normal']
    normal_style.font.name = 'Calibri'
    normal_style.font.size = Pt(9.5)

    # Title
    title_p = doc.add_paragraph()
    title_p.paragraph_format.space_before = Pt(0)
    title_p.paragraph_format.space_after = Pt(2)
    title_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run_brand = title_p.add_run("DJ JC @ BEERBOX MIDRAND • OFFICIAL MASTER ANSWER KEY")
    run_brand.font.size = Pt(15)
    run_brand.font.bold = True
    run_brand.font.color.rgb = RGBColor(180, 83, 9)

    sub_p = doc.add_paragraph()
    sub_p.paragraph_format.space_before = Pt(0)
    sub_p.paragraph_format.space_after = Pt(8)
    sub_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run_sub = sub_p.add_run("Confidential Host & Marker Scoring Guide • All 50 Questions + Tie-Breakers")
    run_sub.font.size = Pt(10)
    run_sub.font.bold = True
    run_sub.font.color.rgb = RGBColor(71, 85, 105)

    for r in quiz_data:
        banner_tbl = doc.add_table(rows=1, cols=1)
        banner_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        c = banner_tbl.cell(0, 0)
        c.width = Mm(186)
        set_cell_shading(c, "0F172A")
        set_cell_margins(c, top=80, bottom=80, left=100, right=100)
        p = c.paragraphs[0]
        p.paragraph_format.space_after = Pt(0)
        r_title = p.add_run(f"{r['title'].upper()} — OFFICIAL ANSWERS")
        r_title.font.bold = True
        r_title.font.size = Pt(10)
        r_title.font.color.rgb = RGBColor(251, 191, 36)

        ans_tbl = doc.add_table(rows=len(r['questions']) + 1, cols=4)
        ans_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        set_table_borders(ans_tbl, color="E2E8F0", sz="4")
        
        col_w = [Mm(10), Mm(90), Mm(40), Mm(46)]
        for row in ans_tbl.rows:
            for idx, w in enumerate(col_w):
                row.cells[idx].width = w

        # Header
        hdr = ans_tbl.rows[0]
        hdr_texts = ["#", "Question", "Official Answer", "Host Notes / Trivia"]
        for idx, text in enumerate(hdr_texts):
            cell = hdr.cells[idx]
            set_cell_shading(cell, "F1F5F9")
            set_cell_margins(cell, top=60, bottom=60, left=80, right=80)
            p = cell.paragraphs[0]
            p.paragraph_format.space_after = Pt(0)
            run = p.add_run(text)
            run.font.bold = True
            run.font.size = Pt(8.5)

        for q_idx, q in enumerate(r['questions']):
            row = ans_tbl.rows[q_idx + 1]
            # Q#
            c0 = row.cells[0]
            set_cell_margins(c0, top=50, bottom=50, left=60, right=60)
            p = c0.paragraphs[0]
            p.paragraph_format.space_after = Pt(0)
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.add_run(f"Q{q_idx + 1}").font.bold = True

            # Question
            c1 = row.cells[1]
            set_cell_margins(c1, top=50, bottom=50, left=80, right=80)
            p = c1.paragraphs[0]
            p.paragraph_format.space_after = Pt(0)
            p.add_run(q['q']).font.size = Pt(8.5)

            # Answer
            c2 = row.cells[2]
            set_cell_shading(c2, "ECFDF5") # Soft green
            set_cell_margins(c2, top=50, bottom=50, left=80, right=80)
            p = c2.paragraphs[0]
            p.paragraph_format.space_after = Pt(0)
            run_a = p.add_run(q['a'])
            run_a.font.bold = True
            run_a.font.size = Pt(9)
            run_a.font.color.rgb = RGBColor(5, 150, 105) # Emerald 600

            # Host Notes
            c3 = row.cells[3]
            set_cell_margins(c3, top=50, bottom=50, left=80, right=80)
            p = c3.paragraphs[0]
            p.paragraph_format.space_after = Pt(0)
            run_n = p.add_run(q.get('notes', ''))
            run_n.font.italic = True
            run_n.font.size = Pt(8)
            run_n.font.color.rgb = RGBColor(100, 116, 139)

        sp = doc.add_paragraph()
        sp.paragraph_format.space_before = Pt(0)
        sp.paragraph_format.space_after = Pt(6)

    doc.save(str(output_path))
    print(f"Successfully generated Host Answer Key: {output_path}")

if __name__ == "__main__":
    html_path = "/home/jakes/repos/quiznight/index.html"
    with open(html_path, "r", encoding="utf-8") as f:
        content = f.read()

    start_marker = "const quizData = "
    end_marker = ";\n    /* ==========================================================\n       APPLICATION STATE"
    start_idx = content.find(start_marker) + len(start_marker)
    end_idx = content.find(end_marker, start_idx)

    quiz_data = json.loads(content[start_idx:end_idx].strip())
    
    out_dir = Path("/home/jakes/repos/quiznight")
    team_paper = out_dir / "Beerbox_Pub_Quiz_Team_Question_Paper_A4.docx"
    host_key = out_dir / "Beerbox_Pub_Quiz_Host_Master_Answer_Key_A4.docx"
    
    build_team_question_paper(quiz_data, team_paper)
    build_host_answer_key(quiz_data, host_key)
