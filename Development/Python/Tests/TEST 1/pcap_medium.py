#!/usr/bin/env python3
"""PCAP-31-03 mock exam - Medium (50 questions)."""

QUESTIONS = [
    {
        "q": "What is the result of list(range(1, 5, 2))?",
        "options": {"A": "[1, 3]", "B": "[1, 2, 3, 4]", "C": "[2, 4]", "D": "[1, 3, 5]"},
        "answer": "A",
    },
    {
        "q": "What is the output of: print('ab' in 'cabd')?",
        "options": {"A": "True", "B": "False", "C": "'ab'", "D": "Error"},
        "answer": "A",
    },
    {
        "q": "Which statement creates a shallow copy of a list a?",
        "options": {"A": "b = a", "B": "b = a[:]", "C": "b = list(a, a)", "D": "b = copy(a)"},
        "answer": "B",
    },
    {
        "q": "What is the result of: 3 < 5 and 2 == 2?",
        "options": {"A": "True", "B": "False", "C": "2", "D": "Error"},
        "answer": "A",
    },
    {
        "q": "Which expression creates a set from the keys of a dict d?",
        "options": {"A": "set(d)", "B": "set(d.values())", "C": "d.keys(set)", "D": "keys(d)"},
        "answer": "A",
    },
    {
        "q": "What does str.split() return?",
        "options": {"A": "A tuple", "B": "A list", "C": "A dict", "D": "A set"},
        "answer": "B",
    },
    {
        "q": "Which function is used to open a file safely with automatic close?",
        "options": {"A": "open()", "B": "with", "C": "file()", "D": "safe_open()"},
        "answer": "B",
    },
    {
        "q": "What is the result of: bool('0')?",
        "options": {"A": "False", "B": "True", "C": "0", "D": "Error"},
        "answer": "B",
    },
    {
        "q": "Which statement defines a function with a default parameter value?",
        "options": {"A": "def f(x=1):", "B": "def f(x==1):", "C": "def f(x:1):", "D": "def f(x->1):"},
        "answer": "A",
    },
    {
        "q": "What does the expression a[-1] return for a non-empty list?",
        "options": {"A": "First element", "B": "Last element", "C": "Middle element", "D": "Error"},
        "answer": "B",
    },
    {
        "q": "Which method removes a specific value from a list?",
        "options": {"A": "pop()", "B": "remove()", "C": "discard()", "D": "delete()"},
        "answer": "B",
    },
    {
        "q": "What is the output of: 'a,b,c'.split(',')?",
        "options": {"A": "['a', 'b', 'c']", "B": "('a','b','c')", "C": "{'a','b','c'}", "D": "Error"},
        "answer": "A",
    },
    {
        "q": "Which operator performs floor division?",
        "options": {"A": "/", "B": "//", "C": "%", "D": "**"},
        "answer": "B",
    },
    {
        "q": "What does dict.get('k', 0) return if 'k' is missing?",
        "options": {"A": "None", "B": "0", "C": "KeyError", "D": "False"},
        "answer": "B",
    },
    {
        "q": "Which statement creates a list comprehension of squares 0..4?",
        "options": {"A": "[x*x for x in range(5)]", "B": "(x*x for x in range(5))", "C": "{x*x for x in range(5)}", "D": "[x**2 in range(5)]"},
        "answer": "A",
    },
    {
        "q": "Which is true about tuples?",
        "options": {"A": "Mutable", "B": "Immutable", "C": "Unordered", "D": "Key-value"},
        "answer": "B",
    },
    {
        "q": "What is the output of: len({1, 1, 2})?",
        "options": {"A": "1", "B": "2", "C": "3", "D": "Error"},
        "answer": "B",
    },
    {
        "q": "Which statement sorts a list in place?",
        "options": {"A": "sorted(a)", "B": "a.sort()", "C": "a = sort(a)", "D": "a.sorted()"},
        "answer": "B",
    },
    {
        "q": "What does the slice a[1:4] include?",
        "options": {"A": "Indexes 1,2,3", "B": "Indexes 1,2,3,4", "C": "Indexes 0,1,2", "D": "Index 4 only"},
        "answer": "A",
    },
    {
        "q": "Which keyword is used to define a generator function?",
        "options": {"A": "yield", "B": "return", "C": "gen", "D": "async"},
        "answer": "A",
    },
    {
        "q": "What is the output of: list('hi')?",
        "options": {"A": "['hi']", "B": "['h', 'i']", "C": "['h', 'i', '']", "D": "Error"},
        "answer": "B",
    },
    {
        "q": "Which built-in returns an iterator?",
        "options": {"A": "iter()", "B": "next()", "C": "range()", "D": "list()"},
        "answer": "A",
    },
    {
        "q": "What is the result of: 10 if 2 > 3 else 20?",
        "options": {"A": "10", "B": "20", "C": "True", "D": "False"},
        "answer": "B",
    },
    {
        "q": "Which function adds a new key only if missing?",
        "options": {"A": "setdefault()", "B": "update()", "C": "get()", "D": "pop()"},
        "answer": "A",
    },
    {
        "q": "What happens if you call next() after an iterator is exhausted?",
        "options": {"A": "Returns None", "B": "Raises StopIteration", "C": "Restarts", "D": "Raises KeyError"},
        "answer": "B",
    },
    {
        "q": "Which of these is a valid with statement for reading?",
        "options": {"A": "with open('f.txt') as f:", "B": "with open('f.txt', 'w') as f:", "C": "with read('f.txt') as f:", "D": "with file('f.txt') as f:"},
        "answer": "A",
    },
    {
        "q": "What is the output of: 'a' * 0?",
        "options": {"A": "'a'", "B": "''", "C": "0", "D": "Error"},
        "answer": "B",
    },
    {
        "q": "Which statement defines keyword-only arguments?",
        "options": {"A": "def f(*, x):", "B": "def f(**x):", "C": "def f(x*):", "D": "def f(*x):"},
        "answer": "A",
    },
    {
        "q": "What is the result of: [x for x in range(3) if x]?",
        "options": {"A": "[0, 1, 2]", "B": "[1, 2]", "C": "[0, 2]", "D": "[]"},
        "answer": "B",
    },
    {
        "q": "Which is true about strings in Python?",
        "options": {"A": "Mutable", "B": "Immutable", "C": "Unordered", "D": "Key-value"},
        "answer": "B",
    },
    {
        "q": "What is the output of: {1,2} | {2,3}?",
        "options": {"A": "{1,2,3}", "B": "{2}", "C": "{1,3}", "D": "Error"},
        "answer": "A",
    },
    {
        "q": "Which statement removes and returns a dict item?",
        "options": {"A": "remove()", "B": "pop()", "C": "discard()", "D": "clear()"},
        "answer": "B",
    },
    {
        "q": "What does enumerate(a) produce?",
        "options": {"A": "Pairs of (index, value)", "B": "Pairs of (value, value)", "C": "List of indexes", "D": "Set of indexes"},
        "answer": "A",
    },
    {
        "q": "Which comparison is chained correctly?",
        "options": {"A": "1 < 2 < 3", "B": "1 < 2 > 3 < 4", "C": "1 < 2 <", "D": "1 < < 2"},
        "answer": "A",
    },
    {
        "q": "What is the output of: 'abc'.find('b')?",
        "options": {"A": "0", "B": "1", "C": "2", "D": "-1"},
        "answer": "B",
    },
    {
        "q": "Which function converts an iterable of pairs to a dict?",
        "options": {"A": "dict()", "B": "list()", "C": "set()", "D": "tuple()"},
        "answer": "A",
    },
    {
        "q": "What is the output of: bool([])?",
        "options": {"A": "True", "B": "False", "C": "[]", "D": "Error"},
        "answer": "B",
    },
    {
        "q": "Which statement creates a generator expression?",
        "options": {"A": "(x for x in range(3))", "B": "[x for x in range(3)]", "C": "{x for x in range(3)}", "D": "{x: x for x in range(3)}"},
        "answer": "A",
    },
    {
        "q": "What is the output of: 'ab' == 'a' + 'b'?",
        "options": {"A": "True", "B": "False", "C": "Error", "D": "'ab'"},
        "answer": "A",
    },
    {
        "q": "Which built-in returns a sorted list without modifying the original?",
        "options": {"A": "sort()", "B": "sorted()", "C": "order()", "D": "arrange()"},
        "answer": "B",
    },
    {
        "q": "What does range(5, 0, -2) produce?",
        "options": {"A": "5,3,1", "B": "5,4,3,2,1", "C": "0,2,4", "D": "5,3,1,-1"},
        "answer": "A",
    },
    {
        "q": "Which of these raises a KeyError?",
        "options": {"A": "d['missing']", "B": "d.get('missing')", "C": "'x' in d", "D": "d.get('missing', 0)"},
        "answer": "A",
    },
    {
        "q": "What is the output of: list(map(str, [1,2]))?",
        "options": {"A": "['1', '2']", "B": "[1, 2]", "C": "('1', '2')", "D": "Error"},
        "answer": "A",
    },
    {
        "q": "Which statement imports sqrt with an alias?",
        "options": {"A": "from math import sqrt as s", "B": "import math.sqrt as s", "C": "from math as s import sqrt", "D": "import sqrt from math as s"},
        "answer": "A",
    },
    {
        "q": "What is the result of: 0 or 5?",
        "options": {"A": "0", "B": "5", "C": "False", "D": "True"},
        "answer": "B",
    },
    {
        "q": "Which method splits a path into (head, tail)?",
        "options": {"A": "os.path.split", "B": "os.path.join", "C": "os.path.basename", "D": "os.path.dirname"},
        "answer": "A",
    },
    {
        "q": "What is the output of: list(filter(None, [0, 1, 2]))?",
        "options": {"A": "[0, 1, 2]", "B": "[1, 2]", "C": "[0]", "D": "[]"},
        "answer": "B",
    },
    {
        "q": "Which statement creates a dict comprehension?",
        "options": {"A": "{x: x*x for x in range(3)}", "B": "[x: x*x for x in range(3)]", "C": "(x: x*x for x in range(3))", "D": "{x, x*x for x in range(3)}"},
        "answer": "A",
    },
    {
        "q": "What does the with statement guarantee?",
        "options": {"A": "Automatic resource cleanup", "B": "Faster execution", "C": "Global scope", "D": "Type checking"},
        "answer": "A",
    },
    {
        "q": "Which module provides random numbers?",
        "options": {"A": "math", "B": "random", "C": "statistics", "D": "time"},
        "answer": "B",
    },
    {
        "q": "What is the output of: tuple([1,2,3])?",
        "options": {"A": "(1, 2, 3)", "B": "[1, 2, 3]", "C": "{1, 2, 3}", "D": "Error"},
        "answer": "A",
    },
]


def print_questions():
    score = 0
    total = len(QUESTIONS)
    for i, item in enumerate(QUESTIONS, start=1):
        print(f"Q{i}. {item['q']}")
        for key in ("A", "B", "C", "D"):
            print(f"  {key}. {item['options'][key]}")

        while True:
            choice = input("Your answer (A-D): ").strip().upper()
            if choice in item["options"]:
                break
            print("Please enter A, B, C, or D.")

        if choice == item["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. Answer: {item['answer']}")

        print()

    percent = (score / total) * 100 if total else 0.0
    print(f"Score: {score}/{total} ({percent:.1f}%)")


if __name__ == "__main__":
    print_questions()
