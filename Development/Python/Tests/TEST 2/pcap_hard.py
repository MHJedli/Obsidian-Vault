"""
PCAP-31-03 Mock Exam — HARD (50 Questions)
Edge cases, multi-step reasoning, tricky output prediction.
Covers the full PCAP-31-03 syllabus at exam-depth.
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
            "    del sys.modules['math']\n"
            "    import math\n"
            "    print('ok')"
        ),
        "options": [
            "A) ModuleNotFoundError",
            "B) ok",
            "C) None",
            "D) ImportError"
        ],
        "answer": "B",
        "explanation": "Deleting from sys.modules forces Python to re-import on the next 'import math'. The module is found again and 'ok' is printed."
    },
    {
        "topic": "Modules & Packages",
        "q": (
            "What does this print?\n\n"
            "    import math\n"
            "    math.pi = 3\n"
            "    import math\n"
            "    print(math.pi)"
        ),
        "options": ["A) 3.141592...", "B) 3", "C) AttributeError", "D) TypeError"],
        "answer": "B",
        "explanation": "Modules are cached in sys.modules. The second 'import math' returns the cached object — which already has pi=3. The modification persists."
    },
    {
        "topic": "Modules & Packages",
        "q": (
            "A package has this __init__.py:\n\n"
            "    from .models import User\n"
            "    __all__ = ['User']\n\n"
            "Which statement is TRUE?"
        ),
        "options": [
            "A) 'from pkg import *' exports nothing",
            "B) 'from pkg import User' raises ImportError",
            "C) 'from pkg import *' exports only User",
            "D) __all__ prevents direct imports"
        ],
        "answer": "C",
        "explanation": "__all__ controls wildcard imports. 'from pkg import *' will only import names listed in __all__, so only User."
    },
    {
        "topic": "Modules & Packages",
        "q": (
            "What does this print?\n\n"
            "    from math import sqrt as s\n"
            "    print(s(16), s.__name__)"
        ),
        "options": [
            "A) 4.0 's'",
            "B) 4.0 'sqrt'",
            "C) 4 'sqrt'",
            "D) AttributeError"
        ],
        "answer": "B",
        "explanation": "'as s' creates a local alias. s is still the same function object — __name__ is 'sqrt', the original function name."
    },
    {
        "topic": "Modules & Packages",
        "q": (
            "What is the difference between pkgutil.iter_modules() and "
            "pkgutil.walk_packages()?"
        ),
        "options": [
            "A) iter_modules returns a generator; walk_packages returns a list",
            "B) iter_modules goes one level deep; walk_packages descends recursively",
            "C) walk_packages only works on namespace packages",
            "D) They are identical"
        ],
        "answer": "B",
        "explanation": "iter_modules yields immediate submodules only. walk_packages recursively yields all descendants of a package tree."
    },
    {
        "topic": "Modules & Packages",
        "q": (
            "What does this print?\n\n"
            "    import math\n"
            "    print(math.__spec__.origin)"
        ),
        "options": [
            "A) 'math'",
            "B) The full file path to the math module",
            "C) 'built-in'",
            "D) None"
        ],
        "answer": "C",
        "explanation": "math is a built-in module (compiled into CPython). Its __spec__.origin is 'built-in'."
    },
    {
        "topic": "Modules & Packages",
        "q": (
            "Given: random.seed(1); a=random.random(); random.seed(1); random.random(); b=random.random()\n"
            "Is a == b?"
        ),
        "options": [
            "A) Yes — same seed always gives same value",
            "B) No — b is the 2nd value of seed(1)'s sequence, not the 1st",
            "C) Yes — random.random() always returns the same value",
            "D) TypeError"
        ],
        "answer": "B",
        "explanation": "Both use seed(1), but 'a' is the 1st draw and 'b' is the 2nd draw. The seed resets the sequence, not the call count."
    },
    {
        "topic": "Modules & Packages",
        "q": "What happens when you add a path to the front of sys.path at runtime?",
        "options": [
            "A) It only affects future imports in the same file",
            "B) It raises AttributeError",
            "C) The added directory is searched first for all subsequent imports in the process",
            "D) It permanently modifies sys.path across sessions"
        ],
        "answer": "C",
        "explanation": "sys.path is searched in order. Inserting at index 0 gives that path the highest priority for all future imports in the running process."
    },
    {
        "topic": "Modules & Packages",
        "q": (
            "What does 'from math import *' import if math defines "
            "__all__ = ['sqrt', 'pi']?"
        ),
        "options": [
            "A) Everything in math",
            "B) Only sqrt and pi",
            "C) Everything except sqrt and pi",
            "D) Nothing — wildcard imports are blocked by __all__"
        ],
        "answer": "B",
        "explanation": "When __all__ is defined, 'import *' imports ONLY the names listed in __all__."
    },
    {
        "topic": "Modules & Packages",
        "q": (
            "What does math.trunc(-4.9) return?"
        ),
        "options": ["A) -5", "B) -4", "C) 4", "D) 5"],
        "answer": "B",
        "explanation": "trunc() removes the decimal part — it always truncates toward zero. trunc(-4.9) = -4. floor(-4.9) would be -5."
    },

    # ── OOP ─────────────────────────────────────────────────────────────────
    {
        "topic": "OOP",
        "q": (
            "What does this print?\n\n"
            "    class A:\n"
            "        def greet(self):\n"
            "            return 'A'\n"
            "    class B(A):\n"
            "        def greet(self):\n"
            "            return 'B+' + super().greet()\n"
            "    class C(A):\n"
            "        def greet(self):\n"
            "            return 'C+' + super().greet()\n"
            "    class D(B, C):\n"
            "        def greet(self):\n"
            "            return 'D+' + super().greet()\n"
            "    print(D().greet())"
        ),
        "options": ["A) D+B+A", "B) D+C+A", "C) D+B+C+A", "D) TypeError"],
        "answer": "C",
        "explanation": "MRO: D→B→C→A. super() in D calls B.greet; super() in B calls C.greet (next in MRO); super() in C calls A.greet. Chain: D+B+C+A."
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
        "options": [
            "A) {'__x': 10}",
            "B) {'x': 10}",
            "C) {'_Foo__x': 10}",
            "D) AttributeError"
        ],
        "answer": "C",
        "explanation": "Name mangling rewrites __x to _Foo__x. The actual key in __dict__ is '_Foo__x'."
    },
    {
        "topic": "OOP",
        "q": (
            "What is printed?\n\n"
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
        "explanation": "Counter.count is incremented twice (once per __init__ call). Both a.count and Counter.count read the same class variable: 2."
    },
    {
        "topic": "OOP",
        "q": (
            "What does this print?\n\n"
            "    class A:\n"
            "        x = 1\n"
            "    class B(A):\n"
            "        pass\n"
            "    b = B()\n"
            "    b.x = 99\n"
            "    print(A.x, B.x, b.x)"
        ),
        "options": ["A) 99 99 99", "B) 1 1 99", "C) 1 99 99", "D) AttributeError"],
        "answer": "B",
        "explanation": "b.x = 99 creates an instance variable on b. A.x and B.x both still return 1 via the class hierarchy."
    },
    {
        "topic": "OOP",
        "q": (
            "What does this output?\n\n"
            "    class MyClass:\n"
            "        def __str__(self): return 'str_result'\n"
            "        def __repr__(self): return 'repr_result'\n"
            "    obj = MyClass()\n"
            "    print([obj])"
        ),
        "options": [
            "A) [str_result]",
            "B) ['str_result']",
            "C) [repr_result]",
            "D) ['repr_result']"
        ],
        "answer": "C",
        "explanation": "Inside containers (list, dict), Python uses __repr__, not __str__. print([obj]) displays [repr_result]."
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
        "options": [
            "A) {'name': 'Rex'}",
            "B) {'breed': 'Lab'}",
            "C) {'name': 'Rex', 'breed': 'Lab'}",
            "D) {'Dog': {'name': 'Rex', 'breed': 'Lab'}}"
        ],
        "answer": "C",
        "explanation": "super().__init__(name) sets self.name. The child adds self.breed. vars(d) returns both instance attributes."
    },
    {
        "topic": "OOP",
        "q": (
            "What does type(type) return?"
        ),
        "options": ["A) object", "B) class", "C) type", "D) metaclass"],
        "answer": "C",
        "explanation": "type is its own metaclass. type(type) returns type — it is an instance of itself."
    },
    {
        "topic": "OOP",
        "q": (
            "What does this print?\n\n"
            "    class Foo:\n"
            "        def method(self): return 'instance'\n"
            "        @classmethod\n"
            "        def cm(cls): return cls.__name__\n"
            "        @staticmethod\n"
            "        def sm(): return 'static'\n"
            "    print(Foo.cm(), Foo.sm())"
        ),
        "options": [
            "A) 'instance' 'static'",
            "B) 'Foo' 'static'",
            "C) 'Foo' 'Foo'",
            "D) TypeError"
        ],
        "answer": "B",
        "explanation": "cm() receives cls=Foo, so cls.__name__ is 'Foo'. sm() has no automatic arguments — returns 'static'."
    },
    {
        "topic": "OOP",
        "q": (
            "What does issubclass(bool, int) return?"
        ),
        "options": ["A) False", "B) TypeError", "C) None", "D) True"],
        "answer": "D",
        "explanation": "bool is a subclass of int in Python. True == 1 and False == 0. issubclass(bool, int) is True."
    },
    {
        "topic": "OOP",
        "q": (
            "Given class Child(Parent1, Parent2), and both parents define method foo(),\n"
            "which foo() does Child().foo() call if Child does not override it?"
        ),
        "options": [
            "A) Parent2's foo() — last one wins",
            "B) Raises AttributeError — ambiguous",
            "C) Parent1's foo() — leftmost parent in MRO",
            "D) A merged version of both"
        ],
        "answer": "C",
        "explanation": "Python's MRO searches left to right. Parent1 comes before Parent2, so Parent1.foo() is found first."
    },

    # ── EXCEPTIONS ──────────────────────────────────────────────────────────
    {
        "topic": "Exceptions",
        "q": (
            "What does this print?\n\n"
            "    def f():\n"
            "        try:\n"
            "            return 1\n"
            "        finally:\n"
            "            return 2\n"
            "    print(f())"
        ),
        "options": ["A) 1", "B) 2", "C) (1, 2)", "D) None"],
        "answer": "B",
        "explanation": "A return inside finally overrides the try's return. The function returns 2, not 1."
    },
    {
        "topic": "Exceptions",
        "q": (
            "What does this print?\n\n"
            "    class AppError(Exception): pass\n"
            "    class DBError(AppError): pass\n"
            "    try:\n"
            "        raise DBError('conn lost')\n"
            "    except AppError as e:\n"
            "        print(type(e).__name__, str(e))"
        ),
        "options": [
            "A) AppError conn lost",
            "B) DBError conn lost",
            "C) Exception conn lost",
            "D) Not caught — falls through"
        ],
        "answer": "B",
        "explanation": "DBError is caught because it inherits from AppError. type(e).__name__ is 'DBError' — the actual raised type, not the handler type."
    },
    {
        "topic": "Exceptions",
        "q": (
            "What is the output?\n\n"
            "    try:\n"
            "        try:\n"
            "            raise ValueError('inner')\n"
            "        finally:\n"
            "            print('inner finally')\n"
            "    except ValueError:\n"
            "        print('outer except')"
        ),
        "options": [
            "A) outer except",
            "B) inner finally",
            "C) inner finally then outer except",
            "D) outer except then inner finally"
        ],
        "answer": "C",
        "explanation": "The inner finally runs first (always), then the exception propagates to the outer except block."
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
        "options": ["A) KeyError", "B) None", "C) ValueError", "D) AttributeError"],
        "answer": "C",
        "explanation": "'from ValueError' sets e.__cause__ to a ValueError instance. Its type name is 'ValueError'."
    },
    {
        "topic": "Exceptions",
        "q": (
            "What is the value of e.args after:\n\n"
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
        "explanation": "super().__init__(msg) passes only 'msg' to Exception.__init__. e.args = ('not found',). The code is stored in e.code only."
    },
    {
        "topic": "Exceptions",
        "q": (
            "What is the output?\n\n"
            "    try:\n"
            "        x = [1,2,3][10]\n"
            "    except (IndexError, KeyError):\n"
            "        print('lookup')\n"
            "    except Exception:\n"
            "        print('general')"
        ),
        "options": ["A) general", "B) lookup", "C) Nothing printed — error propagates", "D) Both printed"],
        "answer": "B",
        "explanation": "List index out of range raises IndexError. The grouped handler catches it, printing 'lookup'. The general handler is not reached."
    },
    {
        "topic": "Exceptions",
        "q": (
            "What does this assert statement do?\n\n"
            "    assert (x := 5) > 0, f'got {x}'"
        ),
        "options": [
            "A) SyntaxError — walrus operator not allowed in assert",
            "B) Assigns x=5, checks 5>0 (True), no exception raised",
            "C) Always raises AssertionError",
            "D) Prints 'got 5'"
        ],
        "answer": "B",
        "explanation": "The walrus operator := is valid inside assert. 5>0 is True so no exception is raised. x is assigned 5."
    },
    {
        "topic": "Exceptions",
        "q": (
            "What exception hierarchy is TRUE?\n"
            "BaseException → Exception → LookupError → IndexError"
        ),
        "options": [
            "A) False — IndexError inherits directly from Exception",
            "B) True — that is the exact inheritance chain",
            "C) False — LookupError doesn't exist",
            "D) False — IndexError inherits from ValueError"
        ],
        "answer": "B",
        "explanation": "The chain is BaseException → Exception → LookupError → IndexError. KeyError is also a LookupError."
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
        "options": [
            "A) no error then 5.0",
            "B) 5.0",
            "C) None",
            "D) no error"
        ],
        "answer": "B",
        "explanation": "The 'return a/b' in try exits the function before else can run. The else block is skipped because the function already returned."
    },
    {
        "topic": "Exceptions",
        "q": (
            "What is printed?\n\n"
            "    import errno, os\n"
            "    try:\n"
            "        open('no_such_file_xyz.txt')\n"
            "    except OSError as e:\n"
            "        print(e.errno == errno.ENOENT)"
        ),
        "options": ["A) False", "B) AttributeError", "C) None", "D) True"],
        "answer": "D",
        "explanation": "Opening a non-existent file raises FileNotFoundError (subclass of OSError) with errno.ENOENT (2). The comparison is True."
    },
    {
        "topic": "Exceptions",
        "q": (
            "What does 'except Exception as e' do to 'e' after the except block ends?"
        ),
        "options": [
            "A) e remains in scope until the function returns",
            "B) e is stored in sys.last_value",
            "C) e is deleted automatically when the except block exits",
            "D) e becomes None"
        ],
        "answer": "C",
        "explanation": "Python explicitly deletes the 'as e' variable when the except block exits, to break reference cycles with tracebacks."
    },

    # ── FILE I/O ─────────────────────────────────────────────────────────────
    {
        "topic": "File I/O",
        "q": (
            "What does this produce?\n\n"
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
        "explanation": "'r+' opens without truncating. seek(2) moves to position 2. write('XY') overwrites characters 2 and 3, giving abXYe."
    },
    {
        "topic": "File I/O",
        "q": (
            "What does this print?\n\n"
            "    import io\n"
            "    buf = io.StringIO()\n"
            "    buf.write('hello')\n"
            "    buf.write(' world')\n"
            "    buf.seek(0)\n"
            "    print(buf.read())"
        ),
        "options": ["A) hello", "B) world", "C) hello world", "D) '"],
        "answer": "C",
        "explanation": "StringIO is an in-memory text buffer. After writing both strings and seeking to 0, read() returns the full 'hello world'."
    },
    {
        "topic": "File I/O",
        "q": (
            "A bytearray is created: ba = bytearray(b'ABCDE')\n"
            "What does ba[1:3] = b'xy' do?"
        ),
        "options": [
            "A) Raises TypeError — bytearrays are immutable",
            "B) Inserts 'xy' at position 1 without removing anything",
            "C) Replaces bytes at positions 1 and 2 with 'x' and 'y'",
            "D) Appends 'xy' to the end"
        ],
        "answer": "C",
        "explanation": "bytearray supports slice assignment. ba[1:3] = b'xy' replaces the slice (B, C) with (x, y), giving bytearray(b'AxyDE')."
    },
    {
        "topic": "File I/O",
        "q": (
            "What is the difference between f.write() and f.writelines()?"
        ),
        "options": [
            "A) writelines() adds newlines automatically; write() does not",
            "B) write() accepts a string; writelines() accepts an iterable of strings — neither adds newlines",
            "C) writelines() is only for binary files",
            "D) write() flushes after each call; writelines() buffers"
        ],
        "answer": "B",
        "explanation": "write(s) writes one string. writelines(seq) writes each string in the iterable — no newlines are inserted automatically."
    },
    {
        "topic": "File I/O",
        "q": (
            "What does sys.stdout = io.StringIO() do to print()?"
        ),
        "options": [
            "A) Raises AttributeError",
            "B) print() raises TypeError",
            "C) print() writes to the StringIO buffer instead of the terminal",
            "D) print() is silenced entirely"
        ],
        "answer": "C",
        "explanation": "print() writes to sys.stdout. Replacing sys.stdout with a StringIO redirects all print() calls to the in-memory buffer."
    },
    {
        "topic": "File I/O",
        "q": (
            "What happens to a file opened in 'a' mode when you seek(0) and write()?"
        ),
        "options": [
            "A) Writing always occurs at the current cursor position",
            "B) On most systems, 'a' mode forces all writes to the end regardless of seek",
            "C) The file is truncated at position 0",
            "D) seek() raises UnsupportedOperation in 'a' mode"
        ],
        "answer": "B",
        "explanation": "The OS-level O_APPEND flag in 'a' mode forces every write to the end of file atomically, ignoring seek position."
    },
    {
        "topic": "File I/O",
        "q": (
            "What does errors='replace' do when opening a file in text mode?"
        ),
        "options": [
            "A) Raises UnicodeDecodeError on bad bytes",
            "B) Silently skips undecodable bytes",
            "C) Replaces undecodable bytes with the Unicode replacement character ?",
            "D) Re-encodes the file using ASCII"
        ],
        "answer": "C",
        "explanation": "errors='replace' substitutes the replacement character (U+FFFD, often displayed as ?) for bytes that cannot be decoded."
    },
    {
        "topic": "File I/O",
        "q": (
            "What does f.readinto(buf) return?"
        ),
        "options": [
            "A) The entire buffer contents as bytes",
            "B) The number of bytes actually read",
            "C) True on success, False at EOF",
            "D) A new bytearray with the data"
        ],
        "answer": "B",
        "explanation": "readinto() fills the buffer in-place and returns the count of bytes read. Check if 0 to detect EOF."
    },
    {
        "topic": "File I/O",
        "q": (
            "What does f.flush() do?"
        ),
        "options": [
            "A) Closes the file",
            "B) Discards unread data",
            "C) Forces buffered writes to be sent to the OS immediately",
            "D) Resets the cursor to position 0"
        ],
        "answer": "C",
        "explanation": "Python buffers writes in memory. flush() forces the buffer to be written to the OS file system without closing the file."
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
        "explanation": "ba[0] = 72 sets the first byte to 72, which is the ASCII code for 'H'. Decoding gives 'Hello'."
    },

    # ── COMPREHENSIONS & LAMBDAS ─────────────────────────────────────────────
    {
        "topic": "Comprehensions & Lambdas",
        "q": (
            "What does this produce?\n\n"
            "    matrix = [[1,2,3],[4,5,6],[7,8,9]]\n"
            "    flat = [n for row in matrix for n in row if n % 2 == 0]\n"
            "    print(flat)"
        ),
        "options": ["A) [2, 4, 6, 8]", "B) [1, 3, 5, 7, 9]", "C) [[2], [4, 6], [8]]", "D) [2, 6]"],
        "answer": "A",
        "explanation": "Flattens the matrix then filters even numbers: 2, 4, 6, 8."
    },
    {
        "topic": "Comprehensions & Lambdas",
        "q": (
            "What is the output?\n\n"
            "    funcs = [lambda i=i: i for i in range(5)]\n"
            "    print(funcs[0](), funcs[4]())"
        ),
        "options": ["A) 4 4", "B) 0 0", "C) 0 4", "D) 4 0"],
        "answer": "C",
        "explanation": "Using i=i as a default argument captures the value at definition time. Each lambda gets its own copy of i."
    },
    {
        "topic": "Comprehensions & Lambdas",
        "q": (
            "What does this produce?\n\n"
            "    result = {v: k for k, v in {'a':1,'b':2,'c':3}.items()}\n"
            "    print(result)"
        ),
        "options": [
            "A) {'a':1, 'b':2, 'c':3}",
            "B) {1:'a', 2:'b', 3:'c'}",
            "C) {1:'a', 2:'b', 3:'c'} — TypeError if values not unique",
            "D) SyntaxError"
        ],
        "answer": "B",
        "explanation": "The dict comprehension swaps keys and values. k=letter, v=number → {number: letter}."
    },
    {
        "topic": "Comprehensions & Lambdas",
        "q": (
            "What does this return?\n\n"
            "    from functools import reduce\n"
            "    reduce(lambda acc, x: acc * x, [1,2,3,4,5])"
        ),
        "options": ["A) 15", "B) 120", "C) [1,2,6,24,120]", "D) 24"],
        "answer": "B",
        "explanation": "reduce multiplies cumulatively: 1*2=2, 2*3=6, 6*4=24, 24*5=120."
    },
    {
        "topic": "Comprehensions & Lambdas",
        "q": (
            "What does this produce?\n\n"
            "    g = (x**2 for x in range(5))\n"
            "    print(next(g), next(g), next(g))"
        ),
        "options": ["A) 0 1 4", "B) [0, 1, 4]", "C) 0 0 0", "D) StopIteration"],
        "answer": "A",
        "explanation": "Generator expressions are lazy. next() pulls one value at a time: 0**2=0, 1**2=1, 2**2=4."
    },

    # ── CLOSURES ────────────────────────────────────────────────────────────
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
        "options": ["A) 1 2 3", "B) 1 1 1", "C) 1 2 1", "D) 0 1 0"],
        "answer": "C",
        "explanation": "Each call to make_counter() creates an independent closure with its own 'count'. c1 increments twice (1,2); c2 starts fresh (1)."
    },
    {
        "topic": "Closures",
        "q": (
            "What does triple.__closure__[0].cell_contents return if:\n\n"
            "    def make_mult(n):\n"
            "        def mult(x): return x * n\n"
            "        return mult\n"
            "    triple = make_mult(3)"
        ),
        "options": ["A) 'n'", "B) make_mult", "C) 3", "D) AttributeError"],
        "answer": "C",
        "explanation": "The closure captures n=3. __closure__[0].cell_contents gives the current value of the captured variable."
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
        "options": [
            "A) outer x: changed | global x: changed",
            "B) outer x: outer | global x: changed",
            "C) outer x: global | global x: changed",
            "D) outer x: outer | global x: outer"
        ],
        "answer": "B",
        "explanation": "'global x' in inner skips outer's x entirely and modifies the module-level x. outer's x stays 'outer'."
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
        "explanation": "Both add and get close over the same 'data' list object. Mutations via append are visible to get(). Output: [1, 2, 3]."
    },
    {
        "topic": "Closures",
        "q": (
            "What is the fix for the late-binding trap in:\n\n"
            "    funcs = [lambda: i for i in range(5)]"
        ),
        "options": [
            "A) funcs = [lambda i: i for i in range(5)]",
            "B) funcs = [lambda i=i: i for i in range(5)]",
            "C) funcs = [(lambda: i)() for i in range(5)]",
            "D) funcs = [def f(): return i for i in range(5)]"
        ],
        "answer": "B",
        "explanation": "Using a default argument 'i=i' captures the current value of i at lambda creation time, not at call time."
    },
]


def run_exam():
    print("=" * 68)
    print("  PCAP-31-03 MOCK EXAM — HARD LEVEL")
    print("  50 Questions | Pass mark: 70% (35/50)")
    print("  Edge cases, multi-step output prediction, tricky behaviour.")
    print("=" * 68)
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

        print("-" * 68)

    elapsed = time.time() - start
    minutes, seconds = divmod(int(elapsed), 60)

    print()
    print("=" * 68)
    print("  RESULTS")
    print("=" * 68)
    print(f"  Score      : {score} / 50  ({score * 2}%)")
    print(f"  Time taken : {minutes}m {seconds}s")
    print(f"  Pass mark  : 35 / 50  (70%)")
    passed = score >= 35
    print(f"  Result     : {'PASS ✓' if passed else 'FAIL ✗'}")
    print()

    if wrong_list:
        print(f"  Review — questions you missed ({len(wrong_list)}):")
        for num, q in wrong_list:
            first_line = q["q"].split("\n")[0][:58]
            print(f"    Q{num:02d} [{q['topic']}]: {first_line}...")
            print(f"         Correct: {q['answer']} — {q['explanation']}")
            print()

    print("=" * 68)


if __name__ == "__main__":
    run_exam()