#!/usr/bin/env python3
"""
PCAP-31-03 Practice Exam - Extreme Level
50 Questions covering expert-level Python concepts
"""

import random

class PCAPExamExtreme:
    def __init__(self):
        self.score = 0
        self.total_questions = 50
        self.questions = [
            {
                "question": "What is the output of: print((lambda f: f(f))(lambda x: lambda: x(x)()))?",
                "options": ["A) RecursionError", "B) <function>", "C) None", "D) Error"],
                "answer": "A"
            },
            {
                "question": "What does sys._getframe() return?",
                "options": ["A) Current frame object", "B) Stack trace", "C) Function frame", "D) All frames"],
                "answer": "A"
            },
            {
                "question": "What is the output of: print(type.__bases__)?",
                "options": ["A) (object,)", "B) (type,)", "C) ()", "D) (<class 'type'>,)"],
                "answer": "A"
            },
            {
                "question": "What does the __prepare__ method do in a metaclass?",
                "options": ["A) Prepares instance", "B) Returns namespace dict for class creation", "C) Initializes metaclass", "D) Validates class"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(object.__bases__)?",
                "options": ["A) (type,)", "B) (object,)", "C) ()", "D) None"],
                "answer": "C"
            },
            {
                "question": "What does the __init_subclass__ method do?",
                "options": ["A) Initializes subclass", "B) Called when class is subclassed", "C) Creates subclass", "D) Validates inheritance"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(type(type))?",
                "options": ["A) <class 'type'>", "B) <class 'object'>", "C) <class 'class'>", "D) <class 'metaclass'>"],
                "answer": "A"
            },
            {
                "question": "What does the __set_name__ method do in a descriptor?",
                "options": ["A) Sets descriptor name", "B) Called when descriptor is assigned to class", "C) Names the owner", "D) Both A and B"],
                "answer": "D"
            },
            {
                "question": "What is the output of: print(type.__mro__)?",
                "options": ["A) (<class 'type'>, <class 'object'>)", "B) (<class 'object'>,)", "C) (type, object)", "D) Error"],
                "answer": "A"
            },
            {
                "question": "What does the __class_getitem__ method enable?",
                "options": ["A) Class indexing", "B) Generic type hints", "C) Item access", "D) Class iteration"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(int.__mro__)?",
                "options": ["A) (<class 'int'>, <class 'object'>)", "B) (<class 'int'>,)", "C) (int, object)", "D) Error"],
                "answer": "A"
            },
            {
                "question": "What does the __instancecheck__ method control?",
                "options": ["A) isinstance() behavior", "B) Instance creation", "C) Type checking", "D) Instance validation"],
                "answer": "A"
            },
            {
                "question": "What is the output of: print(bool.__bases__)?",
                "options": ["A) (object,)", "B) (int,)", "C) (type,)", "D) ()"],
                "answer": "B"
            },
            {
                "question": "What does the __subclasscheck__ method control?",
                "options": ["A) issubclass() behavior", "B) Subclass creation", "C) Inheritance check", "D) Class validation"],
                "answer": "A"
            },
            {
                "question": "What is the output of: print(type(object))?",
                "options": ["A) <class 'object'>", "B) <class 'type'>", "C) object", "D) type"],
                "answer": "B"
            },
            {
                "question": "What does the __mro_entries__ method do?",
                "options": ["A) Returns MRO", "B) Modifies MRO for base classes", "C) Creates MRO", "D) Validates MRO"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(type(None).__name__)?",
                "options": ["A) 'None'", "B) 'NoneType'", "C) 'null'", "D) 'type'"],
                "answer": "B"
            },
            {
                "question": "What does the __index__ method return?",
                "options": ["A) Index value", "B) Integer for use in slicing", "C) Position", "D) Array index"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(NotImplemented == NotImplemented)?",
                "options": ["A) False", "B) True", "C) NotImplemented", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What does the __missing__ method do in dict subclasses?",
                "options": ["A) Finds missing keys", "B) Called when key is not found", "C) Returns default", "D) Raises KeyError"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(Ellipsis == ...)?",
                "options": ["A) False", "B) True", "C) Error", "D) None"],
                "answer": "B"
            },
            {
                "question": "What does the __reduce__ method do?",
                "options": ["A) Reduces size", "B) Returns pickle state", "C) Simplifies object", "D) Compresses data"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(type(Ellipsis).__name__)?",
                "options": ["A) 'Ellipsis'", "B) 'ellipsis'", "C) 'EllipsisType'", "D) '...'"],
                "answer": "B"
            },
            {
                "question": "What does the __reduce_ex__ method do?",
                "options": ["A) Extended reduce", "B) Pickle with protocol version", "C) Reduces exceptions", "D) Exports object"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(type(NotImplemented).__name__)?",
                "options": ["A) 'NotImplemented'", "B) 'NotImplementedType'", "C) 'type'", "D) 'object'"],
                "answer": "B"
            },
            {
                "question": "What does the __getnewargs__ method do?",
                "options": ["A) Gets new arguments", "B) Returns args for __new__ during unpickling", "C) Creates arguments", "D) Validates args"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(type(__builtins__).__name__)?",
                "options": ["A) 'builtins'", "B) 'module'", "C) 'dict'", "D) Depends on context"],
                "answer": "D"
            },
            {
                "question": "What does the __getstate__ method return?",
                "options": ["A) Object state", "B) State for pickling", "C) Current values", "D) Both A and B"],
                "answer": "D"
            },
            {
                "question": "What is the output of: print(sys.intern('a') is sys.intern('a'))?",
                "options": ["A) False", "B) True", "C) Depends", "D) Error"],
                "answer": "B"
            },
            {
                "question": "What does the __setstate__ method do?",
                "options": ["A) Sets state", "B) Restores state during unpickling", "C) Updates object", "D) Initializes state"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print([] is not [])?",
                "options": ["A) False", "B) True", "C) Error", "D) None"],
                "answer": "B"
            },
            {
                "question": "What does the __format__ method do?",
                "options": ["A) Formats output", "B) Returns formatted string for format()", "C) Validates format", "D) Creates format"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print((256 is 256, 257 is 257))?",
                "options": ["A) (True, True)", "B) (True, False)", "C) (False, False)", "D) Depends"],
                "answer": "D"
            },
            {
                "question": "What does the __sizeof__ method return?",
                "options": ["A) Object size", "B) Size in bytes", "C) Memory usage", "D) All of the above"],
                "answer": "D"
            },
            {
                "question": "What is the output of: print(type(lambda: None).__name__)?",
                "options": ["A) 'lambda'", "B) 'function'", "C) 'callable'", "D) '<lambda>'"],
                "answer": "B"
            },
            {
                "question": "What does the __dir__ method return?",
                "options": ["A) Directory path", "B) List of attributes for dir()", "C) File list", "D) Module contents"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(type((x for x in [])).__name__)?",
                "options": ["A) 'generator'", "B) 'iterator'", "C) 'genexpr'", "D) 'comprehension'"],
                "answer": "A"
            },
            {
                "question": "What does the __reversed__ method return?",
                "options": ["A) Reversed list", "B) Reverse iterator", "C) Reversed object", "D) New sequence"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(type(iter([])).__name__)?",
                "options": ["A) 'iterator'", "B) 'list_iterator'", "C) 'iter'", "D) 'iterable'"],
                "answer": "B"
            },
            {
                "question": "What does the __bool__ method return?",
                "options": ["A) Boolean value", "B) Truth value for bool()", "C) True or False", "D) All of the above"],
                "answer": "D"
            },
            {
                "question": "What is the output of: print(type(range(0)).__name__)?",
                "options": ["A) 'range'", "B) 'iterator'", "C) 'sequence'", "D) 'list'"],
                "answer": "A"
            },
            {
                "question": "What does the __bytes__ method return?",
                "options": ["A) Byte string", "B) Bytes representation", "C) Binary data", "D) All of the above"],
                "answer": "D"
            },
            {
                "question": "What is the output of: print(type(zip()).__name__)?",
                "options": ["A) 'zip'", "B) 'iterator'", "C) 'zip_iterator'", "D) 'tuple'"],
                "answer": "A"
            },
            {
                "question": "What does the __complex__ method return?",
                "options": ["A) Complex number", "B) Complex representation", "C) Real and imaginary parts", "D) Both A and B"],
                "answer": "D"
            },
            {
                "question": "What is the output of: print(type(map(int, [])).__name__)?",
                "options": ["A) 'map'", "B) 'iterator'", "C) 'map_iterator'", "D) 'list'"],
                "answer": "A"
            },
            {
                "question": "What does the __int__ method return?",
                "options": ["A) Integer value", "B) Integer representation", "C) Truncated value", "D) Both A and B"],
                "answer": "D"
            },
            {
                "question": "What is the output of: print(type(filter(None, [])).__name__)?",
                "options": ["A) 'filter'", "B) 'iterator'", "C) 'filter_iterator'", "D) 'list'"],
                "answer": "A"
            },
            {
                "question": "What does the __float__ method return?",
                "options": ["A) Float value", "B) Float representation", "C) Decimal value", "D) Both A and B"],
                "answer": "D"
            },
            {
                "question": "What is the output of: print(type(reversed([])).__name__)?",
                "options": ["A) 'reversed'", "B) 'list_reverseiterator'", "C) 'iterator'", "D) 'reverse'"],
                "answer": "B"
            },
            {
                "question": "What does the __round__ method return?",
                "options": ["A) Rounded value", "B) Integer or float", "C) Nearest value", "D) All of the above"],
                "answer": "D"
            }
        ]
    
    def run_exam(self):
        print("=" * 60)
        print("PCAP-31-03 PRACTICE EXAM - EXTREME LEVEL")
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
    exam = PCAPExamExtreme()
    exam.run_exam()
