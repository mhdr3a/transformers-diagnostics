import sys
from math import sqrt

def format_label(label):
    if label == "entailment":
        return "entailment"
    else:
        return "not_entailment"

fi = open(sys.argv[1], "r")

first = True
guess_dict = {}
for line in fi:
    if first:
        first = False
        continue
    else:
        parts = line.strip().split(",")
        guess_dict[parts[0].replace("ex", "")] = format_label(parts[1])

fi = open("AX-b.txt", "r")

correct_dict = {}
first = True

lexical_semantics_list = []
predicate_argument_structure_list = []
logic_list = []
knowledge_list = []

for line in fi:
    if first:
        labels = line.strip().split("\t")
        idIndex = labels.index("idx")
        first = False
        continue
    else:
        parts = line.strip().split("\t")
        while len(parts) < 8:
            parts.append("")
        this_line_dict = {}
        for index, label in enumerate(labels):
            if label == "idx":
                continue
            else:
                this_line_dict[label] = parts[index]
        correct_dict[parts[idIndex]] = this_line_dict
        
        if this_line_dict["lexical-semantics"] != "":
            lexical_semantics_subcases = this_line_dict["lexical-semantics"].split(";")
            for subcase in lexical_semantics_subcases:
                if subcase not in lexical_semantics_list:
                    lexical_semantics_list.append(subcase)
        if this_line_dict["predicate-argument-structure"] != "":
            predicate_argument_structure_subcases = this_line_dict["predicate-argument-structure"].split(";")
            for subcase in predicate_argument_structure_subcases:
                if subcase not in predicate_argument_structure_list:
                    predicate_argument_structure_list.append(subcase)
        if this_line_dict["logic"] != "":
            logic_subcases = this_line_dict["logic"].split(";")
            for subcase in logic_subcases:
                if subcase not in logic_list:
                    logic_list.append(subcase)
        if this_line_dict["knowledge"] != "":
            knowledge_subcases = this_line_dict["knowledge"].split(";")
            for subcase in knowledge_subcases:
                if subcase not in knowledge_list:
                    knowledge_list.append(subcase)

lexical_semantics_ent_correct_count_dict = {}
predicate_argument_structure_correct_count_dict = {}
logic_correct_count_dict = {}
knowledge_correct_count_dict = {}
lexical_semantics_ent_incorrect_count_dict = {}
predicate_argument_structure_incorrect_count_dict = {}
logic_incorrect_count_dict = {}
knowledge_incorrect_count_dict = {}
all_heuristics_ent_correct_count = 0
all_heuristics_ent_incorrect_count = 0
all_heuristics_nonent_correct_count = 0
all_heuristics_nonent_incorrect_count = 0
TP = 0
TN = 0
FP = 0
FN = 0

for heuristic in lexical_semantics_list:
    lexical_semantics_ent_correct_count_dict[heuristic] = 0
    lexical_semantics_ent_incorrect_count_dict[heuristic] = 0

for heuristic in predicate_argument_structure_list:
    predicate_argument_structure_correct_count_dict[heuristic] = 0
    predicate_argument_structure_incorrect_count_dict[heuristic] = 0

for heuristic in logic_list:
    logic_correct_count_dict[heuristic] = 0
    logic_incorrect_count_dict[heuristic] = 0

for heuristic in knowledge_list:
    knowledge_correct_count_dict[heuristic] = 0
    knowledge_incorrect_count_dict[heuristic] = 0

for key in correct_dict:
    traits = correct_dict[key]
    lex_list = traits["lexical-semantics"].split(";")
    pred_list = traits["predicate-argument-structure"].split(";")
    log_list = traits["logic"].split(";")
    know_list = traits["knowledge"].split(";")

    guess = guess_dict[key]
    correct = traits["label"]

    if guess == correct:
        if correct == "entailment":
            all_heuristics_ent_correct_count += 1
            TP += 1
        else:
            all_heuristics_nonent_correct_count += 1
            TN += 1
        
        for lex in lex_list:
            if lex != "":
                lexical_semantics_ent_correct_count_dict[lex] += 1
        for pred in pred_list:
            if pred != "":
                predicate_argument_structure_correct_count_dict[pred] += 1
        for log in log_list:
            if log != "":
                logic_correct_count_dict[log] += 1
        for know in know_list:
            if know != "":
                knowledge_correct_count_dict[know] += 1
    else:
        if correct == "entailment":
            all_heuristics_ent_incorrect_count += 1
            FN += 1
        else:
            all_heuristics_nonent_incorrect_count += 1
            FP += 1
        
        for lex in lex_list:
            if lex != "":
                lexical_semantics_ent_incorrect_count_dict[lex] += 1
        for pred in pred_list:
            if pred != "":
                predicate_argument_structure_incorrect_count_dict[pred] += 1
        for log in log_list:
            if log != "":
                logic_incorrect_count_dict[log] += 1
        for know in know_list:
            if know != "":
                knowledge_incorrect_count_dict[know] += 1
    
print("Heuristic entailed results:")
correct = all_heuristics_ent_correct_count
incorrect = all_heuristics_ent_incorrect_count
total = correct + incorrect
percent = correct * 1.0 / total
print("entailment correct predictions: " + str(percent))
print("")
print("Heuristic non-entailed results:")
correct = all_heuristics_nonent_correct_count
incorrect = all_heuristics_nonent_incorrect_count
total = correct + incorrect
percent = correct * 1.0 / total
print("not_entailment correct predictions: " + str(percent))
print("")
print("MCC = " + str((TP * TN - FP * FN)/(sqrt((TP+FP)*(TP+FN)*(TN+FP)*(TN+FN)))))
print("")
print("lexical-semantics results:")
for heuristic in lexical_semantics_list:
    correct = lexical_semantics_ent_correct_count_dict[heuristic]
    incorrect = lexical_semantics_ent_incorrect_count_dict[heuristic]
    total = correct + incorrect
    percent = correct * 1.0 / total
    print(heuristic + ": " + str(percent))
print("")
print("predicate-argument-structure results:")
for heuristic in predicate_argument_structure_list:
    correct = predicate_argument_structure_correct_count_dict[heuristic]
    incorrect = predicate_argument_structure_incorrect_count_dict[heuristic]
    total = correct + incorrect
    percent = correct * 1.0 / total
    print(heuristic + ": " + str(percent))
print("")
print("logic results:")
for heuristic in logic_list:
    correct = logic_correct_count_dict[heuristic]
    incorrect = logic_incorrect_count_dict[heuristic]
    total = correct + incorrect
    percent = correct * 1.0 / total
    print(heuristic + ": " + str(percent))
print("")
print("knowledge results:")
for heuristic in knowledge_list:
    correct = knowledge_correct_count_dict[heuristic]
    incorrect = knowledge_incorrect_count_dict[heuristic]
    total = correct + incorrect
    percent = correct * 1.0 / total
    print(heuristic + ": " + str(percent))
