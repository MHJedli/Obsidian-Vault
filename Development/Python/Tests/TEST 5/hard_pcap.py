#!/usr/bin/env python3
"""
PCAP-31-03 Mock Exam — HARD (50 Questions)
Topics: OOP inheritance/polymorphism, dunder methods, iterators, generators,
        decorators, closures, advanced exceptions, modules, regex, comprehensions edge cases
"""

import random
import time

QUESTIONS = [
    {
        "q": "What is the output of:\n  class A:\n      def __init__(self):\n          self.x = 1\n  class B(A):\n      pass\n  b = B()\n  print(b.x)",
        "options": ["A) Error", "B) None", "C) 1", "D) 0"],
        "answer": "C",
        "explanation": "B inherits __init__ from A. b.x = 1 is set through inherited __init__."
    },
    {
        "q": "What is the Method Resolution Order (MRO) in Python?",
        "options": [
            "A) The order in which methods are defined in a class",
            "B) The C3 linearization algorithm determining method lookup order in inheritance",
            "C) The order methods are called at runtime",
            "D) The reverse order of inheritance"
        ],
        "answer": "B",
        "explanation": "Python's MRO uses C3 linearization. Use ClassName.__mro__ or mro() to inspect it."
    },
    {
        "q": "What does '__slots__' do in a class?",
        "options": [
            "A) Limits the methods allowed in the class",
            "B) Prevents adding attributes not listed, saving memory by avoiding __dict__",
            "C) Defines slot methods like getters",
            "D) Sets default values for attributes"
        ],
        "answer": "B",
        "explanation": "__slots__ restricts instance attributes and removes __dict__, reducing memory overhead."
    },
    {
        "q": "What is the output of:\n  def counter():\n      n = 0\n      def inc():\n          nonlocal n\n          n += 1\n          return n\n      return inc\n  c = counter()\n  print(c(), c())",
        "options": ["A) 0 0", "B) 1 1", "C) 1 2", "D) Error"],
        "answer": "C",
        "explanation": "'nonlocal n' lets inc() modify n in the enclosing scope. Each call increments: 1, 2."
    },
    {
        "q": "What is the output of:\n  class A:\n      val = 10\n  class B(A):\n      val = 20\n  print(A.val, B.val)",
        "options": ["A) 10 10", "B) 20 20", "C) 10 20", "D) 20 10"],
        "answer": "C",
        "explanation": "Class attributes are separate. A.val=10, B.val=20 (overridden in B)."
    },
    {
        "q": "What dunder method is called by len(obj)?",
        "options": ["A) __size__", "B) __count__", "C) __len__", "D) __length__"],
        "answer": "C",
        "explanation": "len(obj) calls obj.__len__(). Implement it to support len() for custom classes."
    },
    {
        "q": "What does __iter__ and __next__ together implement?",
        "options": [
            "A) A generator",
            "B) The iterator protocol",
            "C) The context manager protocol",
            "D) A decorator"
        ],
        "answer": "B",
        "explanation": "Objects implementing __iter__ (returns self) and __next__ (returns next value) are iterators."
    },
    {
        "q": "What is the output of:\n  class Meta(type):\n      def __new__(mcs, name, bases, ns):\n          ns['greet'] = lambda self: 'hi'\n          return super().__new__(mcs, name, bases, ns)\n  class Foo(metaclass=Meta): pass\n  print(Foo().greet())",
        "options": ["A) Error", "B) 'hi'", "C) None", "D) 'Foo'"],
        "answer": "B",
        "explanation": "Metaclass __new__ injects 'greet' into the namespace. Foo instances get the method."
    },
    {
        "q": "What does @staticmethod allow?",
        "options": [
            "A) A method that can only access class attributes",
            "B) A method that takes no implicit first argument (no self or cls)",
            "C) A method that is called before __init__",
            "D) A method that auto-decorates with @property"
        ],
        "answer": "B",
        "explanation": "@staticmethod defines a method with no implicit first argument — it's like a plain function in the class namespace."
    },
    {
        "q": "What does @classmethod allow?",
        "options": [
            "A) Access to instance attributes via 'self'",
            "B) Receives the class (cls) as first argument instead of the instance",
            "C) Makes the method static",
            "D) Prevents subclasses from overriding the method"
        ],
        "answer": "B",
        "explanation": "@classmethod receives cls (the class) as first argument, useful for factory methods."
    },
    {
        "q": "What is the output of:\n  class Nums:\n      def __init__(self, data): self.data = data\n      def __len__(self): return len(self.data)\n      def __getitem__(self, i): return self.data[i]\n  n = Nums([10,20,30])\n  print(20 in n)",
        "options": ["A) Error", "B) False", "C) True", "D) None"],
        "answer": "C",
        "explanation": "Python's 'in' operator iterates using __getitem__ when __contains__ is absent. 20 is found."
    },
    {
        "q": "What exception does StopIteration signal?",
        "options": [
            "A) The loop exited with break",
            "B) The iterator has no more items to yield",
            "C) A generator encountered an error",
            "D) An index was out of range"
        ],
        "answer": "B",
        "explanation": "StopIteration is raised by __next__ when there are no more items; for loops catch it silently."
    },
    {
        "q": "What is the output of:\n  def gen():\n      yield 1\n      yield 2\n      yield 3\n  g = gen()\n  print(list(g), list(g))",
        "options": [
            "A) [1,2,3] [1,2,3]",
            "B) [1,2,3] []",
            "C) [] [1,2,3]",
            "D) Error"
        ],
        "answer": "B",
        "explanation": "Generators are exhausted after one full iteration. The second list(g) is empty."
    },
    {
        "q": "What is the purpose of 'super()' in Python?",
        "options": [
            "A) Creates a new instance of the superclass",
            "B) Returns a proxy object to delegate method calls to the parent class",
            "C) Converts a class to its superclass",
            "D) Calls all methods in the MRO simultaneously"
        ],
        "answer": "B",
        "explanation": "super() returns a proxy that delegates attribute lookups up the MRO chain."
    },
    {
        "q": "What is the output of:\n  x = [1,2,3]\n  y = x[:]\n  y[0] = 99\n  print(x[0])",
        "options": ["A) 99", "B) 1", "C) None", "D) Error"],
        "answer": "B",
        "explanation": "x[:] creates a shallow copy. Changing y[0] does not affect x."
    },
    {
        "q": "What does 'yield from iterable' do in a generator?",
        "options": [
            "A) Returns the iterable as a list",
            "B) Delegates iteration to a sub-generator or iterable",
            "C) Yields only the first element",
            "D) Raises StopIteration immediately"
        ],
        "answer": "B",
        "explanation": "'yield from' delegates to a sub-generator, yielding each of its values in turn."
    },
    {
        "q": "Which of the following correctly implements a context manager class?",
        "options": [
            "A) Define __start__ and __stop__",
            "B) Define __enter__ and __exit__",
            "C) Define __open__ and __close__",
            "D) Define __init__ and __del__"
        ],
        "answer": "B",
        "explanation": "Context managers require __enter__ (called on 'with') and __exit__ (called on block exit)."
    },
    {
        "q": "What does __exit__(self, exc_type, exc_val, exc_tb) returning True do?",
        "options": [
            "A) Re-raises the exception",
            "B) Suppresses the exception",
            "C) Converts the exception to a warning",
            "D) Logs the exception"
        ],
        "answer": "B",
        "explanation": "Returning a truthy value from __exit__ suppresses the exception."
    },
    {
        "q": "What is operator overloading in Python?",
        "options": [
            "A) Using operators on incompatible types",
            "B) Defining dunder methods to define behavior of operators for custom classes",
            "C) Overriding operators from imported modules",
            "D) Using multiple operators in one expression"
        ],
        "answer": "B",
        "explanation": "Dunder methods like __add__, __eq__, __lt__ let you define operator behavior for classes."
    },
    {
        "q": "What is the output of:\n  a = {1,2,3}\n  b = {2,3,4}\n  print(a ^ b)",
        "options": ["A) {2,3}", "B) {1,4}", "C) {1,2,3,4}", "D) {1,2,3,2,3,4}"],
        "answer": "B",
        "explanation": "^ is symmetric difference — elements in EITHER set but NOT both: {1,4}."
    },
    {
        "q": "What is a property decorator used for?",
        "options": [
            "A) To make a method static",
            "B) To define getter/setter/deleter for an attribute with method-like access",
            "C) To cache method return values",
            "D) To make a class abstract"
        ],
        "answer": "B",
        "explanation": "@property exposes a method as an attribute. @x.setter and @x.deleter add set/delete behavior."
    },
    {
        "q": "What does 'isinstance(obj, (A, B))' check?",
        "options": [
            "A) Whether obj is exactly type A or B",
            "B) Whether obj is an instance of A or B or their subclasses",
            "C) Whether A and B are related",
            "D) Whether obj has both A and B as bases"
        ],
        "answer": "B",
        "explanation": "isinstance with a tuple checks if obj is an instance of any of the listed types (or subclasses)."
    },
    {
        "q": "What is the output of:\n  class A:\n      def method(self): return 'A'\n  class B(A):\n      def method(self): return 'B'\n  class C(A):\n      def method(self): return 'C'\n  class D(B, C): pass\n  print(D().method())",
        "options": ["A) 'A'", "B) 'B'", "C) 'C'", "D) Error (diamond problem)"],
        "answer": "B",
        "explanation": "Python's MRO: D → B → C → A. First match is B.method(), returns 'B'."
    },
    {
        "q": "What is the result of:\n  def f(lst=[]):\n      lst.append(1)\n      return lst\n  print(f(), f())",
        "options": [
            "A) [1] [1]",
            "B) [1] [1, 1]",
            "C) [] [1]",
            "D) Error"
        ],
        "answer": "B",
        "explanation": "Mutable default arguments are shared across calls. After 2 calls: [1] then [1,1]."
    },
    {
        "q": "What does 'functools.wraps' do when used in a decorator?",
        "options": [
            "A) Speeds up the wrapped function",
            "B) Preserves the original function's metadata (__name__, __doc__, etc.)",
            "C) Makes the function thread-safe",
            "D) Caches the wrapped function's results"
        ],
        "answer": "B",
        "explanation": "Without @wraps, the wrapper overwrites __name__ and __doc__. @wraps copies them from the original."
    },
    {
        "q": "What does 're.findall(pattern, string)' return?",
        "options": [
            "A) The first match object",
            "B) A list of all non-overlapping matches",
            "C) A generator of matches",
            "D) A boolean"
        ],
        "answer": "B",
        "explanation": "re.findall() returns a list of all non-overlapping match strings (or groups if groups are present)."
    },
    {
        "q": "What is the output of:\n  d = {}\n  for i in range(3):\n      d[i] = i**2\n  print({v:k for k,v in d.items()})",
        "options": [
            "A) {0:0, 1:1, 4:2}",
            "B) {0:0, 1:1, 2:4}",
            "C) {0:0, 1:1, 9:3}",
            "D) Error"
        ],
        "answer": "A",
        "explanation": "d = {0:0, 1:1, 2:4}. Inverted: {0:0, 1:1, 4:2}."
    },
    {
        "q": "What does 'abc.ABC' provide?",
        "options": [
            "A) A class that auto-implements all abstract methods",
            "B) A base class for defining abstract base classes using @abstractmethod",
            "C) A string comparison utility",
            "D) An alternative to 'object'"
        ],
        "answer": "B",
        "explanation": "abc.ABC + @abstractmethod let you define interfaces that subclasses must implement."
    },
    {
        "q": "What is the output of:\n  print(list(map(lambda x: x*2, filter(lambda x: x%2==0, range(6)))))",
        "options": ["A) [0,2,4]", "B) [0,4,8]", "C) [2,4,6,8]", "D) [1,3,5]"],
        "answer": "B",
        "explanation": "filter keeps evens from 0-5: [0,2,4]. map doubles them: [0,4,8]."
    },
    {
        "q": "What does 'pickle' module do?",
        "options": [
            "A) Encrypts Python objects",
            "B) Serializes (converts to bytes) and deserializes Python objects",
            "C) Compresses Python files",
            "D) Runs Python scripts as background processes"
        ],
        "answer": "B",
        "explanation": "pickle.dumps/loads serializes Python objects to bytes for storage or transmission."
    },
    {
        "q": "What is the difference between 'is' and '==' for small integers like 1?",
        "options": [
            "A) Always the same for integers",
            "B) 'is' may return True for small ints due to interning, but this is implementation-specific",
            "C) 'is' checks value; '==' checks identity for integers",
            "D) They always differ for integers"
        ],
        "answer": "B",
        "explanation": "CPython interns small integers (-5 to 256). 'is' compares identity; '==' compares value. Don't rely on 'is' for value comparison."
    },
    {
        "q": "What is the output of:\n  def dec(f):\n      def wrapper(*args, **kwargs):\n          return f(*args, **kwargs) * 2\n      return wrapper\n  @dec\n  def add(a,b): return a+b\n  print(add(3,4))",
        "options": ["A) 7", "B) 14", "C) 6", "D) Error"],
        "answer": "B",
        "explanation": "add(3,4) calls wrapper(3,4), which returns f(3,4)*2 = 7*2 = 14."
    },
    {
        "q": "What is a 'namedtuple'?",
        "options": [
            "A) A tuple with keys like a dict",
            "B) A tuple subclass with named fields accessible by name or index",
            "C) A mutable named collection",
            "D) A tuple with type hints"
        ],
        "answer": "B",
        "explanation": "collections.namedtuple creates tuple subclasses with named fields: Point = namedtuple('Point', ['x','y'])."
    },
    {
        "q": "What does 'collections.defaultdict(int)' do?",
        "options": [
            "A) Creates a dict that only accepts int keys",
            "B) Creates a dict that returns 0 for missing keys automatically",
            "C) Creates a sorted int dict",
            "D) Converts all values to int"
        ],
        "answer": "B",
        "explanation": "defaultdict(int) uses int() (returns 0) as default factory for missing keys."
    },
    {
        "q": "What is the output of:\n  class Foo:\n      def __repr__(self): return 'Foo()'\n      def __str__(self): return 'a Foo'\n  f = Foo()\n  print(str(f), repr(f))",
        "options": [
            "A) Foo() Foo()",
            "B) a Foo Foo()",
            "C) a Foo a Foo",
            "D) Foo() a Foo"
        ],
        "answer": "B",
        "explanation": "str() calls __str__, repr() calls __repr__. str(f)='a Foo', repr(f)='Foo()'."
    },
    {
        "q": "What does 'itertools.chain(*iterables)' do?",
        "options": [
            "A) Multiplies iterables",
            "B) Connects multiple iterables into a single iterator",
            "C) Creates a linked list",
            "D) Repeats iterables indefinitely"
        ],
        "answer": "B",
        "explanation": "chain([1,2],[3,4]) → 1,2,3,4. It chains iterables end-to-end."
    },
    {
        "q": "What is the output of:\n  x = lambda a, b, c: a + b * c\n  print(x(1, 2, 3))",
        "options": ["A) 9", "B) 7", "C) 6", "D) 12"],
        "answer": "B",
        "explanation": "Operator precedence: b*c = 6 first, then 1+6 = 7."
    },
    {
        "q": "What is a 'coroutine' in Python?",
        "options": [
            "A) A function that runs in a separate thread",
            "B) A function defined with 'async def' that can be suspended with 'await'",
            "C) A generator that yields control to another generator",
            "D) A class method that runs asynchronously"
        ],
        "answer": "B",
        "explanation": "Coroutines are async functions using 'async def'. They're suspended at 'await' expressions."
    },
    {
        "q": "What is the purpose of '__new__' vs '__init__'?",
        "options": [
            "A) They are identical",
            "B) __new__ creates the instance; __init__ initializes it",
            "C) __init__ creates; __new__ initializes",
            "D) __new__ is for class creation; __init__ is for module init"
        ],
        "answer": "B",
        "explanation": "__new__ is called first and creates the object. __init__ is called after to initialize it."
    },
    {
        "q": "What does 'functools.lru_cache' do?",
        "options": [
            "A) Limits the recursion depth",
            "B) Caches the results of function calls to avoid repeated computation",
            "C) Logs function calls",
            "D) Runs functions asynchronously"
        ],
        "answer": "B",
        "explanation": "@lru_cache memoizes function results based on arguments, improving performance for repeated calls."
    },
    {
        "q": "What is the output of:\n  a = (x for x in range(5))\n  b = list(a)\n  c = list(a)\n  print(len(b), len(c))",
        "options": ["A) 5 5", "B) 0 5", "C) 5 0", "D) Error"],
        "answer": "C",
        "explanation": "Generator 'a' is exhausted after list(a) the first time. Second call yields empty list."
    },
    {
        "q": "What does 'raise ... from ...' do?",
        "options": [
            "A) Raises multiple exceptions at once",
            "B) Chains exceptions, preserving the original cause as __cause__",
            "C) Converts one exception type to another",
            "D) Suppresses the original exception"
        ],
        "answer": "B",
        "explanation": "'raise B from A' sets B.__cause__ = A, showing exception chaining in tracebacks."
    },
    {
        "q": "What is the output of:\n  print({k: v for k, v in zip('abc', [1,2,3])})",
        "options": [
            "A) {('a',1), ('b',2), ('c',3)}",
            "B) {'a':1, 'b':2, 'c':3}",
            "C) [('a',1),('b',2),('c',3)]",
            "D) {'abc': [1,2,3]}"
        ],
        "answer": "B",
        "explanation": "zip pairs 'a'→1,'b'→2,'c'→3. Dict comprehension creates {'a':1,'b':2,'c':3}."
    },
    {
        "q": "What does 'object.__class__' return?",
        "options": [
            "A) The module where the object was created",
            "B) The type (class) of the object",
            "C) The parent class",
            "D) The object's string representation"
        ],
        "answer": "B",
        "explanation": "__class__ attribute holds the type of the instance, same as type(obj)."
    },
    {
        "q": "What is a 'descriptor' in Python?",
        "options": [
            "A) A docstring",
            "B) An object that defines __get__, __set__, or __delete__ controlling attribute access",
            "C) A type hint annotation",
            "D) A property alias"
        ],
        "answer": "B",
        "explanation": "Descriptors implement the descriptor protocol (__get__/__set__/__delete__) to control attribute access on classes."
    },
    {
        "q": "What is the output of:\n  class A:\n      x = []\n  a1 = A()\n  a2 = A()\n  a1.x.append(1)\n  print(a2.x)",
        "options": ["A) []", "B) [1]", "C) None", "D) Error"],
        "answer": "B",
        "explanation": "x is a class attribute shared by all instances. Mutating a1.x mutates A.x, visible via a2.x."
    },
    {
        "q": "What does 'typing.Optional[str]' mean?",
        "options": [
            "A) The value can be any type",
            "B) The value is either str or None",
            "C) The value is optionally required",
            "D) The value is a subclass of str"
        ],
        "answer": "B",
        "explanation": "Optional[str] is shorthand for Union[str, None]."
    },
    {
        "q": "What is the output of:\n  def f(): return (x for x in range(3))\n  g1, g2 = f(), f()\n  print(next(g1), next(g2), next(g1))",
        "options": ["A) 0 0 0", "B) 0 0 1", "C) 0 1 1", "D) Error"],
        "answer": "B",
        "explanation": "g1 and g2 are independent generators. next(g1)=0, next(g2)=0, next(g1)=1."
    },
    {
        "q": "What is the result of: issubclass(bool, int)?",
        "options": ["A) False", "B) True", "C) Error", "D) None"],
        "answer": "B",
        "explanation": "bool is a subclass of int in Python. True == 1 and False == 0 in arithmetic."
    },
    {
        "q": "What does 'vars(obj)' return?",
        "options": [
            "A) A list of all method names",
            "B) The __dict__ attribute of the object (instance's namespace)",
            "C) The class's attribute names",
            "D) A tuple of all attributes"
        ],
        "answer": "B",
        "explanation": "vars(obj) returns obj.__dict__, the dict of instance attributes."
    },
    {
        "q": "What is the output of:\n  print(1_000_000 == 1000000)",
        "options": ["A) False", "B) SyntaxError", "C) True", "D) None"],
        "answer": "C",
        "explanation": "Python 3.6+ allows underscores in numeric literals for readability. 1_000_000 = 1000000."
    },
]


