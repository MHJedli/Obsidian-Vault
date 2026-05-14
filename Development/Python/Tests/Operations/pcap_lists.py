#!/usr/bin/env python3
"""
PCAP-31-03 Practice Exam - Lists Focus
30 Questions exclusively about Python Lists
"""

import random

class PCAPExamLists:
    def __init__(self):
        self.score = 0
        self.total_questions = 30
        self.questions = [
            {
                "question": "What is the output of: print([1, 2, 3][1])?",
                "options": ["A) 1", "B) 2", "C) 3", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print([1, 2, 3][-1])?",
                "options": ["A) 1", "B) 2", "C) 3", "D) Error"],
                "answer": "C"
            },
            {
                "question": "What is the output of: print([1, 2, 3, 4, 5][1:3])?",
                "options": ["A) [1, 2]", "B) [2, 3]", "C) [2, 3, 4]", "D) [1, 2, 3]"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print([1, 2, 3][::-1])?",
                "options": ["A) [1, 2, 3]", "B) [3, 2, 1]", "C) [-1, -2, -3]", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(len([1, 2, 3, 4]))?",
                "options": ["A) 3", "B) 4", "C) 5", "D) 10"],
                "answer": "B"
            },
            {
                "question": "What is the output of: lst = [1, 2]; lst.append(3); print(lst)?",
                "options": ["A) [1, 2]", "B) [1, 2, 3]", "C) [3, 1, 2]", "D) None"],
                "answer": "B"
            },
            {
                "question": "What is the output of: lst = [1, 2]; lst.extend([3, 4]); print(lst)?",
                "options": ["A) [1, 2, 3, 4]", "B) [1, 2, [3, 4]]", "C) [3, 4, 1, 2]", "D) None"],
                "answer": "A"
            },
            {
                "question": "What is the output of: lst = [1, 2, 3]; lst.insert(1, 'x'); print(lst)?",
                "options": ["A) [1, 'x', 2, 3]", "B) ['x', 1, 2, 3]", "C) [1, 2, 3, 'x']", "D) None"],
                "answer": "A"
            },
            {
                "question": "What is the output of: lst = [1, 2, 3]; lst.remove(2); print(lst)?",
                "options": ["A) [1, 2, 3]", "B) [1, 3]", "C) [2]", "D) None"],
                "answer": "B"
            },
            {
                "question": "What is the output of: lst = [1, 2, 3]; print(lst.pop())?",
                "options": ["A) 1", "B) 2", "C) 3", "D) [1, 2]"],
                "answer": "C"
            },
            {
                "question": "What is the output of: lst = [1, 2, 3]; print(lst.pop(0))?",
                "options": ["A) 0", "B) 1", "C) 2", "D) 3"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print([1, 2, 3].index(2))?",
                "options": ["A) 0", "B) 1", "C) 2", "D) -1"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print([1, 2, 2, 3].count(2))?",
                "options": ["A) 1", "B) 2", "C) 3", "D) 4"],
                "answer": "B"
            },
            {
                "question": "What is the output of: lst = [3, 1, 2]; lst.sort(); print(lst)?",
                "options": ["A) [3, 1, 2]", "B) [1, 2, 3]", "C) [3, 2, 1]", "D) None"],
                "answer": "B"
            },
            {
                "question": "What is the output of: lst = [1, 2, 3]; lst.reverse(); print(lst)?",
                "options": ["A) [1, 2, 3]", "B) [3, 2, 1]", "C) [-1, -2, -3]", "D) None"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print([1, 2] + [3, 4])?",
                "options": ["A) [1, 2, 3, 4]", "B) [4, 6]", "C) [[1, 2], [3, 4]]", "D) Error"],
                "answer": "A"
            },
            {
                "question": "What is the output of: print([1, 2] * 3)?",
                "options": ["A) [3, 6]", "B) [1, 2, 1, 2, 1, 2]", "C) [1, 2, 3]", "D) Error"],
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
                "question": "What is the output of: print(sorted([3, 1, 2]))?",
                "options": ["A) [3, 1, 2]", "B) [1, 2, 3]", "C) [3, 2, 1]", "D) None"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(list(range(5)))?",
                "options": ["A) [1, 2, 3, 4, 5]", "B) [0, 1, 2, 3, 4]", "C) [0, 1, 2, 3, 4, 5]", "D) range(5)"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print([x*2 for x in [1, 2, 3]])?",
                "options": ["A) [1, 2, 3]", "B) [2, 4, 6]", "C) [1, 2, 3, 1, 2, 3]", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print([x for x in [1, 2, 3, 4] if x % 2 == 0])?",
                "options": ["A) [1, 3]", "B) [2, 4]", "C) [1, 2, 3, 4]", "D) []"],
                "answer": "B"
            },
            {
                "question": "What is the output of: lst = [1, 2, 3]; lst.clear(); print(lst)?",
                "options": ["A) [1, 2, 3]", "B) []", "C) None", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: lst = [1, 2, 3]; lst2 = lst.copy(); lst2[0] = 9; print(lst)?",
                "options": ["A) [9, 2, 3]", "B) [1, 2, 3]", "C) [1, 2, 3, 9]", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print([[1, 2], [3, 4]][1][0])?",
                "options": ["A) 1", "B) 2", "C) 3", "D) 4"],
                "answer": "C"
            },
            {
                "question": "What is the output of: print(list('abc'))?",
                "options": ["A) 'abc'", "B) ['abc']", "C) ['a', 'b', 'c']", "D) ('a', 'b', 'c')"],
                "answer": "C"
            }
        ]
    
    def run_exam(self):
        print("=" * 70)
        print("PCAP-31-03 PRACTICE EXAM - LISTS")
        print("30 Questions about Python Lists")
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
        print("EXAM RESULTS - LISTS")
        print("=" * 70)
        print(f"Score: {self.score}/{self.total_questions}")
        print(f"Percentage: {percentage:.2f}%")
        
        if percentage >= 70:
            print("Status: PASS ✓")
            print("Great job! You understand Python lists well!")
        else:
            print("Status: FAIL ✗")
            print("Keep practicing list operations and methods.")
        
        print("=" * 70)

if __name__ == "__main__":
    exam = PCAPExamLists()
    exam.run_exam()
