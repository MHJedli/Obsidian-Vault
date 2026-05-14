"""
PCAP-31-03 Mock Exam — EASY (50 Questions)
Topics: Modules, OOP, Exceptions, File I/O, Comprehensions, Lambdas, Closures
"""

import time

QUESTIONS = [
    # ── MODULES & PACKAGES ──────────────────────────────────────────────────
    {
        "topic": "Modules & Packages",
        "q": "What keyword is used to import a module in Python?",
        "options": ["A) include", "B) import", "C) require", "D) use"],
        "answer": "B",
        "explanation": "'import' is the keyword used to load a module. e.g. 'import math'."
    },
    {
        "topic": "Modules & Packages",
        "q": "Which syntax imports only the 'sqrt' function from the math module?",
        "options": ["A) import math.sqrt", "B) import sqrt from math", "C) from math import sqrt", "D) include math(sqrt)"],
        "answer": "C",
        "explanation": "'from module import name' imports a specific name into the current namespace."
    },
    {
        "topic": "Modules & Packages",
        "q": "What does 'import math as m' allow you to do?",
        "options": ["A) Rename math permanently", "B) Use 'm' as an alias for math in this file", "C) Import only part of math", "D) Create a copy of math"],
        "answer": "B",
        "explanation": "The 'as' keyword creates a local alias. You then call m.sqrt() instead of math.sqrt()."
    },
    {
        "topic": "Modules & Packages",
        "q": "What file must a directory contain to be treated as a Python package?",
        "options": ["A) main.py", "B) package.py", "C) __init__.py", "D) setup.py"],
        "answer": "C",
        "explanation": "'__init__.py' marks a directory as a package and is executed on first import."
    },
    {
        "topic": "Modules & Packages",
        "q": "What value does __name__ hold when a script is run directly?",
        "options": ["A) The filename", "B) '__main__'", "C) None", "D) '__script__'"],
        "answer": "B",
        "explanation": "Python sets __name__ = '__main__' for the entry-point file."
    },
    {
        "topic": "Modules & Packages",
        "q": "What does sys.path contain?",
        "options": ["A) The current file path", "B) A list of directories Python searches for modules", "C) A dict of imported modules", "D) The Python version"],
        "answer": "B",
        "explanation": "sys.path is a list of directory strings that Python searches when resolving imports."
    },
    {
        "topic": "Modules & Packages",
        "q": "Which module provides the 'pi' constant?",
        "options": ["A) os", "B) sys", "C) random", "D) math"],
        "answer": "D",
        "explanation": "The math module provides math.pi = 3.141592653589793."
    },
    {
        "topic": "Modules & Packages",
        "q": "What does dir(math) return?",
        "options": ["A) The file path of math", "B) A list of all attribute names in the math module", "C) The source code of math", "D) The version of math"],
        "answer": "B",
        "explanation": "dir(obj) returns a sorted list of names in the object's namespace."
    },
    {
        "topic": "Modules & Packages",
        "q": "What folder stores compiled bytecode (.pyc files)?",
        "options": ["A) .cache/", "B) __bytecode__/", "C) __pycache__/", "D) .pyc/"],
        "answer": "C",
        "explanation": "Python caches compiled bytecode in __pycache__/ to speed up future imports."
    },
    {
        "topic": "Modules & Packages",
        "q": "Which random module function returns a float between 0.0 and 1.0?",
        "options": ["A) random.randint()", "B) random.random()", "C) random.float()", "D) random.uniform()"],
        "answer": "B",
        "explanation": "random.random() returns a float in [0.0, 1.0). random.uniform(a,b) lets you choose the range."
    },

    # ── OOP ─────────────────────────────────────────────────────────────────
    {
        "topic": "OOP",
        "q": "What is a class in Python?",
        "options": ["A) A function that returns a value", "B) A blueprint for creating objects", "C) A module alias", "D) A built-in data type"],
        "answer": "B",
        "explanation": "A class defines the structure and behaviour shared by all its instances (objects)."
    },
    {
        "topic": "OOP",
        "q": "What is the first parameter of every instance method by convention?",
        "options": ["A) cls", "B) this", "C) self", "D) obj"],
        "answer": "C",
        "explanation": "'self' refers to the calling instance. Python passes it automatically."
    },
    {
        "topic": "OOP",
        "q": "What is __init__ called in Python?",
        "options": ["A) Destructor", "B) Decorator", "C) Initialiser / Constructor", "D) Metaclass"],
        "answer": "C",
        "explanation": "__init__ is called automatically when an object is created to initialise its attributes."
    },
    {
        "topic": "OOP",
        "q": "How do you create an instance of class Dog?",
        "options": ["A) Dog.new()", "B) new Dog()", "C) Dog.create()", "D) Dog()"],
        "answer": "D",
        "explanation": "Calling the class like a function — Dog() — creates and returns a new instance."
    },
    {
        "topic": "OOP",
        "q": "What does inheritance allow?",
        "options": ["A) A class to share methods with functions", "B) A child class to reuse attributes and methods of a parent class", "C) Two modules to share variables", "D) A function to call itself"],
        "answer": "B",
        "explanation": "Inheritance lets a subclass reuse and extend the behaviour of its superclass."
    },
    {
        "topic": "OOP",
        "q": "Which method controls what print(obj) displays?",
        "options": ["A) __repr__", "B) __print__", "C) __display__", "D) __str__"],
        "answer": "D",
        "explanation": "__str__ is called by str() and print(). __repr__ is used in the interactive shell."
    },
    {
        "topic": "OOP",
        "q": "What does isinstance(obj, MyClass) return?",
        "options": ["A) The type name as a string", "B) True if obj is an instance of MyClass or a subclass", "C) True only if obj's type is exactly MyClass", "D) The class of obj"],
        "answer": "B",
        "explanation": "isinstance() respects inheritance — subclass instances also return True."
    },
    {
        "topic": "OOP",
        "q": "What does a single leading underscore _name signal?",
        "options": ["A) The attribute is deleted after use", "B) Python enforces private access", "C) The attribute is internal by convention", "D) The attribute is a class variable"],
        "answer": "C",
        "explanation": "_name is a convention meaning 'internal/protected'. Python does not enforce it."
    },
    {
        "topic": "OOP",
        "q": "What does super() return?",
        "options": ["A) The root object class", "B) A proxy that delegates method calls to the next class in the MRO", "C) A copy of the parent class", "D) The parent class name as a string"],
        "answer": "B",
        "explanation": "super() follows the MRO to find the next class's method — not necessarily the direct parent."
    },
    {
        "topic": "OOP",
        "q": "What does obj.__dict__ contain?",
        "options": ["A) All attributes including inherited ones", "B) Only class-level attributes", "C) The object's own instance attributes", "D) The methods of the class"],
        "answer": "C",
        "explanation": "__dict__ stores only the attributes that belong directly to that instance, not class attrs."
    },

    # ── EXCEPTIONS ──────────────────────────────────────────────────────────
    {
        "topic": "Exceptions",
        "q": "Which block always runs regardless of whether an exception occurred?",
        "options": ["A) else", "B) except", "C) finally", "D) try"],
        "answer": "C",
        "explanation": "The finally block always executes — whether an exception was raised or not."
    },
    {
        "topic": "Exceptions",
        "q": "What exception does 10 / 0 raise?",
        "options": ["A) ValueError", "B) ArithmeticError", "C) MathError", "D) ZeroDivisionError"],
        "answer": "D",
        "explanation": "Dividing by zero raises ZeroDivisionError, which is a subclass of ArithmeticError."
    },
    {
        "topic": "Exceptions",
        "q": "What exception is raised when you access a list index that doesn't exist?",
        "options": ["A) KeyError", "B) ValueError", "C) IndexError", "D) AttributeError"],
        "answer": "C",
        "explanation": "IndexError is raised when a sequence index is out of range."
    },
    {
        "topic": "Exceptions",
        "q": "What exception does int('hello') raise?",
        "options": ["A) TypeError", "B) ValueError", "C) SyntaxError", "D) ParseError"],
        "answer": "B",
        "explanation": "int() raises ValueError when the string is not a valid integer literal."
    },
    {
        "topic": "Exceptions",
        "q": "Which clause runs only when no exception was raised in the try block?",
        "options": ["A) finally", "B) catch", "C) always", "D) else"],
        "answer": "D",
        "explanation": "The else clause runs only on successful (no-exception) completion of the try block."
    },
    {
        "topic": "Exceptions",
        "q": "How do you raise a ValueError with a message?",
        "options": ["A) throw ValueError('msg')", "B) raise ValueError('msg')", "C) error ValueError('msg')", "D) raise 'ValueError: msg'"],
        "answer": "B",
        "explanation": "The 'raise' keyword triggers an exception. Pass the message as a constructor argument."
    },
    {
        "topic": "Exceptions",
        "q": "What is the base class of all regular (non-system) exceptions?",
        "options": ["A) BaseError", "B) StandardError", "C) Exception", "D) RuntimeError"],
        "answer": "C",
        "explanation": "Exception is the base class for all non-system-exiting exceptions. BaseException is the root."
    },
    {
        "topic": "Exceptions",
        "q": "What exception is raised when a dictionary key is not found?",
        "options": ["A) IndexError", "B) ValueError", "C) AttributeError", "D) KeyError"],
        "answer": "D",
        "explanation": "Accessing a missing key with d['key'] raises KeyError."
    },
    {
        "topic": "Exceptions",
        "q": "How do you catch multiple exception types in one except clause?",
        "options": ["A) except ValueError, TypeError:", "B) except (ValueError, TypeError):", "C) except ValueError | TypeError:", "D) except [ValueError, TypeError]:"],
        "answer": "B",
        "explanation": "Use a tuple: except (ValueError, TypeError). Both types are caught by the same handler."
    },
    {
        "topic": "Exceptions",
        "q": "What does 'except Exception as e' give you?",
        "options": ["A) The exception type as a string", "B) The line number of the error", "C) The exception instance bound to the name e", "D) A copy of the traceback"],
        "answer": "C",
        "explanation": "The 'as e' clause binds the caught exception object to e so you can inspect it."
    },

    # ── FILE I/O ─────────────────────────────────────────────────────────────
    {
        "topic": "File I/O",
        "q": "Which function opens a file in Python?",
        "options": ["A) file()", "B) read()", "C) load()", "D) open()"],
        "answer": "D",
        "explanation": "open(path, mode) returns a file object with read/write methods."
    },
    {
        "topic": "File I/O",
        "q": "What mode opens a file for reading?",
        "options": ["A) 'w'", "B) 'a'", "C) 'r'", "D) 'x'"],
        "answer": "C",
        "explanation": "'r' is read mode. It raises FileNotFoundError if the file doesn't exist."
    },
    {
        "topic": "File I/O",
        "q": "What mode opens a file for writing and erases existing content?",
        "options": ["A) 'a'", "B) 'r'", "C) 'x'", "D) 'w'"],
        "answer": "D",
        "explanation": "'w' opens for writing and truncates (erases) the file if it already exists."
    },
    {
        "topic": "File I/O",
        "q": "What does f.read() return?",
        "options": ["A) A list of lines", "B) The first line only", "C) The entire file content as a string", "D) A bytes object always"],
        "answer": "C",
        "explanation": "f.read() reads the entire file and returns it as a single string (in text mode)."
    },
    {
        "topic": "File I/O",
        "q": "What is the advantage of 'with open(...) as f:'?",
        "options": ["A) It opens files faster", "B) It automatically closes the file when the block exits", "C) It reads files in binary mode by default", "D) It caches the file in memory"],
        "answer": "B",
        "explanation": "The with statement calls __exit__ which calls close() — even if an exception occurs."
    },
    {
        "topic": "File I/O",
        "q": "What does f.readlines() return?",
        "options": ["A) A single string", "B) A generator", "C) An integer (line count)", "D) A list of strings, one per line"],
        "answer": "D",
        "explanation": "readlines() reads all lines into a list. Each string includes the trailing newline character."
    },
    {
        "topic": "File I/O",
        "q": "Which mode appends data to the end of a file without erasing it?",
        "options": ["A) 'w'", "B) 'r+'", "C) 'x'", "D) 'a'"],
        "answer": "D",
        "explanation": "'a' (append) mode positions the cursor at the end of the file. Existing content is preserved."
    },
    {
        "topic": "File I/O",
        "q": "What does f.write('hello') return?",
        "options": ["A) None", "B) True", "C) The number of characters written", "D) The file object"],
        "answer": "C",
        "explanation": "write() returns the number of characters (or bytes) successfully written."
    },
    {
        "topic": "File I/O",
        "q": "What mode must you use to read a PNG image file correctly?",
        "options": ["A) 'r'", "B) 'rb'", "C) 'rt'", "D) 'rw'"],
        "answer": "B",
        "explanation": "Binary mode 'rb' reads raw bytes without any encoding or line-ending translation."
    },
    {
        "topic": "File I/O",
        "q": "What does f.readline() do?",
        "options": ["A) Reads the entire file", "B) Reads one line including the newline character", "C) Reads all lines into a list", "D) Reads a fixed number of bytes"],
        "answer": "B",
        "explanation": "readline() reads up to and including the next \\n. It returns '' at end of file."
    },

    # ── COMPREHENSIONS & LAMBDAS ─────────────────────────────────────────────
    {
        "topic": "Comprehensions & Lambdas",
        "q": "What does [x*2 for x in range(3)] produce?",
        "options": ["A) [0, 1, 2]", "B) [2, 4, 6]", "C) [0, 2, 4]", "D) [1, 2, 3]"],
        "answer": "C",
        "explanation": "range(3) gives 0,1,2. Multiplied by 2: 0,2,4."
    },
    {
        "topic": "Comprehensions & Lambdas",
        "q": "What does the 'if' clause do in a list comprehension?",
        "options": ["A) It transforms each element", "B) It filters — only items where the condition is True are included", "C) It sorts the result", "D) It stops iteration early"],
        "answer": "B",
        "explanation": "[x for x in data if cond] keeps only elements where cond is True."
    },
    {
        "topic": "Comprehensions & Lambdas",
        "q": "What is the syntax of a lambda function?",
        "options": ["A) def lambda args: expr", "B) lambda: args, expr", "C) lambda args: expression", "D) function(args): expression"],
        "answer": "C",
        "explanation": "lambda args: expression — the expression is implicitly returned. No 'return' keyword."
    },
    {
        "topic": "Comprehensions & Lambdas",
        "q": "What does map(func, iterable) return?",
        "options": ["A) A list immediately", "B) A lazy iterator applying func to each element", "C) A tuple", "D) A dict"],
        "answer": "B",
        "explanation": "map() returns a lazy iterator. Wrap it in list() to materialise all results at once."
    },
    {
        "topic": "Comprehensions & Lambdas",
        "q": "What does filter(func, iterable) keep?",
        "options": ["A) Elements where func returns False", "B) Elements where func returns None", "C) All elements unchanged", "D) Elements where func returns True"],
        "answer": "D",
        "explanation": "filter() keeps only elements for which the function returns a truthy value."
    },
    {
        "topic": "Comprehensions & Lambdas",
        "q": "What is a dictionary comprehension?",
        "options": ["A) {k for k in data}", "B) [k: v for k, v in data]", "C) {k: v for k, v in data}", "D) dict[k, v for k, v in data]"],
        "answer": "C",
        "explanation": "Dictionary comprehensions use {key: value for ...} syntax with a colon between key and value."
    },

    # ── CLOSURES ────────────────────────────────────────────────────────────
    {
        "topic": "Closures",
        "q": "What is a closure?",
        "options": [
            "A) A function that closes a file",
            "B) An inner function that captures variables from its enclosing scope",
            "C) A class with no methods",
            "D) A module that cannot be imported"
        ],
        "answer": "B",
        "explanation": "A closure is an inner function plus the variables it captured from the enclosing scope."
    },
    {
        "topic": "Closures",
        "q": "What keyword allows an inner function to modify an enclosing variable?",
        "options": ["A) global", "B) outer", "C) enclosed", "D) nonlocal"],
        "answer": "D",
        "explanation": "'nonlocal' declares that the name refers to the nearest enclosing function scope."
    },
    {
        "topic": "Closures",
        "q": "What does this return: (lambda x: x+1)(5)?",
        "options": ["A) 5", "B) lambda", "C) 6", "D) TypeError"],
        "answer": "C",
        "explanation": "The lambda is immediately called with argument 5, returning 5+1 = 6."
    },
    {
        "topic": "Closures",
        "q": "What is the main practical use of a closure?",
        "options": [
            "A) To replace all classes",
            "B) To import modules dynamically",
            "C) To create factory functions that remember configuration",
            "D) To speed up loops"
        ],
        "answer": "C",
        "explanation": "Closures are ideal as factory functions — each call creates a function with its own captured state."
    },
    {
        "topic": "Closures",
        "q": "If a closure captures a variable 'x = 10', can the outer function's x be read inside the inner function without nonlocal?",
        "options": [
            "A) No — you always need nonlocal to read",
            "B) Yes — reading is allowed; only assignment needs nonlocal",
            "C) Only if x is a string",
            "D) Only after calling super()"
        ],
        "answer": "B",
        "explanation": "Nonlocal is only required for assignment. Reading an enclosing variable works without it."
    },
]


