#!/usr/bin/env python3
"""
PCAP-31-03 Practice Exam - Loops Focus
30 Questions exclusively about Python Loops (for, while)
"""

import random

class PCAPExamLoops:
    def __init__(self):
        self.score = 0
        self.total_questions = 30
        self.questions = [
            {
                "question": "What is the output of: for i in range(3): print(i, end=' ')?",
                "options": ["A) 1 2 3", "B) 0 1 2", "C) 0 1 2 3", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: for i in range(1, 4): print(i, end=' ')?",
                "options": ["A) 1 2 3", "B) 1 2 3 4", "C) 0 1 2 3", "D) 2 3 4"],
                "answer": "A"
            },
            {
                "question": "What is the output of: for i in range(0, 6, 2): print(i, end=' ')?",
                "options": ["A) 0 2 4", "B) 0 2 4 6", "C) 2 4 6", "D) 0 1 2 3 4 5"],
                "answer": "A"
            },
            {
                "question": "What is the output of: for i in 'abc': print(i, end=' ')?",
                "options": ["A) abc", "B) a b c", "C) 0 1 2", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: for i in [1, 2, 3]: print(i*2, end=' ')?",
                "options": ["A) 1 2 3", "B) 2 4 6", "C) 1 2 3 1 2 3", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: x = 0\\nwhile x < 3:\\n    print(x, end=' ')\\n    x += 1?",
                "options": ["A) 0 1 2", "B) 1 2 3", "C) 0 1 2 3", "D) Infinite loop"],
                "answer": "A"
            },
            {
                "question": "What is the output of: for i in range(5):\\n    if i == 3:\\n        break\\n    print(i, end=' ')?",
                "options": ["A) 0 1 2 3", "B) 0 1 2", "C) 0 1 2 3 4", "D) 1 2 3"],
                "answer": "B"
            },
            {
                "question": "What is the output of: for i in range(5):\\n    if i == 3:\\n        continue\\n    print(i, end=' ')?",
                "options": ["A) 0 1 2 3 4", "B) 0 1 2 4", "C) 0 1 2", "D) 3"],
                "answer": "B"
            },
            {
                "question": "What is the output of: for i in range(3):\\n    pass\\nprint('done')?",
                "options": ["A) 0 1 2 done", "B) done", "C) Error", "D) Nothing"],
                "answer": "B"
            },
            {
                "question": "What is the output of: for i in range(3):\\n    print(i, end=' ')\\nelse:\\n    print('end')?",
                "options": ["A) 0 1 2", "B) 0 1 2 end", "C) end", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: for i in range(3):\\n    if i == 1:\\n        break\\nelse:\\n    print('end')?",
                "options": ["A) end", "B) 0 1 end", "C) Nothing", "D) 0 1"],
                "answer": "C"
            },
            {
                "question": "What is the output of: for i in enumerate(['a', 'b']): print(i, end=' ')?",
                "options": ["A) a b", "B) 0 1", "C) (0, 'a') (1, 'b')", "D) Error"],
                "answer": "C"
            },
            {
                "question": "What is the output of: for i, v in enumerate(['a', 'b']): print(i, end=' ')?",
                "options": ["A) a b", "B) 0 1", "C) (0, 'a') (1, 'b')", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: for i in zip([1, 2], ['a', 'b']): print(i, end=' ')?",
                "options": ["A) 1 2 a b", "B) (1, 'a') (2, 'b')", "C) 1 a 2 b", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: for i in reversed([1, 2, 3]): print(i, end=' ')?",
                "options": ["A) 1 2 3", "B) 3 2 1", "C) -1 -2 -3", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: for i in sorted([3, 1, 2]): print(i, end=' ')?",
                "options": ["A) 3 1 2", "B) 1 2 3", "C) 3 2 1", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: for k in {'a': 1, 'b': 2}: print(k, end=' ')?",
                "options": ["A) 1 2", "B) a b", "C) ('a', 1) ('b', 2)", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: for v in {'a': 1, 'b': 2}.values(): print(v, end=' ')?",
                "options": ["A) a b", "B) 1 2", "C) ('a', 1) ('b', 2)", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: for k, v in {'a': 1}.items(): print(k, v)?",
                "options": ["A) a 1", "B) ('a', 1)", "C) 1 a", "D) Error"],
                "answer": "A"
            },
            {
                "question": "What is the output of: x = 0\\nwhile x < 3:\\n    x += 1\\nelse:\\n    print('done')?",
                "options": ["A) done", "B) 0 1 2 done", "C) Nothing", "D) Error"],
                "answer": "A"
            },
            {
                "question": "What is the output of: x = 0\\nwhile x < 3:\\n    x += 1\\n    if x == 2:\\n        break\\nelse:\\n    print('done')?",
                "options": ["A) done", "B) Nothing", "C) 0 1", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: for i in range(2):\\n    for j in range(2):\\n        print(i, j, end=' ')?",
                "options": ["A) 0 0 0 1 1 0 1 1", "B) 0 1 0 1", "C) 0 0 1 1", "D) Error"],
                "answer": "A"
            },
            {
                "question": "What is the output of: for i in []: print(i)?",
                "options": ["A) []", "B) Nothing", "C) None", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: for i in [1, 2, 3]:\\n    if i % 2 == 0:\\n        print(i, end=' ')?",
                "options": ["A) 1 3", "B) 2", "C) 1 2 3", "D) Nothing"],
                "answer": "B"
            },
            {
                "question": "What is the output of: count = 0\\nfor i in range(10):\\n    count += 1\\nprint(count)?",
                "options": ["A) 9", "B) 10", "C) 11", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: for i in range(5, 0, -1): print(i, end=' ')?",
                "options": ["A) 5 4 3 2 1", "B) 5 4 3 2 1 0", "C) 1 2 3 4 5", "D) Error"],
                "answer": "A"
            },
            {
                "question": "What is the output of: for i in range(3):\\n    for j in range(2):\\n        if i == j:\\n            break\\n        print(i, j, end=' ')?",
                "options": ["A) 0 0 1 0 1 1 2 0 2 1", "B) 1 0 2 0 2 1", "C) 0 1 1 0", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: x = 5\\nwhile x:\\n    x -= 1\\n    if x == 2:\\n        continue\\n    print(x, end=' ')?",
                "options": ["A) 4 3 2 1 0", "B) 4 3 1 0", "C) 5 4 3 1 0", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: for i in range(1, 10, 3): print(i, end=' ')?",
                "options": ["A) 1 4 7", "B) 1 4 7 10", "C) 1 3 5 7 9", "D) Error"],
                "answer": "A"
            },
            {
                "question": "What is the output of: for _ in range(3): print('x', end='')?",
                "options": ["A) x x x", "B) xxx", "C) _ _ _", "D) Error"],
                "answer": "B"
            }
        ]
    
    def run_exam(self):
        print("=" * 70)
        print("PCAP-31-03 PRACTICE EXAM - LOOPS")
        print("30 Questions about Python Loops (for, while)")
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
        print("EXAM RESULTS - LOOPS")
        print("=" * 70)
        print(f"Score: {self.score}/{self.total_questions}")
        print(f"Percentage: {percentage:.2f}%")
        
        if percentage >= 70:
            print("Status: PASS ✓")
            print("Great work! You understand Python loops well!")
        else:
            print("Status: FAIL ✗")
            print("Review for/while loops, break, continue, and else clauses.")
        
        print("=" * 70)

if __name__ == "__main__":
    exam = PCAPExamLoops()
    exam.run_exam()
