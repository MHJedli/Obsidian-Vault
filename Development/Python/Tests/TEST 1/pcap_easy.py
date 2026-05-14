#!/usr/bin/env python3
"""PCAP-31-03 mock exam - Easy (50 questions)."""

QUESTIONS = [
    {
        "q": "Which function outputs text to the console?",
        "options": {"A": "print()", "B": "input()", "C": "len()", "D": "type()"},
        "answer": "A",
    },
    {
        "q": "Which type is the result of 3 / 2 in Python 3?",
        "options": {"A": "int", "B": "float", "C": "str", "D": "bool"},
        "answer": "B",
    },
    {
        "q": "What does len([1, 2, 3]) return?",
        "options": {"A": "2", "B": "3", "C": "[1,2,3]", "D": "Error"},
        "answer": "B",
    },
    {
        "q": "Which keyword starts a conditional block?",
        "options": {"A": "for", "B": "if", "C": "def", "D": "class"},
        "answer": "B",
    },
    {
        "q": "Which operator tests equality?",
        "options": {"A": "=", "B": "==", "C": "!=", "D": "<"},
        "answer": "B",
    },
    {
        "q": "Which literal is Boolean False?",
        "options": {"A": "False", "B": "0", "C": "'False'", "D": "None"},
        "answer": "A",
    },
    {
        "q": "How do you start a function definition?",
        "options": {"A": "function", "B": "def", "C": "fun", "D": "define"},
        "answer": "B",
    },
    {
        "q": "What is the index of the first element in a list?",
        "options": {"A": "0", "B": "1", "C": "-1", "D": "None"},
        "answer": "A",
    },
    {
        "q": "Which loop is used to iterate over a sequence?",
        "options": {"A": "if", "B": "while", "C": "for", "D": "try"},
        "answer": "C",
    },
    {
        "q": "Which function reads a line from user input?",
        "options": {"A": "read()", "B": "input()", "C": "scan()", "D": "get()"},
        "answer": "B",
    },
    {
        "q": "What is the result of 'py' + 'thon'?",
        "options": {"A": "py thon", "B": "python", "C": "py+thon", "D": "Error"},
        "answer": "B",
    },
    {
        "q": "Which of these is a tuple literal?",
        "options": {"A": "[1, 2]", "B": "{1, 2}", "C": "(1, 2)", "D": "{1: 2}"},
        "answer": "C",
    },
    {
        "q": "How do you comment a single line?",
        "options": {"A": "//", "B": "#", "C": "/*", "D": "--"},
        "answer": "B",
    },
    {
        "q": "Which built-in converts a string to an integer?",
        "options": {"A": "int()", "B": "str()", "C": "float()", "D": "bool()"},
        "answer": "A",
    },
    {
        "q": "Which keyword exits a loop early?",
        "options": {"A": "stop", "B": "break", "C": "exit", "D": "return"},
        "answer": "B",
    },
    {
        "q": "Which container is ordered and mutable?",
        "options": {"A": "tuple", "B": "set", "C": "list", "D": "frozenset"},
        "answer": "C",
    },
    {
        "q": "What is the result of 2 ** 3?",
        "options": {"A": "6", "B": "8", "C": "9", "D": "Error"},
        "answer": "B",
    },
    {
        "q": "Which value represents 'no value'?",
        "options": {"A": "0", "B": "''", "C": "None", "D": "False"},
        "answer": "C",
    },
    {
        "q": "Which method appends an element to a list?",
        "options": {"A": "add()", "B": "append()", "C": "push()", "D": "insert()"},
        "answer": "B",
    },
    {
        "q": "Which keyword defines a class?",
        "options": {"A": "class", "B": "struct", "C": "object", "D": "type"},
        "answer": "A",
    },
    {
        "q": "What is the result of bool(0)?",
        "options": {"A": "True", "B": "False", "C": "0", "D": "Error"},
        "answer": "B",
    },
    {
        "q": "Which is a dictionary literal?",
        "options": {"A": "{1, 2}", "B": "{1: 'a'}", "C": "[1: 'a']", "D": "(1: 'a')"},
        "answer": "B",
    },
    {
        "q": "Which operator gives the remainder?",
        "options": {"A": "/", "B": "//", "C": "%", "D": "**"},
        "answer": "C",
    },
    {
        "q": "Which keyword handles exceptions?",
        "options": {"A": "try", "B": "catch", "C": "except", "D": "raise"},
        "answer": "C",
    },
    {
        "q": "What does range(3) produce?",
        "options": {"A": "1,2,3", "B": "0,1,2", "C": "0,1,2,3", "D": "3"},
        "answer": "B",
    },
    {
        "q": "Which keyword starts a loop that repeats while a condition is true?",
        "options": {"A": "for", "B": "while", "C": "loop", "D": "repeat"},
        "answer": "B",
    },
    {
        "q": "Which built-in returns the type of an object?",
        "options": {"A": "kind()", "B": "type()", "C": "class()", "D": "id()"},
        "answer": "B",
    },
    {
        "q": "What is the result of 'A' in ['A', 'B']?",
        "options": {"A": "True", "B": "False", "C": "1", "D": "Error"},
        "answer": "A",
    },
    {
        "q": "Which method removes the last list item by default?",
        "options": {"A": "remove()", "B": "pop()", "C": "del()", "D": "clear()"},
        "answer": "B",
    },
    {
        "q": "What is the result of 5 // 2?",
        "options": {"A": "2.5", "B": "2", "C": "3", "D": "Error"},
        "answer": "B",
    },
    {
        "q": "Which keyword returns a value from a function?",
        "options": {"A": "yield", "B": "return", "C": "pass", "D": "break"},
        "answer": "B",
    },
    {
        "q": "How do you create an empty list?",
        "options": {"A": "()", "B": "[]", "C": "{}", "D": "set()"},
        "answer": "B",
    },
    {
        "q": "Which function returns the absolute value?",
        "options": {"A": "abs()", "B": "round()", "C": "sum()", "D": "max()"},
        "answer": "A",
    },
    {
        "q": "Which is a valid variable name?",
        "options": {"A": "2nd", "B": "first-name", "C": "first_name", "D": "class"},
        "answer": "C",
    },
    {
        "q": "Which operator checks membership?",
        "options": {"A": "is", "B": "in", "C": "==", "D": "and"},
        "answer": "B",
    },
    {
        "q": "What does list('ab') produce?",
        "options": {"A": "['ab']", "B": "['a', 'b']", "C": "['a', 'b', '']", "D": "Error"},
        "answer": "B",
    },
    {
        "q": "Which keyword is used to create a module alias?",
        "options": {"A": "as", "B": "alias", "C": "with", "D": "from"},
        "answer": "A",
    },
    {
        "q": "How do you import the math module?",
        "options": {"A": "import math", "B": "include math", "C": "require math", "D": "use math"},
        "answer": "A",
    },
    {
        "q": "Which statement creates a set from a list?",
        "options": {"A": "set([1, 2])", "B": "{[1, 2]}", "C": "(1, 2)", "D": "list({1, 2})"},
        "answer": "A",
    },
    {
        "q": "What is the result of 'abc'.upper()?",
        "options": {"A": "abc", "B": "ABC", "C": "Abc", "D": "Error"},
        "answer": "B",
    },
    {
        "q": "Which keyword does nothing and is a placeholder?",
        "options": {"A": "pass", "B": "skip", "C": "none", "D": "null"},
        "answer": "A",
    },
    {
        "q": "Which is a valid slice of a list named a?",
        "options": {"A": "a[1..3]", "B": "a[1:3]", "C": "a(1:3)", "D": "a{1:3}"},
        "answer": "B",
    },
    {
        "q": "Which function returns the largest item?",
        "options": {"A": "max()", "B": "largest()", "C": "top()", "D": "big()"},
        "answer": "A",
    },
    {
        "q": "What does 'hi' * 3 produce?",
        "options": {"A": "hi3", "B": "hihihi", "C": "hi hi hi", "D": "Error"},
        "answer": "B",
    },
    {
        "q": "Which keyword checks object identity?",
        "options": {"A": "==", "B": "is", "C": "in", "D": "equals"},
        "answer": "B",
    },
    {
        "q": "What is the result of not True?",
        "options": {"A": "True", "B": "False", "C": "1", "D": "0"},
        "answer": "B",
    },
    {
        "q": "Which statement opens a file for reading?",
        "options": {"A": "open('f.txt')", "B": "open('f.txt', 'w')", "C": "read('f.txt')", "D": "file('f.txt')"},
        "answer": "A",
    },
    {
        "q": "Which method removes all items from a list?",
        "options": {"A": "clear()", "B": "delete()", "C": "remove()", "D": "pop()"},
        "answer": "A",
    },
    {
        "q": "What is the result of 7 % 3?",
        "options": {"A": "1", "B": "2", "C": "3", "D": "4"},
        "answer": "B",
    },
    {
        "q": "Which keyword imports specific names from a module?",
        "options": {"A": "use", "B": "from", "C": "get", "D": "select"},
        "answer": "B",
    },
    {
        "q": "Which function returns the smallest item?",
        "options": {"A": "min()", "B": "low()", "C": "small()", "D": "least()"},
        "answer": "A",
    },
    {
        "q": "Which of these is a valid dictionary key?",
        "options": {"A": "[1, 2]", "B": "{1, 2}", "C": "(1, 2)", "D": "{'a': 1}"},
        "answer": "C",
    },
    {
        "q": "How do you start a try/except block?",
        "options": {"A": "try:", "B": "attempt:", "C": "except:", "D": "catch:"},
        "answer": "A",
    },
    {
        "q": "Which built-in returns the sum of items?",
        "options": {"A": "sum()", "B": "add()", "C": "total()", "D": "combine()"},
        "answer": "A",
    },
    {
        "q": "Which statement creates a new empty set?",
        "options": {"A": "{}", "B": "set()", "C": "[]", "D": "()"},
        "answer": "B",
    },
    {
        "q": "Which method adds a key-value pair to a dict?",
        "options": {"A": "add()", "B": "append()", "C": "assign with d[k] = v", "D": "push()"},
        "answer": "C",
    },
    {
        "q": "Which keyword defines an anonymous function?",
        "options": {"A": "lambda", "B": "anon", "C": "def", "D": "func"},
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
