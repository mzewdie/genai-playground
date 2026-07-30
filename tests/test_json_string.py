import json

json_str="""{ "questions": [ { "type": "multiple_choice", "question": "What is the definition of Nutrition according to the document?", "options": [ "The process of preparing food for consumption.", "The science of food and its relation to health.", "The study of cooking techniques and food preservation.", "The practice of consuming only organic foods." ], "correct_answer": 1, "explanation": "The document defines nutrition as 'the science of food and its relation to health.'" }, { "type": "true_false", "question": "The human body is capable of producing all 22 different amino acids required for protein synthesis.", "correct_answer": false, "explanation": "The document states that the human body is capable of producing 13 of the 22 amino acids, while the other 9, called 'Essential Amino Acids,' must be supplied by food sources." }, { "type": "short_answer", "question": "Name the six essential groups of nutrients broadly classified in the document.", "correct_answer": "Carbohydrates, Proteins, Fats, Vitamins, Minerals, and Water", "explanation": "The document lists Carbohydrates, Proteins, Fats, Vitamins, Minerals, and Water as the six essential groups of nutrients." }, { "type": "multiple_choice", "question": "Which macronutrient is identified as the most concentrated source of energy, providing 9 kcal/g?", "options": [ "Carbohydrates", "Proteins", "Fats", "Vitamins" ], "correct_answer": 2, "explanation": "The document states that 'Fats are the most concentrated source of energy providing 9 kcal/g.'" }, { "type": "true_false", "question": "Water-soluble vitamins, such as B-complex and C, can be stored in the body, while fat-soluble vitamins are easily excreted in urine.", "correct_answer": false, "explanation": "The document states that 'Fat –soluble vitamins can be stored in the body while water soluble vitamins are not and get excreted in urine.'" }, { "type": "short_answer", "question": "What are two primary functions of dietary fiber in the body, as described in the document?", "correct_answer": "Increases gastric motility and aids in digestion; May reduce the risk of developing some diseases like heart disease, diabetes and obesity, and certain cancers.", "explanation": "The document lists 'Increases gastric motility and aids in digestion' and 'May reduce the risk of developing some diseases like heart disease, diabetes and obesity, and certain cancers' as functions of dietary fiber." }, { "type": "multiple_choice", "question": "How is Recommended Dietary Allowance (RDA) defined in the document?", "options": [ "The maximum safe intake level of a nutrient for all individuals.", "The amount of nutrient sufficient for the maintenance of health in nearly all people.", "The average daily nutrient intake level estimated to meet the requirements of half of the healthy individuals in a particular life stage and gender group.", "The minimum amount of a nutrient required to prevent deficiency diseases." ], "correct_answer": 1, "explanation": "RDA is defined as 'the amount of nutrient sufficient for the maintenance of health in nearly all people.'" }, { "type": "true_false", "question": "A diet high in unsaturated fats is associated with a lower level of blood cholesterol and reduces the risk of heart disease.", "correct_answer": true, "explanation": "The document states, 'A diet high in unsaturated fats is associated with a lower level of blood cholesterol and reduces the risk of heart disease.'" }, { "type": "short_answer", "question": "List three physiological functions of food as outlined in the document.", "correct_answer": "Providing energy to carry out voluntary work; Growth or body building; Repair or maintenance of the body cells.", "explanation": "The physiological functions of food include 'Providing energy to carry out voluntary work,' 'Growth or body building,' 'Repair or maintenance of the body cells,' 'Regulation of body processes,' and 'Protective function, increasing one’s resistance to infection.' Any three of these are valid." }, { "type": "multiple_choice", "question": "According to the document, what is the recommended maximum daily intake of salt for adults and children 11 years and over?", "options": [ "Not more than 2g per day", "Not more than 5g per day", "Not more than 10g per day", "Unlimited, as long as blood pressure is normal" ], "correct_answer": 1, "explanation": "The document states, 'It is recommended that adults and children 11 years and over not to have more than 5g of salt per day.'" } ] }

"""

# Step 1: Parse the JSON string into a Python dictionary
data = json.loads(json_str)

# Step 2: Access the list of questions
questions_list = data["questions"]

print(f"Total questions loaded: {len(questions_list)}\n")

for index, item in enumerate(questions_list, start=1):
    q_type = item["type"]
    question_text = item["question"]
    explanation = item["explanation"]

    print(f"--- Question {index} ({q_type}) ---")
    print(f"Q: {question_text}")

    # Check if 'options' exist (only multiple choice has options)
    if "options" in item:
        print("Options:")
        for opt_idx, opt in enumerate(item["options"]):
            print(f"  [{opt_idx}] {opt}")

    # For multiple choice, map the index integer back to the option text
    if q_type == "multiple_choice":
        correct_idx = item["correct_answer"]
        print(f"Correct Answer: Index {correct_idx} -> '{item['options'][correct_idx]}'")
    else:
        print(f"Correct Answer: {item['correct_answer']}")

    print(f"Explanation: {explanation}\n")