"""
PCAP-31-03 Mock Exam — MEDIUM (50 Questions)
Topics: Modules, OOP, Exceptions, File I/O, Comprehensions, Lambdas, Closures
Questions require understanding of behaviour, not just definitions.
"""

import time

QUESTIONS = [
    # ── MODULES & PACKAGES ──────────────────────────────────────────────────
    {
        "topic": "Modules & Packages",
        "q": (
            "What does this print?\n\n"
            "    import math as m\n"
            "    print(m.floor(3.9))"
        ),
        "options": ["A) 3.9", "B) 4", "C) 3", "D) NameError"],
        "answer": "C",
        "explanation": "math.floor() rounds down toward -inf. floor(3.9) = 3. The alias 'm' works fine."
    },
    {
        "topic": "Modules & Packages",
        "q": (
            "How many times does a module's top-level code run if it is imported "
            "in three different files during the same program execution?"
        ),
        "options": ["A) Three times", "B) Zero — module code never auto-runs", "C) Once", "D) It depends on __all__"],
        "answer": "C",
        "explanation": "Python caches modules in sys.modules after the first import. Subsequent imports return the cached object."
    },
    {
        "topic": "Modules & Packages",
        "q": (
            "What does this print?\n\n"
            "    import sys, math\n"
            "    print(math is sys.modules['math'])"
        ),
        "options": ["A) False", "B) True", "C) AttributeError", "D) None"],
        "answer": "B",
        "explanation": "sys.modules caches every imported module. Both 'math' and sys.modules['math'] are the same object — 'is' returns True."
    },
    {
        "topic": "Modules & Packages",
        "q": "What does importlib.util.find_spec('nonexistent') return?",
        "options": ["A) False", "B) An empty ModuleSpec", "C) None", "D) ModuleNotFoundError"],
        "answer": "C",
        "explanation": "find_spec() returns None if the module cannot be located, without raising an exception."
    },
    {
        "topic": "Modules & Packages",
        "q": (
            "What does this print?\n\n"
            "    from math import pi as PI, ceil\n"
            "    print(round(PI, 2), ceil(2.1))"
        ),
        "options": ["A) SyntaxError", "B) 3.14 3", "C) 3.14 2", "D) 3.141592653589793 3"],
        "answer": "B",
        "explanation": "round(pi,2) = 3.14. ceil(2.1) rounds up to 3. Multiple imports with 'as' aliases in one from-import are valid."
    },
    {
        "topic": "Modules & Packages",
        "q": "What does 'python -B script.py' do?",
        "options": [
            "A) Runs in debug mode",
            "B) Blocks all network access",
            "C) Prevents writing .pyc bytecode files",
            "D) Runs with optimisation — strips assert"
        ],
        "answer": "C",
        "explanation": "-B sets PYTHONDONTWRITEBYTECODE, suppressing creation of .pyc files in __pycache__."
    },
    {
        "topic": "Modules & Packages",
        "q": (
            "Which function from pkgutil lists ONLY the immediate submodules "
            "of a package (not recursive)?"
        ),
        "options": ["A) pkgutil.walk_packages()", "B) pkgutil.find_modules()", "C) pkgutil.list_modules()", "D) pkgutil.iter_modules()"],
        "answer": "D",
        "explanation": "iter_modules(path) yields one level of submodules. walk_packages() descends recursively."
    },
    {
        "topic": "Modules & Packages",
        "q": "What does a double leading dot mean in a relative import (e.g. from .. import x)?",
        "options": ["A) Import from the current package", "B) Import from the parent package", "C) Import from site-packages", "D) SyntaxError"],
        "answer": "B",
        "explanation": "One dot = current package. Two dots = parent package. Three = grandparent, etc."
    },
    {
        "topic": "Modules & Packages",
        "q": "What is the type of sys.path?",
        "options": ["A) tuple", "B) dict", "C) set", "D) list"],
        "answer": "D",
        "explanation": "sys.path is a list of strings. Because it's a list you can insert or append paths at runtime."
    },
    {
        "topic": "Modules & Packages",
        "q": (
            "What does this print?\n\n"
            "    import random\n"
            "    random.seed(42)\n"
            "    a = random.random()\n"
            "    random.seed(42)\n"
            "    b = random.random()\n"
            "    print(a == b)"
        ),
        "options": ["A) False", "B) TypeError", "C) True", "D) None"],
        "answer": "C",
        "explanation": "The same seed produces the same sequence. Both a and b will be 0.6394..., so a == b is True."
    },

    # ── OOP ─────────────────────────────────────────────────────────────────
    {
        "topic": "OOP",
        "q": (
            "What does this print?\n\n"
            "    class Dog:\n"
            "        legs = 4\n"
            "        def __init__(self, name):\n"
            "            self.name = name\n"
            "    d = Dog('Rex')\n"
            "    d.legs = 3\n"
            "    print(Dog.legs, d.legs)"
        ),
        "options": ["A) 3 3", "B) 4 4", "C) 4 3", "D) AttributeError"],
        "answer": "C",
        "explanation": "d.legs = 3 creates an instance variable that shadows the class variable for d only. Dog.legs stays 4."
    },
    {
        "topic": "OOP",
        "q": "What does name mangling do to self.__secret inside class Foo?",
        "options": [
            "A) Makes it completely inaccessible",
            "B) Renames it to __secret__",
            "C) Deletes it at runtime",
            "D) Renames it to _Foo__secret"
        ],
        "answer": "D",
        "explanation": "Python rewrites __attr to _ClassName__attr at compile time to prevent accidental override in subclasses."
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
        "options": [
            "A) D → A → B → C → object",
            "B) D → C → B → A → object",
            "C) D → B → C → A → object",
            "D) D → A → C → B → object"
        ],
        "answer": "C",
        "explanation": "C3 linearisation: D → B → C → A → object. Left-to-right parent order is respected."
    },
    {
        "topic": "OOP",
        "q": (
            "What does this print?\n\n"
            "    class Animal:\n"
            "        def speak(self): return 'sound'\n"
            "    class Dog(Animal):\n"
            "        def speak(self): return 'woof'\n"
            "    print(Dog().speak())"
        ),
        "options": ["A) sound", "B) woof", "C) AttributeError", "D) None"],
        "answer": "B",
        "explanation": "Dog overrides Animal's speak(). The child's version takes precedence."
    },
    {
        "topic": "OOP",
        "q": "What does @classmethod decorate and what is its first parameter?",
        "options": [
            "A) An instance method; self",
            "B) A static function; nothing",
            "C) A method bound to the class; cls",
            "D) A property; self"
        ],
        "answer": "C",
        "explanation": "@classmethod methods receive the class (cls) as their first argument, not the instance."
    },
    {
        "topic": "OOP",
        "q": "What does @staticmethod create?",
        "options": [
            "A) A method bound to the instance",
            "B) A method bound to the class",
            "C) A plain function inside the class with no automatic first argument",
            "D) A read-only class attribute"
        ],
        "answer": "C",
        "explanation": "@staticmethod attaches a regular function to the class. It receives neither self nor cls automatically."
    },
    {
        "topic": "OOP",
        "q": (
            "What does this print?\n\n"
            "    class A:\n"
            "        def greet(self): return 'A'\n"
            "    class B(A):\n"
            "        def greet(self): return 'B+' + super().greet()\n"
            "    print(B().greet())"
        ),
        "options": ["A) A", "B) B+A", "C) B", "D) TypeError"],
        "answer": "B",
        "explanation": "B.greet() calls super().greet() which finds A.greet(). 'B+' + 'A' = 'B+A'."
    },
    {
        "topic": "OOP",
        "q": "What does issubclass(Dog, Animal) return if Dog inherits from Animal?",
        "options": ["A) False", "B) The Dog class", "C) None", "D) True"],
        "answer": "D",
        "explanation": "issubclass(A, B) returns True if A is B or derives from B. A class is also considered a subclass of itself."
    },
    {
        "topic": "OOP",
        "q": "What does vars(obj) return?",
        "options": [
            "A) All attribute names including inherited",
            "B) obj.__dict__ — the instance's own attribute dictionary",
            "C) A list of method names",
            "D) The type of obj"
        ],
        "answer": "B",
        "explanation": "vars(obj) is equivalent to obj.__dict__ — it shows only the instance's own attributes, not class-level ones."
    },
    {
        "topic": "OOP",
        "q": (
            "What attribute holds the tuple of a class's DIRECT parent classes?\n\n"
            "    class Foo(Bar, Baz): pass"
        ),
        "options": ["A) Foo.__mro__", "B) Foo.__parents__", "C) Foo.__super__", "D) Foo.__bases__"],
        "answer": "D",
        "explanation": "__bases__ is a tuple of direct parent classes. __mro__ is the full resolution order including all ancestors."
    },

    # ── EXCEPTIONS ──────────────────────────────────────────────────────────
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
        "options": ["A) except then finally", "B) Only finally", "C) else then finally", "D) except then else then finally"],
        "answer": "C",
        "explanation": "No exception → except is skipped, else runs, finally always runs."
    },
    {
        "topic": "Exceptions",
        "q": "What is the effect of 'raise NewError() from None'?",
        "options": [
            "A) Chains NewError to the current exception",
            "B) Raises NewError without any exception context (suppresses chaining)",
            "C) SyntaxError — 'from None' is invalid",
            "D) Raises None instead of NewError"
        ],
        "answer": "B",
        "explanation": "'from None' sets __cause__ to None and __suppress_context__ to True, hiding the original exception."
    },
    {
        "topic": "Exceptions",
        "q": "What does e.args contain after: raise ValueError('bad', 42)?",
        "options": ["A) 'bad'", "B) ('bad', 42)", "C) ['bad', 42]", "D) {'msg': 'bad', 'code': 42}"],
        "answer": "B",
        "explanation": "All constructor arguments are stored as a tuple in e.args."
    },
    {
        "topic": "Exceptions",
        "q": (
            "Which exceptions does 'except Exception' NOT catch?\n"
            "(Choose the correct pair.)"
        ),
        "options": [
            "A) ValueError and TypeError",
            "B) OSError and RuntimeError",
            "C) SystemExit and KeyboardInterrupt",
            "D) AttributeError and NameError"
        ],
        "answer": "C",
        "explanation": "SystemExit and KeyboardInterrupt inherit from BaseException directly, not from Exception."
    },
    {
        "topic": "Exceptions",
        "q": (
            "What does this output?\n\n"
            "    try:\n"
            "        raise ValueError('oops')\n"
            "    except ValueError:\n"
            "        print('caught')\n"
            "        raise"
        ),
        "options": [
            "A) caught — then execution continues normally",
            "B) caught — then ValueError propagates up",
            "C) Only 'caught'",
            "D) ValueError is silenced"
        ],
        "answer": "B",
        "explanation": "Bare 'raise' inside except re-raises the same exception. 'caught' is printed, then ValueError propagates."
    },
    {
        "topic": "Exceptions",
        "q": "What assertion does 'assert x > 0, \"x must be positive\"' check, and what does it raise if it fails?",
        "options": [
            "A) Checks x > 0; raises ValueError",
            "B) Checks x > 0; raises AssertionError with the message",
            "C) Always raises AssertionError",
            "D) Raises RuntimeError"
        ],
        "answer": "B",
        "explanation": "assert condition, message — if condition is False, raises AssertionError with the given message."
    },
    {
        "topic": "Exceptions",
        "q": "What is the correct order to catch FileNotFoundError and OSError?",
        "options": [
            "A) OSError first, then FileNotFoundError",
            "B) Either order — it doesn't matter",
            "C) FileNotFoundError first, then OSError",
            "D) They cannot be caught together"
        ],
        "answer": "C",
        "explanation": "Most specific first. FileNotFoundError is a subclass of OSError. If OSError came first it would always match."
    },
    {
        "topic": "Exceptions",
        "q": "What does super().__init__(message) do inside a custom exception's __init__?",
        "options": [
            "A) Calls the built-in print function",
            "B) Creates a new instance of Exception",
            "C) Sets the string representation so str(e) and tracebacks display the message",
            "D) Silences the exception"
        ],
        "answer": "C",
        "explanation": "Calling super().__init__(message) stores the message in self.args and controls how the exception displays."
    },
    {
        "topic": "Exceptions",
        "q": "Why should assert NOT be used for input validation or security checks?",
        "options": [
            "A) It is too slow",
            "B) It only works inside classes",
            "C) assert statements are stripped when Python runs with -O (optimise)",
            "D) It raises the wrong exception type"
        ],
        "answer": "C",
        "explanation": "python -O removes all assert statements. Code relying on assert for security silently loses those checks."
    },
    {
        "topic": "Exceptions",
        "q": "What is the errno value for 'No such file or directory'?",
        "options": ["A) 1", "B) 13", "C) 28", "D) 2"],
        "answer": "D",
        "explanation": "errno.ENOENT = 2 (No such file or directory). errno.EACCES = 13 (Permission denied). errno.ENOSPC = 28 (No space)."
    },

    # ── FILE I/O ─────────────────────────────────────────────────────────────
    {
        "topic": "File I/O",
        "q": (
            "What does this code produce?\n\n"
            "    with open('a.txt', 'w') as f:\n"
            "        f.write('hello')\n"
            "    with open('a.txt', 'w') as f:\n"
            "        f.write('world')\n"
            "    with open('a.txt') as f:\n"
            "        print(f.read())"
        ),
        "options": ["A) helloworld", "B) hello", "C) world", "D) FileNotFoundError"],
        "answer": "C",
        "explanation": "Mode 'w' truncates the file each time. The second write erases 'hello', leaving only 'world'."
    },
    {
        "topic": "File I/O",
        "q": "What does f.seek(0, 2) do?",
        "options": [
            "A) Moves cursor 2 bytes from current position",
            "B) Seeks to byte 2",
            "C) Moves cursor to the end of the file",
            "D) Rewinds to the beginning"
        ],
        "answer": "C",
        "explanation": "seek(offset, whence): whence=0=start, 1=current, 2=end. seek(0, 2) moves to 0 bytes from the end."
    },
    {
        "topic": "File I/O",
        "q": "What does f.tell() return?",
        "options": [
            "A) The total file size",
            "B) The current cursor position as an integer",
            "C) The number of lines remaining",
            "D) The encoding name"
        ],
        "answer": "B",
        "explanation": "tell() returns the current byte position of the file cursor."
    },
    {
        "topic": "File I/O",
        "q": "What is the key difference between bytes and bytearray?",
        "options": [
            "A) bytes stores text; bytearray stores numbers",
            "B) bytes is immutable; bytearray is mutable",
            "C) bytearray can only be used in binary mode",
            "D) bytes is faster to write to disk"
        ],
        "answer": "B",
        "explanation": "bytes is immutable like str. bytearray is mutable — individual bytes can be changed in place."
    },
    {
        "topic": "File I/O",
        "q": "Which file mode raises FileExistsError if the file already exists?",
        "options": ["A) 'w'", "B) 'a'", "C) 'r+'", "D) 'x'"],
        "answer": "D",
        "explanation": "'x' (exclusive creation) fails with FileExistsError if the file is already present."
    },
    {
        "topic": "File I/O",
        "q": "Why should you always specify encoding='utf-8' when opening a text file?",
        "options": [
            "A) It makes reading faster",
            "B) Without it, Python uses the system default which differs across platforms",
            "C) UTF-8 is the only encoding Python supports",
            "D) It prevents binary files from being opened as text"
        ],
        "answer": "B",
        "explanation": "Windows defaults to cp1252; Linux to utf-8. Hardcoding utf-8 ensures consistent cross-platform behaviour."
    },
    {
        "topic": "File I/O",
        "q": "What is sys.stderr used for?",
        "options": [
            "A) Reading user keyboard input",
            "B) Writing error messages, separate from normal stdout",
            "C) Logging to a file",
            "D) Raising exceptions"
        ],
        "answer": "B",
        "explanation": "stderr is a separate output stream for error/diagnostic messages. It can be redirected independently of stdout."
    },
    {
        "topic": "File I/O",
        "q": "What does 'for line in f:' do when f is a text file object?",
        "options": [
            "A) Loads all lines into memory then iterates",
            "B) Reads one line at a time — memory efficient for large files",
            "C) Reads characters one at a time",
            "D) Raises TypeError"
        ],
        "answer": "B",
        "explanation": "File objects are iterators. Iterating with 'for line in f' reads one line at a time without loading the whole file."
    },
    {
        "topic": "File I/O",
        "q": "What does io.StringIO() create?",
        "options": [
            "A) A connection to a remote file",
            "B) A binary-mode file on disk",
            "C) An in-memory text stream that behaves like a file object",
            "D) A secure encrypted buffer"
        ],
        "answer": "C",
        "explanation": "StringIO is an in-memory text stream. Useful for testing code that expects a file without touching the disk."
    },
    {
        "topic": "File I/O",
        "q": "What does f.readinto(buf) do that f.read(n) does not?",
        "options": [
            "A) Reads into a string instead of bytes",
            "B) Reads directly into a pre-allocated buffer without creating a new bytes object",
            "C) Reads the entire file at once",
            "D) Blocks until the file is fully written"
        ],
        "answer": "B",
        "explanation": "readinto(buf) writes bytes directly into an existing bytearray/buffer. It avoids allocating a new bytes object on every read — important in tight loops."
    },

    # ── COMPREHENSIONS & LAMBDAS ─────────────────────────────────────────────
    {
        "topic": "Comprehensions & Lambdas",
        "q": "What does this produce?\n\n    [x**2 for x in range(5) if x % 2 == 0]",
        "options": ["A) [0, 1, 4, 9, 16]", "B) [0, 4, 16]", "C) [1, 9]", "D) [4, 16]"],
        "answer": "B",
        "explanation": "Even numbers in range(5) are 0, 2, 4. Squaring: 0, 4, 16."
    },
    {
        "topic": "Comprehensions & Lambdas",
        "q": (
            "What does this produce?\n\n"
            "    [(x, y) for x in range(2) for y in range(2)]"
        ),
        "options": [
            "A) [(0,0), (1,1)]",
            "B) SyntaxError",
            "C) [(0,0), (0,1), (1,0), (1,1)]",
            "D) [(0,1), (1,0)]"
        ],
        "answer": "C",
        "explanation": "Nested comprehension loops: outer x=0 pairs with y=0,1; outer x=1 pairs with y=0,1."
    },
    {
        "topic": "Comprehensions & Lambdas",
        "q": "What is the difference between [x for x in data] and (x for x in data)?",
        "options": [
            "A) They are identical",
            "B) The first is a list; the second is a lazy generator",
            "C) The second creates a tuple",
            "D) The first is lazy; the second is a list"
        ],
        "answer": "B",
        "explanation": "Square brackets = list comprehension (eager). Parentheses = generator expression (lazy, computed on demand)."
    },
    {
        "topic": "Comprehensions & Lambdas",
        "q": (
            "What does this return?\n\n"
            "    list(map(lambda x, y: x + y, [1,2,3], [10,20,30]))"
        ),
        "options": ["A) [11, 22, 33]", "B) TypeError", "C) [1,2,3,10,20,30]", "D) [10, 40, 90]"],
        "answer": "A",
        "explanation": "map() with two iterables zips them. The lambda adds corresponding elements: 1+10, 2+20, 3+30."
    },
    {
        "topic": "Comprehensions & Lambdas",
        "q": (
            "What does filter(None, ['hello', '', 'world', '', '!']) return when wrapped in list()?"
        ),
        "options": [
            "A) ['hello', 'world', '!']",
            "B) ['', '']",
            "C) TypeError",
            "D) ['hello', '', 'world', '', '!']"
        ],
        "answer": "A",
        "explanation": "filter(None, iterable) removes all falsy values. Empty strings are falsy, so they are filtered out."
    },
    {
        "topic": "Comprehensions & Lambdas",
        "q": (
            "What does sorted(['banana','fig','cherry'], key=lambda w: len(w)) return?"
        ),
        "options": [
            "A) ['banana', 'cherry', 'fig']",
            "B) ['fig', 'banana', 'cherry']",
            "C) ['cherry', 'banana', 'fig']",
            "D) ['fig', 'cherry', 'banana']"
        ],
        "answer": "B",
        "explanation": "Lengths: fig=3, banana=6, cherry=6. Sorted by length ascending: fig, banana, cherry (stable sort preserves original order for ties)."
    },

    # ── CLOSURES ────────────────────────────────────────────────────────────
    {
        "topic": "Closures",
        "q": (
            "What does this print?\n\n"
            "    def outer():\n"
            "        x = 10\n"
            "        def inner():\n"
            "            x = 99\n"
            "            print(x)\n"
            "        inner()\n"
            "        print(x)\n"
            "    outer()"
        ),
        "options": ["A) 99 then 99", "B) 10 then 10", "C) 99 then 10", "D) UnboundLocalError"],
        "answer": "C",
        "explanation": "Without 'nonlocal', x=99 inside inner() creates a LOCAL variable. outer's x stays 10."
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
        "options": ["A) 10", "B) 99", "C) None", "D) UnboundLocalError"],
        "answer": "B",
        "explanation": "'nonlocal x' makes the assignment modify outer's x. After inner() runs, outer's x is 99."
    },
    {
        "topic": "Closures",
        "q": (
            "What is the late-binding problem?\n\n"
            "    funcs = [lambda: i for i in range(5)]\n"
            "    print(funcs[0]())"
        ),
        "options": [
            "A) It prints 0 — closures capture the value at definition time",
            "B) It prints 4 — closures capture the variable by reference, not value",
            "C) It raises NameError",
            "D) It prints a list"
        ],
        "answer": "B",
        "explanation": "All lambdas share the same 'i' variable. When called after the loop, i is 4. Fix: lambda i=i: i."
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
        "options": ["A) 5", "B) 3", "C) 15", "D) 8"],
        "answer": "D",
        "explanation": "make_adder(5) returns the 'add' closure with n=5 captured. Calling it with 3 gives 3+5=8."
    },
    {
        "topic": "Closures",
        "q": "What does closure.__closure__[0].cell_contents reveal?",
        "options": [
            "A) The name of the closure function",
            "B) The captured variable's current value",
            "C) The source code of the closure",
            "D) The number of closures"
        ],
        "answer": "B",
        "explanation": "__closure__ holds a tuple of cell objects. .cell_contents on each cell reveals the captured value."
    },
]


def run_exam():
    print("=" * 65)
    print("  PCAP-31-03 MOCK EXAM — MEDIUM LEVEL")
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
            print("  ✓ Correct!\n")
            score += 1
        else:
            print(f"  ✗ Wrong. Correct answer: {q['answer']}")
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
    print(f"  Result     : {'PASS ✓' if passed else 'FAIL ✗'}")
    print()

    if wrong_list:
        print(f"  Review — questions you missed ({len(wrong_list)}):")
        for num, q in wrong_list:
            first_line = q["q"].split("\n")[0][:55]
            print(f"    Q{num:02d} [{q['topic']}]: {first_line}...")
            print(f"         Correct: {q['answer']} — {q['explanation']}")
            print()

    print("=" * 65)


if __name__ == "__main__":
    run_exam()