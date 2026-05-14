#!/usr/bin/env python3
"""
PCAP-31-03 Practice Exam - Dictionaries Focus
30 Questions exclusively about Python Dictionaries
"""

import random

class PCAPExamDicts:
    def __init__(self):
        self.score = 0
        self.total_questions = 30
        self.questions = [
            {
                "question": "What is the output of: print({'a': 1, 'b': 2}['a'])?",
                "options": ["A) 'a'", "B) 1", "C) 0", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print({'a': 1}.get('b', 0))?",
                "options": ["A) None", "B) 0", "C) 'b'", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print({'a': 1}.get('a'))?",
                "options": ["A) 'a'", "B) 1", "C) None", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(len({'a': 1, 'b': 2, 'c': 3}))?",
                "options": ["A) 2", "B) 3", "C) 6", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print('a' in {'a': 1, 'b': 2})?",
                "options": ["A) False", "B) True", "C) 1", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(1 in {'a': 1, 'b': 2})?",
                "options": ["A) False", "B) True", "C) 'a'", "D) Error"],
                "answer": "A"
            },
            {
                "question": "What is the output of: d = {'a': 1}; d['b'] = 2; print(d)?",
                "options": ["A) {'a': 1}", "B) {'a': 1, 'b': 2}", "C) {'b': 2}", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: d = {'a': 1, 'b': 2}; del d['a']; print(d)?",
                "options": ["A) {'a': 1, 'b': 2}", "B) {'b': 2}", "C) {'a': 1}", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(list({'a': 1, 'b': 2}.keys()))?",
                "options": ["A) ['a', 'b']", "B) [1, 2]", "C) [('a', 1), ('b', 2)]", "D) dict_keys(['a', 'b'])"],
                "answer": "A"
            },
            {
                "question": "What is the output of: print(list({'a': 1, 'b': 2}.values()))?",
                "options": ["A) ['a', 'b']", "B) [1, 2]", "C) [('a', 1), ('b', 2)]", "D) dict_values([1, 2])"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(list({'a': 1, 'b': 2}.items()))?",
                "options": ["A) ['a', 'b']", "B) [1, 2]", "C) [('a', 1), ('b', 2)]", "D) {'a': 1, 'b': 2}"],
                "answer": "C"
            },
            {
                "question": "What is the output of: d = {'a': 1}; print(d.pop('a'))?",
                "options": ["A) 'a'", "B) 1", "C) {'a': 1}", "D) None"],
                "answer": "B"
            },
            {
                "question": "What is the output of: d = {'a': 1}; print(d.pop('b', 0))?",
                "options": ["A) 'b'", "B) 0", "C) None", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: d = {'a': 1}; print(d.popitem())?",
                "options": ["A) 'a'", "B) 1", "C) ('a', 1)", "D) {'a': 1}"],
                "answer": "C"
            },
            {
                "question": "What is the output of: d = {'a': 1}; d.update({'b': 2}); print(d)?",
                "options": ["A) {'a': 1}", "B) {'b': 2}", "C) {'a': 1, 'b': 2}", "D) None"],
                "answer": "C"
            },
            {
                "question": "What is the output of: d = {'a': 1}; print(d.setdefault('b', 2))?",
                "options": ["A) 1", "B) 2", "C) {'a': 1, 'b': 2}", "D) None"],
                "answer": "B"
            },
            {
                "question": "What is the output of: d = {'a': 1}; print(d.setdefault('a', 2))?",
                "options": ["A) 1", "B) 2", "C) {'a': 1}", "D) None"],
                "answer": "A"
            },
            {
                "question": "What is the output of: d = {'a': 1}; d.clear(); print(d)?",
                "options": ["A) {'a': 1}", "B) {}", "C) None", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: d = {'a': 1}; d2 = d.copy(); d2['a'] = 2; print(d)?",
                "options": ["A) {'a': 1}", "B) {'a': 2}", "C) {}", "D) Error"],
                "answer": "A"
            },
            {
                "question": "What is the output of: print(dict(a=1, b=2))?",
                "options": ["A) {'a': 1, 'b': 2}", "B) {a: 1, b: 2}", "C) ['a', 1, 'b', 2]", "D) Error"],
                "answer": "A"
            },
            {
                "question": "What is the output of: print(dict([('a', 1), ('b', 2)]))?",
                "options": ["A) [('a', 1), ('b', 2)]", "B) {'a': 1, 'b': 2}", "C) {('a', 1), ('b', 2)}", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(dict(zip(['a', 'b'], [1, 2])))?",
                "options": ["A) {'a': 1, 'b': 2}", "B) [('a', 1), ('b', 2)]", "C) {1: 'a', 2: 'b'}", "D) Error"],
                "answer": "A"
            },
            {
                "question": "What is the output of: print({x: x**2 for x in range(3)})?",
                "options": ["A) {0: 0, 1: 1, 2: 4}", "B) [0, 1, 4]", "C) {0, 1, 4}", "D) Error"],
                "answer": "A"
            },
            {
                "question": "What is the output of: print({}.get('a') is None)?",
                "options": ["A) False", "B) True", "C) None", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print({})?",
                "options": ["A) None", "B) {}", "C) []", "D) set()"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(len({}))?",
                "options": ["A) 0", "B) 1", "C) None", "D) Error"],
                "answer": "A"
            },
            {
                "question": "What is the output of: print({'a': 1, 'a': 2})?",
                "options": ["A) {'a': 1}", "B) {'a': 2}", "C) {'a': 1, 'a': 2}", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: d = {'a': {'b': 1}}; print(d['a']['b'])?",
                "options": ["A) 'a'", "B) 'b'", "C) 1", "D) {'b': 1}"],
                "answer": "C"
            },
            {
                "question": "What is the output of: print(dict.fromkeys(['a', 'b'], 0))?",
                "options": ["A) {'a': 0, 'b': 0}", "B) {'a': 'b'}", "C) [('a', 0), ('b', 0)]", "D) Error"],
                "answer": "A"
            },
            {
                "question": "What is the output of: print({**{'a': 1}, **{'b': 2}})?",
                "options": ["A) {'a': 1, 'b': 2}", "B) [{'a': 1}, {'b': 2}]", "C) {'a': 1}", "D) Error"],
                "answer": "A"
            }
        ]
    
    def run_exam(self):
        print("=" * 70)
        print("PCAP-31-03 PRACTICE EXAM - DICTIONARIES")
        print("30 Questions about Python Dictionaries")
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
        print("EXAM RESULTS - DICTIONARIES")
        print("=" * 70)
        print(f"Score: {self.score}/{self.total_questions}")
        print(f"Percentage: {percentage:.2f}%")
        
        if percentage >= 70:
            print("Status: PASS ✓")
            print("Fantastic! You've mastered Python dictionaries!")
        else:
            print("Status: FAIL ✗")
            print("Review dictionary methods and operations.")
        
        print("=" * 70)

if __name__ == "__main__":
    exam = PCAPExamDicts()
    exam.run_exam()
