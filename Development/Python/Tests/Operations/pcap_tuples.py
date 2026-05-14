#!/usr/bin/env python3
"""
PCAP-31-03 Practice Exam - Tuples Focus
30 Questions exclusively about Python Tuples
"""

import random

class PCAPExamTuples:
    def __init__(self):
        self.score = 0
        self.total_questions = 30
        self.questions = [
            {
                "question": "What is the output of: print((1, 2, 3)[1])?",
                "options": ["A) 1", "B) 2", "C) 3", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print((1, 2, 3)[-1])?",
                "options": ["A) 1", "B) 2", "C) 3", "D) Error"],
                "answer": "C"
            },
            {
                "question": "What is the output of: print((1, 2, 3, 4, 5)[1:3])?",
                "options": ["A) (1, 2)", "B) (2, 3)", "C) (2, 3, 4)", "D) [2, 3]"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print((1, 2, 3)[::-1])?",
                "options": ["A) (1, 2, 3)", "B) (3, 2, 1)", "C) [-1, -2, -3]", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(len((1, 2, 3, 4)))?",
                "options": ["A) 3", "B) 4", "C) 5", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print((1, 2) + (3, 4))?",
                "options": ["A) (1, 2, 3, 4)", "B) (4, 6)", "C) ((1, 2), (3, 4))", "D) Error"],
                "answer": "A"
            },
            {
                "question": "What is the output of: print((1, 2) * 3)?",
                "options": ["A) (3, 6)", "B) (1, 2, 1, 2, 1, 2)", "C) (1, 2, 3)", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(3 in (1, 2, 3))?",
                "options": ["A) False", "B) True", "C) 2", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print((1, 2, 2, 3).count(2))?",
                "options": ["A) 1", "B) 2", "C) 3", "D) 4"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print((1, 2, 3).index(2))?",
                "options": ["A) 0", "B) 1", "C) 2", "D) -1"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(max((5, 2, 9, 1)))?",
                "options": ["A) 1", "B) 5", "C) 9", "D) 17"],
                "answer": "C"
            },
            {
                "question": "What is the output of: print(min((5, 2, 9, 1)))?",
                "options": ["A) 1", "B) 2", "C) 5", "D) 9"],
                "answer": "A"
            },
            {
                "question": "What is the output of: print(sum((1, 2, 3, 4)))?",
                "options": ["A) 4", "B) 10", "C) 1234", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(sorted((3, 1, 2)))?",
                "options": ["A) (1, 2, 3)", "B) [1, 2, 3]", "C) (3, 1, 2)", "D) [3, 1, 2]"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(tuple([1, 2, 3]))?",
                "options": ["A) [1, 2, 3]", "B) (1, 2, 3)", "C) {1, 2, 3}", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(tuple('abc'))?",
                "options": ["A) 'abc'", "B) ['a', 'b', 'c']", "C) ('a', 'b', 'c')", "D) ('abc',)"],
                "answer": "C"
            },
            {
                "question": "What is the output of: print(tuple(range(3)))?",
                "options": ["A) (0, 1, 2)", "B) [0, 1, 2]", "C) (1, 2, 3)", "D) range(3)"],
                "answer": "A"
            },
            {
                "question": "What is the output of: print(type((1,)))?",
                "options": ["A) <class 'int'>", "B) <class 'tuple'>", "C) <class 'list'>", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(type((1)))?",
                "options": ["A) <class 'int'>", "B) <class 'tuple'>", "C) <class 'list'>", "D) Error"],
                "answer": "A"
            },
            {
                "question": "What is the output of: print(())?",
                "options": ["A) None", "B) ()", "C) []", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(len(()))?",
                "options": ["A) 0", "B) 1", "C) None", "D) Error"],
                "answer": "A"
            },
            {
                "question": "What is the output of: a, b, c = (1, 2, 3); print(b)?",
                "options": ["A) 1", "B) 2", "C) 3", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: a, *b, c = (1, 2, 3, 4); print(b)?",
                "options": ["A) [2, 3]", "B) (2, 3)", "C) 2", "D) Error"],
                "answer": "A"
            },
            {
                "question": "What is the output of: print(((1, 2), (3, 4))[1][0])?",
                "options": ["A) 1", "B) 2", "C) 3", "D) 4"],
                "answer": "C"
            },
            {
                "question": "What is the output of: t = (1, 2, 3); t[0] = 9; print(t)?",
                "options": ["A) (9, 2, 3)", "B) (1, 2, 3)", "C) Error", "D) None"],
                "answer": "C"
            },
            {
                "question": "What is the output of: print(tuple(x*2 for x in (1, 2, 3)))?",
                "options": ["A) (1, 2, 3)", "B) (2, 4, 6)", "C) [2, 4, 6]", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print((1, 2, 3).__len__())?",
                "options": ["A) 2", "B) 3", "C) 4", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print((1, 2, 3).__contains__(2))?",
                "options": ["A) False", "B) True", "C) 1", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print((1, 2, 3).__add__((4, 5)))?",
                "options": ["A) (1, 2, 3, 4, 5)", "B) (5, 7, 3)", "C) Error", "D) None"],
                "answer": "A"
            },
            {
                "question": "What is the output of: print((1, 2).__mul__(2))?",
                "options": ["A) (2, 4)", "B) (1, 2, 1, 2)", "C) (1, 2, 2)", "D) Error"],
                "answer": "B"
            }
        ]
    
    def run_exam(self):
        print("=" * 70)
        print("PCAP-31-03 PRACTICE EXAM - TUPLES")
        print("30 Questions about Python Tuples")
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
        print("EXAM RESULTS - TUPLES")
        print("=" * 70)
        print(f"Score: {self.score}/{self.total_questions}")
        print(f"Percentage: {percentage:.2f}%")
        
        if percentage >= 70:
            print("Status: PASS ✓")
            print("Excellent! You've mastered Python tuples!")
        else:
            print("Status: FAIL ✗")
            print("Review tuple operations and immutability concepts.")
        
        print("=" * 70)

if __name__ == "__main__":
    exam = PCAPExamTuples()
    exam.run_exam()
