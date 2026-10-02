# -*- coding: utf-8 -*-
import json
from generate_sets_2_4 import get_set_2, get_set_3, get_set_4
from generate_sets_5_7 import get_set_5, get_set_6, get_set_7
from generate_sets_8_10 import get_set_8, get_set_9, get_set_10

with open('set1.json', 'r', encoding='utf-8') as f:
    set1 = json.load(f)

sets = [
    set1,
    get_set_2(),
    get_set_3(),
    get_set_4(),
    get_set_5(),
    get_set_6(),
    get_set_7(),
    get_set_8(),
    get_set_9(),
    get_set_10()
]

print(f"Total Sets: {len(sets)}")

total_questions = 0
total_tiebreakers = 0
errors = []

for s_idx, s in enumerate(sets):
    set_num = s_idx + 1
    s['setId'] = set_num
    rounds = s.get('rounds', [])
    if len(rounds) != 6:
        errors.append(f"Set {set_num} has {len(rounds)} rounds, expected 6")
    
    for r_idx, r in enumerate(rounds):
        round_id = r.get('roundId')
        questions = r.get('questions', [])
        expected_len = 3 if round_id == 6 else 10
        if len(questions) != expected_len:
            errors.append(f"Set {set_num} Round {round_id} has {len(questions)} questions, expected {expected_len}")
        
        if round_id == 6:
            total_tiebreakers += len(questions)
        else:
            total_questions += len(questions)
            
        for q_idx, q in enumerate(questions):
            q_text = q.get('q', '').strip()
            options = q.get('options', [])
            ans = q.get('a', '').strip()
            notes = q.get('notes', '').strip()
            
            if not q_text:
                errors.append(f"Set {set_num} R{round_id} Q{q_idx+1} missing question text")
            if len(options) != 4:
                errors.append(f"Set {set_num} R{round_id} Q{q_idx+1} has {len(options)} options, expected 4")
            if not any(ans.startswith(letter) for letter in ['A)', 'B)', 'C)', 'D)']):
                errors.append(f"Set {set_num} R{round_id} Q{q_idx+1} answer '{ans}' does not start with valid letter prefix")
            if ans not in options:
                # Check if trimmed letter matches
                matched = False
                for opt in options:
                    if opt.strip() == ans.strip():
                        matched = True
                        break
                if not matched:
                    errors.append(f"Set {set_num} R{round_id} Q{q_idx+1} answer '{ans}' not found in options {options}")
            if not notes:
                errors.append(f"Set {set_num} R{round_id} Q{q_idx+1} missing notes")

if errors:
    print(f"Validation FAILED with {len(errors)} errors:")
    for err in errors[:20]:
        print(f"  - {err}")
    exit(1)

print("Validation PASSED flawlessly!")
print(f"Total Standard Questions: {total_questions} (10 sets x 5 rounds x 10 questions)")
print(f"Total Tie-Breakers: {total_tiebreakers} (10 sets x 3 overtime questions)")
print(f"Grand Total Questions: {total_questions + total_tiebreakers}")

# Write to quizSets.js
js_content = "/* ==========================================================\n"
js_content += "   BEERBOX PUB QUIZ - 10 ROTATING QUESTION SETS (10x5x10)\n"
js_content += "   500 Regulation Questions + 30 Sudden-Death Tie-Breakers\n"
js_content += "   ========================================================== */\n"
js_content += "window.quizSets = " + json.dumps(sets, indent=2, ensure_ascii=False) + ";\n"

with open('quizSets.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

print("quizSets.js written successfully!")
