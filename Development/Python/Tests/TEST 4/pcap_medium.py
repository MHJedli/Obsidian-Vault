#!/usr/bin/env python3
"""
PCAP-31-03 Practice Exam - Medium Level (TEST 4)
50 Questions with emphasis on strings and intermediate concepts
"""

import random

class PCAPExamMedium:
    def __init__(self):
        self.score = 0
        self.total_questions = 50
        self.questions = [
            # Advanced String Questions (25 questions)
            {
                "question": "What is the output of: print('Python'[::-1])?",
                "options": ["A) 'Python'", "B) 'nohtyP'", "C) 'nohty'", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print('test'.center(10, '*'))?",
                "options": ["A) '***test***'", "B) '**test****'", "C) 'test******'", "D) '***test***'"],
                "answer": "A"
            },
            {
                "question": "What is the output of: print('hello\\nworld'.splitlines())?",
                "options": ["A) ['hello', 'world']", "B) 'hello world'", "C) ['hello\\nworld']", "D) Error"],
                "answer": "A"
            },
            {
                "question": "What is the output of: print('test'.ljust(8, '-'))?",
                "options": ["A) '----test'", "B) 'test----'", "C) '--test--'", "D) 'test'"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print('test'.rjust(8, '-'))?",
                "options": ["A) '----test'", "B) 'test----'", "C) '--test--'", "D) 'test'"],
                "answer": "A"
            },
            {
                "question": "What is the output of: print('TeSt'.swapcase())?",
                "options": ["A) 'test'", "B) 'TEST'", "C) 'tEsT'", "D) 'TeSt'"],
                "answer": "C"
            },
            {
                "question": "What is the output of: print('hello world'.title())?",
                "options": ["A) 'Hello World'", "B) 'Hello world'", "C) 'HELLO WORLD'", "D) 'hello world'"],
                "answer": "A"
            },
            {
                "question": "What is the output of: print('test'.zfill(8))?",
                "options": ["A) '0000test'", "B) 'test0000'", "C) '00test00'", "D) 'test'"],
                "answer": "A"
            },
            {
                "question": "What is the output of: print('  test  '.lstrip())?",
                "options": ["A) '  test  '", "B) 'test  '", "C) '  test'", "D) 'test'"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print('  test  '.rstrip())?",
                "options": ["A) '  test  '", "B) 'test  '", "C) '  test'", "D) 'test'"],
                "answer": "C"
            },
            {
                "question": "What is the output of: print('test123'.partition('1'))?",
                "options": ["A) ('test', '1', '23')", "B) ['test', '1', '23']", "C) 'test 1 23'", "D) Error"],
                "answer": "A"
            },
            {
                "question": "What is the output of: print('a-b-c'.rpartition('-'))?",
                "options": ["A) ('a-b', '-', 'c')", "B) ('a', '-', 'b-c')", "C) ['a', 'b', 'c']", "D) Error"],
                "answer": "A"
            },
            {
                "question": "What is the output of: print('test'.expandtabs())?",
                "options": ["A) 'test'", "B) 'test    '", "C) '    test'", "D) Error"],
                "answer": "A"
            },
            {
                "question": "What is the output of: print('test'.encode())?",
                "options": ["A) 'test'", "B) b'test'", "C) [116, 101, 115, 116]", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(b'test'.decode())?",
                "options": ["A) b'test'", "B) 'test'", "C) [116, 101, 115, 116]", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print('test'.index('e'))?",
                "options": ["A) 0", "B) 1", "C) 2", "D) -1"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print('test'.rindex('t'))?",
                "options": ["A) 0", "B) 3", "C) 2", "D) -1"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print('test'.rfind('x'))?",
                "options": ["A) 0", "B) -1", "C) None", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print('TEST'.isupper())?",
                "options": ["A) False", "B) True", "C) 'TEST'", "D) None"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print('test'.islower())?",
                "options": ["A) False", "B) True", "C) 'test'", "D) None"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print('Test'.istitle())?",
                "options": ["A) False", "B) True", "C) 'Test'", "D) None"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print('   '.isspace())?",
                "options": ["A) False", "B) True", "C) None", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print('test123'.isprintable())?",
                "options": ["A) False", "B) True", "C) None", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print('test'.removeprefix('te'))?",
                "options": ["A) 'test'", "B) 'st'", "C) 'te'", "D) Error in Python < 3.9"],
                "answer": "D"
            },
            {
                "question": "What is the output of: print('test'.removesuffix('st'))?",
                "options": ["A) 'test'", "B) 'te'", "C) 'st'", "D) Error in Python < 3.9"],
                "answer": "D"
            },
            # Other intermediate topics (25 questions)
            {
                "question": "What is the output of: print({x: x**2 for x in range(3)})?",
                "options": ["A) {0: 0, 1: 1, 2: 4}", "B) [0, 1, 4]", "C) {0, 1, 4}", "D) Error"],
                "answer": "A"
            },
            {
                "question": "What is the output of: print([x for x in 'abc'])?",
                "options": ["A) 'abc'", "B) ['a', 'b', 'c']", "C) ('a', 'b', 'c')", "D) {'a', 'b', 'c'}"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(tuple('abc'))?",
                "options": ["A) 'abc'", "B) ['a', 'b', 'c']", "C) ('a', 'b', 'c')", "D) {'a', 'b', 'c'}"],
                "answer": "C"
            },
            {
                "question": "What is the output of: print(set('aabbcc'))?",
                "options": ["A) {'a', 'b', 'c'}", "B) {'aa', 'bb', 'cc'}", "C) ['a', 'b', 'c']", "D) 'abc'"],
                "answer": "A"
            },
            {
                "question": "What is the output of: print(dict(zip(['a', 'b'], [1, 2])))?",
                "options": ["A) {'a': 1, 'b': 2}", "B) [('a', 1), ('b', 2)]", "C) {1: 'a', 2: 'b'}", "D) Error"],
                "answer": "A"
            },
            {
                "question": "What is the output of: print(list(enumerate('abc')))?",
                "options": ["A) ['a', 'b', 'c']", "B) [(0, 'a'), (1, 'b'), (2, 'c')]", "C) [0, 1, 2]", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(''.join(reversed('abc')))?",
                "options": ["A) 'abc'", "B) 'cba'", "C) ['c', 'b', 'a']", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(sorted('dcba'))?",
                "options": ["A) 'abcd'", "B) ['a', 'b', 'c', 'd']", "C) ('a', 'b', 'c', 'd')", "D) 'dcba'"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print('test' if True else 'fail')?",
                "options": ["A) 'test'", "B) 'fail'", "C) True", "D) Error"],
                "answer": "A"
            },
            {
                "question": "What is the output of: print([1, 2, 3].copy())?",
                "options": ["A) [1, 2, 3]", "B) [[1, 2, 3]]", "C) (1, 2, 3)", "D) {1, 2, 3}"],
                "answer": "A"
            },
            {
                "question": "What is the output of: print([1, 2, 3].clear() or 'empty')?",
                "options": ["A) []", "B) 'empty'", "C) None", "D) [1, 2, 3]"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print([1, 2, 2, 3].count(2))?",
                "options": ["A) 1", "B) 2", "C) 3", "D) 4"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print([1, 2, 3].index(2))?",
                "options": ["A) 0", "B) 1", "C) 2", "D) -1"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print([1, 2, 3].insert(1, 'x'))?",
                "options": ["A) [1, 'x', 2, 3]", "B) None", "C) ['x', 1, 2, 3]", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print({'a': 1}.keys())?",
                "options": ["A) ['a']", "B) dict_keys(['a'])", "C) ('a',)", "D) 'a'"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print({'a': 1}.values())?",
                "options": ["A) [1]", "B) dict_values([1])", "C) (1,)", "D) 1"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print({'a': 1}.items())?",
                "options": ["A) [('a', 1)]", "B) dict_items([('a', 1)])", "C) ('a', 1)", "D) {'a': 1}"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print({'a': 1}.pop('a'))?",
                "options": ["A) {'a': 1}", "B) 1", "C) 'a'", "D) None"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print({'a': 1}.popitem())?",
                "options": ["A) 'a'", "B) 1", "C) ('a', 1)", "D) {'a': 1}"],
                "answer": "C"
            },
            {
                "question": "What is the output of: print({'a': 1}.setdefault('b', 2))?",
                "options": ["A) 1", "B) 2", "C) {'a': 1, 'b': 2}", "D) None"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print({1, 2} | {2, 3})?",
                "options": ["A) {1, 2, 3}", "B) {2}", "C) {1, 3}", "D) Error"],
                "answer": "A"
            },
            {
                "question": "What is the output of: print({1, 2} & {2, 3})?",
                "options": ["A) {1, 2, 3}", "B) {2}", "C) {1, 3}", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print({1, 2} - {2, 3})?",
                "options": ["A) {1}", "B) {3}", "C) {1, 3}", "D) Error"],
                "answer": "A"
            },
            {
                "question": "What is the output of: print({1, 2} ^ {2, 3})?",
                "options": ["A) {1, 2, 3}", "B) {2}", "C) {1, 3}", "D) Error"],
                "answer": "C"
            },
            {
                "question": "What is the output of: print(lambda x: x.upper())('test')?",
                "options": ["A) 'test'", "B) 'TEST'", "C) Error", "D) <function>"],
                "answer": "B"
            }
        ]
    
    def run_exam(self):
        print("=" * 70)
        print("PCAP-31-03 PRACTICE EXAM - MEDIUM LEVEL (TEST 4)")
        print("Focus: Advanced Strings and Intermediate Python Concepts")
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
            print("Excellent! You have a solid grasp of intermediate concepts!")
        else:
            print("Status: FAIL ✗")
            print("Review string methods and data structure operations.")
        
        print("=" * 70)

if __name__ == "__main__":
    exam = PCAPExamMedium()
    exam.run_exam()
