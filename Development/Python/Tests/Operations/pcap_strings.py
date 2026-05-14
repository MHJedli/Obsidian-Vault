#!/usr/bin/env python3
"""
PCAP-31-03 Practice Exam - Strings Focus
30 Questions exclusively about Python Strings
"""

import random

class PCAPExamStrings:
    def __init__(self):
        self.score = 0
        self.total_questions = 30
        self.questions = [
            {
                "question": "What is the output of: print('Hello'[0])?",
                "options": ["A) 'H'", "B) 'e'", "C) 0", "D) Error"],
                "answer": "A"
            },
            {
                "question": "What is the output of: print('Hello'[-1])?",
                "options": ["A) 'H'", "B) 'o'", "C) -1", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print('Hello'[1:4])?",
                "options": ["A) 'Hel'", "B) 'ell'", "C) 'ello'", "D) 'Hell'"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print('Hello'[::-1])?",
                "options": ["A) 'Hello'", "B) 'olleH'", "C) 'lleH'", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(len('Hello'))?",
                "options": ["A) 4", "B) 5", "C) 6", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print('Hello' + 'World')?",
                "options": ["A) 'Hello World'", "B) 'HelloWorld'", "C) Error", "D) 'Hello+World'"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print('Hi' * 3)?",
                "options": ["A) 'Hi3'", "B) 'HiHiHi'", "C) 'Hi Hi Hi'", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print('test'.upper())?",
                "options": ["A) 'test'", "B) 'TEST'", "C) 'Test'", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print('TEST'.lower())?",
                "options": ["A) 'TEST'", "B) 'test'", "C) 'Test'", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print('hello world'.capitalize())?",
                "options": ["A) 'Hello World'", "B) 'Hello world'", "C) 'HELLO WORLD'", "D) 'hello world'"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print('hello world'.title())?",
                "options": ["A) 'Hello World'", "B) 'Hello world'", "C) 'HELLO WORLD'", "D) 'hello world'"],
                "answer": "A"
            },
            {
                "question": "What is the output of: print('a,b,c'.split(','))?",
                "options": ["A) 'a,b,c'", "B) ['a', 'b', 'c']", "C) ('a', 'b', 'c')", "D) {'a', 'b', 'c'}"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print('-'.join(['a', 'b', 'c']))?",
                "options": ["A) 'abc'", "B) 'a-b-c'", "C) ['a', 'b', 'c']", "D) 'a b c'"],
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
                "question": "What is the output of: print('test'.find('e'))?",
                "options": ["A) 0", "B) 1", "C) 2", "D) -1"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print('test'.find('x'))?",
                "options": ["A) 0", "B) -1", "C) None", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print('test'.count('t'))?",
                "options": ["A) 1", "B) 2", "C) 3", "D) 0"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print('test'.startswith('te'))?",
                "options": ["A) False", "B) True", "C) 'te'", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print('test'.endswith('st'))?",
                "options": ["A) False", "B) True", "C) 'st'", "D) Error"],
                "answer": "B"
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
                "question": "What is the output of: print('abc123'.isalnum())?",
                "options": ["A) False", "B) True", "C) None", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print('TEST'.isupper())?",
                "options": ["A) False", "B) True", "C) 'TEST'", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print('test'.islower())?",
                "options": ["A) False", "B) True", "C) 'test'", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print('   '.isspace())?",
                "options": ["A) False", "B) True", "C) None", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print('test' in 'testing')?",
                "options": ["A) False", "B) True", "C) 0", "D) 4"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print('x' not in 'test')?",
                "options": ["A) False", "B) True", "C) None", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print('test'.index('e'))?",
                "options": ["A) 0", "B) 1", "C) 2", "D) -1"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print('TeSt'.swapcase())?",
                "options": ["A) 'test'", "B) 'TEST'", "C) 'tEsT'", "D) 'TeSt'"],
                "answer": "C"
            }
        ]
    
    def run_exam(self):
        print("=" * 70)
        print("PCAP-31-03 PRACTICE EXAM - STRINGS")
        print("30 Questions about Python Strings")
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
        print("EXAM RESULTS - STRINGS")
        print("=" * 70)
        print(f"Score: {self.score}/{self.total_questions}")
        print(f"Percentage: {percentage:.2f}%")
        
        if percentage >= 70:
            print("Status: PASS ✓")
            print("Great job! You understand Python strings well!")
        else:
            print("Status: FAIL ✗")
            print("Keep practicing string methods and operations.")
        
        print("=" * 70)

if __name__ == "__main__":
    exam = PCAPExamStrings()
    exam.run_exam()
