#!/usr/bin/env python3
"""
PCAP-31-03 Practice Exam - Medium Level
50 Questions covering intermediate Python concepts
"""

import random

class PCAPExamMedium:
    def __init__(self):
        self.score = 0
        self.total_questions = 50
        self.questions = [
            {
                "question": "What is the output of: print([1, 2, 3] + [4, 5])?",
                "options": ["A) [1, 2, 3, 4, 5]", "B) [5, 7, 3]", "C) Error", "D) [[1, 2, 3], [4, 5]]"],
                "answer": "A"
            },
            {
                "question": "What does the 'self' parameter represent in a class method?",
                "options": ["A) The class itself", "B) The instance of the class", "C) A keyword", "D) A global variable"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print({1, 2, 2, 3})?",
                "options": ["A) {1, 2, 2, 3}", "B) {1, 2, 3}", "C) [1, 2, 3]", "D) Error"],
                "answer": "B"
            },
            {
                "question": "Which method is called when an object is created?",
                "options": ["A) __init__", "B) __new__", "C) __create__", "D) __start__"],
                "answer": "A"
            },
            {
                "question": "What is the output of: print('hello'.upper().isupper())?",
                "options": ["A) False", "B) True", "C) 'HELLO'", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What does the 'pass' statement do?",
                "options": ["A) Exits the program", "B) Does nothing", "C) Skips iteration", "D) Returns None"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(list('abc'))?",
                "options": ["A) ['abc']", "B) ['a', 'b', 'c']", "C) 'abc'", "D) Error"],
                "answer": "B"
            },
            {
                "question": "Which keyword is used to inherit from a parent class?",
                "options": ["A) extends", "B) inherits", "C) class ChildClass(ParentClass)", "D) super"],
                "answer": "C"
            },
            {
                "question": "What is the output of: print([x**2 for x in range(3)])?",
                "options": ["A) [0, 1, 4]", "B) [1, 4, 9]", "C) [0, 1, 2]", "D) Error"],
                "answer": "A"
            },
            {
                "question": "What does the 'global' keyword do?",
                "options": ["A) Creates a global variable", "B) Accesses a global variable inside a function", "C) Deletes a variable", "D) Makes a function global"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print({'a': 1}.get('b', 0))?",
                "options": ["A) None", "B) 0", "C) Error", "D) 'b'"],
                "answer": "B"
            },
            {
                "question": "Which method is used to add multiple elements to a list?",
                "options": ["A) append()", "B) add()", "C) extend()", "D) insert()"],
                "answer": "C"
            },
            {
                "question": "What is the output of: print(lambda x: x*2)(5)?",
                "options": ["A) 10", "B) 5", "C) x*2", "D) Error"],
                "answer": "A"
            },
            {
                "question": "What does the 'yield' keyword do?",
                "options": ["A) Returns a value and exits", "B) Creates a generator", "C) Pauses execution", "D) Raises an exception"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print('test'.replace('t', 'T'))?",
                "options": ["A) 'TesT'", "B) 'Test'", "C) 'TesT'", "D) 'TEST'"],
                "answer": "C"
            },
            {
                "question": "Which exception is raised when dividing by zero?",
                "options": ["A) ValueError", "B) ZeroDivisionError", "C) ArithmeticError", "D) DivisionError"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(all([True, True, False]))?",
                "options": ["A) True", "B) False", "C) [True, True, False]", "D) None"],
                "answer": "B"
            },
            {
                "question": "What does the 'with' statement do?",
                "options": ["A) Creates a loop", "B) Manages context and resources", "C) Defines a function", "D) Imports a module"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print({x: x**2 for x in range(3)})?",
                "options": ["A) {0: 0, 1: 1, 2: 4}", "B) [0, 1, 4]", "C) {0, 1, 4}", "D) Error"],
                "answer": "A"
            },
            {
                "question": "Which method is used to remove a specific element from a list?",
                "options": ["A) delete()", "B) remove()", "C) pop()", "D) discard()"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(any([False, False, True]))?",
                "options": ["A) True", "B) False", "C) None", "D) Error"],
                "answer": "A"
            },
            {
                "question": "What does the '*args' parameter do in a function?",
                "options": ["A) Accepts keyword arguments", "B) Accepts variable number of positional arguments", "C) Multiplies arguments", "D) Creates a pointer"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print('a' in {'a': 1})?",
                "options": ["A) False", "B) True", "C) 1", "D) Error"],
                "answer": "B"
            },
            {
                "question": "Which method is used to sort a list in place?",
                "options": ["A) sorted()", "B) sort()", "C) order()", "D) arrange()"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(isinstance(5, int))?",
                "options": ["A) False", "B) True", "C) 5", "D) int"],
                "answer": "B"
            },
            {
                "question": "What does the '__str__' method do?",
                "options": ["A) Converts to string", "B) Returns string representation for print()", "C) Creates a string", "D) Compares strings"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print([1, 2, 3][::-1])?",
                "options": ["A) [1, 2, 3]", "B) [3, 2, 1]", "C) [-1, -2, -3]", "D) Error"],
                "answer": "B"
            },
            {
                "question": "Which function is used to open a file?",
                "options": ["A) file()", "B) open()", "C) read()", "D) load()"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(zip([1, 2], ['a', 'b']))?",
                "options": ["A) [(1, 'a'), (2, 'b')]", "B) [1, 2, 'a', 'b']", "C) <zip object>", "D) Error"],
                "answer": "C"
            },
            {
                "question": "What does the '**kwargs' parameter do?",
                "options": ["A) Accepts positional arguments", "B) Accepts keyword arguments", "C) Exponentiates arguments", "D) Creates a dictionary"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(set([1, 2, 2, 3]))?",
                "options": ["A) [1, 2, 3]", "B) {1, 2, 2, 3}", "C) {1, 2, 3}", "D) (1, 2, 3)"],
                "answer": "C"
            },
            {
                "question": "Which method is used to get all keys from a dictionary?",
                "options": ["A) keys()", "B) getKeys()", "C) allKeys()", "D) keyList()"],
                "answer": "A"
            },
            {
                "question": "What is the output of: print(enumerate(['a', 'b']))?",
                "options": ["A) [(0, 'a'), (1, 'b')]", "B) <enumerate object>", "C) [0, 1]", "D) ['a', 'b']"],
                "answer": "B"
            },
            {
                "question": "What does the 'finally' block do in exception handling?",
                "options": ["A) Catches exceptions", "B) Always executes", "C) Raises exceptions", "D) Skips exceptions"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(list(map(str, [1, 2, 3])))?",
                "options": ["A) [1, 2, 3]", "B) ['1', '2', '3']", "C) '123'", "D) Error"],
                "answer": "B"
            },
            {
                "question": "Which operator is used for identity comparison?",
                "options": ["A) ==", "B) is", "C) ===", "D) equals"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(tuple([1, 2, 3]))?",
                "options": ["A) [1, 2, 3]", "B) (1, 2, 3)", "C) {1, 2, 3}", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What does the 'staticmethod' decorator do?",
                "options": ["A) Makes method static", "B) Creates class method", "C) Makes method private", "D) Prevents inheritance"],
                "answer": "A"
            },
            {
                "question": "What is the output of: print(list(filter(lambda x: x>2, [1,2,3,4])))?",
                "options": ["A) [1, 2]", "B) [3, 4]", "C) [2, 3, 4]", "D) [1, 2, 3, 4]"],
                "answer": "B"
            },
            {
                "question": "Which method is used to update a dictionary?",
                "options": ["A) add()", "B) update()", "C) merge()", "D) append()"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print('test'.startswith('te'))?",
                "options": ["A) False", "B) True", "C) 'te'", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What does the 'classmethod' decorator do?",
                "options": ["A) Creates instance method", "B) Creates class method", "C) Makes method static", "D) Prevents overriding"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print([1, 2] * 2)?",
                "options": ["A) [2, 4]", "B) [1, 2, 1, 2]", "C) [1, 2, 2]", "D) Error"],
                "answer": "B"
            },
            {
                "question": "Which exception is raised when a key is not found in a dictionary?",
                "options": ["A) ValueError", "B) KeyError", "C) IndexError", "D) AttributeError"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(sorted([3, 1, 2]))?",
                "options": ["A) [3, 1, 2]", "B) [1, 2, 3]", "C) [3, 2, 1]", "D) None"],
                "answer": "B"
            },
            {
                "question": "What does the 'property' decorator do?",
                "options": ["A) Creates a property", "B) Makes attribute private", "C) Creates getter method", "D) Both A and C"],
                "answer": "D"
            },
            {
                "question": "What is the output of: print(dict(a=1, b=2))?",
                "options": ["A) {'a': 1, 'b': 2}", "B) {a: 1, b: 2}", "C) ['a', 1, 'b', 2]", "D) Error"],
                "answer": "A"
            },
            {
                "question": "Which method is used to reverse a list in place?",
                "options": ["A) reversed()", "B) reverse()", "C) [::-1]", "D) backward()"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(hasattr('test', 'upper'))?",
                "options": ["A) False", "B) True", "C) 'upper'", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What does the 'raise' keyword do?",
                "options": ["A) Catches exceptions", "B) Raises an exception", "C) Handles errors", "D) Returns error"],
                "answer": "B"
            }
        ]
    
    def run_exam(self):
        print("=" * 60)
        print("PCAP-31-03 PRACTICE EXAM - MEDIUM LEVEL")
        print("=" * 60)
        print(f"Total Questions: {self.total_questions}")
        print("Instructions: Enter A, B, C, or D for each question")
        print("=" * 60)
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
            
            print("-" * 60)
        
        self.show_results()
    
    def show_results(self):
        percentage = (self.score / self.total_questions) * 100
        print("\n" + "=" * 60)
        print("EXAM RESULTS")
        print("=" * 60)
        print(f"Score: {self.score}/{self.total_questions}")
        print(f"Percentage: {percentage:.2f}%")
        
        if percentage >= 70:
            print("Status: PASS ✓")
        else:
            print("Status: FAIL ✗")
        
        print("=" * 60)

if __name__ == "__main__":
    exam = PCAPExamMedium()
    exam.run_exam()
