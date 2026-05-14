#!/usr/bin/env python3
"""
PCAP-31-03 Practice Exam - Hard Level (TEST 4)
50 Questions with emphasis on strings and advanced concepts
"""

import random

class PCAPExamHard:
    def __init__(self):
        self.score = 0
        self.total_questions = 50
        self.questions = [
            # Complex String Questions (20 questions)
            {
                "question": "What is the output of: print('test'.translate(str.maketrans('t', 'T')))?",
                "options": ["A) 'test'", "B) 'TesT'", "C) 'TEST'", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(f'{\"test\":>10}')?",
                "options": ["A) 'test      '", "B) '      test'", "C) '   test   '", "D) 'test'"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(f'{\"test\":<10}')?",
                "options": ["A) 'test      '", "B) '      test'", "C) '   test   '", "D) 'test'"],
                "answer": "A"
            },
            {
                "question": "What is the output of: print(f'{\"test\":^10}')?",
                "options": ["A) 'test      '", "B) '      test'", "C) '   test   '", "D) 'test'"],
                "answer": "C"
            },
            {
                "question": "What is the output of: print(f'{100:08d}')?",
                "options": ["A) '100'", "B) '00000100'", "C) '10000000'", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(f'{3.14159:.2f}')?",
                "options": ["A) '3.14'", "B) '3.14159'", "C) '3.1'", "D) '3'"],
                "answer": "A"
            },
            {
                "question": "What is the output of: print('{0}{1}{0}'.format('a', 'b'))?",
                "options": ["A) 'aba'", "B) 'aab'", "C) 'baa'", "D) Error"],
                "answer": "A"
            },
            {
                "question": "What is the output of: print('{name}'.format(name='test'))?",
                "options": ["A) '{name}'", "B) 'test'", "C) 'name'", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print('%s %d' % ('test', 5))?",
                "options": ["A) 'test 5'", "B) '%s %d'", "C) 'test5'", "D) Error"],
                "answer": "A"
            },
            {
                "question": "What is the output of: print('%.2f' % 3.14159)?",
                "options": ["A) '3.14159'", "B) '3.14'", "C) '3.1'", "D) '3'"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(r'\\n')?",
                "options": ["A) '\\n' (newline)", "B) '\\\\n'", "C) '\\n' (literal)", "D) Error"],
                "answer": "C"
            },
            {
                "question": "What is the output of: print('test'.__len__())?",
                "options": ["A) 4", "B) 'test'", "C) Error", "D) None"],
                "answer": "A"
            },
            {
                "question": "What is the output of: print('test'.__contains__('es'))?",
                "options": ["A) False", "B) True", "C) 1", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print('test'.__add__('ing'))?",
                "options": ["A) 'test'", "B) 'testing'", "C) 'tesing'", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print('test'.__mul__(2))?",
                "options": ["A) 'test'", "B) 'testtest'", "C) 'test2'", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print('test'.__getitem__(1))?",
                "options": ["A) 't'", "B) 'e'", "C) 's'", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(str.join('-', ['a', 'b', 'c']))?",
                "options": ["A) 'a-b-c'", "B) '-abc'", "C) 'abc-'", "D) Error"],
                "answer": "A"
            },
            {
                "question": "What is the output of: print(ascii('café'))?",
                "options": ["A) 'café'", "B) \"'caf\\\\xe9'\"", "C) 'cafe'", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(repr('test\\n'))?",
                "options": ["A) 'test\\n'", "B) \"'test\\\\n'\"", "C) 'test'", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print('test'.casefold() == 'TEST'.casefold())?",
                "options": ["A) False", "B) True", "C) None", "D) Error"],
                "answer": "B"
            },
            # Advanced Python topics (30 questions)
            {
                "question": "What is the output of: print(slice(1, 5, 2).indices(10))?",
                "options": ["A) (1, 5, 2)", "B) [1, 3]", "C) slice(1, 5, 2)", "D) Error"],
                "answer": "A"
            },
            {
                "question": "What is the output of: print('test'[slice(1, 3)])?",
                "options": ["A) 'te'", "B) 'es'", "C) 'st'", "D) 'test'"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(bytes.fromhex('48656c6c6f').decode())?",
                "options": ["A) '48656c6c6f'", "B) 'Hello'", "C) b'Hello'", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print('Hello'.encode().hex())?",
                "options": ["A) 'Hello'", "B) '48656c6c6f'", "C) b'48656c6c6f'", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(bytearray(b'test')[0])?",
                "options": ["A) 't'", "B) b't'", "C) 116", "D) 0"],
                "answer": "C"
            },
            {
                "question": "What is the output of: print(memoryview(b'test').tobytes())?",
                "options": ["A) 'test'", "B) b'test'", "C) [116, 101, 115, 116]", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(str.maketrans('abc', '123'))?",
                "options": ["A) {'a': '1', 'b': '2', 'c': '3'}", "B) {97: 49, 98: 50, 99: 51}", "C) 'abc123'", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print('test'.translate({116: 84}))?",
                "options": ["A) 'test'", "B) 'Test'", "C) 'TEST'", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(format(255, '#x'))?",
                "options": ["A) '255'", "B) 'ff'", "C) '0xff'", "D) '#xff'"],
                "answer": "C"
            },
            {
                "question": "What is the output of: print(format(10, 'b'))?",
                "options": ["A) '10'", "B) '1010'", "C) '0b1010'", "D) 10"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print('{:,}'.format(1000000))?",
                "options": ["A) '1000000'", "B) '1,000,000'", "C) '1.000.000'", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print('{:.2%}'.format(0.5))?",
                "options": ["A) '0.5'", "B) '50%'", "C) '50.00%'", "D) '0.50'"],
                "answer": "C"
            },
            {
                "question": "What is the output of: print('{:=+10}'.format(5))?",
                "options": ["A) '+        5'", "B) '+5        '", "C) '+       5'", "D) Error"],
                "answer": "C"
            },
            {
                "question": "What is the output of: print(f'{5:05d}')?",
                "options": ["A) '5'", "B) '00005'", "C) '50000'", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(f'{-5:05d}')?",
                "options": ["A) '-0005'", "B) '0-005'", "C) '-5000'", "D) Error"],
                "answer": "A"
            },
            {
                "question": "What is the output of: print('{0[0]}'.format(['a', 'b']))?",
                "options": ["A) 'a'", "B) 'b'", "C) ['a', 'b']", "D) Error"],
                "answer": "A"
            },
            {
                "question": "What is the output of: print('{0.real}'.format(3+4j))?",
                "options": ["A) 3", "B) 3.0", "C) 4", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(isinstance('test', str))?",
                "options": ["A) False", "B) True", "C) 'test'", "D) str"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(issubclass(bool, int))?",
                "options": ["A) False", "B) True", "C) None", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(getattr('test', 'upper')())?",
                "options": ["A) 'test'", "B) 'TEST'", "C) Error", "D) <method>"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(setattr(type('C', (), {}), 'x', 5))?",
                "options": ["A) 5", "B) None", "C) <class 'C'>", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(delattr(type('C', (), {'x': 5}), 'x'))?",
                "options": ["A) 5", "B) None", "C) Error", "D) <class 'C'>"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(dir('test')[:3])?",
                "options": ["A) ['t', 'e', 's']", "B) First 3 methods", "C) ['__add__', '__class__', '__contains__']", "D) Error"],
                "answer": "C"
            },
            {
                "question": "What is the output of: print(vars(type('C', (), {'x': 5})()))?",
                "options": ["A) {'x': 5}", "B) {}", "C) None", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(hash('test') == hash('test'))?",
                "options": ["A) False", "B) True", "C) Depends", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(id('a') == id('a'))?",
                "options": ["A) False", "B) True", "C) Depends", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(iter('abc').__next__())?",
                "options": ["A) 'abc'", "B) 'a'", "C) 0", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(next(iter('abc'), 'default'))?",
                "options": ["A) 'abc'", "B) 'a'", "C) 'default'", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(all('test'))?",
                "options": ["A) False", "B) True", "C) 'test'", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(any(''))?",
                "options": ["A) False", "B) True", "C) ''", "D) Error"],
                "answer": "A"
            }
        ]
    
    def run_exam(self):
        print("=" * 70)
        print("PCAP-31-03 PRACTICE EXAM - HARD LEVEL (TEST 4)")
        print("Focus: Complex Strings and Advanced Python Concepts")
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
            print("Outstanding! You've mastered advanced Python concepts!")
        else:
            print("Status: FAIL ✗")
            print("Focus on string formatting, encoding, and advanced built-ins.")
        
        print("=" * 70)

if __name__ == "__main__":
    exam = PCAPExamHard()
    exam.run_exam()
