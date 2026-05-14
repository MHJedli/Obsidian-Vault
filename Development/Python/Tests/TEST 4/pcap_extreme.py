#!/usr/bin/env python3
"""
PCAP-31-03 Practice Exam - Extreme Level (TEST 4)
50 Questions with emphasis on strings and expert-level concepts
"""

import random

class PCAPExamExtreme:
    def __init__(self):
        self.score = 0
        self.total_questions = 50
        self.questions = [
            # Expert String Questions (15 questions)
            {
                "question": "What is the output of: print('test'.encode('utf-16').decode('utf-16'))?",
                "options": ["A) 'test'", "B) b'test'", "C) Error", "D) '\\xff\\xfet\\x00e\\x00s\\x00t\\x00'"],
                "answer": "A"
            },
            {
                "question": "What is the output of: print(str.__mro__)?",
                "options": ["A) (<class 'str'>, <class 'object'>)", "B) (str, object)", "C) <class 'str'>", "D) Error"],
                "answer": "A"
            },
            {
                "question": "What is the output of: print(type(str.__dict__))?",
                "options": ["A) <class 'dict'>", "B) <class 'mappingproxy'>", "C) dict", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print('test'.__class__.__name__)?",
                "options": ["A) 'test'", "B) 'str'", "C) 'string'", "D) 'type'"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(str.__bases__)?",
                "options": ["A) ()", "B) (object,)", "C) (type,)", "D) (<class 'object'>,)"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print('test'.__sizeof__())?",
                "options": ["A) 4", "B) 53", "C) 49 or 53 (depends)", "D) Error"],
                "answer": "C"
            },
            {
                "question": "What is the output of: print(intern('test') is intern('test'))?",
                "options": ["A) False", "B) True", "C) Depends", "D) Error"],
                "answer": "D"
            },
            {
                "question": "What is the output of: print(sys.intern('test') is sys.intern('test'))?",
                "options": ["A) False", "B) True", "C) Depends", "D) Error without import"],
                "answer": "D"
            },
            {
                "question": "What is the output of: print('test'.__format__('s'))?",
                "options": ["A) 'test'", "B) 's'", "C) Error", "D) 'tests'"],
                "answer": "A"
            },
            {
                "question": "What is the output of: print('test'.__repr__())?",
                "options": ["A) test", "B) 'test'", "C) \"'test'\"", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print('test'.__str__())?",
                "options": ["A) test", "B) 'test'", "C) \"'test'\"", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print('test'.__hash__() == 'test'.__hash__())?",
                "options": ["A) False", "B) True", "C) Depends", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print('test'.__eq__('test'))?",
                "options": ["A) False", "B) True", "C) 'test'", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print('test'.__ne__('TEST'))?",
                "options": ["A) False", "B) True", "C) None", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print('a'.__lt__('b'))?",
                "options": ["A) False", "B) True", "C) -1", "D) Error"],
                "answer": "B"
            },
            # Expert-level Python topics (35 questions)
            {
                "question": "What is the output of: print('a'.__gt__('A'))?",
                "options": ["A) False", "B) True", "C) 1", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print('a'.__le__('a'))?",
                "options": ["A) False", "B) True", "C) 0", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print('a'.__ge__('b'))?",
                "options": ["A) False", "B) True", "C) -1", "D) Error"],
                "answer": "A"
            },
            {
                "question": "What is the output of: print('test'.__mod__('s'))?",
                "options": ["A) 'test'", "B) 'tets'", "C) Error", "D) NotImplemented"],
                "answer": "D"
            },
            {
                "question": "What is the output of: print('test'.__rmod__('%s'))?",
                "options": ["A) 'test'", "B) '%s'", "C) Error", "D) NotImplemented"],
                "answer": "A"
            },
            {
                "question": "What is the output of: print(str.__doc__[:20])?",
                "options": ["A) First 20 chars of str docstring", "B) 'str(object='') -> str'", "C) None", "D) Error"],
                "answer": "A"
            },
            {
                "question": "What is the output of: print(type(str.__dict__['upper']))?",
                "options": ["A) <class 'function'>", "B) <class 'method'>", "C) <class 'method_descriptor'>", "D) <class 'builtin_function_or_method'>"],
                "answer": "C"
            },
            {
                "question": "What is the output of: print(str.__subclasses__())?",
                "options": ["A) []", "B) List of str subclasses", "C) Error", "D) None"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print('test'.__dir__()[:3])?",
                "options": ["A) ['t', 'e', 's']", "B) First 3 attributes", "C) ['__add__', '__class__', '__contains__']", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print('test'.__reduce__())?",
                "options": ["A) 'test'", "B) (<class 'str'>, ('test',))", "C) Error", "D) None"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print('test'.__reduce_ex__(4))?",
                "options": ["A) 'test'", "B) (<class 'str'>, ('test',))", "C) Error", "D) None"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print('test'.__getnewargs__())?",
                "options": ["A) ('test',)", "B) 'test'", "C) ()", "D) Error"],
                "answer": "A"
            },
            {
                "question": "What is the output of: print(object.__subclasshook__(str, type('C', (), {})))?",
                "options": ["A) True", "B) False", "C) NotImplemented", "D) Error"],
                "answer": "C"
            },
            {
                "question": "What is the output of: print(str.__instancecheck__(str, 'test'))?",
                "options": ["A) True", "B) False", "C) Error", "D) NotImplemented"],
                "answer": "C"
            },
            {
                "question": "What is the output of: print(type.__instancecheck__(str, 'test'))?",
                "options": ["A) False", "B) True", "C) Error", "D) NotImplemented"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(str.__subclasscheck__(str, type('C', (str,), {})))?",
                "options": ["A) False", "B) True", "C) Error", "D) NotImplemented"],
                "answer": "C"
            },
            {
                "question": "What is the output of: print(type.__subclasscheck__(str, type('C', (str,), {})))?",
                "options": ["A) False", "B) True", "C) Error", "D) NotImplemented"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(str.__init__('test'))?",
                "options": ["A) 'test'", "B) None", "C) Error", "D) <str object>"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(str.__new__(str, 'test'))?",
                "options": ["A) 'test'", "B) None", "C) Error", "D) <str object>"],
                "answer": "A"
            },
            {
                "question": "What is the output of: print('test'.__iter__().__next__())?",
                "options": ["A) 'test'", "B) 't'", "C) 0", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print('test'[0:2].__class__.__name__)?",
                "options": ["A) 'slice'", "B) 'str'", "C) 'substring'", "D) 'string'"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(bytes.__bases__)?",
                "options": ["A) (str,)", "B) (object,)", "C) (bytearray,)", "D) ()"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(bytearray.__bases__)?",
                "options": ["A) (bytes,)", "B) (object,)", "C) (str,)", "D) ()"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(type(b'test').__name__)?",
                "options": ["A) 'str'", "B) 'bytes'", "C) 'bytearray'", "D) 'byte'"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(type(bytearray(b'test')).__name__)?",
                "options": ["A) 'bytes'", "B) 'bytearray'", "C) 'array'", "D) 'byte'"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(type(memoryview(b'test')).__name__)?",
                "options": ["A) 'bytes'", "B) 'memoryview'", "C) 'memory'", "D) 'view'"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(memoryview(b'test').format)?",
                "options": ["A) 'B'", "B) 'b'", "C) 'bytes'", "D) Error"],
                "answer": "A"
            },
            {
                "question": "What is the output of: print(memoryview(b'test').itemsize)?",
                "options": ["A) 1", "B) 4", "C) 8", "D) Error"],
                "answer": "A"
            },
            {
                "question": "What is the output of: print(memoryview(b'test').ndim)?",
                "options": ["A) 0", "B) 1", "C) 2", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(memoryview(b'test').readonly)?",
                "options": ["A) False", "B) True", "C) None", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(memoryview(bytearray(b'test')).readonly)?",
                "options": ["A) False", "B) True", "C) None", "D) Error"],
                "answer": "A"
            },
            {
                "question": "What is the output of: print(b'test'.hex(' '))?",
                "options": ["A) '74 65 73 74'", "B) '74657374'", "C) 'test'", "D) Error in Python < 3.8"],
                "answer": "D"
            },
            {
                "question": "What is the output of: print(int.from_bytes(b'\\x00\\x01', 'big'))?",
                "options": ["A) 0", "B) 1", "C) 256", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print((1).to_bytes(2, 'big'))?",
                "options": ["A) b'\\x00\\x01'", "B) b'\\x01\\x00'", "C) b'\\x01'", "D) Error"],
                "answer": "A"
            },
            {
                "question": "What is the output of: print(str.isidentifier('_test'))?",
                "options": ["A) False", "B) True", "C) None", "D) Error"],
                "answer": "B"
            }
        ]
    
    def run_exam(self):
        print("=" * 70)
        print("PCAP-31-03 PRACTICE EXAM - EXTREME LEVEL (TEST 4)")
        print("Focus: Expert Strings and Python Internals")
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
            print("Exceptional! You're a Python expert!")
        else:
            print("Status: FAIL ✗")
            print("Study string internals, magic methods, and Python object model.")
        
        print("=" * 70)

if __name__ == "__main__":
    exam = PCAPExamExtreme()
    exam.run_exam()
