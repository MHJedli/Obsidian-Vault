#!/usr/bin/env python3
"""
PCAP-31-03 Practice Exam - Conditionals Focus
30 Questions exclusively about Python Conditionals (if, elif, else)
"""

import random

class PCAPExamConditionals:
    def __init__(self):
        self.score = 0
        self.total_questions = 30
        self.questions = [
            {
                "question": "What is the output of: x = 5\\nif x > 3:\\n    print('yes')?",
                "options": ["A) yes", "B) no", "C) Nothing", "D) Error"],
                "answer": "A"
            },
            {
                "question": "What is the output of: x = 2\\nif x > 3:\\n    print('yes')\\nelse:\\n    print('no')?",
                "options": ["A) yes", "B) no", "C) Nothing", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: x = 5\\nif x > 10:\\n    print('a')\\nelif x > 3:\\n    print('b')\\nelse:\\n    print('c')?",
                "options": ["A) a", "B) b", "C) c", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: x = 5\\nif x > 3 and x < 10:\\n    print('yes')?",
                "options": ["A) yes", "B) no", "C) Nothing", "D) Error"],
                "answer": "A"
            },
            {
                "question": "What is the output of: x = 5\\nif x > 10 or x < 10:\\n    print('yes')?",
                "options": ["A) yes", "B) no", "C) Nothing", "D) Error"],
                "answer": "A"
            },
            {
                "question": "What is the output of: x = 5\\nif not x > 10:\\n    print('yes')?",
                "options": ["A) yes", "B) no", "C) Nothing", "D) Error"],
                "answer": "A"
            },
            {
                "question": "What is the output of: x = 5\\nprint('yes' if x > 3 else 'no')?",
                "options": ["A) yes", "B) no", "C) True", "D) Error"],
                "answer": "A"
            },
            {
                "question": "What is the output of: x = 0\\nif x:\\n    print('yes')\\nelse:\\n    print('no')?",
                "options": ["A) yes", "B) no", "C) 0", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: x = []\\nif x:\\n    print('yes')\\nelse:\\n    print('no')?",
                "options": ["A) yes", "B) no", "C) []", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: x = [1]\\nif x:\\n    print('yes')\\nelse:\\n    print('no')?",
                "options": ["A) yes", "B) no", "C) [1]", "D) Error"],
                "answer": "A"
            },
            {
                "question": "What is the output of: x = ''\\nif x:\\n    print('yes')\\nelse:\\n    print('no')?",
                "options": ["A) yes", "B) no", "C) ''", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: x = None\\nif x:\\n    print('yes')\\nelse:\\n    print('no')?",
                "options": ["A) yes", "B) no", "C) None", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: x = 5\\nif x == 5:\\n    print('yes')?",
                "options": ["A) yes", "B) no", "C) True", "D) Error"],
                "answer": "A"
            },
            {
                "question": "What is the output of: x = 5\\nif x != 3:\\n    print('yes')?",
                "options": ["A) yes", "B) no", "C) False", "D) Error"],
                "answer": "A"
            },
            {
                "question": "What is the output of: x = 5\\nif 3 < x < 10:\\n    print('yes')?",
                "options": ["A) yes", "B) no", "C) Nothing", "D) Error"],
                "answer": "A"
            },
            {
                "question": "What is the output of: x = 5\\nif x in [1, 2, 3]:\\n    print('yes')\\nelse:\\n    print('no')?",
                "options": ["A) yes", "B) no", "C) Nothing", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: x = 5\\nif x not in [1, 2, 3]:\\n    print('yes')?",
                "options": ["A) yes", "B) no", "C) Nothing", "D) Error"],
                "answer": "A"
            },
            {
                "question": "What is the output of: x = 'test'\\nif x is 'test':\\n    print('yes')\\nelse:\\n    print('no')?",
                "options": ["A) yes", "B) no", "C) Depends", "D) Error"],
                "answer": "C"
            },
            {
                "question": "What is the output of: x = None\\nif x is None:\\n    print('yes')?",
                "options": ["A) yes", "B) no", "C) None", "D) Error"],
                "answer": "A"
            },
            {
                "question": "What is the output of: x = 5\\nif x is not None:\\n    print('yes')?",
                "options": ["A) yes", "B) no", "C) None", "D) Error"],
                "answer": "A"
            },
            {
                "question": "What is the output of: x = 5\\nif x >= 5:\\n    print('yes')?",
                "options": ["A) yes", "B) no", "C) Nothing", "D) Error"],
                "answer": "A"
            },
            {
                "question": "What is the output of: x = 5\\nif x <= 5:\\n    print('yes')?",
                "options": ["A) yes", "B) no", "C) Nothing", "D) Error"],
                "answer": "A"
            },
            {
                "question": "What is the output of: x = 5\\nif x > 3:\\n    if x < 10:\\n        print('yes')?",
                "options": ["A) yes", "B) no", "C) Nothing", "D) Error"],
                "answer": "A"
            },
            {
                "question": "What is the output of: x = 5\\nif x > 3:\\n    pass\\nprint('done')?",
                "options": ["A) yes done", "B) done", "C) Nothing", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: x = True\\nif x:\\n    print('yes')?",
                "options": ["A) yes", "B) True", "C) 1", "D) Error"],
                "answer": "A"
            },
            {
                "question": "What is the output of: x = False\\nif not x:\\n    print('yes')?",
                "options": ["A) yes", "B) no", "C) False", "D) Error"],
                "answer": "A"
            },
            {
                "question": "What is the output of: x = 5\\ny = 10\\nif x < y < 15:\\n    print('yes')?",
                "options": ["A) yes", "B) no", "C) Nothing", "D) Error"],
                "answer": "A"
            },
            {
                "question": "What is the output of: x = 5\\nresult = 'even' if x % 2 == 0 else 'odd'\\nprint(result)?",
                "options": ["A) even", "B) odd", "C) 5", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: x = 10\\nif x > 5:\\n    print('a')\\nif x > 8:\\n    print('b')?",
                "options": ["A) a", "B) b", "C) a b", "D) Nothing"],
                "answer": "C"
            },
            {
                "question": "What is the output of: x = 5\\nif x == 5 or x == 10:\\n    print('yes')?",
                "options": ["A) yes", "B) no", "C) Nothing", "D) Error"],
                "answer": "A"
            }
        ]
    
    def run_exam(self):
        print("=" * 70)
        print("PCAP-31-03 PRACTICE EXAM - CONDITIONALS")
        print("30 Questions about Python Conditionals (if, elif, else)")
        print("=" * 70)
        print(f"Total Questions: {self.total_questions}")
        print("Instructions: Enter A, B, C, or D for each question")
        print("=" * 70)
        print()
        
        for i, q in enumerate(self.questions, 1):
            print(f"Question {i}/{self.total_questions}")
            print(q["question"])
            for option in q["options"]:
                print(option)
            
            while True:
                answer = input("\nYour answer: ").strip().upper()
                if answer in ['A', 'B', 'C', 'D']:
                    break
                print("Invalid input. Please enter A, B, C, or D.")
            
            if answer == q["answer"]:
                self.score += 1
                print("✓ Correct!\n")
            else:
                print(f"✗ Incorrect. The correct answer is {q['answer']}\n")
            
            print("-" * 70)
        
        self.show_results()
    
    def show_results(self):
        percentage = (self.score / self.total_questions) * 100
        print("\n" + "=" * 70)
        print("EXAM RESULTS - CONDITIONALS")
        print("=" * 70)
        print(f"Score: {self.score}/{self.total_questions}")
        print(f"Percentage: {percentage:.2f}%")
        
        if percentage >= 70:
            print("Status: PASS ✓")
            print("Excellent! You've mastered Python conditionals!")
        else:
            print("Status: FAIL ✗")
            print("Review if/elif/else, logical operators, and truthiness.")
        
        print("=" * 70)

if __name__ == "__main__":
    exam = PCAPExamConditionals()
    exam.run_exam()
