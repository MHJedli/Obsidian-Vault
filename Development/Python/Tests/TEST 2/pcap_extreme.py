"""
PCAP-31-03 Mock Exam — EXTREME (50 Questions)
Deep internals, pathological edge cases, uncommon interactions.
If you pass this, you are ready for the real exam.
"""

import time

QUESTIONS = [
    # ── MODULES & PACKAGES ──────────────────────────────────────────────────
    {
        "topic": "Modules & Packages",
        "q": (
            "What does this print?\n\n"
            "    import sys\n"
            "    import math\n"
            "    math.pi = 3\n"
            "    del sys.modules['math']\n"
            "    import math\n"
            "    print(math.pi)"
        ),
        "options": [
            "A) 3 — the modified value persists",
            "B) 3.141592653589793 — re-import reloads fresh copy",
            "C) AttributeError",
            "D) 0"
        ],
        "answer": "B",
        "explanation": "Deleting from sys.modules forces a full re-import on the next import statement. A fresh copy of math is loaded, restoring pi to its original value."
    },
    {
        "topic": "Modules & Packages",
        "q": (
            "What is printed?\n\n"
            "    import importlib\n"
            "    import math\n"
            "    math.pi = 0\n"
            "    importlib.reload(math)\n"
            "    print(math.pi)"
        ),
        "options": [
            "A) 0 — reload preserves mutations",
            "B) 3.141592653589793 — reload re-executes the module",
            "C) ImportError",
            "D) None"
        ],
        "answer": "B",
        "explanation": "importlib.reload() re-executes the module code in the existing module object, resetting all attributes to their original values."
    },
    {
        "topic": "Modules & Packages",
        "q": (
            "A module 'pkg/sub/mod.py' uses: from ... import util\n"
            "How many dots are correct for this relative import?"
        ),
        "options": [
            "A) One dot — current package",
            "B) Two dots — parent package (pkg/sub → pkg)",
            "C) Three dots — grandparent package (pkg/sub → pkg → parent of pkg)",
            "D) SyntaxError — you cannot go up more than one level"
        ],
        "answer": "C",
        "explanation": "Three dots go up three package levels: mod.py is inside sub, which is inside pkg. Three dots reaches the parent of pkg."
    },
    {
        "topic": "Modules & Packages",
        "q": (
            "What does this print?\n\n"
            "    import math\n"
            "    print(type(math))"
        ),
        "options": [
            "A) <class 'package'>",
            "B) <class 'builtin_function_or_method'>",
            "C) <class 'module'>",
            "D) <class 'type'>"
        ],
        "answer": "C",
        "explanation": "All imported modules are instances of the 'module' type. type(math) is <class 'module'>."
    },
    {
        "topic": "Modules & Packages",
        "q": (
            "You call random.choices(['a','b','c'], cum_weights=[10,40,100], k=1).\n"
            "What is the probability of picking 'b'?"
        ),
        "options": ["A) 40%", "B) 10%", "C) 30%", "D) 33.3%"],
        "answer": "C",
        "explanation": "cum_weights are cumulative: 'a'=10, 'b'=40-10=30, 'c'=100-40=60. Total=100. P('b') = 30/100 = 30%."
    },
    {
        "topic": "Modules & Packages",
        "q": (
            "What does math.hypot(3, 4, 0) return?"
        ),
        "options": ["A) 5.0", "B) 7.0", "C) 25.0", "D) TypeError — hypot only takes 2 args"],
        "answer": "A",
        "explanation": "Since Python 3.8, hypot accepts N arguments. sqrt(3^2+4^2+0^2) = sqrt(9+16+0) = sqrt(25) = 5.0."
    },
    {
        "topic": "Modules & Packages",
        "q": (
            "What does this print?\n\n"
            "    import sys\n"
            "    class FakeModule:\n"
            "        pi = 99\n"
            "    sys.modules['math'] = FakeModule()\n"
            "    import math\n"
            "    print(math.pi)"
        ),
        "options": [
            "A) 3.141592...",
            "B) AttributeError",
            "C) 99",
            "D) ImportError"
        ],
        "answer": "C",
        "explanation": "Python checks sys.modules first. A FakeModule instance was inserted, so 'import math' returns it. math.pi is 99."
    },
    {
        "topic": "Modules & Packages",
        "q": (
            "What does random.sample(range(10**9), k=5) do, and why is it efficient?"
        ),
        "options": [
            "A) Creates a list of 10^9 elements then picks 5 — very slow",
            "B) Raises MemoryError",
            "C) Samples 5 unique integers without materialising the entire range",
            "D) Returns 5 zeros — range objects cannot be sampled"
        ],
        "answer": "C",
        "explanation": "random.sample() supports range objects directly via __len__ and __getitem__ — it never materialises the full sequence."
    },
    {
        "topic": "Modules & Packages",
        "q": (
            "What is the __spec__ attribute of a module and what does it contain?"
        ),
        "options": [
            "A) A string with the module's docstring",
            "B) A ModuleSpec object describing the module's name, origin, and loader",
            "C) A dict of all public attributes",
            "D) The module's __all__ list"
        ],
        "answer": "B",
        "explanation": "__spec__ is a ModuleSpec instance. It provides metadata including the module's name, the file it came from (origin), and the loader that imported it."
    },
    {
        "topic": "Modules & Packages",
        "q": (
            "What does this return?\n\n"
            "    import math\n"
            "    getattr(math, 'sqrt')(25)"
        ),
        "options": ["A) 25", "B) 5.0", "C) AttributeError", "D) '5.0'"],
        "answer": "B",
        "explanation": "getattr(math, 'sqrt') retrieves math.sqrt by name. Calling it with 25 returns 5.0."
    },

    # ── OOP ─────────────────────────────────────────────────────────────────
    {
        "topic": "OOP",
        "q": (
            "What does this print?\n\n"
            "    class Meta(type):\n"
            "        def __new__(mcs, name, bases, ns):\n"
            "            ns['extra'] = 42\n"
            "            return super().__new__(mcs, name, bases, ns)\n"
            "    class Foo(metaclass=Meta): pass\n"
            "    print(Foo.extra)"
        ),
        "options": ["A) AttributeError", "B) None", "C) 42", "D) TypeError"],
        "answer": "C",
        "explanation": "The metaclass __new__ injects 'extra' into the namespace before the class is created. Foo.extra = 42."
    },
    {
        "topic": "OOP",
        "q": (
            "What does this print?\n\n"
            "    class A:\n"
            "        def __init_subclass__(cls, **kw):\n"
            "            super().__init_subclass__(**kw)\n"
            "            cls.registered = True\n"
            "    class B(A): pass\n"
            "    print(B.registered)"
        ),
        "options": ["A) AttributeError", "B) False", "C) True", "D) None"],
        "answer": "C",
        "explanation": "__init_subclass__ is called on A whenever a subclass is defined. It injects 'registered=True' into B's namespace."
    },
    {
        "topic": "OOP",
        "q": (
            "What does this output?\n\n"
            "    class Descriptor:\n"
            "        def __get__(self, obj, cls):\n"
            "            return 42\n"
            "    class Foo:\n"
            "        x = Descriptor()\n"
            "    f = Foo()\n"
            "    print(f.x, Foo.x)"
        ),
        "options": [
            "A) 42 42",
            "B) <Descriptor> 42",
            "C) 42 <Descriptor>",
            "D) AttributeError"
        ],
        "answer": "A",
        "explanation": "When obj is None (class access), __get__(self, None, cls) is called. Both instance and class access trigger the descriptor — both return 42."
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
        "explanation": "__new__ returns the cached instance on every call. a and b are the same object — 'is' returns True."
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
        "options": [
            "A) True True",
            "B) False True",
            "C) True False",
            "D) False False"
        ],
        "answer": "B",
        "explanation": "B.__init__ doesn't call super().__init__(), so A's self.x = 1 never runs. Only self.y = 2 is set."
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
        "options": [
            "A) 3",
            "B) AttributeError — __slots__ prevents arbitrary attributes",
            "C) None",
            "D) TypeError"
        ],
        "answer": "B",
        "explanation": "__slots__ prevents the creation of __dict__ on instances. Only 'x' and 'y' can be set — attempting f.z = 3 raises AttributeError."
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
        "options": ["A) []", "B) [1]", "C) AttributeError", "D) [1, 1]"],
        "answer": "B",
        "explanation": "val is a mutable list defined on A. B.val and C.val both resolve to the SAME list on A. Mutating it via B.val.append() is visible via C.val."
    },
    {
        "topic": "OOP",
        "q": (
            "What does this print?\n\n"
            "    class Foo:\n"
            "        def __repr__(self): return 'Foo()'\n"
            "        def __str__(self): return 'a Foo'\n"
            "    f = Foo()\n"
            "    print(f'{f!r}  {f!s}')"
        ),
        "options": [
            "A) a Foo  a Foo",
            "B) Foo()  Foo()",
            "C) Foo()  a Foo",
            "D) a Foo  Foo()"
        ],
        "answer": "C",
        "explanation": "In f-strings, !r forces repr() and !s forces str(). So {f!r} = 'Foo()' and {f!s} = 'a Foo'."
    },
    {
        "topic": "OOP",
        "q": (
            "What is printed?\n\n"
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
        "explanation": "MRO: D→B→C→A. super() in D calls B, super() in B calls C (next in MRO, not A), super() in C calls A. Print order: D B C A."
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
        "explanation": "f has no instance variable 'x', so Python looks it up on Foo. Foo.x was changed to 2 after f was created. f.x = 2."
    },

    # ── EXCEPTIONS ──────────────────────────────────────────────────────────
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
        "options": [
            "A) inner then outer",
            "B) inner then ValueError propagates",
            "C) outer",
            "D) inner only"
        ],
        "answer": "B",
        "explanation": "'inner' is printed by the nested handler. Bare 'raise' re-raises the outer ValueError. The second 'except Exception' is in the same try — it won't re-catch. ValueError propagates."
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
        "options": ["A) except", "B) ValueError raised", "C) finally", "D) except then finally"],
        "answer": "C",
        "explanation": "A return inside finally overrides any return or raised exception from try/except. 'finally' is returned."
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
        "options": [
            "A) a None",
            "B) a b",
            "C) b a",
            "D) ValueError: a"
        ],
        "answer": "B",
        "explanation": "str(e) = 'a' (the raised exception's message). e.__cause__ is the ValueError('b'), str gives 'b'."
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
        "options": [
            "A) (404,) 404",
            "B) () 404",
            "C) (404,) AttributeError",
            "D) () AttributeError"
        ],
        "answer": "B",
        "explanation": "Err.__init__ does NOT call super().__init__(), so nothing is passed to Exception. e.args is an empty tuple (). e.code = 404."
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
        "options": [
            "A) Exception",
            "B) ZeroDivisionError",
            "C) ArithmeticError",
            "D) None"
        ],
        "answer": "B",
        "explanation": "sys.exc_info() returns (type, value, traceback). exc[0] is the exception class — ZeroDivisionError."
    },
    {
        "topic": "Exceptions",
        "q": (
            "What is printed?\n\n"
            "    try:\n"
            "        open('missing_xyz')\n"
            "    except FileNotFoundError as e:\n"
            "        print(issubclass(type(e), OSError))"
        ),
        "options": ["A) False", "B) TypeError", "C) None", "D) True"],
        "answer": "D",
        "explanation": "FileNotFoundError is a subclass of OSError. issubclass(FileNotFoundError, OSError) is True."
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
        "options": [
            "A) AssertionError('test')",
            "B) 'test'",
            "C) False",
            "D) AssertionError()"
        ],
        "answer": "A",
        "explanation": "repr(e) for an AssertionError with message 'test' is AssertionError('test')."
    },
    {
        "topic": "Exceptions",
        "q": (
            "What happens when an exception is raised inside a finally block?"
        ),
        "options": [
            "A) The original exception is chained to the new one automatically",
            "B) The original exception is silently discarded and the new one propagates",
            "C) Both exceptions are raised simultaneously",
            "D) The finally exception is swallowed"
        ],
        "answer": "B",
        "explanation": "A new exception in finally replaces (silently discards) any exception from try/except. Only the finally exception propagates."
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
        "options": [
            "A) ValueError()",
            "B) NameError: e is not defined",
            "C) None",
            "D) ''"
        ],
        "answer": "B",
        "explanation": "Python deletes the 'as e' variable when the except block exits. Accessing 'e' after the block raises NameError."
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
        "options": [
            "A) x",
            "B) base!",
            "C) Child: x",
            "D) Base: base!"
        ],
        "answer": "B",
        "explanation": "Child inherits __str__ from Base. str(e) calls Base.__str__ which returns 'base!'. The 'x' argument is ignored by this __str__."
    },

    # ── FILE I/O ─────────────────────────────────────────────────────────────
    {
        "topic": "File I/O",
        "q": (
            "What does this print?\n\n"
            "    import io\n"
            "    s = io.StringIO('hello\\nworld\\n')\n"
            "    lines = s.readlines()\n"
            "    print(len(lines), repr(lines[0]))"
        ),
        "options": [
            "A) 2 'hello'",
            "B) 2 'hello\\n'",
            "C) 1 'hello\\nworld\\n'",
            "D) 3 'hello\\n'"
        ],
        "answer": "B",
        "explanation": "readlines() keeps the newline. 'hello\\n' and 'world\\n' are two elements. lines[0] = 'hello\\n'."
    },
    {
        "topic": "File I/O",
        "q": (
            "What does this code print?\n\n"
            "    ba = bytearray(b'\\x00' * 4)\n"
            "    import struct\n"
            "    struct.pack_into('>I', ba, 0, 255)\n"
            "    print(list(ba))"
        ),
        "options": [
            "A) [255, 0, 0, 0]",
            "B) [0, 0, 0, 255]",
            "C) [0, 255, 0, 0]",
            "D) [0, 0, 255, 0]"
        ],
        "answer": "B",
        "explanation": "'>I' is big-endian unsigned int. 255 = 0x000000FF. In big-endian order: [0, 0, 0, 255]."
    },
    {
        "topic": "File I/O",
        "q": (
            "What does sys.stdout.write('hello') return?"
        ),
        "options": ["A) None", "B) True", "C) 5", "D) 'hello'"],
        "answer": "C",
        "explanation": "write() returns the number of characters written. 'hello' is 5 characters, so it returns 5."
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
        "options": [
            "A) 'captured'",
            "B) 'captured\\n'",
            "C) captured",
            "D) Nothing — print was redirected"
        ],
        "answer": "B",
        "explanation": "print() appends '\\n'. The StringIO captured 'captured\\n'. After restoring stdout, repr(val) = \"'captured\\\\n'\"."
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
        "options": [
            "A) '\\xff\\xfe'",
            "B) ''",
            "C) UnicodeDecodeError",
            "D) '??'"
        ],
        "answer": "B",
        "explanation": "0xFF 0xFE is not valid UTF-8. errors='ignore' silently drops undecodable bytes. The result is an empty string ''."
    },
    {
        "topic": "File I/O",
        "q": (
            "What is the correct way to read a large binary file in 64KB chunks without wasting memory?"
        ),
        "options": [
            "A) data = f.read(); process in chunks after",
            "B) buf = bytearray(65536); while n := f.readinto(buf): process(buf[:n])",
            "C) for line in f: process(line)",
            "D) f.readlines() then slice"
        ],
        "answer": "B",
        "explanation": "Pre-allocating a bytearray and using readinto avoids creating new bytes objects. The walrus operator captures the byte count. This is the most memory-efficient pattern."
    },
    {
        "topic": "File I/O",
        "q": (
            "What does f.seek(-5, 2) do on a file of 100 bytes?"
        ),
        "options": [
            "A) Seeks to byte 5 from the start",
            "B) Seeks to byte 95 (5 bytes before the end)",
            "C) Raises ValueError — negative offsets not allowed",
            "D) Seeks 5 bytes back from current position"
        ],
        "answer": "B",
        "explanation": "seek(offset, 2) seeks relative to end-of-file. -5 bytes from the end of a 100-byte file is position 95."
    },
    {
        "topic": "File I/O",
        "q": (
            "What does this print after writing 'hello' to a file and immediately reading it?\n\n"
            "    with open('t.txt','w+') as f:\n"
            "        f.write('hello')\n"
            "        print(repr(f.read()))"
        ),
        "options": [
            "A) 'hello'",
            "B) ''",
            "C) FileNotFoundError",
            "D) None"
        ],
        "answer": "B",
        "explanation": "After write(), the cursor is at position 5 (end of file). read() from there returns '' — no data left to read. Use f.seek(0) first to read from the beginning."
    },
    {
        "topic": "File I/O",
        "q": (
            "What does bytearray(b'ABC') == bytes(b'ABC') evaluate to?"
        ),
        "options": [
            "A) True — they compare equal by value",
            "B) False — different types are never equal",
            "C) TypeError",
            "D) NotImplemented"
        ],
        "answer": "A",
        "explanation": "bytearray and bytes support cross-type equality. bytearray(b'ABC') == b'ABC' is True."
    },
    {
        "topic": "File I/O",
        "q": (
            "What is printed?\n\n"
            "    import io\n"
            "    buf = io.BytesIO(b'ABCDE')\n"
            "    buf.seek(2)\n"
            "    print(buf.read(2))\n"
            "    print(buf.tell())"
        ),
        "options": [
            "A) b'AB' then 2",
            "B) b'CD' then 4",
            "C) b'CE' then 5",
            "D) b'CD' then 2"
        ],
        "answer": "B",
        "explanation": "seek(2) positions cursor at index 2. read(2) reads bytes at index 2 and 3: b'CD'. tell() returns 4."
    },

    # ── COMPREHENSIONS & LAMBDAS ─────────────────────────────────────────────
    {
        "topic": "Comprehensions & Lambdas",
        "q": (
            "What does this print?\n\n"
            "    x = 10\n"
            "    result = [x for x in range(3)]\n"
            "    print(x, result)"
        ),
        "options": [
            "A) 2 [0, 1, 2]",
            "B) 10 [0, 1, 2]",
            "C) 10 [10, 10, 10]",
            "D) 2 [10, 10, 10]"
        ],
        "answer": "B",
        "explanation": "List comprehensions have their own scope in Python 3. The 'x' inside does NOT leak. The outer x stays 10."
    },
    {
        "topic": "Comprehensions & Lambdas",
        "q": (
            "What does this return?\n\n"
            "    from functools import reduce\n"
            "    reduce(lambda a, b: a + [b], range(4), [])"
        ),
        "options": [
            "A) 6",
            "B) [0, 1, 2, 3]",
            "C) [[0], [1], [2], [3]]",
            "D) [[], 0, 1, 2, 3]"
        ],
        "answer": "B",
        "explanation": "reduce starts with accumulator []. Each step appends one element: []+[0]=[0], [0]+[1]=[0,1], etc. Result: [0,1,2,3]."
    },
    {
        "topic": "Comprehensions & Lambdas",
        "q": (
            "What does this produce?\n\n"
            "    nested = [[i*j for j in range(1,4)] for i in range(1,4)]\n"
            "    print(nested[1][2])"
        ),
        "options": ["A) 2", "B) 6", "C) 4", "D) 9"],
        "answer": "B",
        "explanation": "nested[1] is row i=2: [2*1,2*2,2*3]=[2,4,6]. nested[1][2] = 6."
    },
    {
        "topic": "Comprehensions & Lambdas",
        "q": (
            "What does this return?\n\n"
            "    f = lambda *args, **kw: (args, kw)\n"
            "    f(1, 2, x=3, y=4)"
        ),
        "options": [
            "A) ((1, 2), {'x': 3, 'y': 4})",
            "B) TypeError",
            "C) (1, 2, 3, 4)",
            "D) ((1, 2, 3, 4), {})"
        ],
        "answer": "A",
        "explanation": "Lambdas support *args and **kwargs. Positional args become a tuple, keyword args become a dict."
    },
    {
        "topic": "Comprehensions & Lambdas",
        "q": (
            "What does this print?\n\n"
            "    gen = (x for x in range(10) if x % 3 == 0)\n"
            "    print(list(gen))\n"
            "    print(list(gen))"
        ),
        "options": [
            "A) [0,3,6,9] then [0,3,6,9]",
            "B) [0,3,6,9] then []",
            "C) [0,3,6,9] then StopIteration",
            "D) [] then []"
        ],
        "answer": "B",
        "explanation": "Generators are single-use. After list(gen) exhausts it, a second list(gen) returns [] — the generator is done."
    },

    # ── CLOSURES ────────────────────────────────────────────────────────────
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
        "explanation": "Using x=i as a default argument captures the value of i at definition time. Each inner function gets its own x: 0, 1, 2."
    },
    {
        "topic": "Closures",
        "q": (
            "What does this print?\n\n"
            "    def make():\n"
            "        fns = []\n"
            "        for i in range(3):\n"
            "            fns.append(lambda: i)\n"
            "        return fns\n"
            "    fns = make()\n"
            "    print(fns[0](), fns[1](), fns[2]())"
        ),
        "options": ["A) 0 1 2", "B) 2 2 2", "C) 0 0 0", "D) NameError"],
        "answer": "B",
        "explanation": "Classic late-binding: all lambdas capture the same variable 'i'. After the loop, i=2. All three return 2."
    },
    {
        "topic": "Closures",
        "q": (
            "What does this print?\n\n"
            "    def outer():\n"
            "        x = 1\n"
            "        def middle():\n"
            "            x = 2\n"
            "            def inner():\n"
            "                nonlocal x\n"
            "                x = 3\n"
            "            inner()\n"
            "            print('middle x:', x)\n"
            "        middle()\n"
            "        print('outer x:', x)\n"
            "    outer()"
        ),
        "options": [
            "A) middle x: 3 | outer x: 3",
            "B) middle x: 3 | outer x: 1",
            "C) middle x: 2 | outer x: 1",
            "D) middle x: 2 | outer x: 3"
        ],
        "answer": "B",
        "explanation": "'nonlocal x' in inner refers to MIDDLE's x (nearest enclosing that has x). middle's x becomes 3. outer's x stays 1."
    },
    {
        "topic": "Closures",
        "q": (
            "What does this print?\n\n"
            "    def adder(x):\n"
            "        def inner(y):\n"
            "            return x + y\n"
            "        return inner\n"
            "    add5 = adder(5)\n"
            "    add5.__closure__[0].cell_contents = 100\n"
            "    print(add5(1))"
        ),
        "options": [
            "A) 6",
            "B) 101",
            "C) AttributeError — cell_contents is read-only",
            "D) TypeError"
        ],
        "answer": "C",
        "explanation": "cell_contents is a read-only attribute in CPython. Attempting to assign to it raises AttributeError."
    },
    {
        "topic": "Closures",
        "q": (
            "What does this print?\n\n"
            "    def counter(start=0):\n"
            "        n = start\n"
            "        def inc(): nonlocal n; n += 1; return n\n"
            "        def dec(): nonlocal n; n -= 1; return n\n"
            "        def val(): return n\n"
            "        return inc, dec, val\n"
            "    inc, dec, val = counter(10)\n"
            "    inc(); inc(); dec()\n"
            "    print(val())"
        ),
        "options": ["A) 10", "B) 11", "C) 12", "D) 9"],
        "answer": "B",
        "explanation": "Start 10. inc()→11, inc()→12, dec()→11. val() returns the shared n = 11."
    },
    {
        "topic": "Closures",
        "q": (
            "What does this output?\n\n"
            "    def memoize(f):\n"
            "        cache = {}\n"
            "        def wrapper(*args):\n"
            "            if args not in cache:\n"
            "                cache[args] = f(*args)\n"
            "            return cache[args]\n"
            "        return wrapper\n"
            "    @memoize\n"
            "    def add(a, b): return a + b\n"
            "    print(add(1,2), add(1,2), len(add.__closure__[0].cell_contents))"
        ),
        "options": [
            "A) 3 3 1",
            "B) 3 3 0",
            "C) 3 6 1",
            "D) TypeError"
        ],
        "answer": "A",
        "explanation": "add(1,2) = 3 twice (from cache second time). The cache dict has 1 entry: {(1,2): 3}. len = 1."
    },
]