def run_exam():
    print("=" * 60)
    print("  PCAP-31-03 MOCK EXAM — EASY LEVEL")
    print("  50 Questions | Pass mark: 70% (35/50)")
    print("=" * 60)
    print()

    score = 0
    wrong_list = []
    start = time.time()

    for i, q in enumerate(QUESTIONS, 1):
        print(f"[{i:02d}/50] [{q['topic']}]")
        print(f"  {q['q']}")
        for opt in q["options"]:
            print(f"    {opt}")
        print()

        while True:
            ans = input("  Your answer (A/B/C/D): ").strip().upper()
            if ans in ("A", "B", "C", "D"):
                break
            print("  Please enter A, B, C or D.")

        if ans == q["answer"]:
            print("  ✓ Correct!\n")
            score += 1
        else:
            print(f"  ✗ Wrong. Correct answer: {q['answer']}")
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
    print(f"  Result     : {'PASS ✓' if passed else 'FAIL ✗'}")
    print()

    if wrong_list:
        print(f"  Questions you missed ({len(wrong_list)}):")
        for num, q in wrong_list:
            print(f"    Q{num:02d} [{q['topic']}]: {q['q'][:55]}...")
            print(f"         Correct: {q['answer']} — {q['explanation']}")
            print()

    print("=" * 60)


if __name__ == "__main__":
    run_exam()