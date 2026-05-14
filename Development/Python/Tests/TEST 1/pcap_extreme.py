#!/usr/bin/env python3
"""PCAP-31-03 mock exam - Extreme (50 questions)."""

QUESTIONS = [
    {
        "q": "What is the output of: (lambda x, y=2, *a: x + y + len(a))(1, 3, 4, 5)?",
        "options": {"A": "6", "B": "7", "C": "8", "D": "9"},
        "answer": "B",
    },
    {
        "q": "Which statement about method resolution order (MRO) is correct?",
        "options": {"A": "Python uses depth-first, left-to-right only", "B": "Python uses C3 linearization", "C": "Python ignores base classes order", "D": "MRO is random"},
        "answer": "B",
    },
    {
        "q": "What is the output of: (True and False) or (True and not False)?",
        "options": {"A": "True", "B": "False", "C": "None", "D": "Error"},
        "answer": "A",
    },
    {
        "q": "Which expression creates a generator that yields squares of even numbers?",
        "options": {"A": "(x*x for x in range(10) if x%2==0)", "B": "[x*x for x in range(10) if x%2==0]", "C": "{x*x for x in range(10) if x%2==0}", "D": "(x**2 in range(10) if x%2==0)"},
        "answer": "A",
    },
    {
        "q": "What is the output of: (1, 2, 3) == (1, 2, 3.0)?",
        "options": {"A": "True", "B": "False", "C": "TypeError", "D": "Error"},
        "answer": "A",
    },
    {
        "q": "Which statement about slicing with step is correct?",
        "options": {"A": "a[::-1] reverses the list", "B": "a[::0] is valid", "C": "a[1:5:-1] always returns elements", "D": "a[::-2] is invalid"},
        "answer": "A",
    },
    {
        "q": "What is the output of: [i for i in range(5) if i in (0,2,4)]?",
        "options": {"A": "[0, 2, 4]", "B": "[1, 3, 5]", "C": "[2, 4]", "D": "[0, 1, 2, 3, 4]"},
        "answer": "A",
    },
    {
        "q": "Which is true about weak references?",
        "options": {"A": "They increase refcount", "B": "They do not prevent garbage collection", "C": "They are the default for all refs", "D": "They disable GC"},
        "answer": "B",
    },
    {
        "q": "What is the output of: (lambda x: [x, x*2])(3)[1]?",
        "options": {"A": "3", "B": "6", "C": "[3, 6]", "D": "Error"},
        "answer": "B",
    },
    {
        "q": "Which statement about decorators is correct?",
        "options": {"A": "They must return None", "B": "They can replace a function with another callable", "C": "They only work on methods", "D": "They are evaluated at call time"},
        "answer": "B",
    },
    {
        "q": "What is the output of: {x: x*x for x in range(3)}[2]?",
        "options": {"A": "2", "B": "3", "C": "4", "D": "Error"},
        "answer": "C",
    },
    {
        "q": "Which statement about descriptors is true?",
        "options": {"A": "They are only for modules", "B": "They define __get__, __set__, or __delete__", "C": "They are synonyms for decorators", "D": "They cannot be classes"},
        "answer": "B",
    },
    {
        "q": "What is the output of: list({i for i in range(3)})?",
        "options": {"A": "[0, 1, 2]", "B": "[2, 1, 0]", "C": "Order is arbitrary", "D": "Error"},
        "answer": "C",
    },
    {
        "q": "Which statement about the GIL is correct?",
        "options": {"A": "It guarantees parallel CPU execution in threads", "B": "It allows only one thread to execute Python bytecode at a time", "C": "It disables threading", "D": "It is removed in CPython"},
        "answer": "B",
    },
    {
        "q": "What is the output of: list(map(lambda x: x[0], ['ab','cd']))?",
        "options": {"A": "['a', 'c']", "B": "['b', 'd']", "C": "['ab', 'cd']", "D": "Error"},
        "answer": "A",
    },
    {
        "q": "Which is true about __slots__?",
        "options": {"A": "They allow arbitrary attributes", "B": "They can reduce memory usage", "C": "They enable multiple inheritance only", "D": "They are required for dataclasses"},
        "answer": "B",
    },
    {
        "q": "What is the output of: (lambda x: (y:=x+1))(4)?",
        "options": {"A": "4", "B": "5", "C": "None", "D": "Error"},
        "answer": "B",
    },
    {
        "q": "Which statement about context managers is correct?",
        "options": {"A": "They must implement __enter__ and __exit__", "B": "They cannot suppress exceptions", "C": "They are only for files", "D": "They cannot be generators"},
        "answer": "A",
    },
    {
        "q": "What is the output of: sum([i for i in range(4) if i%2])?",
        "options": {"A": "2", "B": "3", "C": "4", "D": "6"},
        "answer": "B",
    },
    {
        "q": "Which statement about dataclasses is correct?",
        "options": {"A": "They are in the typing module", "B": "They can auto-generate __init__", "C": "They cannot be frozen", "D": "They disable type hints"},
        "answer": "B",
    },
    {
        "q": "What is the output of: [i for i in range(6) if i%2==0][::-1]?",
        "options": {"A": "[0, 2, 4]", "B": "[4, 2, 0]", "C": "[2, 4]", "D": "[5, 3, 1]"},
        "answer": "B",
    },
    {
        "q": "Which statement about itertools is true?",
        "options": {"A": "It only works with lists", "B": "It provides iterator building blocks", "C": "It is for threading", "D": "It is deprecated"},
        "answer": "B",
    },
    {
        "q": "What is the output of: (lambda f: f(2))(lambda x: x**3)?",
        "options": {"A": "4", "B": "6", "C": "8", "D": "Error"},
        "answer": "C",
    },
    {
        "q": "Which statement about namedtuple is correct?",
        "options": {"A": "It creates mutable objects", "B": "It provides tuple subclasses with named fields", "C": "It is part of math", "D": "It is deprecated"},
        "answer": "B",
    },
    {
        "q": "What is the output of: [x for x in range(3) for y in range(2)]?",
        "options": {"A": "[0, 0, 1, 1, 2, 2]", "B": "[0, 1, 2]", "C": "[0, 1, 0, 1, 0, 1]", "D": "[0, 1, 2, 3, 4, 5]"},
        "answer": "A",
    },
    {
        "q": "Which is true about generators and return statements?",
        "options": {"A": "return stops iteration with StopIteration", "B": "return yields a value", "C": "return is ignored", "D": "return converts to yield"},
        "answer": "A",
    },
    {
        "q": "What is the output of: isinstance(True, int)?",
        "options": {"A": "True", "B": "False", "C": "TypeError", "D": "Error"},
        "answer": "A",
    },
    {
        "q": "Which statement about pattern matching (match/case) is true?",
        "options": {"A": "Introduced in Python 2", "B": "Introduced in Python 3.10", "C": "Only matches strings", "D": "Replaces if entirely"},
        "answer": "B",
    },
    {
        "q": "What is the output of: (lambda x: x)([1,2])[::-1]?",
        "options": {"A": "[2, 1]", "B": "[1, 2]", "C": "(2, 1)", "D": "Error"},
        "answer": "A",
    },
    {
        "q": "Which statement about async functions is correct?",
        "options": {"A": "They return coroutines", "B": "They run in a new thread", "C": "They block by default", "D": "They cannot use await"},
        "answer": "A",
    },
    {
        "q": "What is the output of: {'a':1,'b':2} | {'b':3}?",
        "options": {"A": "{'a':1,'b':2}", "B": "{'a':1,'b':3}", "C": "{'b':3}", "D": "Error"},
        "answer": "B",
    },
    {
        "q": "Which is true about frozenset?",
        "options": {"A": "Mutable", "B": "Hashable", "C": "Ordered", "D": "Indexable"},
        "answer": "B",
    },
    {
        "q": "What is the output of: (1, 2, 3)[-2]?",
        "options": {"A": "1", "B": "2", "C": "3", "D": "Error"},
        "answer": "B",
    },
    {
        "q": "Which statement about __iter__ and __next__ is correct?",
        "options": {"A": "__next__ returns StopIteration on end", "B": "__iter__ returns an iterator", "C": "Both are optional", "D": "They are only for lists"},
        "answer": "B",
    },
    {
        "q": "What is the output of: list(filter(lambda x: x>1, [1,2,3]))?",
        "options": {"A": "[1, 2, 3]", "B": "[2, 3]", "C": "[1]", "D": "[]"},
        "answer": "B",
    },
    {
        "q": "Which statement about property is true?",
        "options": {"A": "It creates class variables", "B": "It defines managed attributes", "C": "It makes methods static", "D": "It disables inheritance"},
        "answer": "B",
    },
    {
        "q": "What is the output of: [i for i in range(4) if i%2] and [9]?",
        "options": {"A": "[1, 3]", "B": "[9]", "C": "True", "D": "False"},
        "answer": "B",
    },
    {
        "q": "Which statement about __call__ is correct?",
        "options": {"A": "It makes an instance callable", "B": "It prevents instantiation", "C": "It is required for classes", "D": "It is used for slicing"},
        "answer": "A",
    },
    {
        "q": "What is the output of: (lambda: [i*i for i in range(3)])()?",
        "options": {"A": "[0, 1, 4]", "B": "[1, 4, 9]", "C": "[0, 1, 2]", "D": "Error"},
        "answer": "A",
    },
    {
        "q": "Which statement about multiple inheritance is true?",
        "options": {"A": "Python forbids it", "B": "MRO resolves method lookup order", "C": "Leftmost base is ignored", "D": "Only works with empty classes"},
        "answer": "B",
    },
    {
        "q": "What is the output of: (lambda x: x and 5)(0)?",
        "options": {"A": "0", "B": "5", "C": "True", "D": "False"},
        "answer": "A",
    },
    {
        "q": "Which statement about recursion is correct?",
        "options": {"A": "Python has no recursion limit", "B": "Recursion uses the call stack", "C": "Recursion is always faster", "D": "Recursion is forbidden in functions"},
        "answer": "B",
    },
    {
        "q": "What is the output of: (lambda x: x is None)(None)?",
        "options": {"A": "True", "B": "False", "C": "None", "D": "Error"},
        "answer": "A",
    },
    {
        "q": "Which statement about bytes is correct?",
        "options": {"A": "They are mutable", "B": "They are sequences of integers 0-255", "C": "They are the same as str", "D": "They cannot be indexed"},
        "answer": "B",
    },
    {
        "q": "What is the output of: '10'.zfill(4)?",
        "options": {"A": "0010", "B": "0100", "C": "1000", "D": "0001"},
        "answer": "A",
    },
    {
        "q": "Which statement about global is correct?",
        "options": {"A": "It creates a new global variable", "B": "It binds a name to global scope", "C": "It makes variables immutable", "D": "It is used for imports"},
        "answer": "B",
    },
    {
        "q": "What is the output of: sum({1,2,3})?",
        "options": {"A": "6", "B": "7", "C": "5", "D": "Error"},
        "answer": "A",
    },
    {
        "q": "Which statement about type hints is correct?",
        "options": {"A": "They are enforced at runtime", "B": "They are optional and for tooling", "C": "They replace docstrings", "D": "They change bytecode"},
        "answer": "B",
    },
    {
        "q": "What is the output of: (lambda x: x == 1 or x == 2)(2)?",
        "options": {"A": "True", "B": "False", "C": "2", "D": "Error"},
        "answer": "A",
    },
    {
        "q": "Which statement about functools.lru_cache is true?",
        "options": {"A": "It disables recursion", "B": "It memoizes function results", "C": "It is for sorting", "D": "It is only for methods"},
        "answer": "B",
    },
    {
        "q": "What is the output of: list(range(1, 10, 3))?",
        "options": {"A": "[1, 4, 7]", "B": "[1, 3, 5, 7, 9]", "C": "[1, 4, 7, 10]", "D": "[2, 5, 8]"},
        "answer": "A",
    },
    {
        "q": "Which statement about __repr__ is correct?",
        "options": {"A": "It should return a string", "B": "It must print to console", "C": "It is called only once", "D": "It returns bytes"},
        "answer": "A",
    },
    {
        "q": "What is the output of: (lambda x: x if x else 'no')('')?",
        "options": {"A": "''", "B": "'no'", "C": "None", "D": "Error"},
        "answer": "B",
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
