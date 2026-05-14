#!/usr/bin/env python3
"""
PCAP-31-03 Mock Exam — EASY (50 Questions)
Topics: Basic syntax, data types, operators, simple control flow, built-ins
"""

import random
import time

QUESTIONS = [
    {
        "q": "What is the output of: print(type(42))?",
        "options": ["A) <class 'int'>", "B) <class 'float'>", "C) <class 'str'>", "D) <class 'number'>"],
        "answer": "A",
        "explanation": "42 is an integer literal, so type() returns <class 'int'>."
    },
    {
        "q": "Which keyword is used to define a function in Python?",
        "options": ["A) function", "B) def", "C) func", "D) define"],
        "answer": "B",
        "explanation": "'def' is the keyword used to define a function in Python."
    },
    {
        "q": "What does len('hello') return?",
        "options": ["A) 4", "B) 6", "C) 5", "D) None"],
        "answer": "C",
        "explanation": "'hello' has 5 characters, so len() returns 5."
    },
    {
        "q": "What is the result of 10 % 3?",
        "options": ["A) 3", "B) 1", "C) 0", "D) 3.33"],
        "answer": "B",
        "explanation": "The modulo operator % returns the remainder. 10 / 3 = 3 remainder 1."
    },
    {
        "q": "Which of the following is a valid Python comment?",
        "options": ["A) // This is a comment", "B) /* comment */", "C) # This is a comment", "D) <!-- comment -->"],
        "answer": "C",
        "explanation": "Python uses # for single-line comments."
    },
    {
        "q": "What is the output of: print(2 ** 3)?",
        "options": ["A) 6", "B) 9", "C) 8", "D) 5"],
        "answer": "C",
        "explanation": "** is the exponentiation operator. 2**3 = 2*2*2 = 8."
    },
    {
        "q": "Which data type is immutable?",
        "options": ["A) list", "B) dict", "C) tuple", "D) set"],
        "answer": "C",
        "explanation": "Tuples are immutable — they cannot be changed after creation."
    },
    {
        "q": "What does the 'input()' function return?",
        "options": ["A) int", "B) float", "C) str", "D) bool"],
        "answer": "C",
        "explanation": "input() always returns a string, regardless of what the user types."
    },
    {
        "q": "What is the output of: bool(0)?",
        "options": ["A) True", "B) False", "C) 0", "D) None"],
        "answer": "B",
        "explanation": "0 is falsy in Python, so bool(0) returns False."
    },
    {
        "q": "How do you create an empty list in Python?",
        "options": ["A) list = {}", "B) list = []", "C) list = ()", "D) list = <>"],
        "answer": "B",
        "explanation": "[] creates an empty list. {} creates an empty dict, () creates an empty tuple."
    },
    {
        "q": "What is the output of: 'Hello' + ' ' + 'World'?",
        "options": ["A) HelloWorld", "B) Hello World", "C) 'Hello World'", "D) Error"],
        "answer": "B",
        "explanation": "The + operator concatenates strings. Result is 'Hello World'."
    },
    {
        "q": "Which function converts a string to an integer?",
        "options": ["A) str()", "B) float()", "C) int()", "D) convert()"],
        "answer": "C",
        "explanation": "int() converts a compatible string or float to an integer."
    },
    {
        "q": "What is the correct way to start an if statement in Python?",
        "options": ["A) if (x > 0)", "B) if x > 0:", "C) if x > 0 then", "D) if x > 0 {"],
        "answer": "B",
        "explanation": "Python if statements use 'if condition:' with a colon and no parentheses required."
    },
    {
        "q": "What does 'print(10 / 4)' output?",
        "options": ["A) 2", "B) 2.5", "C) 3", "D) 2.0"],
        "answer": "B",
        "explanation": "/ is true division in Python 3, always returning a float. 10/4 = 2.5."
    },
    {
        "q": "Which of the following is NOT a Python built-in data type?",
        "options": ["A) list", "B) array", "C) dict", "D) tuple"],
        "answer": "B",
        "explanation": "'array' is not a built-in type; it's available via the 'array' module."
    },
    {
        "q": "What is the output of: print('abc' * 2)?",
        "options": ["A) abc2", "B) abcabc", "C) 6", "D) Error"],
        "answer": "B",
        "explanation": "String repetition: 'abc' * 2 = 'abcabc'."
    },
    {
        "q": "How do you access the first element of a list named 'items'?",
        "options": ["A) items[1]", "B) items.first()", "C) items[0]", "D) items(-1)"],
        "answer": "C",
        "explanation": "Python uses zero-based indexing, so the first element is at index 0."
    },
    {
        "q": "What keyword is used to create a loop that runs a fixed number of times?",
        "options": ["A) while", "B) repeat", "C) for", "D) loop"],
        "answer": "C",
        "explanation": "'for' loops iterate over a sequence. Use range() for a fixed number of iterations."
    },
    {
        "q": "What is the output of: print(True and False)?",
        "options": ["A) True", "B) False", "C) 1", "D) 0"],
        "answer": "B",
        "explanation": "'and' returns True only if BOTH operands are True. True and False = False."
    },
    {
        "q": "Which method adds an element to the end of a list?",
        "options": ["A) list.add()", "B) list.insert()", "C) list.append()", "D) list.push()"],
        "answer": "C",
        "explanation": "list.append(item) adds item to the end of the list."
    },
    {
        "q": "What does 'range(5)' generate?",
        "options": ["A) [1, 2, 3, 4, 5]", "B) [0, 1, 2, 3, 4]", "C) [0, 1, 2, 3, 4, 5]", "D) [1, 2, 3, 4]"],
        "answer": "B",
        "explanation": "range(5) generates numbers from 0 up to (not including) 5: 0,1,2,3,4."
    },
    {
        "q": "What is the output of: print(not True)?",
        "options": ["A) True", "B) False", "C) Not True", "D) 0"],
        "answer": "B",
        "explanation": "'not' negates a boolean. not True = False."
    },
    {
        "q": "Which keyword exits a loop prematurely?",
        "options": ["A) stop", "B) exit", "C) continue", "D) break"],
        "answer": "D",
        "explanation": "'break' immediately exits the enclosing loop."
    },
    {
        "q": "What is the output of: print(int(3.9))?",
        "options": ["A) 4", "B) 3.9", "C) 3", "D) Error"],
        "answer": "C",
        "explanation": "int() truncates (does not round) toward zero. int(3.9) = 3."
    },
    {
        "q": "How do you check if a key exists in a dictionary 'd'?",
        "options": ["A) key in d.keys()", "B) d.has(key)", "C) key in d", "D) Both A and C"],
        "answer": "D",
        "explanation": "Both 'key in d' and 'key in d.keys()' work, though 'key in d' is preferred."
    },
    {
        "q": "What is the output of: [1, 2, 3][1:]?",
        "options": ["A) [1, 2]", "B) [2, 3]", "C) [1, 2, 3]", "D) [1]"],
        "answer": "B",
        "explanation": "Slicing [1:] returns elements from index 1 to end: [2, 3]."
    },
    {
        "q": "What does the 'pass' statement do?",
        "options": ["A) Exits the function", "B) Skips the next iteration", "C) Does nothing (placeholder)", "D) Passes a value"],
        "answer": "C",
        "explanation": "'pass' is a null statement used as a placeholder where syntax requires a statement."
    },
    {
        "q": "What is the output of: print('hello'.upper())?",
        "options": ["A) HELLO", "B) Hello", "C) hello", "D) hELLO"],
        "answer": "A",
        "explanation": "str.upper() returns the string with all characters uppercased."
    },
    {
        "q": "Which operator is used for floor division?",
        "options": ["A) /", "B) %", "C) //", "D) **"],
        "answer": "C",
        "explanation": "// is the floor division operator, e.g., 7 // 2 = 3."
    },
    {
        "q": "What is printed by: print(type([]))?",
        "options": ["A) <class 'list'>", "B) <class 'array'>", "C) <class 'tuple'>", "D) <class 'dict'>"],
        "answer": "A",
        "explanation": "[] is an empty list, so type([]) returns <class 'list'>."
    },
    {
        "q": "What is the result of 'hello'[0]?",
        "options": ["A) 'e'", "B) 'h'", "C) 'hello'", "D) Error"],
        "answer": "B",
        "explanation": "Index 0 accesses the first character: 'h'."
    },
    {
        "q": "How do you create a variable with value None?",
        "options": ["A) x = null", "B) x = NULL", "C) x = None", "D) x = nil"],
        "answer": "C",
        "explanation": "Python uses 'None' (capital N) as its null value."
    },
    {
        "q": "What does 'print(round(3.567, 2))' output?",
        "options": ["A) 3.5", "B) 3.57", "C) 3.56", "D) 4.0"],
        "answer": "B",
        "explanation": "round(3.567, 2) rounds to 2 decimal places: 3.57."
    },
    {
        "q": "What is a correct way to write a multi-line string in Python?",
        "options": ["A) 'line1\\nline2'", "B) \"\"\"line1\\nline2\"\"\"", "C) Triple quotes: '''text'''", "D) All of the above"],
        "answer": "D",
        "explanation": "All three methods can represent multi-line strings in Python."
    },
    {
        "q": "Which of these creates a tuple with a single element?",
        "options": ["A) t = (1)", "B) t = (1,)", "C) t = tuple(1)", "D) t = [1]"],
        "answer": "B",
        "explanation": "A trailing comma is required for single-element tuples: (1,). (1) is just 1."
    },
    {
        "q": "What does 'elif' stand for in Python?",
        "options": ["A) else if", "B) else in loop", "C) external if", "D) end loop if"],
        "answer": "A",
        "explanation": "'elif' is shorthand for 'else if', used in chained conditional checks."
    },
    {
        "q": "What is the output of: print(max(1, 5, 3, 2))?",
        "options": ["A) 1", "B) 3", "C) 5", "D) 2"],
        "answer": "C",
        "explanation": "max() returns the largest argument: 5."
    },
    {
        "q": "How do you remove the last element from a list?",
        "options": ["A) list.remove()", "B) list.pop()", "C) list.delete()", "D) list.discard()"],
        "answer": "B",
        "explanation": "list.pop() removes and returns the last element. list.remove(x) removes first occurrence of x."
    },
    {
        "q": "What is the output of: print(abs(-7))?",
        "options": ["A) -7", "B) 7", "C) 0", "D) Error"],
        "answer": "B",
        "explanation": "abs() returns the absolute value: abs(-7) = 7."
    },
    {
        "q": "What keyword is used to return a value from a function?",
        "options": ["A) send", "B) output", "C) return", "D) yield"],
        "answer": "C",
        "explanation": "'return' exits a function and optionally sends a value back to the caller."
    },
    {
        "q": "What does 'str.strip()' do?",
        "options": [
            "A) Removes vowels",
            "B) Removes leading and trailing whitespace",
            "C) Splits the string",
            "D) Converts to uppercase"
        ],
        "answer": "B",
        "explanation": "strip() removes leading and trailing whitespace (or specified characters)."
    },
    {
        "q": "What is the output of: print(list(range(2, 6)))?",
        "options": ["A) [2, 3, 4, 5, 6]", "B) [2, 3, 4, 5]", "C) [1, 2, 3, 4, 5]", "D) [2, 4, 6]"],
        "answer": "B",
        "explanation": "range(2, 6) generates 2, 3, 4, 5 (stop is exclusive)."
    },
    {
        "q": "Which of the following is used to import a module?",
        "options": ["A) include math", "B) using math", "C) import math", "D) require math"],
        "answer": "C",
        "explanation": "'import module_name' is the standard way to import a module in Python."
    },
    {
        "q": "What does 'continue' do in a loop?",
        "options": [
            "A) Exits the loop",
            "B) Ends the program",
            "C) Skips to the next iteration",
            "D) Pauses the loop"
        ],
        "answer": "C",
        "explanation": "'continue' skips the rest of the current iteration and moves to the next one."
    },
    {
        "q": "What is the output of: print(sorted([3,1,4,1,5]))?",
        "options": ["A) [1, 1, 3, 4, 5]", "B) [3, 1, 4, 1, 5]", "C) [5, 4, 3, 1, 1]", "D) [1, 3, 4, 5]"],
        "answer": "A",
        "explanation": "sorted() returns a new sorted list in ascending order."
    },
    {
        "q": "What is the result of '5' == 5 in Python?",
        "options": ["A) True", "B) False", "C) Error", "D) None"],
        "answer": "B",
        "explanation": "== checks value AND type. '5' is a string and 5 is an int, so they are not equal."
    },
    {
        "q": "Which built-in function returns the number of items in an object?",
        "options": ["A) size()", "B) count()", "C) length()", "D) len()"],
        "answer": "D",
        "explanation": "len() is Python's built-in function for getting the length/size of an object."
    },
    {
        "q": "What does 'x += 5' mean?",
        "options": ["A) x = x - 5", "B) x = x * 5", "C) x = x + 5", "D) x = 5"],
        "answer": "C",
        "explanation": "+= is the augmented addition operator: x += 5 is shorthand for x = x + 5."
    },
    {
        "q": "What is the output of print(bool('')) ?",
        "options": ["A) True", "B) False", "C) ''", "D) Error"],
        "answer": "B",
        "explanation": "An empty string is falsy in Python, so bool('') is False."
    },
    {
        "q": "What does the 'in' operator do when used with a list?",
        "options": [
            "A) Adds an item to the list",
            "B) Checks if an item exists in the list",
            "C) Removes an item from the list",
            "D) Counts occurrences of an item"
        ],
        "answer": "B",
        "explanation": "'x in list' returns True if x is found in the list, False otherwise."
    },
    {
        "q": "What is the output of: print('Python'[-1])?",
        "options": ["A) 'P'", "B) 'n'", "C) 'o'", "D) Error"],
        "answer": "B",
        "explanation": "Negative indexing: -1 refers to the last character. 'Python'[-1] = 'n'."
    },
]


