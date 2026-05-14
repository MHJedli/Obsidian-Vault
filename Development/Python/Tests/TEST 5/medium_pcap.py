#!/usr/bin/env python3
"""
PCAP-31-03 Mock Exam — MEDIUM (50 Questions)
Topics: Functions, scope, comprehensions, exceptions, OOP basics, modules, file I/O basics
"""

import random
import time

QUESTIONS = [
    {
        "q": "What is the output of:\n  def f(x, y=10):\n      return x + y\n  print(f(5))",
        "options": ["A) 5", "B) 10", "C) 15", "D) Error"],
        "answer": "C",
        "explanation": "y has a default value of 10. f(5) uses x=5, y=10, returns 15."
    },
    {
        "q": "What does *args represent in a function definition?",
        "options": [
            "A) A dictionary of keyword arguments",
            "B) A single required argument",
            "C) A tuple of variable positional arguments",
            "D) A pointer to args"
        ],
        "answer": "C",
        "explanation": "*args collects extra positional arguments into a tuple."
    },
    {
        "q": "What is the output of:\n  x = [i**2 for i in range(4)]\n  print(x)",
        "options": ["A) [0, 1, 4, 9]", "B) [1, 4, 9, 16]", "C) [0, 1, 2, 3]", "D) [1, 2, 3, 4]"],
        "answer": "A",
        "explanation": "range(4) gives 0,1,2,3. Squaring each: 0,1,4,9."
    },
    {
        "q": "What does **kwargs capture in a function?",
        "options": [
            "A) All positional arguments as a list",
            "B) All keyword arguments as a dictionary",
            "C) A single keyword argument",
            "D) Double-starred arguments as a set"
        ],
        "answer": "B",
        "explanation": "**kwargs collects extra keyword arguments into a dictionary."
    },
    {
        "q": "What is a lambda function?",
        "options": [
            "A) A named function defined with 'def'",
            "B) An anonymous, single-expression function",
            "C) A function that takes no arguments",
            "D) A recursive function"
        ],
        "answer": "B",
        "explanation": "Lambda creates an anonymous function: lambda x: x*2."
    },
    {
        "q": "What is the output of:\n  try:\n      x = 1/0\n  except ZeroDivisionError:\n      print('caught')\n  else:\n      print('no error')",
        "options": ["A) caught", "B) no error", "C) caught\\nno error", "D) Error"],
        "answer": "A",
        "explanation": "ZeroDivisionError is raised. The except block runs. The else block is skipped."
    },
    {
        "q": "Which LEGB rule describes Python's scope lookup order?",
        "options": [
            "A) Local → Enclosing → Global → Built-in",
            "B) Global → Local → Enclosing → Built-in",
            "C) Built-in → Global → Enclosing → Local",
            "D) Local → Global → Built-in → Enclosing"
        ],
        "answer": "A",
        "explanation": "LEGB: Local, Enclosing (closures), Global, Built-in — this is the lookup order."
    },
    {
        "q": "What is the result of:\n  def outer():\n      x = 10\n      def inner():\n          return x\n      return inner()\n  print(outer())",
        "options": ["A) Error", "B) None", "C) 10", "D) 0"],
        "answer": "C",
        "explanation": "inner() accesses x from the enclosing scope (closure), which is 10."
    },
    {
        "q": "What does list.extend([4,5]) do?",
        "options": [
            "A) Adds [4,5] as a single element",
            "B) Appends 4 and 5 as individual elements",
            "C) Inserts [4,5] at index 0",
            "D) Returns a new list"
        ],
        "answer": "B",
        "explanation": "extend() iterates over the argument and appends each element individually."
    },
    {
        "q": "What is the output of:\n  d = {'a':1, 'b':2}\n  print(d.get('c', 99))",
        "options": ["A) None", "B) Error", "C) 99", "D) 'c'"],
        "answer": "C",
        "explanation": "dict.get(key, default) returns default (99) if key is not found."
    },
    {
        "q": "Which statement correctly raises a custom exception?",
        "options": [
            "A) throw ValueError('msg')",
            "B) raise ValueError('msg')",
            "C) except ValueError('msg')",
            "D) error ValueError('msg')"
        ],
        "answer": "B",
        "explanation": "Python uses 'raise' to raise exceptions."
    },
    {
        "q": "What does the 'finally' block guarantee?",
        "options": [
            "A) It runs only if no exception occurs",
            "B) It runs only if an exception occurs",
            "C) It always runs, exception or not",
            "D) It catches all exceptions"
        ],
        "answer": "C",
        "explanation": "'finally' always executes regardless of whether an exception was raised."
    },
    {
        "q": "What is the output of:\n  s = {1, 2, 3, 2, 1}\n  print(len(s))",
        "options": ["A) 5", "B) 3", "C) 2", "D) 1"],
        "answer": "B",
        "explanation": "Sets store unique elements. {1,2,3,2,1} stores only {1,2,3}, length = 3."
    },
    {
        "q": "What does 'import math; print(math.floor(4.7))' output?",
        "options": ["A) 5", "B) 4.0", "C) 4", "D) 5.0"],
        "answer": "C",
        "explanation": "math.floor() returns the largest integer ≤ the value: floor(4.7) = 4."
    },
    {
        "q": "What is a generator in Python?",
        "options": [
            "A) A function that returns all values at once",
            "B) A function using 'yield' that produces values lazily",
            "C) A list comprehension",
            "D) A class method that generates instances"
        ],
        "answer": "B",
        "explanation": "Generators use 'yield' to produce values one at a time, using lazy evaluation."
    },
    {
        "q": "What is the output of:\n  print([x for x in range(10) if x % 2 == 0])",
        "options": ["A) [1,3,5,7,9]", "B) [0,2,4,6,8,10]", "C) [0,2,4,6,8]", "D) [2,4,6,8]"],
        "answer": "C",
        "explanation": "Even numbers from range(10) (0-9): 0,2,4,6,8."
    },
    {
        "q": "Which method is used to open a file in Python?",
        "options": ["A) File()", "B) read()", "C) open()", "D) fopen()"],
        "answer": "C",
        "explanation": "open(filename, mode) is the built-in for file operations."
    },
    {
        "q": "What mode opens a file for writing (creates if not exists, truncates if exists)?",
        "options": ["A) 'r'", "B) 'a'", "C) 'w'", "D) 'x'"],
        "answer": "C",
        "explanation": "'w' opens for writing. 'r' = read, 'a' = append, 'x' = exclusive create."
    },
    {
        "q": "What is the recommended way to open a file to ensure it's closed automatically?",
        "options": [
            "A) f = open(); ... ; f.close()",
            "B) with open(...) as f:",
            "C) try: open(...) finally: close()",
            "D) file.autoclose()"
        ],
        "answer": "B",
        "explanation": "The 'with' statement (context manager) ensures the file is closed automatically."
    },
    {
        "q": "What does 'enumerate(['a','b','c'])' produce?",
        "options": [
            "A) [(0,'a'), (1,'b'), (2,'c')]",
            "B) ['a','b','c']",
            "C) [0, 1, 2]",
            "D) {'a':0, 'b':1, 'c':2}"
        ],
        "answer": "A",
        "explanation": "enumerate() yields (index, value) pairs as tuples."
    },
    {
        "q": "What is the output of:\n  a, b, *c = [1, 2, 3, 4, 5]\n  print(c)",
        "options": ["A) [3, 4, 5]", "B) [1, 2]", "C) [3]", "D) (3, 4, 5)"],
        "answer": "A",
        "explanation": "*c captures remaining elements after a=1, b=2 → c = [3,4,5]."
    },
    {
        "q": "What does 'zip([1,2,3], ['a','b','c'])' produce?",
        "options": [
            "A) [[1,'a'], [2,'b'], [3,'c']]",
            "B) An iterator of (1,'a'), (2,'b'), (3,'c')",
            "C) [1,2,3,'a','b','c']",
            "D) {'1':'a', '2':'b', '3':'c'}"
        ],
        "answer": "B",
        "explanation": "zip() produces an iterator of tuples pairing elements from each iterable."
    },
    {
        "q": "What is the output of:\n  x = 5\n  def f():\n      global x\n      x = 10\n  f()\n  print(x)",
        "options": ["A) 5", "B) 10", "C) None", "D) Error"],
        "answer": "B",
        "explanation": "'global x' inside f() allows modifying the global x. After f(), x becomes 10."
    },
    {
        "q": "Which is a valid dict comprehension?",
        "options": [
            "A) {x: x**2 for x in range(5)}",
            "B) [x: x**2 for x in range(5)]",
            "C) dict[x, x**2 for x in range(5)]",
            "D) {x, x**2 for x in range(5)}"
        ],
        "answer": "A",
        "explanation": "Dict comprehensions use {key: value for ... in ...} syntax."
    },
    {
        "q": "What does 'map(str, [1, 2, 3])' return?",
        "options": [
            "A) ['1', '2', '3']",
            "B) A map object (iterator) yielding '1','2','3'",
            "C) '123'",
            "D) {1:'1', 2:'2', 3:'3'}"
        ],
        "answer": "B",
        "explanation": "map() returns a lazy iterator. Wrap in list() to get ['1','2','3']."
    },
    {
        "q": "What does 'filter(lambda x: x>2, [1,2,3,4])' produce when converted to a list?",
        "options": ["A) [1, 2]", "B) [3, 4]", "C) [2, 3, 4]", "D) [1, 2, 3]"],
        "answer": "B",
        "explanation": "filter keeps elements where the function returns True: x>2 gives [3, 4]."
    },
    {
        "q": "What is the output of:\n  class Dog:\n      def __init__(self, name):\n          self.name = name\n  d = Dog('Rex')\n  print(d.name)",
        "options": ["A) Dog", "B) Rex", "C) name", "D) Error"],
        "answer": "B",
        "explanation": "__init__ sets self.name = name. d.name accesses instance attribute 'Rex'."
    },
    {
        "q": "What is 'self' in a Python class method?",
        "options": [
            "A) A global variable",
            "B) A reference to the current instance",
            "C) A keyword for static methods",
            "D) A reference to the class itself"
        ],
        "answer": "B",
        "explanation": "'self' refers to the instance calling the method — it's a convention, not a keyword."
    },
    {
        "q": "Which exception is raised when you try to access a non-existent dict key directly?",
        "options": ["A) IndexError", "B) ValueError", "C) KeyError", "D) AttributeError"],
        "answer": "C",
        "explanation": "Accessing d['missing'] raises KeyError. Use d.get('missing') to avoid it."
    },
    {
        "q": "What does 'str.split(',')' do?",
        "options": [
            "A) Joins strings with a comma",
            "B) Splits string at each comma into a list",
            "C) Removes commas from string",
            "D) Counts commas in the string"
        ],
        "answer": "B",
        "explanation": "split(sep) splits the string at each occurrence of sep, returning a list."
    },
    {
        "q": "What is the output of:\n  print(','.join(['a','b','c']))",
        "options": ["A) ['a','b','c']", "B) 'a,b,c'", "C) a b c", "D) a,b,c"],
        "answer": "D",
        "explanation": "str.join(iterable) joins elements with the string as separator: 'a,b,c'."
    },
    {
        "q": "What exception is raised by: int('abc')?",
        "options": ["A) TypeError", "B) SyntaxError", "C) ValueError", "D) ConversionError"],
        "answer": "C",
        "explanation": "int('abc') raises ValueError because 'abc' cannot be converted to integer."
    },
    {
        "q": "What is the difference between '==' and 'is'?",
        "options": [
            "A) No difference",
            "B) '==' checks value equality; 'is' checks identity (same object)",
            "C) 'is' checks value; '==' checks type",
            "D) '==' is for strings only"
        ],
        "answer": "B",
        "explanation": "'==' tests value equality. 'is' tests if two variables point to the same object."
    },
    {
        "q": "What is the output of:\n  a = [1,2,3]\n  b = a\n  b.append(4)\n  print(a)",
        "options": ["A) [1,2,3]", "B) [1,2,3,4]", "C) [4]", "D) Error"],
        "answer": "B",
        "explanation": "b = a makes b reference the same list. Mutating b also mutates a."
    },
    {
        "q": "How do you copy a list to avoid aliasing?",
        "options": [
            "A) b = a",
            "B) b = a.copy() or b = a[:]",
            "C) b = copy(a)",
            "D) b = list.clone(a)"
        ],
        "answer": "B",
        "explanation": "a.copy() or a[:] creates a shallow copy, a new list object."
    },
    {
        "q": "What does 'sorted(d.items())' return for dict d = {'b':2,'a':1}?",
        "options": [
            "A) [('a',1), ('b',2)]",
            "B) [('b',2), ('a',1)]",
            "C) {'a':1,'b':2}",
            "D) [1, 2]"
        ],
        "answer": "A",
        "explanation": "items() returns key-value pairs. sorted() sorts them by key alphabetically."
    },
    {
        "q": "What is a decorator in Python?",
        "options": [
            "A) A class that extends another class",
            "B) A function that wraps another function to modify its behavior",
            "C) A string formatting tool",
            "D) A module for styling output"
        ],
        "answer": "B",
        "explanation": "Decorators are higher-order functions using @syntax to wrap/modify other functions."
    },
    {
        "q": "What happens when 'assert False, \"fail\"' is executed?",
        "options": ["A) Nothing", "B) Prints 'fail'", "C) Raises AssertionError: fail", "D) Returns False"],
        "answer": "C",
        "explanation": "assert raises AssertionError (with optional message) when condition is False."
    },
    {
        "q": "What does 'os.path.join('dir', 'file.txt')' do?",
        "options": [
            "A) Opens the file",
            "B) Combines path components in an OS-appropriate way",
            "C) Creates the directory",
            "D) Returns the file size"
        ],
        "answer": "B",
        "explanation": "os.path.join() safely combines path parts using the OS separator."
    },
    {
        "q": "What is a set operation for elements in A but NOT in B?",
        "options": ["A) A & B", "B) A | B", "C) A - B", "D) A ^ B"],
        "answer": "C",
        "explanation": "A - B (or A.difference(B)) returns elements in A not in B."
    },
    {
        "q": "What is the output of:\n  g = (x**2 for x in range(3))\n  print(next(g))",
        "options": ["A) 4", "B) 1", "C) 0", "D) [0,1,4]"],
        "answer": "C",
        "explanation": "Generator starts at x=0. next(g) yields 0**2 = 0."
    },
    {
        "q": "What does 'sys.argv' contain?",
        "options": [
            "A) All Python version info",
            "B) Command-line arguments as a list (first element is script name)",
            "C) System environment variables",
            "D) A list of imported modules"
        ],
        "answer": "B",
        "explanation": "sys.argv is a list where [0] is the script name and [1:] are command-line arguments."
    },
    {
        "q": "What does 'str.format()' do?",
        "options": [
            "A) Converts string to uppercase",
            "B) Inserts values into a string template using {}",
            "C) Strips whitespace",
            "D) Splits a string"
        ],
        "answer": "B",
        "explanation": "str.format() substitutes values into {} placeholders in the string."
    },
    {
        "q": "What is a f-string (formatted string literal)?",
        "options": [
            "A) A floating point string",
            "B) A string prefixed with f allowing {expression} embedding",
            "C) A function string",
            "D) A frozen string"
        ],
        "answer": "B",
        "explanation": "f-strings (f'...') let you embed expressions directly: f'{name} is {age} years old'."
    },
    {
        "q": "What exception is raised on: my_list[100] when list has 3 elements?",
        "options": ["A) KeyError", "B) ValueError", "C) IndexError", "D) TypeError"],
        "answer": "C",
        "explanation": "Accessing an index beyond the list's range raises IndexError."
    },
    {
        "q": "What is the output of:\n  t = (1, 2, [3, 4])\n  t[2].append(5)\n  print(t)",
        "options": [
            "A) (1, 2, [3, 4, 5])",
            "B) Error: tuple is immutable",
            "C) (1, 2, [3, 4], 5)",
            "D) (1, 2, 3, 4, 5)"
        ],
        "answer": "A",
        "explanation": "Tuples are immutable but can contain mutable objects. The list inside can be modified."
    },
    {
        "q": "What does 'dict.update({'key': 'val'})' do?",
        "options": [
            "A) Returns a new dict",
            "B) Merges/updates the dict in-place with new key-value pairs",
            "C) Removes the key",
            "D) Raises an error if key exists"
        ],
        "answer": "B",
        "explanation": "update() merges the given dict into the existing dict, overwriting existing keys."
    },
    {
        "q": "What is the purpose of '__str__' in a class?",
        "options": [
            "A) Returns the memory address",
            "B) Defines a human-readable string representation for print()",
            "C) Converts the class to a string type",
            "D) Creates a static string attribute"
        ],
        "answer": "B",
        "explanation": "__str__ defines what's returned by str() and print() for an object."
    },
    {
        "q": "What is the output of:\n  print(all([True, True, False]))",
        "options": ["A) True", "B) False", "C) [True,True,False]", "D) None"],
        "answer": "B",
        "explanation": "all() returns True only if ALL elements are truthy. False in the list → False."
    },
    {
        "q": "What is the output of:\n  print(any([False, False, True]))",
        "options": ["A) False", "B) True", "C) [True]", "D) None"],
        "answer": "B",
        "explanation": "any() returns True if AT LEAST ONE element is truthy. True is present → True."
    },
    {
        "q": "What is a 'shallow copy' vs a 'deep copy'?",
        "options": [
            "A) They are the same",
            "B) Shallow copies top-level only; deep copy recursively copies nested objects",
            "C) Deep copy copies references; shallow copy copies values",
            "D) Shallow is for lists only; deep is for dicts only"
        ],
        "answer": "B",
        "explanation": "Shallow copy (copy.copy) copies one level. Deep copy (copy.deepcopy) recursively copies all nested objects."
    },
]


