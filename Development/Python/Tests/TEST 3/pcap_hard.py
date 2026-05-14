#!/usr/bin/env python3
"""
PCAP-31-03 Practice Exam - Hard Level
50 Questions covering advanced Python concepts
"""

import random

class PCAPExamHard:
    def __init__(self):
        self.score = 0
        self.total_questions = 50
        self.questions = [
            {
                "question": "What is the output of: print([x for x in range(10) if x % 2 == 0 if x % 3 == 0])?",
                "options": ["A) [0, 6]", "B) [0, 2, 4, 6, 8]", "C) [0, 3, 6, 9]", "D) [6]"],
                "answer": "A"
            },
            {
                "question": "What does the __call__ method allow an object to do?",
                "options": ["A) Be printed", "B) Be called like a function", "C) Be compared", "D) Be iterated"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(type(type(int)))?",
                "options": ["A) <class 'type'>", "B) <class 'int'>", "C) <class 'object'>", "D) <class 'class'>"],
                "answer": "A"
            },
            {
                "question": "What is the MRO in Python?",
                "options": ["A) Method Resolution Order", "B) Multiple Return Objects", "C) Module Reference Order", "D) Memory Resource Optimization"],
                "answer": "A"
            },
            {
                "question": "What is the output of: print((lambda x, y=2: x*y)(3))?",
                "options": ["A) 5", "B) 6", "C) Error", "D) 3"],
                "answer": "B"
            },
            {
                "question": "What does the __slots__ attribute do in a class?",
                "options": ["A) Defines allowed attributes", "B) Creates slots for methods", "C) Limits memory usage", "D) Both A and C"],
                "answer": "D"
            },
            {
                "question": "What is the output of: print(next(iter([1, 2, 3])))?",
                "options": ["A) [1, 2, 3]", "B) 1", "C) <iterator>", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What does the @functools.lru_cache decorator do?",
                "options": ["A) Caches function results", "B) Limits recursion", "C) Creates cache object", "D) Clears cache"],
                "answer": "A"
            },
            {
                "question": "What is the output of: print({**{'a': 1}, **{'b': 2}})?",
                "options": ["A) {'a': 1, 'b': 2}", "B) [{'a': 1}, {'b': 2}]", "C) Error", "D) {'a': 1}"],
                "answer": "A"
            },
            {
                "question": "What is a descriptor in Python?",
                "options": ["A) A documentation string", "B) An object with __get__, __set__, or __delete__", "C) A type annotation", "D) A class decorator"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(all([]))?",
                "options": ["A) False", "B) True", "C) None", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What does the __enter__ and __exit__ methods define?",
                "options": ["A) Iterator protocol", "B) Context manager protocol", "C) Descriptor protocol", "D) Callable protocol"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(int('10', 2))?",
                "options": ["A) 10", "B) 2", "C) 2", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What does the __new__ method do?",
                "options": ["A) Initializes instance", "B) Creates instance", "C) Deletes instance", "D) Copies instance"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(frozenset([1, 2, 2, 3]))?",
                "options": ["A) frozenset({1, 2, 3})", "B) {1, 2, 3}", "C) [1, 2, 3]", "D) (1, 2, 3)"],
                "answer": "A"
            },
            {
                "question": "What is a metaclass?",
                "options": ["A) A class of classes", "B) A parent class", "C) An abstract class", "D) A static class"],
                "answer": "A"
            },
            {
                "question": "What is the output of: print((x:=5, x+1))?",
                "options": ["A) (5, 6)", "B) Error", "C) 6", "D) (5, 5)"],
                "answer": "A"
            },
            {
                "question": "What does the __getattr__ method do?",
                "options": ["A) Gets all attributes", "B) Called when attribute is not found", "C) Gets attribute type", "D) Creates attribute"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(bytes([65, 66, 67]).decode())?",
                "options": ["A) [65, 66, 67]", "B) 'ABC'", "C) b'ABC'", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What does the __repr__ method return?",
                "options": ["A) String for users", "B) String for developers/debugging", "C) Object representation", "D) Both B and C"],
                "answer": "D"
            },
            {
                "question": "What is the output of: print(divmod(17, 5))?",
                "options": ["A) 3.4", "B) (3, 2)", "C) [3, 2]", "D) 3"],
                "answer": "B"
            },
            {
                "question": "What does the __setattr__ method do?",
                "options": ["A) Sets all attributes", "B) Called when setting an attribute", "C) Creates setter", "D) Validates attributes"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(complex(2, 3).real)?",
                "options": ["A) 2", "B) 3", "C) 2.0", "D) (2+3j)"],
                "answer": "C"
            },
            {
                "question": "What is a closure in Python?",
                "options": ["A) A closed function", "B) Function with access to enclosing scope", "C) A private function", "D) A nested class"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(memoryview(b'abc')[0])?",
                "options": ["A) 'a'", "B) b'a'", "C) 97", "D) 0"],
                "answer": "C"
            },
            {
                "question": "What does the __delattr__ method do?",
                "options": ["A) Deletes all attributes", "B) Called when deleting an attribute", "C) Removes class", "D) Clears memory"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(ord('A'))?",
                "options": ["A) 'A'", "B) 65", "C) 1", "D) 97"],
                "answer": "B"
            },
            {
                "question": "What does the __hash__ method return?",
                "options": ["A) Object ID", "B) Hash value for object", "C) Memory address", "D) String representation"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(chr(65))?",
                "options": ["A) 65", "B) 'A'", "C) 'a'", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What does the __eq__ method define?",
                "options": ["A) Equality comparison", "B) Identity comparison", "C) Type comparison", "D) Value assignment"],
                "answer": "A"
            },
            {
                "question": "What is the output of: print(bin(10))?",
                "options": ["A) 10", "B) '0b1010'", "C) 1010", "D) '1010'"],
                "answer": "B"
            },
            {
                "question": "What does the __lt__ method define?",
                "options": ["A) Less than comparison", "B) Less than or equal", "C) Length test", "D) List type"],
                "answer": "A"
            },
            {
                "question": "What is the output of: print(hex(255))?",
                "options": ["A) 255", "B) 'ff'", "C) '0xff'", "D) 'FF'"],
                "answer": "C"
            },
            {
                "question": "What does the __len__ method return?",
                "options": ["A) Object size", "B) Length of object", "C) Number of attributes", "D) Memory size"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(oct(8))?",
                "options": ["A) 8", "B) '0o10'", "C) '10'", "D) 10"],
                "answer": "B"
            },
            {
                "question": "What does the __iter__ method return?",
                "options": ["A) List of items", "B) Iterator object", "C) First item", "D) Length"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(pow(2, 3, 3))?",
                "options": ["A) 8", "B) 2", "C) 6", "D) 9"],
                "answer": "B"
            },
            {
                "question": "What does the __next__ method do?",
                "options": ["A) Returns next item", "B) Moves to next", "C) Creates iterator", "D) Both A and B"],
                "answer": "A"
            },
            {
                "question": "What is the output of: print(vars() == locals())?",
                "options": ["A) False", "B) True", "C) Error", "D) None"],
                "answer": "B"
            },
            {
                "question": "What does the __contains__ method define?",
                "options": ["A) Container type", "B) 'in' operator behavior", "C) Content validation", "D) Size check"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(eval('2 + 3'))?",
                "options": ["A) '2 + 3'", "B) 5", "C) '5'", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What does the __getitem__ method allow?",
                "options": ["A) Get all items", "B) Indexing and slicing", "C) Get item count", "D) Get item type"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(compile('x=1', '', 'exec'))?",
                "options": ["A) 1", "B) x=1", "C) <code object>", "D) Error"],
                "answer": "C"
            },
            {
                "question": "What does the __setitem__ method allow?",
                "options": ["A) Set all items", "B) Item assignment via indexing", "C) Set item type", "D) Create items"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(callable(lambda: None))?",
                "options": ["A) False", "B) True", "C) None", "D) <function>"],
                "answer": "B"
            },
            {
                "question": "What does the __delitem__ method allow?",
                "options": ["A) Delete all items", "B) Item deletion via del", "C) Clear container", "D) Remove duplicates"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(id(5) == id(5))?",
                "options": ["A) False", "B) True", "C) Depends on implementation", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What does the __add__ method define?",
                "options": ["A) Addition operation", "B) Append operation", "C) Accumulation", "D) Aggregation"],
                "answer": "A"
            },
            {
                "question": "What is the output of: print(format(255, 'x'))?",
                "options": ["A) 255", "B) 'ff'", "C) '0xff'", "D) 'FF'"],
                "answer": "B"
            },
            {
                "question": "What does the __mul__ method define?",
                "options": ["A) Multiplication operation", "B) Multiple values", "C) Multi-threading", "D) Multiplexing"],
                "answer": "A"
            }
        ]
    
    def run_exam(self):
        print("=" * 60)
        print("PCAP-31-03 PRACTICE EXAM - HARD LEVEL")
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
    exam = PCAPExamHard()
    exam.run_exam()
