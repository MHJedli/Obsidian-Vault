"""
PCAP-31-03 Mock Exam - EASY (50 Questions)
Topics: Modules, OOP, Exceptions, File I/O, Comprehensions, Lambdas, Closures
"""

import time

QUESTIONS = [
    # -- MODULES & PACKAGES --
    {
        "topic": "Modules & Packages",
        "q": "Which statement imports math and gives it the alias m?",
        "options": ["A) import math as m", "B) import m from math", "C) from math import m", "D) import math.m"],
        "answer": "A",
        "explanation": "The 'as' keyword creates a local alias: import math as m."
    },
    {
        "topic": "Modules & Packages",
        "q": "What is __name__ when a module is imported (not run directly)?",
        "options": ["A) '__main__'", "B) None", "C) The module's name", "D) The file path"],
        "answer": "C",
        "explanation": "When imported, __name__ is set to the module's name."
    },
    {
        "topic": "Modules & Packages",
        "q": "What is sys.path?",
        "options": ["A) A list of directories Python searches for modules", "B) A dict of imported modules", "C) The current working directory only", "D) The system PATH"],
        "answer": "A",
        "explanation": "sys.path is a list of directories used during module import."
    },
    {
        "topic": "Modules & Packages",
        "q": "What does dir(math) return?",
        "options": ["A) The source code of math", "B) A list of attribute names", "C) The file path to math", "D) The version of math"],
        "answer": "B",
        "explanation": "dir() returns a list of names in the object's namespace."
    },
    {
        "topic": "Modules & Packages",
        "q": "What can random.randint(1, 3) return?",
        "options": ["A) 1 or 2 only", "B) 1, 2, or 3", "C) 0, 1, or 2", "D) 2 only"],
        "answer": "B",
        "explanation": "randint(a, b) is inclusive of both endpoints."
    },
    {
        "topic": "Modules & Packages",
        "q": "What does 'from math import sqrt' do?",
        "options": ["A) Imports the math module", "B) Imports only the sqrt function", "C) Imports all math names", "D) Imports math as sqrt"],
        "answer": "B",
        "explanation": "It brings sqrt directly into the current namespace."
    },
    {
        "topic": "Modules & Packages",
        "q": "What is the purpose of an if __name__ == '__main__' block?",
        "options": ["A) It makes the file a package", "B) It prevents imports", "C) It runs code only when the file is executed directly", "D) It speeds up imports"],
        "answer": "C",
        "explanation": "It guards code so it runs only when the script is the entry point."
    },
    {
        "topic": "Modules & Packages",
        "q": "Which file marks a directory as a Python package?",
        "options": ["A) __init__.py", "B) package.py", "C) main.py", "D) setup.cfg"],
        "answer": "A",
        "explanation": "__init__.py marks a directory as a package."
    },
    {
        "topic": "Modules & Packages",
        "q": "What does 'import os.path' allow you to do?",
        "options": ["A) Import only os, not path", "B) Access os.path as a submodule", "C) Replace os.path", "D) Import path from the current folder"],
        "answer": "B",
        "explanation": "os.path is a submodule of os and becomes available as os.path."
    },
    {
        "topic": "Modules & Packages",
        "q": "What does help(math) show?",
        "options": ["A) The bytecode of math", "B) Documentation for math", "C) The import path only", "D) Nothing"],
        "answer": "B",
        "explanation": "help() shows documentation and available members."
    },

    # -- OOP --
    {
        "topic": "OOP",
        "q": "How do you define a class named Car?",
        "options": ["A) class Car:", "B) def Car():", "C) new class Car", "D) class Car()"],
        "answer": "A",
        "explanation": "Use the class keyword: class Car:."
    },
    {
        "topic": "OOP",
        "q": "What does 'self' refer to inside an instance method?",
        "options": ["A) The class", "B) The module", "C) The instance", "D) The superclass"],
        "answer": "C",
        "explanation": "self is the instance that called the method."
    },
    {
        "topic": "OOP",
        "q": "What is __init__ used for?",
        "options": ["A) Deleting an object", "B) Initializing new instances", "C) Printing objects", "D) Loading modules"],
        "answer": "B",
        "explanation": "__init__ runs on object creation to set up attributes."
    },
    {
        "topic": "OOP",
        "q": "How do you create an instance of class Dog?",
        "options": ["A) Dog.create()", "B) new Dog()", "C) Dog()", "D) Dog.instance()"],
        "answer": "C",
        "explanation": "Calling the class like a function creates an instance."
    },
    {
        "topic": "OOP",
        "q": "What does inheritance provide?",
        "options": ["A) A class can reuse and extend another class", "B) A module can import another module", "C) A function can be called twice", "D) A list can contain any type"],
        "answer": "A",
        "explanation": "Inheritance lets a subclass reuse attributes and methods from a base class."
    },
    {
        "topic": "OOP",
        "q": "What is method overriding?",
        "options": ["A) Changing a module name", "B) A subclass defining a method with the same name", "C) Using globals", "D) Deleting a method"],
        "answer": "B",
        "explanation": "A subclass can override a parent method by defining it again."
    },
    {
        "topic": "OOP",
        "q": "What is a class variable?",
        "options": ["A) A variable stored on each instance", "B) A variable shared by all instances", "C) A variable inside a method", "D) A variable in another module"],
        "answer": "B",
        "explanation": "Class variables are stored on the class and shared across instances."
    },
    {
        "topic": "OOP",
        "q": "What does isinstance(obj, MyClass) check?",
        "options": ["A) Exact type match only", "B) Whether obj is an instance of MyClass or a subclass", "C) Whether obj is a module", "D) Whether obj is callable"],
        "answer": "B",
        "explanation": "isinstance respects inheritance and returns True for subclasses."
    },
    {
        "topic": "OOP",
        "q": "Which method controls what print(obj) shows?",
        "options": ["A) __repr__", "B) __print__", "C) __str__", "D) __show__"],
        "answer": "C",
        "explanation": "print() calls str(obj), which uses __str__."
    },
    {
        "topic": "OOP",
        "q": "What does @staticmethod create?",
        "options": ["A) A method with self", "B) A method with cls", "C) A function attached to the class with no automatic first arg", "D) A property"],
        "answer": "C",
        "explanation": "@staticmethod attaches a plain function to the class."
    },

    # -- EXCEPTIONS --
    {
        "topic": "Exceptions",
        "q": "Which block always runs in a try/except statement?",
        "options": ["A) else", "B) finally", "C) except", "D) try"],
        "answer": "B",
        "explanation": "finally runs whether or not an exception occurred."
    },
    {
        "topic": "Exceptions",
        "q": "What exception is raised by int('abc')?",
        "options": ["A) TypeError", "B) ValueError", "C) IndexError", "D) KeyError"],
        "answer": "B",
        "explanation": "int() raises ValueError for invalid strings."
    },
    {
        "topic": "Exceptions",
        "q": "What exception is raised by [1,2,3][5]?",
        "options": ["A) IndexError", "B) KeyError", "C) ValueError", "D) AttributeError"],
        "answer": "A",
        "explanation": "IndexError is raised for out-of-range indexes."
    },
    {
        "topic": "Exceptions",
        "q": "What exception is raised by {'a': 1}['b']?",
        "options": ["A) IndexError", "B) KeyError", "C) TypeError", "D) NameError"],
        "answer": "B",
        "explanation": "Accessing a missing dict key raises KeyError."
    },
    {
        "topic": "Exceptions",
        "q": "Which clause runs only if no exception was raised?",
        "options": ["A) else", "B) except", "C) finally", "D) raise"],
        "answer": "A",
        "explanation": "The else block runs only when the try block succeeds."
    },
    {
        "topic": "Exceptions",
        "q": "How do you raise a ValueError with a message?",
        "options": ["A) throw ValueError('msg')", "B) raise ValueError('msg')", "C) error ValueError('msg')", "D) raise 'ValueError: msg'"],
        "answer": "B",
        "explanation": "Use the raise keyword with the exception class."
    },
    {
        "topic": "Exceptions",
        "q": "How do you catch multiple exception types in one except clause?",
        "options": ["A) except ValueError, TypeError", "B) except (ValueError, TypeError)", "C) except ValueError | TypeError", "D) except [ValueError, TypeError]"],
        "answer": "B",
        "explanation": "Use a tuple of exception types."
    },
    {
        "topic": "Exceptions",
        "q": "What exception does assert False raise?",
        "options": ["A) AssertionError", "B) ValueError", "C) RuntimeError", "D) SyntaxError"],
        "answer": "A",
        "explanation": "assert raises AssertionError when the condition is False."
    },
    {
        "topic": "Exceptions",
        "q": "What is the base class for most exceptions?",
        "options": ["A) BaseError", "B) Exception", "C) RuntimeError", "D) StandardError"],
        "answer": "B",
        "explanation": "Exception is the base class for most application errors."
    },
    {
        "topic": "Exceptions",
        "q": "What does 'except Exception as e' give you?",
        "options": ["A) The exception instance bound to e", "B) The line number", "C) The traceback as a string", "D) The exception type name"],
        "answer": "A",
        "explanation": "The caught exception instance is stored in e."
    },

    # -- FILE I/O --
    {
        "topic": "File I/O",
        "q": "Which function opens a file?",
        "options": ["A) file()", "B) read()", "C) open()", "D) load()"],
        "answer": "C",
        "explanation": "open() returns a file object for reading or writing."
    },
    {
        "topic": "File I/O",
        "q": "Which mode opens a file for reading?",
        "options": ["A) 'r'", "B) 'w'", "C) 'a'", "D) 'x'"],
        "answer": "A",
        "explanation": "'r' is read mode."
    },
    {
        "topic": "File I/O",
        "q": "Which mode appends to a file without erasing it?",
        "options": ["A) 'w'", "B) 'a'", "C) 'r'", "D) 'x'"],
        "answer": "B",
        "explanation": "'a' appends to the end of a file."
    },
    {
        "topic": "File I/O",
        "q": "Why use 'with open(...) as f'?",
        "options": ["A) It opens faster", "B) It auto-closes the file", "C) It reads binary by default", "D) It skips errors"],
        "answer": "B",
        "explanation": "The context manager closes the file automatically."
    },
    {
        "topic": "File I/O",
        "q": "What does f.read() return in text mode?",
        "options": ["A) A list of lines", "B) The entire file as a string", "C) An integer", "D) A bytes object"],
        "answer": "B",
        "explanation": "f.read() returns the full content as a string in text mode."
    },
    {
        "topic": "File I/O",
        "q": "What does f.readline() do?",
        "options": ["A) Reads all lines", "B) Reads one line", "C) Reads one byte", "D) Reads the last line"],
        "answer": "B",
        "explanation": "readline() reads one line including the trailing newline."
    },
    {
        "topic": "File I/O",
        "q": "What does f.readlines() return?",
        "options": ["A) A list of lines", "B) A single string", "C) A generator", "D) A dict"],
        "answer": "A",
        "explanation": "readlines() returns a list of strings, one per line."
    },
    {
        "topic": "File I/O",
        "q": "What does f.write('hi') return?",
        "options": ["A) None", "B) True", "C) The number of characters written", "D) The file object"],
        "answer": "C",
        "explanation": "write() returns the count of characters written."
    },
    {
        "topic": "File I/O",
        "q": "Which mode should you use to read a PNG file?",
        "options": ["A) 'r'", "B) 'rb'", "C) 'rt'", "D) 'rw'"],
        "answer": "B",
        "explanation": "Binary files should be opened with 'rb'."
    },
    {
        "topic": "File I/O",
        "q": "What does f.seek(0) do?",
        "options": ["A) Moves to the end of the file", "B) Moves to the start of the file", "C) Reads a byte", "D) Closes the file"],
        "answer": "B",
        "explanation": "seek(0) moves the cursor to the beginning."
    },

    # -- COMPREHENSIONS & LAMBDAS --
    {
        "topic": "Comprehensions & Lambdas",
        "q": "What does [x for x in range(3)] produce?",
        "options": ["A) [1, 2, 3]", "B) [0, 1, 2]", "C) [0, 1, 2, 3]", "D) [3, 2, 1]"],
        "answer": "B",
        "explanation": "range(3) produces 0, 1, 2."
    },
    {
        "topic": "Comprehensions & Lambdas",
        "q": "What does {x: x*x for x in range(3)} produce?",
        "options": ["A) {0, 1, 4}", "B) {0: 0, 1: 1, 2: 4}", "C) {1: 1, 2: 4, 3: 9}", "D) [0, 1, 4]"],
        "answer": "B",
        "explanation": "A dict comprehension uses key: value pairs."
    },
    {
        "topic": "Comprehensions & Lambdas",
        "q": "What is (x for x in range(3))?",
        "options": ["A) A list", "B) A tuple", "C) A generator expression", "D) A set"],
        "answer": "C",
        "explanation": "Parentheses create a generator expression."
    },
    {
        "topic": "Comprehensions & Lambdas",
        "q": "Which is the correct lambda syntax?",
        "options": ["A) lambda x: x + 1", "B) lambda(x) => x + 1", "C) def lambda x: x + 1", "D) function(x): x + 1"],
        "answer": "A",
        "explanation": "lambda args: expression is the correct syntax."
    },
    {
        "topic": "Comprehensions & Lambdas",
        "q": "What does map(func, items) return?",
        "options": ["A) A list immediately", "B) A lazy iterator", "C) A dict", "D) A tuple"],
        "answer": "B",
        "explanation": "map() returns an iterator in Python 3."
    },

    # -- CLOSURES --
    {
        "topic": "Closures",
        "q": "What is a closure?",
        "options": ["A) A class with no methods", "B) A function that closes files", "C) An inner function that captures outer variables", "D) A module that cannot be imported"],
        "answer": "C",
        "explanation": "Closures capture variables from an enclosing scope."
    },
    {
        "topic": "Closures",
        "q": "Which keyword lets an inner function assign to an outer variable?",
        "options": ["A) global", "B) nonlocal", "C) outer", "D) static"],
        "answer": "B",
        "explanation": "nonlocal allows assignment to a variable in an enclosing scope."
    },
    {
        "topic": "Closures",
        "q": "What is a common use of closures?",
        "options": ["A) Creating factory functions that remember settings", "B) Importing modules faster", "C) Replacing lists", "D) Modifying global variables"],
        "answer": "A",
        "explanation": "Closures can capture configuration and return specialized functions."
    },
    {
        "topic": "Closures",
        "q": "How do you fix the late-binding issue in lambdas in a loop?",
        "options": ["A) Use global", "B) Use a default argument like lambda i=i: i", "C) Use list()", "D) Use try/except"],
        "answer": "B",
        "explanation": "Default arguments capture the current value at definition time."
    },
    {
        "topic": "Closures",
        "q": "What does 'global x' inside a function do?",
        "options": ["A) Creates a new local x", "B) Refers to the module-level x", "C) Refers to the nearest enclosing x", "D) Deletes x"],
        "answer": "B",
        "explanation": "global refers to the module-level variable."
    },
]