def run_exam(questions, title="MEDIUM"):
    print("=" * 60)
    print(f"  PCAP-31-03 MOCK EXAM — {title} DIFFICULTY")
    print(f"  {len(questions)} Questions | Time Limit: 45 minutes")
    print("=" * 60)
    print("\nInstructions: Enter A, B, C, or D for each answer.")
    print("Type 'q' at any time to quit and see your score.\n")
    input("Press ENTER to begin...")
    print()

    score = 0
    wrong = []
    start_time = time.time()
    last_i = 0

    for i, item in enumerate(questions, 1):
        last_i = i
        print(f"Q{i}/{len(questions)}: {item['q']}")
        for opt in item["options"]:
            print(f"  {opt}")
        while True:
            ans = input("Your answer: ").strip().upper()
            if ans == "Q":
                break
            if ans in ("A", "B", "C", "D"):
                break
            print("  Invalid input. Please enter A, B, C, or D.")

        if ans == "Q":
            print("\n--- Exam terminated early ---")
            break

        if ans == item["answer"]:
            print("  ✔  Correct!\n")
            score += 1
        else:
            print(f"  ✘  Incorrect. Correct answer: {item['answer']}")
            print(f"     {item['explanation']}\n")
            wrong.append((i, item))

    elapsed = time.time() - start_time
    mins, secs = divmod(int(elapsed), 60)

    print("\n" + "=" * 60)
    print("  RESULTS")
    print("=" * 60)
    print(f"  Score    : {score} / {last_i}")
    percent = (score / last_i * 100) if last_i else 0
    print(f"  Percent  : {percent:.1f}%")
    print(f"  Time     : {mins}m {secs}s")
    status = "PASS ✔" if percent >= 70 else "FAIL ✘"
    print(f"  Status   : {status}  (passing = 70%)")

    if wrong:
        print(f"\n  Missed questions ({len(wrong)}):")
        for num, item in wrong:
            print(f"  Q{num}: {item['q'][:60]}...")
            print(f"        Correct: {item['answer']} — {item['explanation']}")
    print("=" * 60)


if __name__ == "__main__":
    q_list = QUESTIONS.copy()
    random.shuffle(q_list)
    run_exam(q_list, title="MEDIUM")