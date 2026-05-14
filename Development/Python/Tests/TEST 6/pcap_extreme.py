"""
PCAP-31-03 Mock Exam - EXTREME (50 Questions)
Deep internals, uncommon interactions, and tricky edge cases.
"""

import time

QUESTIONS = [
    # -- MODULES & PACKAGES --
    {
        "topic": "Modules & Packages",
        "q": (
            "What does this print?\n\n"
            "    import importlib\n"
            "    import math\n"
            "    math.pi = 0\n"
            "    importlib.reload(math)\n"
            "    print(math.pi)"
        ),
        "options": ["A) 0", "B) 3.141592653589793", "C) AttributeError", "D) None"],
        "answer": "B",
        "explanation": "reload re-executes the module code, restoring the original constant."
    },
    {
        "topic": "Modules & Packages",
        "q": (
            "What does this print?\n\n"
            "    import sys\n"
            "    class Fake:\n"
            "        pi = 99\n"
            "    sys.modules['math'] = Fake()\n"
            "    import math\n"
            "    print(math.pi)"
        ),
        "options": ["A) 3.141592653589793", "B) 99", "C) AttributeError", "D) ImportError"],
        "answer": "B",
        "explanation": "Python returns the cached entry from sys.modules."
    },
    {
        "topic": "Modules & Packages",
        "q": "What does math.hypot(3, 4, 0) return?",
        "options": ["A) 5.0", "B) 7.0", "C) 25.0", "D) TypeError"],
        "answer": "A",
        "explanation": "hypot accepts multiple args; sqrt(3^2+4^2+0^2)=5.0."
    },
    {
        "topic": "Modules & Packages",
        "q": "What is the probability of picking 'b' in random.choices(['a','b','c'], cum_weights=[10,40,100], k=1)?",
        "options": ["A) 10%", "B) 30%", "C) 40%", "D) 33.3%"],
        "answer": "B",
        "explanation": "cum_weights imply weights [10, 30, 60]; P(b)=30/100."
    },
    {
        "topic": "Modules & Packages",
        "q": "What does random.sample(range(10**6), k=5) do efficiently?",
        "options": ["A) Builds a list of 10**6 elements", "B) Samples without materializing the full range", "C) Returns duplicate values", "D) Raises MemoryError"],
        "answer": "B",
        "explanation": "range supports indexing and length, so sampling is efficient."
    },
    {
        "topic": "Modules & Packages",
        "q": "What does getattr(math, 'sqrt')(25) return?",
        "options": ["A) 25", "B) 5.0", "C) '5.0'", "D) AttributeError"],
        "answer": "B",
        "explanation": "getattr returns the function object, then it is called."
    },
    {
        "topic": "Modules & Packages",
        "q": "What does module.__spec__ contain?",
        "options": ["A) The docstring", "B) A ModuleSpec with name, origin, loader", "C) A dict of public names", "D) The module version"],
        "answer": "B",
        "explanation": "__spec__ is a ModuleSpec describing how the module was loaded."
    },
    {
        "topic": "Modules & Packages",
        "q": "What does 'from .. import x' mean inside a package?",
        "options": ["A) Import from current package", "B) Import from parent package", "C) Import from site-packages", "D) SyntaxError"],
        "answer": "B",
        "explanation": "Two dots refer to the parent package."
    },
    {
        "topic": "Modules & Packages",
        "q": "What does type(math) return?",
        "options": ["A) <class 'package'>", "B) <class 'module'>", "C) <class 'type'>", "D) <class 'builtin_function_or_method'>"],
        "answer": "B",
        "explanation": "Imported modules are instances of the module type."
    },
    {
        "topic": "Modules & Packages",
        "q": "Which is correct for pkgutil.iter_modules() vs pkgutil.walk_packages()?",
        "options": ["A) iter_modules is recursive, walk_packages is not", "B) iter_modules is one level, walk_packages is recursive", "C) Both are recursive", "D) Both are non-recursive"],
        "answer": "B",
        "explanation": "iter_modules yields immediate children; walk_packages descends recursively."
    },

    # -- OOP --
    {
        "topic": "OOP",
        "q": (
            "What does this print?\n\n"
            "    class Meta(type):\n"
            "        def __new__(mcs, name, bases, ns):\n"
            "            ns['extra'] = 42\n"
            "            return super().__new__(mcs, name, bases, ns)\n"
            "    class Foo(metaclass=Meta):\n"
            "        pass\n"
            "    print(Foo.extra)"
        ),
        "options": ["A) AttributeError", "B) None", "C) 42", "D) TypeError"],
        "answer": "C",
        "explanation": "The metaclass injects extra into the class namespace."
    },
    {
        "topic": "OOP",
        "q": (
            "What does this print?\n\n"
            "    class A:\n"
            "        def __init_subclass__(cls, **kw):\n"
            "            super().__init_subclass__(**kw)\n"
            "            cls.registered = True\n"
            "    class B(A):\n"
            "        pass\n"
            "    print(B.registered)"
        ),
        "options": ["A) AttributeError", "B) False", "C) True", "D) None"],
        "answer": "C",
        "explanation": "__init_subclass__ runs when B is defined and sets registered."
    },
    {
        "topic": "OOP",
        "q": (
            "What does this print?\n\n"
            "    class Descriptor:\n"
            "        def __get__(self, obj, cls):\n"
            "            return 42\n"
            "    class Foo:\n"
            "        x = Descriptor()\n"
            "    f = Foo()\n"
            "    print(f.x, Foo.x)"
        ),
        "options": ["A) 42 42", "B) <Descriptor> 42", "C) 42 <Descriptor>", "D) AttributeError"],
        "answer": "A",
        "explanation": "Descriptor __get__ runs for both instance and class access."
    },
    {
        "topic": "OOP",
        "q": (
            "What does this print?\n\n"
            "    class Singleton:\n"
            "        _inst = None\n"
            "        def __new__(cls):\n"
            "            if cls._inst is None:\n"
            "                cls._inst = super().__new__(cls)\n"
            "            return cls._inst\n"
            "    a = Singleton()\n"
            "    b = Singleton()\n"
            "    print(a is b)"
        ),
        "options": ["A) False", "B) True", "C) TypeError", "D) None"],
        "answer": "B",
        "explanation": "__new__ returns the same instance each time."
    },
    {
        "topic": "OOP",
        "q": (
            "What does this print?\n\n"
            "    class A:\n"
            "        def __init__(self): self.x = 1\n"
            "    class B(A):\n"
            "        def __init__(self):\n"
            "            self.y = 2\n"
            "    b = B()\n"
            "    print(hasattr(b, 'x'), hasattr(b, 'y'))"
        ),
        "options": ["A) True True", "B) False True", "C) True False", "D) False False"],
        "answer": "B",
        "explanation": "B.__init__ does not call super().__init__, so x is never set."
    },
    {
        "topic": "OOP",
        "q": (
            "What does this print?\n\n"
            "    class Foo:\n"
            "        __slots__ = ['x', 'y']\n"
            "        def __init__(self):\n"
            "            self.x = 1\n"
            "            self.y = 2\n"
            "    f = Foo()\n"
            "    f.z = 3\n"
            "    print(f.z)"
        ),
        "options": ["A) 3", "B) AttributeError", "C) None", "D) TypeError"],
        "answer": "B",
        "explanation": "__slots__ prevents setting undeclared attributes."
    },
    {
        "topic": "OOP",
        "q": (
            "What does this print?\n\n"
            "    class A:\n"
            "        val = []\n"
            "    class B(A): pass\n"
            "    class C(A): pass\n"
            "    B.val.append(1)\n"
            "    print(C.val)"
        ),
        "options": ["A) []", "B) [1]", "C) [1, 1]", "D) AttributeError"],
        "answer": "B",
        "explanation": "Both classes share the same mutable class attribute."
    },
    {
        "topic": "OOP",
        "q": (
            "What does this print?\n\n"
            "    class Foo:\n"
            "        x = 1\n"
            "    f = Foo()\n"
            "    Foo.x = 2\n"
            "    print(f.x)"
        ),
        "options": ["A) 1", "B) 2", "C) AttributeError", "D) None"],
        "answer": "B",
        "explanation": "The instance reads the updated class attribute."
    },
    {
        "topic": "OOP",
        "q": (
            "What does this print?\n\n"
            "    class A:\n"
            "        def __init__(self):\n"
            "            print('A')\n"
            "    class B(A):\n"
            "        def __init__(self):\n"
            "            print('B')\n"
            "            super().__init__()\n"
            "    class C(A):\n"
            "        def __init__(self):\n"
            "            print('C')\n"
            "            super().__init__()\n"
            "    class D(B, C):\n"
            "        def __init__(self):\n"
            "            print('D')\n"
            "            super().__init__()\n"
            "    D()"
        ),
        "options": ["A) D B A C", "B) D B C A", "C) D C B A", "D) D A"],
        "answer": "B",
        "explanation": "MRO is D -> B -> C -> A."
    },
    {
        "topic": "OOP",
        "q": "What does issubclass(list, object) return?",
        "options": ["A) True", "B) False", "C) TypeError", "D) None"],
        "answer": "A",
        "explanation": "All new-style classes inherit from object."
    },

    # -- EXCEPTIONS --
    {
        "topic": "Exceptions",
        "q": (
            "What does this print?\n\n"
            "    try:\n"
            "        raise ValueError('v')\n"
            "    except ValueError:\n"
            "        try:\n"
            "            raise TypeError('t')\n"
            "        except TypeError:\n"
            "            print('inner')\n"
            "        raise\n"
            "    except Exception:\n"
            "        print('outer')"
        ),
        "options": ["A) inner then outer", "B) inner then ValueError propagates", "C) outer", "D) inner only"],
        "answer": "B",
        "explanation": "The bare raise re-raises ValueError; the second except does not re-catch it."
    },
    {
        "topic": "Exceptions",
        "q": (
            "What does this print?\n\n"
            "    def f():\n"
            "        try:\n"
            "            raise ValueError\n"
            "        except ValueError:\n"
            "            return 'except'\n"
            "        finally:\n"
            "            return 'finally'\n"
            "    print(f())"
        ),
        "options": ["A) except", "B) finally", "C) ValueError", "D) except then finally"],
        "answer": "B",
        "explanation": "Return in finally overrides the except return."
    },
    {
        "topic": "Exceptions",
        "q": (
            "What does this print?\n\n"
            "    try:\n"
            "        raise ValueError('a') from ValueError('b')\n"
            "    except ValueError as e:\n"
            "        print(str(e), str(e.__cause__))"
        ),
        "options": ["A) a None", "B) a b", "C) b a", "D) ValueError: a"],
        "answer": "B",
        "explanation": "The raised exception is 'a' and the cause is 'b'."
    },
    {
        "topic": "Exceptions",
        "q": (
            "What does this print?\n\n"
            "    class Err(Exception):\n"
            "        def __init__(self, code):\n"
            "            self.code = code\n"
            "    try:\n"
            "        raise Err(404)\n"
            "    except Err as e:\n"
            "        print(e.args, e.code)"
        ),
        "options": ["A) (404,) 404", "B) () 404", "C) (404,) AttributeError", "D) () AttributeError"],
        "answer": "B",
        "explanation": "Err.__init__ does not call super().__init__, so args is empty."
    },
    {
        "topic": "Exceptions",
        "q": (
            "What does this print?\n\n"
            "    import sys\n"
            "    try:\n"
            "        1 / 0\n"
            "    except:\n"
            "        exc = sys.exc_info()\n"
            "        print(exc[0].__name__)"
        ),
        "options": ["A) Exception", "B) ZeroDivisionError", "C) ArithmeticError", "D) None"],
        "answer": "B",
        "explanation": "exc[0] is the exception class."
    },
    {
        "topic": "Exceptions",
        "q": (
            "What does this print?\n\n"
            "    try:\n"
            "        open('missing_xyz')\n"
            "    except FileNotFoundError as e:\n"
            "        print(issubclass(type(e), OSError))"
        ),
        "options": ["A) False", "B) TypeError", "C) None", "D) True"],
        "answer": "D",
        "explanation": "FileNotFoundError is a subclass of OSError."
    },
    {
        "topic": "Exceptions",
        "q": (
            "What does this print?\n\n"
            "    def risky():\n"
            "        assert False, 'test'\n"
            "    try:\n"
            "        risky()\n"
            "    except AssertionError as e:\n"
            "        print(repr(e))"
        ),
        "options": ["A) AssertionError('test')", "B) 'test'", "C) False", "D) AssertionError()"],
        "answer": "A",
        "explanation": "repr shows AssertionError with its message."
    },
    {
        "topic": "Exceptions",
        "q": "What happens to the original exception if a new one is raised in finally?",
        "options": ["A) It is chained", "B) It is discarded", "C) Both are raised", "D) It is logged"],
        "answer": "B",
        "explanation": "A new exception in finally replaces the original."
    },
    {
        "topic": "Exceptions",
        "q": "What does this print?\n\n    try:\n        raise ValueError\n    except ValueError as e:\n        pass\n    print(e)",
        "options": ["A) ValueError()", "B) NameError", "C) None", "D) ''"],
        "answer": "B",
        "explanation": "The exception name is deleted when the except block ends."
    },
    {
        "topic": "Exceptions",
        "q": (
            "What does this print?\n\n"
            "    class Base(Exception):\n"
            "        def __str__(self):\n"
            "            return 'base!'\n"
            "    class Child(Base): pass\n"
            "    try:\n"
            "        raise Child('x')\n"
            "    except Child as e:\n"
            "        print(str(e))"
        ),
        "options": ["A) x", "B) base!", "C) Child: x", "D) Base: base!"],
        "answer": "B",
        "explanation": "Child inherits Base.__str__."
    },

    # -- FILE I/O --
    {
        "topic": "File I/O",
        "q": (
            "What does this print?\n\n"
            "    import io\n"
            "    s = io.StringIO('hello\\nworld\\n')\n"
            "    lines = s.readlines()\n"
            "    print(len(lines), repr(lines[0]))"
        ),
        "options": ["A) 2 'hello'", "B) 2 'hello\\n'", "C) 1 'hello\\nworld\\n'", "D) 3 'hello\\n'"],
        "answer": "B",
        "explanation": "readlines keeps newlines; the first line is 'hello\n'."
    },
    {
        "topic": "File I/O",
        "q": (
            "What does this print?\n\n"
            "    ba = bytearray(b'\\x00' * 4)\n"
            "    import struct\n"
            "    struct.pack_into('>I', ba, 0, 255)\n"
            "    print(list(ba))"
        ),
        "options": ["A) [255, 0, 0, 0]", "B) [0, 0, 0, 255]", "C) [0, 255, 0, 0]", "D) [0, 0, 255, 0]"],
        "answer": "B",
        "explanation": "Big-endian 255 is 0x000000FF, so bytes are [0,0,0,255]."
    },
    {
        "topic": "File I/O",
        "q": "What does f.readinto(buf) return?",
        "options": ["A) The buffer contents", "B) The number of bytes read", "C) True/False", "D) A new bytearray"],
        "answer": "B",
        "explanation": "readinto returns a byte count."
    },
    {
        "topic": "File I/O",
        "q": "What does errors='ignore' do when decoding text?",
        "options": ["A) Raises UnicodeDecodeError", "B) Drops undecodable bytes", "C) Replaces with '?'", "D) Uses ASCII"],
        "answer": "B",
        "explanation": "Undecodable bytes are silently skipped."
    },
    {
        "topic": "File I/O",
        "q": (
            "What does this print?\n\n"
            "    with open('x.bin','wb') as f:\n"
            "        f.write(b'\\xff\\xfe')\n"
            "    with open('x.bin','r', encoding='utf-8', errors='ignore') as f:\n"
            "        print(repr(f.read()))"
        ),
        "options": ["A) '\\xff\\xfe'", "B) ''", "C) UnicodeDecodeError", "D) '??'"],
        "answer": "B",
        "explanation": "Invalid UTF-8 bytes are ignored, leaving an empty string."
    },
    {
        "topic": "File I/O",
        "q": "Which is the most memory-efficient way to read a binary file in 64KB chunks?",
        "options": ["A) data = f.read()", "B) buf = bytearray(65536); while n := f.readinto(buf): process(buf[:n])", "C) f.readlines()", "D) for line in f"],
        "answer": "B",
        "explanation": "readinto reuses a buffer and avoids repeated allocations."
    },
    {
        "topic": "File I/O",
        "q": "What does f.seek(-5, 2) do on a 100-byte file?",
        "options": ["A) Seek to byte 5", "B) Seek to byte 95", "C) Error", "D) Seek to byte 105"],
        "answer": "B",
        "explanation": "Offset -5 from the end moves to position 95."
    },
    {
        "topic": "File I/O",
        "q": "What does bytearray(b'ABC') == bytes(b'ABC') evaluate to?",
        "options": ["A) True", "B) False", "C) TypeError", "D) NotImplemented"],
        "answer": "A",
        "explanation": "bytes and bytearray compare equal by value."
    },
    {
        "topic": "File I/O",
        "q": "What does sys.stdout.write('hello') return?",
        "options": ["A) None", "B) True", "C) 5", "D) 'hello'"],
        "answer": "C",
        "explanation": "write returns the number of characters written."
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
        "explanation": "print adds a newline, so the buffer contains 'captured\n'."
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
        "explanation": "List comprehensions have their own scope in Python 3."
    },
    {
        "topic": "Comprehensions & Lambdas",
        "q": "What does reduce(lambda acc, x: acc * x, [1,2,3,4,5]) return?",
        "options": ["A) 15", "B) 120", "C) [1,2,6,24,120]", "D) 24"],
        "answer": "B",
        "explanation": "The reduce multiplies cumulatively: 1*2*3*4*5 = 120."
    },
    {
        "topic": "Comprehensions & Lambdas",
        "q": (
            "What does this print?\n\n"
            "    g = (x**2 for x in range(5))\n"
            "    print(next(g), next(g), next(g))"
        ),
        "options": ["A) 0 1 4", "B) [0, 1, 4]", "C) 0 0 0", "D) StopIteration"],
        "answer": "A",
        "explanation": "Generator expressions are lazy; next pulls values one by one."
    },
    {
        "topic": "Comprehensions & Lambdas",
        "q": "What does f = lambda *args, **kw: (args, kw); f(1,2,x=3,y=4) return?",
        "options": ["A) ((1, 2), {'x': 3, 'y': 4})", "B) (1, 2, 3, 4)", "C) {'x': 3, 'y': 4}", "D) TypeError"],
        "answer": "A",
        "explanation": "Positional args become a tuple; keyword args become a dict."
    },
    {
        "topic": "Comprehensions & Lambdas",
        "q": "What does result = {v: k for k, v in {'a':1,'b':2}.items()} produce?",
        "options": ["A) {'a': 1, 'b': 2}", "B) {1: 'a', 2: 'b'}", "C) TypeError", "D) SyntaxError"],
        "answer": "B",
        "explanation": "Keys and values are swapped in the comprehension."
    },

    # -- CLOSURES --
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
        "explanation": "Assignment in inner makes x local there, outer x stays 10."
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
        "explanation": "nonlocal allows inner to update outer's x."
    },
    {
        "topic": "Closures",
        "q": (
            "What does this print?\n\n"
            "    funcs = [lambda: i for i in range(5)]\n"
            "    print(funcs[0]())"
        ),
        "options": ["A) 0", "B) 4", "C) 5", "D) NameError"],
        "answer": "B",
        "explanation": "Late binding captures i by reference; after the loop i is 4."
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
        "explanation": "Each closure has independent state."
    },
    {
        "topic": "Closures",
        "q": "What is the fix for the late-binding trap in lambdas inside loops?",
        "options": ["A) Use lambda i=i: i", "B) Use global", "C) Use list()", "D) Use try/except"],
        "answer": "A",
        "explanation": "Default arguments capture the current value."
    },
]


def run_exam():
    print("=" * 70)
    print("  PCAP-31-03 MOCK EXAM - EXTREME LEVEL")
    print("  50 Questions | Pass mark: 70% (35/50)")
    print("  Tip: these questions target edge cases and internals.")
    print("=" * 70)
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

        print("-" * 70)

    elapsed = time.time() - start
    minutes, seconds = divmod(int(elapsed), 60)

    print()
    print("=" * 70)
    print("  RESULTS")
    print("=" * 70)
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

    print("=" * 70)


if __name__ == "__main__":
    run_exam()
