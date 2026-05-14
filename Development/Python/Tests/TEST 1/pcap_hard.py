#!/usr/bin/env python3
"""PCAP-31-03 mock exam - Hard (50 questions)."""

QUESTIONS = [
    {
        "q": "What is the output of: (lambda x=1: x + 1)()?",
        "options": {"A": "1", "B": "2", "C": "None", "D": "Error"},
        "answer": "B",
    },
    {
        "q": "Which expression creates a shallow copy of a nested list a?",
        "options": {"A": "a[:]", "B": "copy.deepcopy(a)", "C": "list(a, a)", "D": "a.copy(True)"},
        "answer": "A",
    },
    {
        "q": "What is the output of: [i for i in range(3)][-1]?",
        "options": {"A": "0", "B": "1", "C": "2", "D": "3"},
        "answer": "C",
    },
    {
        "q": "Which statement about default arguments is true?",
        "options": {"A": "Evaluated at call time", "B": "Evaluated at definition time", "C": "Always deep-copied", "D": "Cannot be mutable"},
        "answer": "B",
    },
    {
        "q": "What is the output of: (1, 2) + (3,)?",
        "options": {"A": "(1, 2, 3)", "B": "(1, 2, (3,))", "C": "(1, 2) + (3) ", "D": "Error"},
        "answer": "A",
    },
    {
        "q": "Which exception is raised when converting 'a' to int?",
        "options": {"A": "TypeError", "B": "ValueError", "C": "KeyError", "D": "IndexError"},
        "answer": "B",
    },
    {
        "q": "What is the result of: {x for x in [1,1,2,2]}?",
        "options": {"A": "{1, 2}", "B": "[1, 2]", "C": "{1, 1, 2, 2}", "D": "Error"},
        "answer": "A",
    },
    {
        "q": "Which is true about list.sort()?",
        "options": {"A": "Returns a new list", "B": "Sorts in place and returns None", "C": "Returns a tuple", "D": "Sorts a copy"},
        "answer": "B",
    },
    {
        "q": "What is the output of: 1 < 2 < 2?",
        "options": {"A": "True", "B": "False", "C": "1", "D": "Error"},
        "answer": "B",
    },
    {
        "q": "Which statement about slicing is correct?",
        "options": {"A": "End index is inclusive", "B": "End index is exclusive", "C": "Slices mutate the original", "D": "Slices return iterators"},
        "answer": "B",
    },
    {
        "q": "What does the expression any([]) return?",
        "options": {"A": "True", "B": "False", "C": "None", "D": "Error"},
        "answer": "B",
    },
    {
        "q": "What is the output of: all([1, 2, 0])?",
        "options": {"A": "True", "B": "False", "C": "0", "D": "Error"},
        "answer": "B",
    },
    {
        "q": "Which line correctly catches two exception types?",
        "options": {"A": "except (ValueError, TypeError):", "B": "except ValueError, TypeError:", "C": "except ValueError | TypeError:", "D": "except [ValueError, TypeError]:"},
        "answer": "A",
    },
    {
        "q": "What is the output of: list(zip([1,2], ['a','b','c']))?",
        "options": {"A": "[(1, 'a'), (2, 'b')]", "B": "[(1, 'a'), (2, 'b'), (None, 'c')]", "C": "[(1, 'a'), (2, 'b'), (0, 'c')]", "D": "Error"},
        "answer": "A",
    },
    {
        "q": "Which module provides deque?",
        "options": {"A": "collections", "B": "itertools", "C": "functools", "D": "queue"},
        "answer": "A",
    },
    {
        "q": "What is the output of: dict.fromkeys('ab', 0)?",
        "options": {"A": "{'a': 0, 'b': 0}", "B": "{'ab': 0}", "C": "{'a': 'b': 0}", "D": "Error"},
        "answer": "A",
    },
    {
        "q": "Which statement about generators is true?",
        "options": {"A": "They store all values in memory", "B": "They are iterators", "C": "They require indexing", "D": "They are mutable sequences"},
        "answer": "B",
    },
    {
        "q": "What is the output of: next(iter([10, 20]))?",
        "options": {"A": "10", "B": "20", "C": "[10, 20]", "D": "Error"},
        "answer": "A",
    },
    {
        "q": "Which of these is a valid way to open a file for binary write?",
        "options": {"A": "open('f', 'bw')", "B": "open('f', 'wb')", "C": "open('f', 'w+b')", "D": "open('f', 'b')"},
        "answer": "B",
    },
    {
        "q": "What is the output of: 'x' is 'x'?",
        "options": {"A": "Always True", "B": "Always False", "C": "Implementation-dependent", "D": "Error"},
        "answer": "C",
    },
    {
        "q": "Which statement best describes EAFP?",
        "options": {"A": "Check before doing", "B": "Do first, handle exceptions", "C": "Avoid exceptions", "D": "Avoid type hints"},
        "answer": "B",
    },
    {
        "q": "What is the output of: [*range(3)]?",
        "options": {"A": "[0, 1, 2]", "B": "(0, 1, 2)", "C": "{0, 1, 2}", "D": "Error"},
        "answer": "A",
    },
    {
        "q": "Which is true about dict views (keys, values, items)?",
        "options": {"A": "They are lists", "B": "They are dynamic views", "C": "They are tuples", "D": "They are copies"},
        "answer": "B",
    },
    {
        "q": "What is the output of: {**{'a':1}, **{'b':2}}?",
        "options": {"A": "{'a': 1, 'b': 2}", "B": "{'a': 1}", "C": "{'b': 2}", "D": "Error"},
        "answer": "A",
    },
    {
        "q": "Which statement creates a closure?",
        "options": {"A": "A nested function referencing outer scope", "B": "A class method", "C": "A lambda with no free vars", "D": "A global variable"},
        "answer": "A",
    },
    {
        "q": "What is the output of: list(reversed([1,2,3]))?",
        "options": {"A": "[3, 2, 1]", "B": "[1, 2, 3]", "C": "(3, 2, 1)", "D": "Error"},
        "answer": "A",
    },
    {
        "q": "Which is true about exceptions in a finally block?",
        "options": {"A": "Finally never runs", "B": "Finally always runs", "C": "Finally runs only on success", "D": "Finally replaces exceptions"},
        "answer": "B",
    },
    {
        "q": "What is the output of: list(filter(lambda x: x%2, [0,1,2,3]))?",
        "options": {"A": "[0, 2]", "B": "[1, 3]", "C": "[0, 1, 2, 3]", "D": "[]"},
        "answer": "B",
    },
    {
        "q": "Which keyword declares a variable as nonlocal?",
        "options": {"A": "global", "B": "nonlocal", "C": "local", "D": "outer"},
        "answer": "B",
    },
    {
        "q": "What is the output of: 2 ** 3 ** 2?",
        "options": {"A": "64", "B": "512", "C": "81", "D": "Error"},
        "answer": "B",
    },
    {
        "q": "Which method removes and returns the last set element?",
        "options": {"A": "remove()", "B": "pop()", "C": "discard()", "D": "clear()"},
        "answer": "B",
    },
    {
        "q": "Which statement correctly uses enumerate with start=1?",
        "options": {"A": "enumerate(a, start=1)", "B": "enumerate(a, 1)", "C": "enumerate(a, first=1)", "D": "A and B"},
        "answer": "D",
    },
    {
        "q": "What is the output of: {'a':1, 'b':2}.get('c', 3)?",
        "options": {"A": "None", "B": "3", "C": "KeyError", "D": "'c'"},
        "answer": "B",
    },
    {
        "q": "Which is true about list multiplication?",
        "options": {"A": "[[]] * 3 creates three distinct lists", "B": "[[]] * 3 creates references to the same list", "C": "It deep-copies nested lists", "D": "It is not allowed"},
        "answer": "B",
    },
    {
        "q": "What is the output of: 'ab'.replace('a', 'aa')?",
        "options": {"A": "aab", "B": "aaab", "C": "ab", "D": "Error"},
        "answer": "A",
    },
    {
        "q": "Which statement about __name__ is true?",
        "options": {"A": "It is always '__main__'", "B": "It is the module name", "C": "It is a function", "D": "It is undefined"},
        "answer": "B",
    },
    {
        "q": "What is the output of: (1, 2, 3)[1:3]?",
        "options": {"A": "(2, 3)", "B": "(1, 2)", "C": "(3,)", "D": "Error"},
        "answer": "A",
    },
    {
        "q": "Which statement about try/except/else is correct?",
        "options": {"A": "else runs if exception occurs", "B": "else runs if no exception occurs", "C": "else runs always", "D": "else runs before try"},
        "answer": "B",
    },
    {
        "q": "What is the output of: [x for x in range(5) if x%2==0]?",
        "options": {"A": "[0, 2, 4]", "B": "[1, 3, 5]", "C": "[2, 4]", "D": "[0, 1, 2, 3, 4]"},
        "answer": "A",
    },
    {
        "q": "Which statement about sets is true?",
        "options": {"A": "They are ordered", "B": "They cannot contain mutable elements", "C": "They allow duplicate items", "D": "They are indexed"},
        "answer": "B",
    },
    {
        "q": "What is the output of: 'a,b,c'.split(',', 1)?",
        "options": {"A": "['a', 'b', 'c']", "B": "['a', 'b,c']", "C": "['a,b', 'c']", "D": "Error"},
        "answer": "B",
    },
    {
        "q": "Which function returns both quotient and remainder?",
        "options": {"A": "divmod()", "B": "quotrem()", "C": "split()", "D": "mod()"},
        "answer": "A",
    },
    {
        "q": "What is the output of: list(map(lambda x: x+1, [1,2]))?",
        "options": {"A": "[2, 3]", "B": "[1, 2]", "C": "[1, 3]", "D": "Error"},
        "answer": "A",
    },
    {
        "q": "Which exception is raised by open('missing.txt')?",
        "options": {"A": "KeyError", "B": "FileNotFoundError", "C": "IOError", "D": "StopIteration"},
        "answer": "B",
    },
    {
        "q": "Which is true about function annotations?",
        "options": {"A": "They enforce types", "B": "They are stored in __annotations__", "C": "They are required", "D": "They change runtime behavior"},
        "answer": "B",
    },
    {
        "q": "What is the output of: list(''.join(['a','b']))?",
        "options": {"A": "['a', 'b']", "B": "['ab']", "C": "['a', 'b', '']", "D": "Error"},
        "answer": "A",
    },
    {
        "q": "Which statement about class attributes is true?",
        "options": {"A": "They are stored per instance", "B": "They are shared across instances", "C": "They cannot be overridden", "D": "They are private"},
        "answer": "B",
    },
    {
        "q": "What is the output of: (lambda *a: len(a))(1,2,3)?",
        "options": {"A": "2", "B": "3", "C": "1", "D": "Error"},
        "answer": "B",
    },
    {
        "q": "Which statement about multiple assignment is correct?",
        "options": {"A": "Left side evaluates before right side", "B": "Right side evaluates before left side", "C": "Evaluates left to right only", "D": "Evaluation order is undefined"},
        "answer": "B",
    },
    {
        "q": "What is the output of: {x: x for x in range(2)}.items() ?",
        "options": {"A": "[(0, 0), (1, 1)]", "B": "dict_items([(0, 0), (1, 1)])", "C": "{(0, 0), (1, 1)}", "D": "Error"},
        "answer": "B",
    },
    {
        "q": "Which statement about inheritance is true?",
        "options": {"A": "Subclass cannot override methods", "B": "Subclass can extend or override methods", "C": "Subclass must redefine __init__", "D": "Subclass cannot call super()"},
        "answer": "B",
    },
    {
        "q": "What is the output of: sorted('bca')?",
        "options": {"A": "['a', 'b', 'c']", "B": "'abc'", "C": "('a', 'b', 'c')", "D": "Error"},
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