def run_exam(questions, title="EASY"):
    print("=" * 60)
    print(f"  PCAP-31-03 MOCK EXAM — {title} DIFFICULTY")
    print(f"  {len(questions)} Questions | Time Limit: 40 minutes")
    print("=" * 60)
    print("\nInstructions: Enter A, B, C, or D for each answer.")
    print("Type 'q' at any time to quit and see your score.\n")
    input("Press ENTER to begin...")
    print()

    score = 0
    wrong = []
    start_time = time.time()

    for i, item in enumerate(questions, 1):
        print(f"Q{i}/{len(questions)}: {item['q']}")
        for opt in item["options"]:
            print(f"  {opt}")
        while True:
            ans = input("Your answer: ").strip().upper()
            if ans == "Q":
                print("\n--- Exam terminated early ---")
                break
            if ans in ("A", "B", "C", "D"):
                break
            print("  Invalid input. Please enter A, B, C, or D.")

        if ans == "Q":
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
    answered = i  # last index
    print(f"  Score    : {score} / {answered}")
    percent = (score / answered * 100) if answered else 0
    print(f"  Percent  : {percent:.1f}%")
    print(f"  Time     : {mins}m {secs}s")
    status = "PASS ✔" if percent >= 70 else "FAIL ✘"
    print(f"  Status   : {status}  (passing = 70%)")

    if wrong:
        print(f"\n  Questions you missed ({len(wrong)}):")
        for num, item in wrong:
            print(f"  Q{num}: {item['q'][:60]}...")
            print(f"        Correct: {item['answer']} — {item['explanation']}")
    print("=" * 60)


if __name__ == "__main__":
    q_list = QUESTIONS.copy()
    random.shuffle(q_list)
    run_exam(q_list, title="EASY")