def run_exam():
    print("=" * 72)
    print("  PCAP-31-03 MOCK EXAM — EXTREME LEVEL")
    print("  50 Questions | Pass mark: 70% (35/50)")
    print("  Deep internals, pathological edge cases, uncommon interactions.")
    print("  Warning: this is harder than the real exam.")
    print("=" * 72)
    print()

    score = 0
    topic_scores = {}
    wrong_list = []
    start = time.time()

    for i, q in enumerate(QUESTIONS, 1):
        topic = q["topic"]
        if topic not in topic_scores:
            topic_scores[topic] = {"correct": 0, "total": 0}
        topic_scores[topic]["total"] += 1

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
            topic_scores[topic]["correct"] += 1
        else:
            print(f"  ✗ Wrong. Correct answer: {q['answer']}")
            print(f"  Explanation: {q['explanation']}\n")
            wrong_list.append((i, q))

        print("-" * 72)

    elapsed = time.time() - start
    minutes, seconds = divmod(int(elapsed), 60)
    pct = score * 2

    print()
    print("=" * 72)
    print("  RESULTS")
    print("=" * 72)
    print(f"  Score      : {score} / 50  ({pct}%)")
    print(f"  Time taken : {minutes}m {seconds}s")
    print(f"  Pass mark  : 35 / 50  (70%)")
    passed = score >= 35
    print(f"  Result     : {'PASS ✓' if passed else 'FAIL ✗'}")
    print()

    print("  Score by topic:")
    for topic, data in topic_scores.items():
        bar_len = int(data["correct"] / max(data["total"], 1) * 20)
        bar = "█" * bar_len + "░" * (20 - bar_len)
        print(f"    {topic:<28} {data['correct']:>2}/{data['total']:<2}  {bar}")
    print()

    if wrong_list:
        print(f"  Review — questions you missed ({len(wrong_list)}):")
        for num, q in wrong_list:
            first_line = q["q"].split("\n")[0][:60]
            print(f"    Q{num:02d} [{q['topic']}]: {first_line}...")
            print(f"         Correct: {q['answer']} — {q['explanation']}")
            print()

    if passed:
        print("  Outstanding! You are ready for the real PCAP-31-03 exam.")
    elif pct >= 55:
        print("  Close — focus on the topics where you missed the most.")
    else:
        print("  Keep going — revisit the fundamentals and retry.")

    print("=" * 72)


if __name__ == "__main__":
    run_exam()