def run_exam():
    print("=" * 60)
    print("  PCAP-31-03 MOCK EXAM - EASY LEVEL")
    print("  50 Questions | Pass mark: 70% (35/50)")
    print("=" * 60)
    print()

    score = 0
    wrong_list = []
    start = time.time()

    for i, q in enumerate(QUESTIONS, 1):
        print(f"[{i:02d}/50] [{q['topic']}]")
        print()
        for line in q["q"].split("\n"):
            print(f"  {line}")
        print()
        for opt in q["options"]:
            print(f"    {opt}")
        print()

        while True:
            ans = input("  Your answer (A/B/C/D): ").strip().upper()
            if ans in ("A", "B", "C", "D"):
                break
            print("  Please enter A, B, C or D.")

        if ans == q["answer"]:
            print("  Correct!\n")
            score += 1
        else:
            print(f"  Wrong. Correct answer: {q['answer']}")
            print(f"  Explanation: {q['explanation']}\n")
            wrong_list.append((i, q))

        print("-" * 60)

    elapsed = time.time() - start
    minutes, seconds = divmod(int(elapsed), 60)

    print()
    print("=" * 60)
    print("  RESULTS")
    print("=" * 60)
    print(f"  Score      : {score} / 50  ({score * 2}%)")
    print(f"  Time taken : {minutes}m {seconds}s")
    print(f"  Pass mark  : 35 / 50  (70%)")
    passed = score >= 35
    print(f"  Result     : {'PASS' if passed else 'FAIL'}")
    print()

    if wrong_list:
        print(f"  Questions you missed ({len(wrong_list)}):")
        for num, q in wrong_list:
            first_line = q["q"].split("\n")[0][:55]
            print(f"    Q{num:02d} [{q['topic']}]: {first_line}...")
            print(f"         Correct: {q['answer']} - {q['explanation']}")
            print()

    print("=" * 60)


if __name__ == "__main__":
    run_exam()
