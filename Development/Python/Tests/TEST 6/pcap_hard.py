"""
PCAP-31-03 Mock Exam - HARD (50 Questions)
Edge cases, multi-step reasoning, and tricky output prediction.
"""

import time

QUESTIONS = [
    # -- MODULES & PACKAGES --
    {
        "topic": "Modules & Packages",
        "q": (
            "What does this print?\n\n"
            "    import sys\n"
            "    import math\n"
            "    del sys.modules['math']\n"
            "    import math\n"
            "    print('ok')"
        ),
        "options": ["A) ModuleNotFoundError", "B) ok", "C) ImportError", "D) None"],
        "answer": "B",
        "explanation": "Deleting from sys.modules forces a reload on the next import; math is found again."
    },
    {
        "topic": "Modules & Packages",
        "q": (
            "What does this print?\n\n"
            "    from math import sqrt as s\n"
            "    print(s(16), s.__name__)"
        ),
        "options": ["A) 4.0 s", "B) 4.0 sqrt", "C) 4 sqrt", "D) AttributeError"],
        "answer": "B",
        "explanation": "The alias keeps the same function object; __name__ remains 'sqrt'."
    },
    {
        "topic": "Modules & Packages",
        "q": "Which is true about pkgutil.iter_modules() vs pkgutil.walk_packages()?",
        "options": ["A) Both are identical", "B) iter_modules is recursive; walk_packages is not", "C) iter_modules is one level; walk_packages is recursive", "D) walk_packages works only on namespace packages"],
        "answer": "C",
        "explanation": "iter_modules yields immediate children; walk_packages descends recursively."
    },
    {
        "topic": "Modules & Packages",
        "q": "What does math.__spec__.origin return for built-in math?",
        "options": ["A) The file path", "B) 'built-in'", "C) None", "D) 'math'"],
        "answer": "B",
        "explanation": "Built-in modules have __spec__.origin == 'built-in'."
    },
    {
        "topic": "Modules & Packages",
        "q": "What happens if you insert a fake module into sys.modules?",
        "options": ["A) Imports ignore it", "B) It is used for future imports with that name", "C) It raises ImportError", "D) It deletes the real module"],
        "answer": "B",
        "explanation": "Python checks sys.modules first and returns the cached object."
    },
    {
        "topic": "Modules & Packages",
        "q": "What does random.sample(range(10**9), k=3) do?",
        "options": ["A) Builds a list of 10**9 items", "B) Samples without materializing the whole range", "C) Raises MemoryError", "D) Returns repeated values"],
        "answer": "B",
        "explanation": "random.sample supports range objects without creating the full list."
    },
    {
        "topic": "Modules & Packages",
        "q": "What does math.trunc(-2.9) return?",
        "options": ["A) -3", "B) -2", "C) 2", "D) 3"],
        "answer": "B",
        "explanation": "trunc removes the fractional part and truncates toward zero."
    },
    {
        "topic": "Modules & Packages",
        "q": "What does __all__ control in a package?",
        "options": ["A) Which names 'from pkg import *' exports", "B) Which files are compiled", "C) The module search path", "D) The package version"],
        "answer": "A",
        "explanation": "__all__ limits what wildcard imports export."
    },
    {
        "topic": "Modules & Packages",
        "q": "What is the result of: hasattr(math, 'tau') in Python 3.11?",
        "options": ["A) True", "B) False", "C) AttributeError", "D) None"],
        "answer": "A",
        "explanation": "math.tau exists in modern Python versions (2*pi)."
    },
    {
        "topic": "Modules & Packages",
        "q": "What does importlib.reload(mod) do?",
        "options": ["A) Creates a new module object", "B) Re-executes the module code in the existing object", "C) Deletes the module", "D) Clears sys.path"],
        "answer": "B",
        "explanation": "reload() re-executes code in the same module object."
    },

    # -- OOP --
    {
        "topic": "OOP",
        "q": (
            "What does this print?\n\n"
            "    class A:\n"
            "        def greet(self): return 'A'\n"
            "    class B(A):\n"
            "        def greet(self): return 'B+' + super().greet()\n"
            "    class C(A):\n"
            "        def greet(self): return 'C+' + super().greet()\n"
            "    class D(B, C):\n"
            "        def greet(self): return 'D+' + super().greet()\n"
            "    print(D().greet())"
        ),
        "options": ["A) D+B+A", "B) D+C+A", "C) D+B+C+A", "D) D+A"],
        "answer": "C",
        "explanation": "MRO is D -> B -> C -> A, so the chain is D+B+C+A."
    },
    {
        "topic": "OOP",
        "q": (
            "What does this print?\n\n"
            "    class Foo:\n"
            "        def __init__(self):\n"
            "            self.__x = 10\n"
            "    f = Foo()\n"
            "    print(f.__dict__)"
        ),
        "options": ["A) {'__x': 10}", "B) {'x': 10}", "C) {'_Foo__x': 10}", "D) AttributeError"],
        "answer": "C",
        "explanation": "Name mangling rewrites __x to _Foo__x."
    },
    {
        "topic": "OOP",
        "q": (
            "What does this print?\n\n"
            "    class Counter:\n"
            "        count = 0\n"
            "        def __init__(self):\n"
            "            Counter.count += 1\n"
            "    a = Counter()\n"
            "    b = Counter()\n"
            "    print(a.count, Counter.count)"
        ),
        "options": ["A) 1 1", "B) 0 2", "C) 2 2", "D) 1 2"],
        "answer": "C",
        "explanation": "The class variable is incremented twice; both reads show 2."
    },
    {
        "topic": "OOP",
        "q": (
            "What does this print?\n\n"
            "    class Foo:\n"
            "        def __repr__(self): return 'Foo()'\n"
            "        def __str__(self): return 'a Foo'\n"
            "    f = Foo()\n"
            "    print(f'{f!r} {f!s}')"
        ),
        "options": ["A) a Foo a Foo", "B) Foo() Foo()", "C) Foo() a Foo", "D) a Foo Foo()"],
        "answer": "C",
        "explanation": "!r uses repr, !s uses str."
    },
    {
        "topic": "OOP",
        "q": (
            "What does this print?\n\n"
            "    class A:\n"
            "        x = []\n"
            "    class B(A): pass\n"
            "    class C(A): pass\n"
            "    B.x.append(1)\n"
            "    print(C.x)"
        ),
        "options": ["A) []", "B) [1]", "C) [1, 1]", "D) AttributeError"],
        "answer": "B",
        "explanation": "B.x and C.x refer to the same list on A."
    },
    {
        "topic": "OOP",
        "q": (
            "What does this print?\n\n"
            "    class Foo:\n"
            "        __slots__ = ['x']\n"
            "        def __init__(self):\n"
            "            self.x = 1\n"
            "    f = Foo()\n"
            "    f.y = 2\n"
            "    print(f.y)"
        ),
        "options": ["A) 2", "B) AttributeError", "C) None", "D) TypeError"],
        "answer": "B",
        "explanation": "__slots__ prevents adding attributes not listed."
    },
    {
        "topic": "OOP",
        "q": "What does type(type) return?",
        "options": ["A) object", "B) class", "C) type", "D) metaclass"],
        "answer": "C",
        "explanation": "type is its own metaclass."
    },
    {
        "topic": "OOP",
        "q": (
            "Which parent method is called first in class Child(Parent1, Parent2) "
            "if both define foo() and Child does not override it?"
        ),
        "options": ["A) Parent2", "B) Parent1", "C) Neither; AttributeError", "D) Both"],
        "answer": "B",
        "explanation": "MRO searches left to right; Parent1 is first."
    },
    {
        "topic": "OOP",
        "q": "What does Foo.__bases__ contain?",
        "options": ["A) The full MRO", "B) Direct parent classes", "C) All subclasses", "D) Only object"],
        "answer": "B",
        "explanation": "__bases__ is a tuple of direct parents."
    },
    {
        "topic": "OOP",
        "q": (
            "What does this print?\n\n"
            "    class Animal:\n"
            "        def __init__(self, name):\n"
            "            self.name = name\n"
            "    class Dog(Animal):\n"
            "        def __init__(self, name, breed):\n"
            "            super().__init__(name)\n"
            "            self.breed = breed\n"
            "    d = Dog('Rex', 'Lab')\n"
            "    print(vars(d))"
        ),
        "options": ["A) {'name': 'Rex'}", "B) {'breed': 'Lab'}", "C) {'name': 'Rex', 'breed': 'Lab'}", "D) {}"],
        "answer": "C",
        "explanation": "Both name and breed are stored on the instance."
    },

    # -- EXCEPTIONS --
    {
        "topic": "Exceptions",
        "q": (
            "What does this print?\n\n"
            "    def f():\n"
            "        try:\n"
            "            raise ValueError('x')\n"
            "        finally:\n"
            "            return 'done'\n"
            "    print(f())"
        ),
        "options": ["A) ValueError", "B) done", "C) None", "D) x"],
        "answer": "B",
        "explanation": "Return in finally overrides the exception."
    },
    {
        "topic": "Exceptions",
        "q": (
            "What is printed?\n\n"
            "    try:\n"
            "        try:\n"
            "            raise ValueError('inner')\n"
            "        finally:\n"
            "            print('inner finally')\n"
            "    except ValueError:\n"
            "        print('outer except')"
        ),
        "options": ["A) outer except", "B) inner finally", "C) inner finally then outer except", "D) outer except then inner finally"],
        "answer": "C",
        "explanation": "The inner finally runs, then the outer except handles the error."
    },
    {
        "topic": "Exceptions",
        "q": (
            "What does this print?\n\n"
            "    try:\n"
            "        raise KeyError('k') from ValueError('v')\n"
            "    except KeyError as e:\n"
            "        print(type(e.__cause__).__name__)"
        ),
        "options": ["A) KeyError", "B) ValueError", "C) None", "D) AttributeError"],
        "answer": "B",
        "explanation": "__cause__ is the ValueError('v')."
    },
    {
        "topic": "Exceptions",
        "q": (
            "What is e.args after this?\n\n"
            "    class MyError(Exception):\n"
            "        def __init__(self, code, msg):\n"
            "            self.code = code\n"
            "            super().__init__(msg)\n"
            "    try:\n"
            "        raise MyError(404, 'not found')\n"
            "    except MyError as e:\n"
            "        print(e.args)"
        ),
        "options": ["A) (404, 'not found')", "B) ('not found',)", "C) ()", "D) 'not found'"],
        "answer": "B",
        "explanation": "Only msg is passed to Exception, so e.args contains ('not found',)."
    },
    {
        "topic": "Exceptions",
        "q": (
            "What does this print?\n\n"
            "    try:\n"
            "        x = [1,2,3][10]\n"
            "    except (IndexError, KeyError):\n"
            "        print('lookup')\n"
            "    except Exception:\n"
            "        print('general')"
        ),
        "options": ["A) lookup", "B) general", "C) both", "D) nothing"],
        "answer": "A",
        "explanation": "IndexError is caught by the grouped handler."
    },
    {
        "topic": "Exceptions",
        "q": "What is the correct chain? BaseException -> Exception -> LookupError -> IndexError",
        "options": ["A) False", "B) True", "C) Only in Python 2", "D) IndexError is a ValueError"],
        "answer": "B",
        "explanation": "IndexError inherits from LookupError."
    },
    {
        "topic": "Exceptions",
        "q": (
            "What does this print?\n\n"
            "    def safe_div(a, b):\n"
            "        try:\n"
            "            return a / b\n"
            "        except ZeroDivisionError:\n"
            "            return None\n"
            "        else:\n"
            "            print('no error')\n"
            "    print(safe_div(10, 2))"
        ),
        "options": ["A) no error then 5.0", "B) 5.0", "C) None", "D) no error"],
        "answer": "B",
        "explanation": "The return in try exits before else can run."
    },
    {
        "topic": "Exceptions",
        "q": (
            "What does this print?\n\n"
            "    try:\n"
            "        raise ValueError\n"
            "    except ValueError as e:\n"
            "        pass\n"
            "    print(e)"
        ),
        "options": ["A) ValueError()", "B) NameError", "C) None", "D) ''"],
        "answer": "B",
        "explanation": "The exception name is deleted after the except block."
    },
    {
        "topic": "Exceptions",
        "q": "What does sys.exc_info()[0].__name__ return inside an except block?",
        "options": ["A) The exception type name", "B) The message", "C) The traceback", "D) The line number"],
        "answer": "A",
        "explanation": "sys.exc_info() returns (type, value, traceback)."
    },
    {
        "topic": "Exceptions",
        "q": "What happens if an exception is raised in a finally block?",
        "options": ["A) Original exception is chained", "B) Original exception is replaced", "C) Both exceptions are raised", "D) It is ignored"],
        "answer": "B",
        "explanation": "The new exception replaces the original."
    },

    # -- FILE I/O --
    {
        "topic": "File I/O",
        "q": (
            "What does this print?\n\n"
            "    with open('t.txt','w+') as f:\n"
            "        f.write('hello')\n"
            "        print(repr(f.read()))"
        ),
        "options": ["A) 'hello'", "B) ''", "C) None", "D) FileNotFoundError"],
        "answer": "B",
        "explanation": "After write, the cursor is at the end; read returns ''."
    },
    {
        "topic": "File I/O",
        "q": "What does errors='replace' do in text mode?",
        "options": ["A) Raises UnicodeDecodeError", "B) Replaces bad bytes with a replacement char", "C) Drops all bytes", "D) Uses ASCII"],
        "answer": "B",
        "explanation": "Invalid bytes are replaced with the Unicode replacement character."
    },
    {
        "topic": "File I/O",
        "q": "What does f.readinto(buf) return?",
        "options": ["A) The buffer", "B) The number of bytes read", "C) True/False", "D) A bytes object"],
        "answer": "B",
        "explanation": "readinto returns the count of bytes read into the buffer."
    },
    {
        "topic": "File I/O",
        "q": "What does f.flush() do?",
        "options": ["A) Closes the file", "B) Forces buffered data to the OS", "C) Deletes the file", "D) Moves to start"],
        "answer": "B",
        "explanation": "flush pushes buffered writes without closing the file."
    },
    {
        "topic": "File I/O",
        "q": (
            "What does this print?\n\n"
            "    import io\n"
            "    buf = io.BytesIO(b'ABCDE')\n"
            "    buf.seek(2)\n"
            "    print(buf.read(2))\n"
            "    print(buf.tell())"
        ),
        "options": ["A) b'AB' then 2", "B) b'CD' then 4", "C) b'CE' then 5", "D) b'CD' then 2"],
        "answer": "B",
        "explanation": "Reading from position 2 yields b'CD' and moves to 4."
    },
    {
        "topic": "File I/O",
        "q": (
            "What does this print?\n\n"
            "    ba = bytearray(b'hello')\n"
            "    ba[0] = 72\n"
            "    print(ba.decode('utf-8'))"
        ),
        "options": ["A) hello", "B) Hello", "C) 72ello", "D) TypeError"],
        "answer": "B",
        "explanation": "72 is 'H' in ASCII, so the result is Hello."
    },
    {
        "topic": "File I/O",
        "q": "What does bytearray(b'ABC') == bytes(b'ABC') evaluate to?",
        "options": ["A) True", "B) False", "C) TypeError", "D) NotImplemented"],
        "answer": "A",
        "explanation": "bytearray and bytes compare equal by value."
    },
    {
        "topic": "File I/O",
        "q": "What does f.seek(-5, 2) do?",
        "options": ["A) Moves to byte 5 from start", "B) Moves to 5 bytes before the end", "C) Moves 5 bytes from current", "D) Raises ValueError"],
        "answer": "B",
        "explanation": "whence=2 means relative to end of file."
    },
    {
        "topic": "File I/O",
        "q": "What does sys.stdout.write('hello') return?",
        "options": ["A) None", "B) True", "C) 5", "D) 'hello'"],
        "answer": "C",
        "explanation": "write() returns the number of characters written."
    },
    {
        "topic": "File I/O",
        "q": (
            "What does this print?\n\n"
            "    import io, sys\n"
            "    old = sys.stdout\n"
            "    sys.stdout = io.StringIO()\n"
            "    print('captured')\n"
            "    val = sys.stdout.getvalue()\n"
            "    sys.stdout = old\n"
            "    print(repr(val))"
        ),
        "options": ["A) 'captured'", "B) 'captured\\n'", "C) captured", "D) Nothing"],
        "answer": "B",
        "explanation": "print adds a newline, so the buffer has 'captured\n'."
    },

    # -- COMPREHENSIONS & LAMBDAS --
    {
        "topic": "Comprehensions & Lambdas",
        "q": (
            "What does this print?\n\n"
            "    x = 10\n"
            "    result = [x for x in range(3)]\n"
            "    print(x, result)"
        ),
        "options": ["A) 2 [0, 1, 2]", "B) 10 [0, 1, 2]", "C) 10 [10, 10, 10]", "D) 2 [10, 10, 10]"],
        "answer": "B",
        "explanation": "In Python 3, list comprehensions have their own scope."
    },
    {
        "topic": "Comprehensions & Lambdas",
        "q": "What does reduce(lambda a, b: a + [b], range(4), []) return?",
        "options": ["A) 6", "B) [0, 1, 2, 3]", "C) [[0], [1], [2], [3]]", "D) [[], 0, 1, 2, 3]"],
        "answer": "B",
        "explanation": "Each step appends one element to the list."
    },
    {
        "topic": "Comprehensions & Lambdas",
        "q": (
            "What does this print?\n\n"
            "    gen = (x for x in range(10) if x % 3 == 0)\n"
            "    print(list(gen))\n"
            "    print(list(gen))"
        ),
        "options": ["A) [0,3,6,9] then [0,3,6,9]", "B) [0,3,6,9] then []", "C) [] then []", "D) StopIteration"],
        "answer": "B",
        "explanation": "Generators are single-use; the second list is empty."
    },
    {
        "topic": "Comprehensions & Lambdas",
        "q": "What does f = lambda *args, **kw: (args, kw); f(1,2,x=3) return?",
        "options": ["A) ((1, 2), {'x': 3})", "B) (1, 2, 3)", "C) {'x': 3}", "D) TypeError"],
        "answer": "A",
        "explanation": "*args becomes a tuple, **kw becomes a dict."
    },
    {
        "topic": "Comprehensions & Lambdas",
        "q": "What does nested = [[i*j for j in range(1,4)] for i in range(1,4)]; nested[1][2] return?",
        "options": ["A) 2", "B) 4", "C) 6", "D) 9"],
        "answer": "C",
        "explanation": "nested[1] is [2,4,6], so nested[1][2] is 6."
    },

    # -- CLOSURES --
    {
        "topic": "Closures",
        "q": (
            "What does this print?\n\n"
            "    def outer():\n"
            "        results = []\n"
            "        for i in range(3):\n"
            "            def inner(x=i):\n"
            "                return x\n"
            "            results.append(inner)\n"
            "        return results\n"
            "    fns = outer()\n"
            "    print([f() for f in fns])"
        ),
        "options": ["A) [2, 2, 2]", "B) [0, 0, 0]", "C) [0, 1, 2]", "D) [2, 1, 0]"],
        "answer": "C",
        "explanation": "Default args capture i at definition time."
    },
    {
        "topic": "Closures",
        "q": (
            "What does this print?\n\n"
            "    def make_mult(n):\n"
            "        def mult(x): return x * n\n"
            "        return mult\n"
            "    triple = make_mult(3)\n"
            "    print(triple.__closure__[0].cell_contents)"
        ),
        "options": ["A) 'n'", "B) 3", "C) make_mult", "D) AttributeError"],
        "answer": "B",
        "explanation": "The closure captures n=3."
    },
    {
        "topic": "Closures",
        "q": (
            "What does this print?\n\n"
            "    x = 'global'\n"
            "    def outer():\n"
            "        x = 'outer'\n"
            "        def inner():\n"
            "            global x\n"
            "            x = 'changed'\n"
            "        inner()\n"
            "        print('outer x:', x)\n"
            "    outer()\n"
            "    print('global x:', x)"
        ),
        "options": ["A) outer x: changed | global x: changed", "B) outer x: outer | global x: changed", "C) outer x: global | global x: changed", "D) outer x: outer | global x: outer"],
        "answer": "B",
        "explanation": "global modifies the module-level x, not outer's x."
    },
    {
        "topic": "Closures",
        "q": (
            "What does this print?\n\n"
            "    def outer():\n"
            "        data = []\n"
            "        def add(item):\n"
            "            data.append(item)\n"
            "        def get():\n"
            "            return data\n"
            "        return add, get\n"
            "    add, get = outer()\n"
            "    add(1); add(2); add(3)\n"
            "    print(get())"
        ),
        "options": ["A) []", "B) [1, 2, 3]", "C) NameError", "D) [3]"],
        "answer": "B",
        "explanation": "Both functions close over the same list."
    },
    {
        "topic": "Closures",
        "q": "What is the fix for late binding in: funcs = [lambda: i for i in range(5)]?",
        "options": ["A) Use lambda i=i: i", "B) Use global i", "C) Use i + 0", "D) Use list()"],
        "answer": "A",
        "explanation": "Default arguments capture the current value of i."
    },
]


def run_exam():
    print("=" * 65)
    print("  PCAP-31-03 MOCK EXAM - HARD LEVEL")
    print("  50 Questions | Pass mark: 70% (35/50)")
    print("  Tip: watch for edge cases and MRO details.")
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
