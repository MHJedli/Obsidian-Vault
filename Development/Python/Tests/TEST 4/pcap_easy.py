#!/usr/bin/env python3
"""
PCAP-31-03 Practice Exam - Easy Level (TEST 4)
50 Questions with emphasis on strings and fundamental concepts
"""

import random

class PCAPExamEasy:
    def __init__(self):
        self.score = 0
        self.total_questions = 50
        self.questions = [
            # String Questions (20 questions)
            {
                "question": "What is the output of: print('Hello'[1])?",
                "options": ["A) 'H'", "B) 'e'", "C) 'l'", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print('Python'.find('th'))?",
                "options": ["A) -1", "B) 2", "C) 3", "D) 4"],
                "answer": "D"
            },
            {
                "question": "What is the output of: print('abc'.upper())?",
                "options": ["A) 'abc'", "B) 'ABC'", "C) 'Abc'", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(len('Hello World'))?",
                "options": ["A) 10", "B) 11", "C) 12", "D) 9"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print('test'.capitalize())?",
                "options": ["A) 'test'", "B) 'TEST'", "C) 'Test'", "D) 'tEst'"],
                "answer": "C"
            },
            {
                "question": "What is the output of: print('hello' * 2)?",
                "options": ["A) 'hello2'", "B) 'hellohello'", "C) 'hello hello'", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print('Python'[0:3])?",
                "options": ["A) 'Pyt'", "B) 'Pyth'", "C) 'yth'", "D) 'Py'"],
                "answer": "A"
            },
            {
                "question": "What is the output of: print('TEST'.lower())?",
                "options": ["A) 'TEST'", "B) 'test'", "C) 'Test'", "D) 'tEsT'"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print('a,b,c'.split(','))?",
                "options": ["A) 'a,b,c'", "B) ['a', 'b', 'c']", "C) ('a', 'b', 'c')", "D) {'a', 'b', 'c'}"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print('  test  '.strip())?",
                "options": ["A) '  test  '", "B) 'test  '", "C) '  test'", "D) 'test'"],
                "answer": "D"
            },
            {
                "question": "What is the output of: print('hello'.replace('l', 'L'))?",
                "options": ["A) 'heLLo'", "B) 'heLlo'", "C) 'helLo'", "D) 'hello'"],
                "answer": "A"
            },
            {
                "question": "What is the output of: print('123'.isdigit())?",
                "options": ["A) False", "B) True", "C) 123", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print('abc'.isalpha())?",
                "options": ["A) False", "B) True", "C) 'abc'", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print('-'.join(['a', 'b', 'c']))?",
                "options": ["A) 'abc'", "B) 'a-b-c'", "C) ['a', 'b', 'c']", "D) 'a b c'"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print('Python'[-1])?",
                "options": ["A) 'P'", "B) 'n'", "C) 'o'", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print('test'.count('t'))?",
                "options": ["A) 1", "B) 2", "C) 3", "D) 0"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print('Hello'.startswith('He'))?",
                "options": ["A) False", "B) True", "C) 'He'", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print('World'.endswith('ld'))?",
                "options": ["A) False", "B) True", "C) 'ld'", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print('abc123'.isalnum())?",
                "options": ["A) False", "B) True", "C) None", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print('test' in 'testing')?",
                "options": ["A) False", "B) True", "C) 0", "D) 4"],
                "answer": "B"
            },
            # Other fundamental topics (30 questions)
            {
                "question": "What is the output of: print(5 + 3)?",
                "options": ["A) 53", "B) 8", "C) '8'", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(10 - 4)?",
                "options": ["A) 6", "B) 14", "C) 104", "D) Error"],
                "answer": "A"
            },
            {
                "question": "What is the output of: print(3 * 4)?",
                "options": ["A) 7", "B) 12", "C) 34", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(15 / 3)?",
                "options": ["A) 5", "B) 5.0", "C) 4", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(7 % 3)?",
                "options": ["A) 2", "B) 1", "C) 0", "D) 2.33"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print([1, 2, 3][0])?",
                "options": ["A) 0", "B) 1", "C) 2", "D) [1]"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(len([1, 2, 3, 4]))?",
                "options": ["A) 3", "B) 4", "C) 5", "D) 10"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(True and True)?",
                "options": ["A) False", "B) True", "C) 1", "D) None"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(False or True)?",
                "options": ["A) False", "B) True", "C) 0", "D) 1"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(not False)?",
                "options": ["A) False", "B) True", "C) None", "D) 1"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(5 > 3)?",
                "options": ["A) False", "B) True", "C) 2", "D) 5"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(4 < 2)?",
                "options": ["A) False", "B) True", "C) 2", "D) 4"],
                "answer": "A"
            },
            {
                "question": "What is the output of: print(5 >= 5)?",
                "options": ["A) False", "B) True", "C) 0", "D) 5"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(3 <= 2)?",
                "options": ["A) False", "B) True", "C) 1", "D) 3"],
                "answer": "A"
            },
            {
                "question": "What is the output of: print(5 != 5)?",
                "options": ["A) False", "B) True", "C) 0", "D) None"],
                "answer": "A"
            },
            {
                "question": "What is the output of: print(type(3.14))?",
                "options": ["A) <class 'int'>", "B) <class 'float'>", "C) <class 'str'>", "D) float"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(type(True))?",
                "options": ["A) <class 'bool'>", "B) <class 'int'>", "C) bool", "D) True"],
                "answer": "A"
            },
            {
                "question": "What is the output of: print(int(5.9))?",
                "options": ["A) 5", "B) 6", "C) 5.9", "D) Error"],
                "answer": "A"
            },
            {
                "question": "What is the output of: print(str(100))?",
                "options": ["A) 100", "B) '100'", "C) 100.0", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(bool(1))?",
                "options": ["A) False", "B) True", "C) 1", "D) None"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(bool(''))?",
                "options": ["A) False", "B) True", "C) ''", "D) None"],
                "answer": "A"
            },
            {
                "question": "What is the output of: print([1, 2] + [3, 4])?",
                "options": ["A) [1, 2, 3, 4]", "B) [4, 6]", "C) [[1, 2], [3, 4]]", "D) Error"],
                "answer": "A"
            },
            {
                "question": "What is the output of: print(max([5, 2, 9, 1]))?",
                "options": ["A) 1", "B) 5", "C) 9", "D) 17"],
                "answer": "C"
            },
            {
                "question": "What is the output of: print(min([5, 2, 9, 1]))?",
                "options": ["A) 1", "B) 2", "C) 5", "D) 9"],
                "answer": "A"
            },
            {
                "question": "What is the output of: print(sum([1, 2, 3, 4]))?",
                "options": ["A) 4", "B) 10", "C) 1234", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(abs(-10))?",
                "options": ["A) -10", "B) 10", "C) 0", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(round(4.6))?",
                "options": ["A) 4", "B) 5", "C) 4.6", "D) 4.0"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(3 in [1, 2, 3])?",
                "options": ["A) False", "B) True", "C) 2", "D) 3"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(5 not in [1, 2, 3])?",
                "options": ["A) False", "B) True", "C) None", "D) 5"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(list(range(5)))?",
                "options": ["A) [1, 2, 3, 4, 5]", "B) [0, 1, 2, 3, 4]", "C) [0, 1, 2, 3, 4, 5]", "D) range(5)"],
                "answer": "B"
            }
        ]
    
    def run_exam(self):
        print("=" * 70)
        print("PCAP-31-03 PRACTICE EXAM - EASY LEVEL (TEST 4)")
        print("Focus: Strings and Fundamental Python Concepts")
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
        print("EXAM RESULTS")
        print("=" * 70)
        print(f"Score: {self.score}/{self.total_questions}")
        print(f"Percentage: {percentage:.2f}%")
        
        if percentage >= 70:
            print("Status: PASS ✓")
            print("Great job! You're ready for the next level!")
        else:
            print("Status: FAIL ✗")
            print("Keep practicing! Focus on string methods and basic operations.")
        
        print("=" * 70)

if __name__ == "__main__":
    exam = PCAPExamEasy()
    exam.run_exam()
