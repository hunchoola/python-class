from art import text2art

art = text2art("EXAM WIZARD")
print(art)


def exam_wizard():
    print("=============Welcome to the Exam Wizard!=============")
    print("Please answer the following theory questions:\n")

    total_score = 0

    all_questions = [
        {
            "question": "Explain the process of photosynthesis.",
            "keywords": {
                "photosynthesis": 2,
                "light energy": 1,
                "chemical energy": 1,
                "chloroplasts": 2,
                "chlorophyll": 1,
                "carbon dioxide": 1,
                "water": 1,
                "glucose": 1,
                "oxygen": 1,
                "atp": 1
            }
        },
        {
            "question": "What is a noun?",
            "keywords": {
                "name": 3,
                "place": 3,
                "animal": 3,
                "thing": 1,
            }
        },
        {
            "question": "Define computer.",
            "keywords": {
                "hardware": 2,
                "software": 1,
                "data": 1,
                "input": 1,
                "process": 1,
                "output": 1
            }
        },
        {
            "question": "Explain algorithm?",
            "keywords": {
                "step by step": 2,
                "procedure": 1,
                "solving": 2,
                "complex": 1,
                "problem": 2,
            }
        },
        {
            "question": "What are the features to consider before saying a code is a good code?",
            "keywords": {
                "readable": 3,
                "meet user expectations": 3,
                "flexible": 2,
                "portable": 2
            }
        }
    ]

    for exam_question in all_questions:
        print(exam_question["question"])

        student_answer = input(": ").lower()

        for keyword, score in exam_question["keywords"].items():
            if keyword in student_answer:
                total_score += score

    

    print(f"Your total score is: {total_score} out of 50")


exam_wizard()