def run_exam(questions, title="HARD"):
    print("=" * 60)
    print(f"  PCAP-31-03 MOCK EXAM — {title} DIFFICULTY")
    print(f"  {len(questions)} Questions | Time Limit: 50 minutes")
    print("=" * 60)
    print("\nInstructions: Enter A, B, C, or D for each answer.")
    print("Type 'q' at any time to quit and see your score.\n")
    input("Press ENTER to begin...")
    print()

    score = 0
    wrong = []
    start_time = time.time()
    last_i = 0

    for i, item in enumerate(questions, 1):
        last_i = i
        print(f"Q{i}/{len(questions)}: {item['q']}")
        for opt in item["options"]:
            print(f"  {opt}")
        while True:
            ans = input("Your answer: ").strip().upper()
            if ans == "Q":
                break
            if ans in ("A", "B", "C", "D"):
                break
            print("  Invalid input. Please enter A, B, C, or D.")

        if ans == "Q":
            print("\n--- Exam terminated early ---")
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
    print(f"  Score    : {score} / {last_i}")
    percent = (score / last_i * 100) if last_i else 0
    print(f"  Percent  : {percent:.1f}%")
    print(f"  Time     : {mins}m {secs}s")
    status = "PASS ✔" if percent >= 70 else "FAIL ✘"
    print(f"  Status   : {status}  (passing = 70%)")

    if wrong:
        print(f"\n  Missed questions ({len(wrong)}):")
        for num, item in wrong:
            print(f"  Q{num}: {item['q'][:60]}...")
            print(f"        Correct: {item['answer']} — {item['explanation']}")
    print("=" * 60)


if __name__ == "__main__":
    q_list = QUESTIONS.copy()
    random.shuffle(q_list)
    run_exam(q_list, title="HARD")