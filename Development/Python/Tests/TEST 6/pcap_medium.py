"""
PCAP-31-03 Mock Exam - MEDIUM (50 Questions)
Behavior-focused questions across the core PCAP topics.
"""

import time

QUESTIONS = [
    # -- MODULES & PACKAGES --
    {
        "topic": "Modules & Packages",
        "q": (
            "What does this print?\n\n"
            "    import math\n"
            "    math.pi = 0\n"
            "    import math\n"
            "    print(math.pi)"
        ),
        "options": ["A) 3.141592653589793", "B) 0", "C) AttributeError", "D) ImportError"],
        "answer": "B",
        "explanation": "Modules are cached in sys.modules. Re-importing returns the same object with pi = 0."
    },
    {
        "topic": "Modules & Packages",
        "q": (
            "How many times does a module's top-level code run if it is imported "
            "in multiple files during one program execution?"
        ),
        "options": ["A) Once", "B) Every time it is imported", "C) Zero times", "D) Depends on __all__"],
        "answer": "A",
        "explanation": "A module is executed once, then cached in sys.modules."
    },
    {
        "topic": "Modules & Packages",
        "q": (
            "What does this print?\n\n"
            "    import random\n"
            "    random.seed(7)\n"
            "    a = random.random()\n"
            "    random.seed(7)\n"
            "    b = random.random()\n"
            "    print(a == b)"
        ),
        "options": ["A) False", "B) True", "C) TypeError", "D) None"],
        "answer": "B",
        "explanation": "The same seed produces the same sequence, so a == b is True."
    },
    {
        "topic": "Modules & Packages",
        "q": "What does importlib.util.find_spec('missing_module') return?",
        "options": ["A) False", "B) None", "C) ModuleNotFoundError", "D) An empty ModuleSpec"],
        "answer": "B",
        "explanation": "find_spec returns None when it cannot locate the module."
    },
    {
        "topic": "Modules & Packages",
        "q": "What does a single leading dot mean in a relative import?",
        "options": ["A) Import from the current package", "B) Import from the parent package", "C) Import from site-packages", "D) SyntaxError"],
        "answer": "A",
        "explanation": "One dot refers to the current package."
    },
    {
        "topic": "Modules & Packages",
        "q": "What does sys.path.insert(0, '/tmp') do?",
        "options": ["A) Removes /tmp", "B) Makes /tmp the first directory searched for imports", "C) Permanently edits PATH", "D) Imports /tmp automatically"],
        "answer": "B",
        "explanation": "Inserting at index 0 gives /tmp highest import priority for the process."
    },
    {
        "topic": "Modules & Packages",
        "q": "What is __name__ inside a module run with 'python -m package.mod'?",
        "options": ["A) package.mod", "B) '__main__'", "C) None", "D) 'mod'"],
        "answer": "B",
        "explanation": "The executed module becomes __main__."
    },
    {
        "topic": "Modules & Packages",
        "q": "What does this return?\n\n    import math\n    math.sqrt(9)",
        "options": ["A) 3", "B) 3.0", "C) 9", "D) 81"],
        "answer": "B",
        "explanation": "math.sqrt returns a float. sqrt(9) is 3.0."
    },
    {
        "topic": "Modules & Packages",
        "q": "Which statement imports only the name 'path' from os?",
        "options": ["A) import os.path", "B) from os import path", "C) import path from os", "D) from os.path import os"],
        "answer": "B",
        "explanation": "from os import path imports the path name directly."
    },
    {
        "topic": "Modules & Packages",
        "q": "What does sys.modules store?",
        "options": ["A) The current PATH", "B) A cache of imported modules", "C) The list of packages on disk", "D) The Python version"],
        "answer": "B",
        "explanation": "sys.modules maps module names to module objects already loaded."
    },

    # -- OOP --
    {
        "topic": "OOP",
        "q": (
            "What does this print?\n\n"
            "    class Dog:\n"
            "        legs = 4\n"
            "    d = Dog()\n"
            "    d.legs = 3\n"
            "    print(Dog.legs, d.legs)"
        ),
        "options": ["A) 3 3", "B) 4 3", "C) 4 4", "D) 3 4"],
        "answer": "B",
        "explanation": "d.legs creates an instance attribute that shadows the class attribute."
    },
    {
        "topic": "OOP",
        "q": "What does name-mangling do to __secret inside class Foo?",
        "options": ["A) It deletes it", "B) It renames it to _Foo__secret", "C) It makes it global", "D) It changes it to __secret__"],
        "answer": "B",
        "explanation": "__secret becomes _Foo__secret."
    },
    {
        "topic": "OOP",
        "q": (
            "What is the MRO of D?\n\n"
            "    class A: pass\n"
            "    class B(A): pass\n"
            "    class C(A): pass\n"
            "    class D(B, C): pass"
        ),
        "options": ["A) D, B, C, A, object", "B) D, C, B, A, object", "C) D, A, B, C, object", "D) D, B, A, C, object"],
        "answer": "A",
        "explanation": "C3 linearization preserves left-to-right order: D -> B -> C -> A -> object."
    },
    {
        "topic": "OOP",
        "q": "What does @property do?",
        "options": ["A) Makes a method static", "B) Exposes a method as an attribute", "C) Makes a class immutable", "D) Hides the method"],
        "answer": "B",
        "explanation": "@property lets you access a method like an attribute."
    },
    {
        "topic": "OOP",
        "q": (
            "What does this print?\n\n"
            "    class A:\n"
            "        def greet(self): return 'A'\n"
            "    class B(A):\n"
            "        def greet(self): return 'B' + super().greet()\n"
            "    print(B().greet())"
        ),
        "options": ["A) A", "B) BA", "C) B", "D) AB"],
        "answer": "B",
        "explanation": "super().greet() returns 'A', so result is 'BA'."
    },
    {
        "topic": "OOP",
        "q": "What is the first argument of a @classmethod?",
        "options": ["A) self", "B) cls", "C) args", "D) None"],
        "answer": "B",
        "explanation": "@classmethod receives the class as cls."
    },
    {
        "topic": "OOP",
        "q": "Which statement about @staticmethod is correct?",
        "options": ["A) It receives self", "B) It receives cls", "C) It receives no automatic first arg", "D) It becomes a property"],
        "answer": "C",
        "explanation": "@staticmethod attaches a plain function to the class."
    },
    {
        "topic": "OOP",
        "q": (
            "What does this print?\n\n"
            "    class X:\n"
            "        def __str__(self): return 'str'\n"
            "        def __repr__(self): return 'repr'\n"
            "    print([X()])"
        ),
        "options": ["A) [str]", "B) [repr]", "C) str", "D) repr"],
        "answer": "B",
        "explanation": "Containers use __repr__ for their elements."
    },
    {
        "topic": "OOP",
        "q": "What does vars(obj) return?",
        "options": ["A) A list of methods", "B) obj.__dict__", "C) The class name", "D) The MRO"],
        "answer": "B",
        "explanation": "vars(obj) returns the instance attribute dict."
    },
    {
        "topic": "OOP",
        "q": "What does issubclass(bool, int) return?",
        "options": ["A) True", "B) False", "C) TypeError", "D) None"],
        "answer": "A",
        "explanation": "bool is a subclass of int in Python."
    },

    # -- EXCEPTIONS --
    {
        "topic": "Exceptions",
        "q": (
            "What does this print?\n\n"
            "    try:\n"
            "        pass\n"
            "    except Exception:\n"
            "        print('except')\n"
            "    else:\n"
            "        print('else')\n"
            "    finally:\n"
            "        print('finally')"
        ),
        "options": ["A) except then finally", "B) else then finally", "C) only finally", "D) except only"],
        "answer": "B",
        "explanation": "No exception: else runs, then finally."
    },
    {
        "topic": "Exceptions",
        "q": "What does 'raise NewError() from None' do?",
        "options": ["A) Chains the error", "B) Suppresses the original exception context", "C) Raises None", "D) SyntaxError"],
        "answer": "B",
        "explanation": "from None suppresses exception chaining."
    },
    {
        "topic": "Exceptions",
        "q": "What is e.args after: raise ValueError('bad', 1)?",
        "options": ["A) ('bad', 1)", "B) 'bad'", "C) (1,)", "D) []"],
        "answer": "A",
        "explanation": "All constructor args are stored as a tuple in e.args."
    },
    {
        "topic": "Exceptions",
        "q": "Which two exceptions are NOT caught by except Exception?",
        "options": ["A) ValueError and TypeError", "B) SystemExit and KeyboardInterrupt", "C) OSError and RuntimeError", "D) KeyError and IndexError"],
        "answer": "B",
        "explanation": "SystemExit and KeyboardInterrupt inherit from BaseException directly."
    },
    {
        "topic": "Exceptions",
        "q": "Why should assert not be used for input validation?",
        "options": ["A) It is too slow", "B) It is removed with -O", "C) It only works in classes", "D) It logs to stderr"],
        "answer": "B",
        "explanation": "Assertions are stripped when Python runs with -O."
    },
    {
        "topic": "Exceptions",
        "q": "Which handler should come first?",
        "options": ["A) except OSError then except FileNotFoundError", "B) except FileNotFoundError then except OSError", "C) Either order is fine", "D) They cannot be combined"],
        "answer": "B",
        "explanation": "Catch the more specific subclass first."
    },
    {
        "topic": "Exceptions",
        "q": (
            "What happens here?\n\n"
            "    try:\n"
            "        raise ValueError('x')\n"
            "    except ValueError:\n"
            "        print('caught')\n"
            "        raise"
        ),
        "options": ["A) Only 'caught'", "B) 'caught' then ValueError propagates", "C) ValueError is silenced", "D) SyntaxError"],
        "answer": "B",
        "explanation": "A bare raise re-raises the same exception."
    },
    {
        "topic": "Exceptions",
        "q": "What does super().__init__(msg) do in a custom exception?",
        "options": ["A) It logs the message", "B) It stores the message in args for display", "C) It silences the exception", "D) It sets errno"],
        "answer": "B",
        "explanation": "The message becomes part of the exception's string representation."
    },
    {
        "topic": "Exceptions",
        "q": (
            "What does this return?\n\n"
            "    def f():\n"
            "        try:\n"
            "            return 1\n"
            "        finally:\n"
            "            return 2\n"
            "    f()"
        ),
        "options": ["A) 1", "B) 2", "C) (1, 2)", "D) None"],
        "answer": "B",
        "explanation": "A return in finally overrides the try return."
    },
    {
        "topic": "Exceptions",
        "q": "What happens to the exception variable after an except block?",
        "options": ["A) It remains defined", "B) It becomes None", "C) It is deleted", "D) It becomes a string"],
        "answer": "C",
        "explanation": "Python deletes the name to break reference cycles."
    },

    # -- FILE I/O --
    {
        "topic": "File I/O",
        "q": (
            "What does this print?\n\n"
            "    with open('a.txt', 'w') as f:\n"
            "        f.write('hello')\n"
            "    with open('a.txt', 'w') as f:\n"
            "        f.write('world')\n"
            "    with open('a.txt') as f:\n"
            "        print(f.read())"
        ),
        "options": ["A) helloworld", "B) hello", "C) world", "D) FileNotFoundError"],
        "answer": "C",
        "explanation": "The second 'w' truncates the file before writing."
    },
    {
        "topic": "File I/O",
        "q": "What does f.seek(0, 2) do?",
        "options": ["A) Moves to start", "B) Moves to end", "C) Moves 2 bytes from current", "D) Raises error"],
        "answer": "B",
        "explanation": "seek(0, 2) moves the cursor to the end of the file."
    },
    {
        "topic": "File I/O",
        "q": "What does f.tell() return?",
        "options": ["A) The file size", "B) Current cursor position", "C) The line count", "D) The encoding"],
        "answer": "B",
        "explanation": "tell() returns the current byte position."
    },
    {
        "topic": "File I/O",
        "q": "Which mode raises FileExistsError if the file exists?",
        "options": ["A) 'w'", "B) 'a'", "C) 'x'", "D) 'r+'"],
        "answer": "C",
        "explanation": "'x' is exclusive creation mode."
    },
    {
        "topic": "File I/O",
        "q": "Why specify encoding='utf-8' when opening text files?",
        "options": ["A) It is faster", "B) Defaults vary by OS", "C) It forces binary", "D) It disables errors"],
        "answer": "B",
        "explanation": "Explicit encoding ensures consistent behavior across platforms."
    },
    {
        "topic": "File I/O",
        "q": "What does 'for line in f:' do?",
        "options": ["A) Reads one line at a time", "B) Reads all lines into memory", "C) Reads one char", "D) Raises TypeError"],
        "answer": "A",
        "explanation": "File objects are iterators over lines."
    },
    {
        "topic": "File I/O",
        "q": "What does io.StringIO() create?",
        "options": ["A) A binary file", "B) An in-memory text stream", "C) A socket", "D) A temp file"],
        "answer": "B",
        "explanation": "StringIO provides a file-like text buffer in memory."
    },
    {
        "topic": "File I/O",
        "q": "What does f.readinto(buf) do?",
        "options": ["A) Returns a new bytes object", "B) Reads into a pre-allocated buffer", "C) Reads only text", "D) Writes to disk"],
        "answer": "B",
        "explanation": "readinto fills an existing buffer and avoids extra allocations."
    },
    {
        "topic": "File I/O",
        "q": (
            "What does this print?\n\n"
            "    with open('f.txt','w') as f:\n"
            "        f.write('abcde')\n"
            "    with open('f.txt','r+') as f:\n"
            "        f.seek(2)\n"
            "        f.write('XY')\n"
            "        f.seek(0)\n"
            "        print(f.read())"
        ),
        "options": ["A) XYcde", "B) abXYe", "C) abcde", "D) XYabcde"],
        "answer": "B",
        "explanation": "r+ overwrites in place at position 2, producing abXYe."
    },
    {
        "topic": "File I/O",
        "q": "What happens to writes in 'a' mode after seek(0)?",
        "options": ["A) Writes go to the cursor", "B) Writes still go to the end", "C) The file is truncated", "D) seek() fails"],
        "answer": "B",
        "explanation": "Append mode forces writes to the end regardless of seek."
    },

    # -- COMPREHENSIONS & LAMBDAS --
    {
        "topic": "Comprehensions & Lambdas",
        "q": "What does [(x, y) for x in range(2) for y in range(2)] produce?",
        "options": ["A) [(0,0), (1,1)]", "B) [(0,0), (0,1), (1,0), (1,1)]", "C) [(0,1), (1,0)]", "D) SyntaxError"],
        "answer": "B",
        "explanation": "Nested loops generate all pairs in order."
    },
    {
        "topic": "Comprehensions & Lambdas",
        "q": "What is the difference between [x for x in data] and (x for x in data)?",
        "options": ["A) No difference", "B) List vs generator", "C) Tuple vs list", "D) Generator vs set"],
        "answer": "B",
        "explanation": "Square brackets create a list; parentheses create a generator."
    },
    {
        "topic": "Comprehensions & Lambdas",
        "q": "What does list(map(lambda x, y: x + y, [1,2], [10,20])) return?",
        "options": ["A) [11, 22]", "B) [1,2,10,20]", "C) [10, 20]", "D) TypeError"],
        "answer": "A",
        "explanation": "map zips the two lists and adds element pairs."
    },
    {
        "topic": "Comprehensions & Lambdas",
        "q": "What does list(filter(None, ['a', '', 'b'])) return?",
        "options": ["A) ['', '']", "B) ['a', 'b']", "C) ['a', '', 'b']", "D) TypeError"],
        "answer": "B",
        "explanation": "filter(None, ...) removes falsy values like ''."
    },
    {
        "topic": "Comprehensions & Lambdas",
        "q": "What does sorted(['aa','b','ccc'], key=len) return?",
        "options": ["A) ['aa', 'b', 'ccc']", "B) ['b', 'aa', 'ccc']", "C) ['ccc', 'aa', 'b']", "D) ['b', 'ccc', 'aa']"],
        "answer": "B",
        "explanation": "Sorting by length gives b (1), aa (2), ccc (3)."
    },

    # -- CLOSURES --
    {
        "topic": "Closures",
        "q": (
            "What does this print?\n\n"
            "    def outer():\n"
            "        x = 10\n"
            "        def inner():\n"
            "            print(x)\n"
            "        inner()\n"
            "    outer()"
        ),
        "options": ["A) 10", "B) NameError", "C) UnboundLocalError", "D) 0"],
        "answer": "A",
        "explanation": "inner reads the captured variable x from outer."
    },
    {
        "topic": "Closures",
        "q": (
            "What does this print?\n\n"
            "    def outer():\n"
            "        x = 10\n"
            "        def inner():\n"
            "            nonlocal x\n"
            "            x = 99\n"
            "        inner()\n"
            "        print(x)\n"
            "    outer()"
        ),
        "options": ["A) 10", "B) 99", "C) NameError", "D) UnboundLocalError"],
        "answer": "B",
        "explanation": "nonlocal allows inner to modify outer's x."
    },
    {
        "topic": "Closures",
        "q": (
            "What does make_adder(5)(3) return?\n\n"
            "    def make_adder(n):\n"
            "        def add(x):\n"
            "            return x + n\n"
            "        return add"
        ),
        "options": ["A) 5", "B) 3", "C) 8", "D) 15"],
        "answer": "C",
        "explanation": "The closure captures n=5, so add(3) returns 8."
    },
    {
        "topic": "Closures",
        "q": "What does closure.__closure__[0].cell_contents give you?",
        "options": ["A) The function name", "B) The captured variable value", "C) The source code", "D) The argument list"],
        "answer": "B",
        "explanation": "It reveals the current value of a captured variable."
    },
    {
        "topic": "Closures",
        "q": (
            "What does this print?\n\n"
            "    def make_counter():\n"
            "        count = 0\n"
            "        def inc():\n"
            "            nonlocal count\n"
            "            count += 1\n"
            "            return count\n"
            "        return inc\n"
            "    c1 = make_counter()\n"
            "    c2 = make_counter()\n"
            "    print(c1(), c1(), c2())"
        ),
        "options": ["A) 1 2 3", "B) 1 2 1", "C) 1 1 1", "D) 2 2 2"],
        "answer": "B",
        "explanation": "Each closure has its own count. c1 increments twice; c2 starts fresh."
    },
]


def run_exam():
    print("=" * 65)
    print("  PCAP-31-03 MOCK EXAM - MEDIUM LEVEL")
    print("  50 Questions | Pass mark: 70% (35/50)")
    print("  Tip: read code snippets carefully before answering.")
    print("=" * 65)
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

        print("-" * 65)

    elapsed = time.time() - start
    minutes, seconds = divmod(int(elapsed), 60)

    print()
    print("=" * 65)
    print("  RESULTS")
    print("=" * 65)
    print(f"  Score      : {score} / 50  ({score * 2}%)")
    print(f"  Time taken : {minutes}m {seconds}s")
    print(f"  Pass mark  : 35 / 50  (70%)")
    passed = score >= 35
    print(f"  Result     : {'PASS' if passed else 'FAIL'}")
    print()

    if wrong_list:
        print(f"  Review - questions you missed ({len(wrong_list)}):")
        for num, q in wrong_list:
            first_line = q["q"].split("\n")[0][:55]
            print(f"    Q{num:02d} [{q['topic']}]: {first_line}...")
            print(f"         Correct: {q['answer']} - {q['explanation']}")
            print()

    print("=" * 65)


if __name__ == "__main__":
    run_exam()
