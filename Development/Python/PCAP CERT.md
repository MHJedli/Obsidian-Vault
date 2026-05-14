 PCAP = Python Certified Associate Programmer
 Due Date : 14/06/26

# Resources :

https://www.youtube.com/watch?v=_Tv2z3NRBQw&list=PLP1c80t4iv8p0Np7FubW73gLJsIHOsMpJ&index=1

https://www.youtube.com/watch?v=HR9hBlcKGho&list=PLP1c80t4iv8r4PcNu27KCzQnZ9V85WhKd

# Section To Study:

[[#1. Modules & Packages (~6 Questions - 12%)]]
	[[#1.1. import and use modules and packages]]
	[[#1.2. The math Module]]
	[[#1.3. The random Module]]
	[[#1.4. The platform Module]]
[[#2. Exceptions (~5 Questions - 14%)]]
	[[#2.1. Exception Handling Syntax]]
	[[#2.2. Raising & Asserting]]
	[[#2.3. Exception Hierarchy & Classes]]
	[[#2.4. Custom Exceptions]]
[[#3. Strings (~8 Questions - 18%)]]
[[#4. OOP (~12 Questions - 34%)]]
	[[#4.1. Core OOP Concept]]
	[[#4.2. Methods & Constructors]]
	[[#4.3. Introspection]]
[[#5. Miscellaneous (~9 Questions - 22%)]]
	[[#5.1. List Comprehensions]]
	[[#5.2. Lambda Function]]
	[[#5.3. Closures]]
	[[#5.4. File I/O - Concepts]]
	[[#5.5. File I/O - Operations]]

---
# 1. Modules & Packages : (~6 Questions - 12%)

## 1.1. import and use modules and packages :

```python
import math
import math, random
```

* **Namespaces:**
* When importing a module, python is going to maintain a seperate namespace by default([[Exp1.canvas]])

- To import something specific from a module :
```python
from module_name import <var>
# Example
from math import pi
area = pi * radius**2

# We are referencing pi imported from math by calling it by its name
# NOTE: We cannot redefine pi because its value will be affected from the one that we imported earlier
```

- We can set an alias to a module name / function imported from a module:
```python
import math as m

from math import pi as pie
```

 - **The directory function / dir() :**
 - The dir() function in Python **lists** ==all attributes and methods== of ==an object== or ==the current local scope==. It helps ==explore== and understand ==what's available in an object or module==
```python
import math
print(dir(math))
>>> ['__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'cbrt', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'exp2', 'expm1', 'fabs', 'factorial', 'floor', 'fma', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'sumprod', 'tan', 'tanh', 'tau', 'trunc', 'ulp']
```

**The sys.path variable :**
* The **sys.path** is a list in Python that contains the directories where the interpreter looks for modules to import. It is initialized when Python starts and can be modified using the PYTHONPATH environment variable to include additional directories.
```python
import sys
for i,p in enumerate(sys.path):
	print(f"{i:2d} {p}")

>>>
0 /home/mhj/Desktop/working/python_working
1 /usr/lib64/python314.zip
2 /usr/lib64/python3.14
3 /usr/lib64/python3.14/lib-dynload
4 /home/mhj/.local/lib/python3.14/site-packages
5 /usr/lib64/python3.14/site-packages
6 /usr/lib/python3.14/site-packages
```

**Creating Modules**
```
my_app/
	network/
		dns.py
		https.py
	security/
		hashing.py
		crypto.py
```

- Here, `network/` and `security/` are called **packages**
- The files : `dns.py`, `https.py`, `hashing.py` and `crypto.py` are called **modules**.

- **Packages** are folders/subfolders that contains **Modules**
- **Modules** are `.py` files that contains functions
```python
# To import dns module, we use the dot notation to navigate
import my_app.network.dns
```

**PyPI (Package Index) :**
- Public package repository
- Searchable catalog
- Hosts package release
- Used by **Pip**

**PIP :**
- Python's common installer
- Pulls from PyPI
- Installs dependencies
```
// TODO: add how to manipulate pip
```

**__pycache__ :**

- When Python runs a `.py` file, it compiles it to **bytecode** and stores it in `__pycache__` to speed up future imports.
```
# Example of a working directory
myproject/
├── main.py
├── utils.py
└── __pycache__/
    ├── utils.cpython-311.pyc
    └── main.cpython-311.pyc
```

>[!note]
>* Bytecode is a **low-level intermediate representation** — not machine code, not source code

- Some key behaviors of `__pycache__` directory :
	1. Only created for **imported** modules :
		```python
	 	# utils.py is imported → __pycache__/utils.pyc created
	 	import utils
	
		# main.py run directly → no .pyc for main.py
		# python main.py
		```

	 2. Auto-invalidated on changes
	 3. Version-specific (Multiple Python versions coexist without conflict.)

- We can disable `__pycache__` by adding `-B` flag when running our program :
```python
python -B main.py
```



 **The `__main__` variable :**
 
* In Python, `__main__` is the name of the top-level code environment where the main script is executed.
* It serves two primary purposes:
	1. It indicates that a Python file is being run directly as a script.
	2. It allows for the execution of code only when the script is run directly, preventing it from executing when the file is imported as a module.
* Using the `if __name__ == "__main__":` construct provides several advantages:
	1. Control Execution: It allows you to define code that runs only when the script is executed directly, which is useful for testing or running specific functions.
	2. Prevent Unintended Execution: Code within this block will not run if the script is imported as a module in another script, avoiding potential side effects.
	3. Organize Code: It encourages the use of a `main()` function, which can help keep the global namespace clean and improve code readability.
```python
def main():
	print("This script is running directly")
if __name__ == "__main__":
	main()
```

**Advanced qualifying for nested modules:**

- Let's suppose, we have the current working directory :
```
python_working/
	common_function/
		add.py
		multiply.py
	main.py
```

 - In our `main.py` :
 ```python
 import common_functions.add
 print(common_functions.add.add(5,10))
 >>> 15
 ```
- As we can see, the calling is too long and we may introduce some typos which can be overwhelming.
- To fix this issue, we can use `from ... import ...` for an easy to use call
```python
from common_functions.add import add
print(add(5, 10))
>>> 15
```

**Nested packages vs. directory trees :**

- Both look identical on disk. The difference is whether `__init__.py` is present and how Python treats the directory.
```
Nested Package                  Plain Directory Tree
──────────────────────────────────────────────────────
myapp/                          myapp/
├── __init__.py   ✅             ├── (no __init__.py) ❌
├── models/                      ├── models/
│   ├── __init__.py ✅           │   ├── (no __init__.py) ❌
│   ├── user.py                  │   ├── user.py
│   └── product.py               │   └── product.py
└── utils/                       └── utils/
    ├── __init__.py ✅               ├── (no __init__.py) ❌
    └── helpers.py                   └── helpers.py
```

**1. Nested Package - Full Python Package :**

- Every directory has `__init__.py` → fully importable at every level :
```python
# All of these work
import myapp
import myapp.models
import myapp.utils

from myapp.models import user
from myapp.models.user import User
from myapp.utils.helpers import format_date
```

**2. Plain Directory Tree - Just Files :**

- No `__init__.py` → Python 3.3+ treats it as a **namespace package** (limited) or just a folder:
```python
import myapp          # may work as namespace package
import myapp.models   # may work as namespace package

# But:
# — no __init__.py code runs
# — no re-exports
# — no __all__, __version__
# — behavior is implicit and fragile
```

- How Python Resolves Imports :
```
import myapp.models.user
         ↓
1. Find myapp/          → check for __init__.py → run it
2. Find myapp/models/   → check for __init__.py → run it
3. Find myapp/models/user.py → load it
```
- Without `__init__.py` at any level, step 1 or 2 may fail or behave unexpectedly.

```
# Example of Real-World Structure
myapp/
├── __init__.py              # package root
├── main.py
│
├── models/                  # sub-package
│   ├── __init__.py          # re-exports User, Product
│   ├── user.py
│   └── product.py
│
├── services/                # sub-package
│   ├── __init__.py
│   ├── auth.py
│   └── email.py
│
├── templates/               # plain directory — not imported
│   └── index.html
│
├── static/                  # plain directory — not imported
│   └── style.css
│
└── tests/                   # sub-package
    ├── __init__.py
    ├── test_user.py
    └── test_auth.py
```

- Decision Guide :
```
Do you need Python to import from this directory?
├── Yes → add __init__.py → Nested Package
│         ├── Do you want a clean public API?
│         │   └── Yes → add re-exports to __init__.py
│         └── Do you want version/metadata?
│             └── Yes → add __version__, __author__
│
└── No  → leave it as a plain directory
          (templates, static, data, config)
```


**Public and Private Variables in modules :**

- The difference between a `global` variable and a `private` variable, in a module, is `_`.
```python
# Module_Exp
def _calculate():
	# Code here
def export():
	# Code here
```

in `main.py` :
```python
import Module_Exp
Module_Exp.export() # Works
Modules_Exp._calculate() # Still Works but not preferred to use it
```

- `_calculate()` is a private function and `export()` is a global function
* It is all a naming convention
* We can access`_calculate()` but it's not preferred to do it.

**The __init__.py File - making a directory a package :**
- `__init__.py` is a special file that marks a directory as a **Python package** and runs automatically when the package is imported.
```
# Example of a working directory :
mypackage/
│── __init__.py       ← makes this a package
│── module_a.py
│── module_b.py
└── subpackage/
    │── __init__.py
    └── module_c.py
```

```python
import mypackage # triggers mypackage/__init__.py
from mypackage import something
```

- The `__init__.py` file can be :
	1. Empty : Just its presence is enough to make the directory a package
	2. Package-level variables / metadata
	3. Re-exporting for a cleaner API
	4. Controlling `import *` with `__all__` :
	```
	# __init__.py
	from .module_a import ClassA, ClassB
	from .module_b import utility

	__all__ = ["ClassA", "utility"]  # ClassB excluded from *
	```
	5. Running initialization code

- In Python 3.3+, we have **Implicit namespace packages**, meaning directories can be imported as packages without the need of `__init__.py` but with some penalties :

| Feature                     | With `__init__.py` | Without `__init__.py` |
| --------------------------- | ------------------ | --------------------- |
| Package initialization code | Yes                | No                    |
| Re-exports / clean API      | Yes                | No                    |
| `__all__`, `__version__`    | Yes                | No                    |
| Works as a package          | Yes                | Yes (Namespace Only)  |


## 1.2. The math Module :

**.ceil() :**

```python
import math as m
# Round up a number
print(m.ceil(1.2))
>>> 2
```

**.floor() :**
```python
import math as m

# Round up a number
print(m.floor(1.2))
>>> 1
```

**.trunc() :**
```python
import math as m

# Removes the decimal part and returns the integer part only, always 
# truncating toward zero
print(m.trunc(4.9))
>>> 4
print(m.trunc(-4.9))
>>> -4
```

**.factorial() :**
```python
import math as m

# calculate the factorial of an integer
print(m.factorial(5))
>>> 120
```

**.hypot():**

- Calculate the **Euclidean distance**, originally designed for the hypotenuse of a right triangle, extended in Python 3.8+ to work in **n-dimensions**.
- Basic Usage — Hypotenuse (2D) √(x² + y²):
```python
import math as m

print(m.hypot(3,4))
>>> 5
```

- Distance Between Two Points :
```python
# In 2D :
def distance(p1, p2):
    return math.hypot(p2[0] - p1[0], p2[1] - p1[1])

distance((0, 0), (3, 4))    # 5.0
distance((1, 2), (4, 6))    # 5.0

# In 3D :
def distance_3d(p1, p2):
    return math.hypot(p2[0]-p1[0], p2[1]-p1[1], p2[2]-p1[2])

distance_3d((0,0,0), (1,2,2))   # 3.0
```

**.sqrt() :**

```python
import math as m

# calculate the square root of a number
print(m.sqrt(25))
>>> 5.0
 
print(m.sqrt(2))
>>> 1.4142135623730951
```
## 1.3. The random Module :

**.random() :**

```python
import random as r

# Generate a random float between 0 (inclusive) and 1 (exclusive)
print(r.random())
>>> 0.14630538140657734
>>> 0.293024501677716

# Generate a random float between a (inclusive) and b (inclusive)
print(r.uniform(2.5, 5.0))

# Generate an integer between a and b (inclusive on both)
print(r.randint(5, 10))

# Generate an integer between a (inclusive) and b (exclusive)
print(r.randrange(0, 10))

```

**.seed() :**
- Sets the **starting point** of the random number generator, guaranteeing the same sequence of random numbers every time the same seed is used.
```python
import random

random.seed(42)
print(random.random())    # 0.6394267984578837
print(random.random())    # 0.025010755222666936
print(random.randint(1, 10))  # 2

# Reset with same seed → identical sequence
random.seed(42)
print(random.random())    # 0.6394267984578837 (same)
print(random.random())    # 0.025010755222666936 (same)
print(random.randint(1, 10))  # 2 (same)
```

- Accepted types of seed :
```python
random.seed(42)         # int
random.seed(3.14)       # float
random.seed("hello")    # string
random.seed(b"bytes")   # bytes
random.seed(None)       # None → uses system time/os.urandom (default)
```

**.choice(), choices() and sample() :**

```python
import random

# Picks a single random element from a non-empty sequence.

random.choice([1, 2, 3, 4, 5])        # 3
random.choice(["a", "b", "c"])        # "a"
random.choice("hello")                # "l"  — works on strings too
random.choice((10, 20, 30))           # 20   — works on tuples

items = ["a", "b", "c", "d"]
random.choice(items)            # "b"         — 1 item
random.choices(items, k=3)      # ["a","a","c"] — k items, WITH replacement
random.sample(items, k=3)       # ["d","b","a"] — k items, WITHOUT replacement
```
## 1.4. The platform Module :

**.platform() :**
```python
import platform as p

# returns a single string that contains detailed information about the 
# underlying platform, including the operating system and version.
print(f"The system is running : {p.platform()}")
```

**.machine() :**
```python
import platform as p

# returns the machine type (x86_64, arm64, ...)
print(p.machine())
```

**.processor() :**
```python
import platform as p

print(p.processor())
```

**.system() :**
```python
import platform as p

# Returns the OS name
print(p.system())
>>> Linux
```

**.version() :**
```python
import platform as p

# Returns the system's release version
print(f"OS Version : {p.version()}")
>>> OS Version : #1 SMP PREEMPT_DYNAMIC Fri May 8 16:02:43 UTC 2026
```

**.python_implementation() :**
```python
import platform as p

# Returns the Python implementation
print(f"Python: {p.python_implementation()}")
>>> Python: CPython
```

**.python_version() :**
```python
import platform as p

# Returns the python version installed
print(f"Python v{p.python_version()}")
>>> Python v3.14.4

# Returns the python version as tuple
print(f"Python v{p.python_version_tuple()}")
>>> Python v('3', '14', '4')
```

# 2. Exceptions (~5 Questions - 14%) :

## 2.1. Exception Handling Syntax :

**Basic `try/except` block :**
```python
try:
	x = int(input("Type a number :"))
	print(f"x = {x}")
except:
	print("The input should be a number !")
	
# The `try` block runs normally — if an exception occurs, Python jumps 
# immediately to the matching `except` branch. Any code after the error line in # `try` is skipped.
```

**Ordering `except` Branches, Most Specific first :**

- Python checks branches **top to bottom** and runs the first match :
```python
try:
    x = int("abc")
except ValueError:
    print("Invalid value")       # ✅ catches it here
except Exception:
    print("General error")       # never reached for ValueError
```

- Wrong order, broad catches block specific ones :
```python
try:
    x = int("abc")
except Exception:           # too broad — catches everything
    print("General error")
except ValueError:          # ⚠️ unreachable — never gets here
    print("Invalid value")
```

- Exception hierarchy, child classes must come before parents :
```
#        BaseException
#             ↓
#          Exception
#         ↙        ↘
#   ValueError    OSError
#       ↓              ↓
# UnicodeError    FileNotFoundError

try:
    ...
except FileNotFoundError:   # ✅ child first
    ...
except OSError:             # ✅ parent after
    ...
except Exception:           # ✅ broadest last
    ...
```

**except ExceptionType as variable :**
- Captures the exception object so you can inspect it:
```python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(e)           # division by zero
    print(type(e))     # <class 'ZeroDivisionError'>
    print(e.args)      # ('division by zero',)
```

**Grouped Exceptions — except (TypeError, ValueError) :**
- Handle multiple exception types with the same block:
```python
try:
    value = int(input("Enter a number: "))
except (TypeError, ValueError):
    print("That's not a valid number")
```

- With a variable:
```python
try:
    process(data)
except (TypeError, ValueError) as e:
    print(f"Bad input: {e}")
except (OSError, IOError) as e:
    print(f"IO problem: {e}")
```

**else Clause :**
- Runs Only When No Exception Was Raised :
```python
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Division failed")
else:
    print(f"Success: {result}")   # runs only if no exception ✅
```

- Why use **else** instead of putting code at the end of **try** ? :
```python
# ❌ Risky — process() errors are caught by except, masking bugs
try:
    result = divide(a, b)
    process(result)           # unrelated — shouldn't be here
except ZeroDivisionError:
    print("Division failed")

# ✅ Clean — only divide() is guarded; process() errors propagate naturally
try:
    result = divide(a, b)
except ZeroDivisionError:
    print("Division failed")
else:
    process(result)           # only runs if divide() succeeded
```

**finally clause :**
- Runs whether an exception occured or not, even if there's a **return** or **raise** :
```python
try:
    f = open("data.txt")
    data = f.read()
except FileNotFoundError:
    print("File not found")
finally:
    f.close()    # always runs — guaranteed cleanup ✅
```

**Round up:**
```python
try:
    result = divide(a, b)          # guarded code
except ZeroDivisionError as e:
    print(f"Math error: {e}")      # specific exception
except Exception as e:
    print(f"Unexpected: {e}")      # catch-all fallback
else:
    print(f"Result: {result}")     # no exception raised
finally:
    print("Done")                  # always runs
    
# Execution path :    
# Exception raised → except → finally
# No exception     → else   → finally
```
## 2.2. Raising & Asserting :

**raise - Re-raise current exception :**
- Used inside an **except** block to re-raise the **same exception** without losing the original traceback :
```python
try:
	value = int(input("Enter a number: "))
except ValueError:
	print("That's not a valid number")
	raise

>>> Enter a number : abc
That's not a valid number
Traceback (most recent call last):
  File "/home/mhj/Desktop/working/python_working/test2.py", line 2, in <module>
    value = int(input("Enter a number: "))
ValueError: invalid literal for int() with base 10: 'qsd'
```

>[!note]
>`raise` with no argument only works inside `except` — otherwise `RuntimeError`

**raise ExceptionType(message) - Raise a New Exception :**
- Manually trigger an exception anywhere in your code :
```python
raise ValueError("Age must be positive")
raise TypeError("Expected a string")
raise FileNotFoundError("Config file missing")
raise RuntimeError("Something went wrong")
```

```python
def set_age(age):
    if not isinstance(age, int):
        raise TypeError(f"Expected int, got {type(age).__name__}")
    if age < 0:
        raise ValueError(f"Age cannot be negative: {age}")
    if age > 150:
        raise ValueError(f"Age unrealistically large: {age}")
    self.age = age
```

**Exception Chaining — `raise ... from` :**
- Links a new exception to its cause,  can preserves full context :
```python
try:
    data = config["timeout"]
except KeyError as e:
    raise ValueError("Missing required config field") from e

# KeyError: 'timeout'
# The above exception was the direct cause of the following exception:
# ValueError: Missing required config field
```

- You can suppress the chain with `from None` allowing to hide the original :
```python
try:
    data = config["timeout"]
except KeyError:
    raise ValueError("Invalid configuration") from None
# only ValueError is shown — KeyError hidden
```

**assert — Debugging Assertions :**
- Checks a condition and raises **AssertionError** if it's **False**:
```python
assert condition               # no message
assert condition, "message"    # with message shown on failure
```

```python
a, b = 9, 10
assert a > b, "a is not greater or equal to b"

# Traceback (most recent call last):
# File "/home/mhj/Desktop/working/python_working/test2.py", line 2, in <module>
# assert a > b, "a is not greater or equal to b"
```

- We use **assert** to catch bugs during development but not for real validation

>[!note]
>We can use `raise` for validation and `assert` for Internal sanity checks
>```
># raise — user/external input
>def set_age(age):
 >   if age < 0:
>        raise ValueError("Age cannot be negative")  # ✅ always enforced
># assert — internal invariants
>def _internal_calc(data):
 >   assert isinstance(data, list)   # ✅ catches bugs in your own code
>```

- We can eliminate the assertion by adding the `-O` flag, when running the program :
```python
python -O main.py # assertions disabled - assert lines do nothing
```
## 2.3. Exception Hierarchy & Classes :
![[Python_exception_hierarchy.png]]

## 2.4. Custom Exceptions :

- Subclass `Exception` to create meaningful, catchable errors:
```python
class AppError(Exception):
    """Base class for all app errors"""
    pass

class ValidationError(AppError):
    def __init__(self, field, message):
        self.field = field
        super().__init__(f"{field}: {message}")

class NetworkError(AppError):
    pass

class TimeoutError(NetworkError):
    pass
```

```python
# raising
raise ValidationError("email", "invalid format")
raise TimeoutError("Connection timed out after 30s")

# catching — hierarchy works as expected
try:
    process()
except ValidationError as e:
    print(e.field)       # "email"
except AppError:
    print("generic app error")
```

**Simplest Form — class MyError(Exception): pass :**
- Just naming it is often enough — the class itself carries meaning:
```python
class InsufficientFundsError(Exception): pass
class UserNotFoundError(Exception): pass
class ConfigMissingError(Exception): pass
```

```python
raise InsufficientFundsError("Balance too low")
raise UserNotFoundError(f"No user with id {user_id}")
```

- Catching by name makes the code self-documenting :
```python
try:
    withdraw(account, amount)
except InsufficientFundsError:
    print("Please top up your account")
```

**Overriding __init__ — Structured Data on Exceptions :**
- Attach extra context beyond just a message:
```python
class InsufficientFundsError(Exception):
    def __init__(self, amount, balance):
        self.amount = amount
        self.balance = balance
        self.shortfall = amount - balance
        super().__init__(f"Cannot withdraw {amount}, balance is {balance}")
```

```python
try:
    withdraw(account, 500)
except InsufficientFundsError as e:
    print(e)               # Cannot withdraw 500, balance is 120
    print(e.amount)        # 500
    print(e.balance)       # 120
    print(e.shortfall)     # 380
```

>[!note]
>`super().__init__(message)` sets the string representation — always call it.

**Overriding __str__ — Custom Display :**
- Control exactly how the exception prints :
```python
class ValidationError(Exception):
    def __init__(self, field, value, reason):
        self.field = field
        self.value = value
        self.reason = reason
        super().__init__()       # no message passed up

    def __str__(self):
        return (
            f"Validation failed:\n"
            f"  Field : {self.field}\n"
            f"  Value : {self.value!r}\n"
            f"  Reason: {self.reason}"
        )
```

```python
raise ValidationError("email", "not-an-email", "missing @ symbol")

# ValidationError:
# Validation failed:
#   Field : email
#   Value : 'not-an-email'
#   Reason: missing @ symbol
```

**Integrating Into Existing Hierarchies :**
- Build a layered hierarchy — broad at the top, specific at the bottom:
```python
# Base — catch-all for the entire app
class AppError(Exception):
    """Base class for all application errors"""
    pass

# Mid-level — catch entire subsystems
class DatabaseError(AppError): pass
class NetworkError(AppError): pass
class ValidationError(AppError): pass

# Specific — catch individual failure modes
class ConnectionTimeoutError(NetworkError): pass
class DNSResolutionError(NetworkError): pass
class RecordNotFoundError(DatabaseError): pass
class DuplicateKeyError(DatabaseError): pass
class FieldRequiredError(ValidationError): pass
class FieldTooLongError(ValidationError): pass
```

```
AppError
├── DatabaseError
│   ├── RecordNotFoundError
│   └── DuplicateKeyError
├── NetworkError
│   ├── ConnectionTimeoutError
│   └── DNSResolutionError
└── ValidationError
    ├── FieldRequiredError
    └── FieldTooLongError
```

- Catching at any level:
```python
try:
    fetch_user(user_id)
except RecordNotFoundError:
    print("User doesn't exist")       # most specific
except DatabaseError:
    print("DB subsystem failed")      # whole subsystem
except AppError:
    print("Application error")        # anything in the app
except Exception:
    print("Totally unexpected")       # last resort
```
# 3. Strings : (~8 Questions - 18%)

# 4. OOP : (~12 Questions - 34%)

## 4.1. Core OOP Concept :

**Class — blueprint for creating objects :**
- A class defines the structure and behaviour that all its objects will share. It is not an object itself — it is the template
```python
class Dog:
    species = "Canis familiaris"    # class attribute — shared by all instances
	
	# __init__ is the constructor of the class Dog
    def __init__(self, name, age):
        self.name = name            # instance attribute — unique per object
        self.age = age

    def bark(self):
        return f"{self.name} says woof!"
```

- We can create instantiate those class in a variables, which we call them **objects** :
```python
class Member:
	def __init__(self # equivalent to this ):
	print("A new member has been added !")

member_one = Member()
member_two = Member()
>>>A new member has been added !
>>>A new member has been added !

# To know which class the object is instantiated from :
print(member_one.__class__)
>>> <class '__main__.Member'>
```

**Object / Instance — A Concrete Realisation :**

- An object is created by calling the class like a function. Each object is independent:
```python
rex   = Dog("Rex", 3)      # object 1
bella = Dog("Bella", 5)    # object 2

rex.name      # "Rex"
bella.name    # "Bella"
rex is bella  # False — two separate objects in memory
```

- `__init__` is called automatically when an object is created — it initialises the instance's attributes.
```python
type(rex)           # <class '__main__.Dog'>
isinstance(rex, Dog)  # True
```

**Property / Attribute — Data Stored in an Object :**
- There are two kinds:
```python
class Circle:
    pi = 3.14159      # class attribute — belongs to the class, shared by all

    def __init__(self, radius):
        self.radius = radius   # instance attribute — belongs to this object only
```

```python
c1 = Circle(5)
c2 = Circle(10)

Circle.pi     # 3.14159  — accessed on the class
c1.pi         # 3.14159  — found on class (not instance)
c1.radius     # 5
c2.radius     # 10

Circle.pi = 3  # changes it for ALL instances
c1.pi          # 3
c2.pi          # 3

c1.pi = 99     # creates an instance attribute that shadows the class one
c1.pi          # 99   — local to c1
c2.pi          # 3    — still the class attribute
Circle.pi      # 3    — class unchanged
```

**Method — Function Defined Inside a Class :**

- Methods are functions that operate on the object's data. The first parameter is always `self` — a reference to the calling instance:
```python
class Rectangle:
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):                    # instance method
        return self.w * self.h

    def scale(self, factor):
        self.w *= factor               # modifies the object in place
        self.h *= factor

    @classmethod
    def square(cls, side):             # class method — receives the class
        return cls(side, side)

    @staticmethod
    def is_valid(w, h):                # static method — no self, no cls
        return w > 0 and h > 0
```

```python
r = Rectangle(4, 5)
r.area()                  # 20
r.scale(2)
r.area()                  # 80

Rectangle.square(6)       # Rectangle(6, 6)
Rectangle.is_valid(3, 4)  # True
```

| Method Type     | First param | Access To      |
| --------------- | ----------- | -------------- |
| Instance Method | self        | instance+class |
| Class Method    | cls         | class only     |
| Static Method   | -           | neither        |
**Encapsulation — Bundling Data and Behaviour :**

| Prefix | Convention | Effect                            |
| ------ | ---------- | --------------------------------- |
| name   | public     | fully accessible                  |
| _name  | protected  | accessible, but only "internally" |
| __name | private    | name-mangled to _ClassName__name  |
```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner          # public
        self._balance = balance     # protected — convention only
        self.__pin = "1234"         # private — name-mangled

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount

    def get_balance(self):          # controlled read access
        return self._balance
```

```python
acc = BankAccount("Alice", 1000)

acc.owner          # "Alice"   ✅ public
acc._balance       # 1000      ⚠️ accessible but discouraged
acc.__pin          # AttributeError ❌ name-mangled
acc._BankAccount__pin  # "1234"  — still reachable, but clearly internal
```

>[!note]
>Python has no true access enforcement — it relies on convention and discipline.


**Inheritance — Deriving a New Class from an Existing One :**

- A subclass inherits all attributes and methods of its parent, and can extend or override them:
```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound"

    def __str__(self):
        return f"Animal({self.name})"


class Dog(Animal):                     # Dog inherits from Animal
    def speak(self):                   # override
        return f"{self.name} says woof!"

    def fetch(self):                   # new method — only on Dog
        return f"{self.name} fetches the ball"


class Cat(Animal):
    def speak(self):
        return f"{self.name} says meow!"
```

```python
d = Dog("Rex")
d.speak()     # "Rex says woof!"     — overridden
d.fetch()     # "Rex fetches the ball" — Dog-only
str(d)        # "Animal(Rex)"        — inherited from Animal

isinstance(d, Dog)     # True
isinstance(d, Animal)  # True — a Dog IS an Animal
```

**Superclass / Subclass — Parent / Child :**

```
          Animal          ← superclass / parent / base class
        ↙       ↘
     Dog         Cat     ← subclass / child / derived class
      ↓
   GuideDog               ← further subclass
```

```python
class GuideDog(Dog):           # child of Dog, grandchild of Animal
    def __init__(self, name, owner):
        super().__init__(name)       # call parent's __init__
        self.owner = owner

    def speak(self):
        base = super().speak()       # call parent's speak()
        return f"{base} (trained)"

g = GuideDog("Buddy", "Alice")
g.speak()    # "Buddy says woof! (trained)"
g.fetch()    # "Buddy fetches the ball"  — inherited from Dog
```

**Method Resolution Order (MRO) :**
- When Python looks up a method, it follows the MRO — the linearized order of classes to search:
```python
class A: pass
class B(A): pass
class C(A): pass
class D(B, C): pass     # multiple inheritance

D.__mro__
# (<class 'D'>, <class 'B'>, <class 'C'>, <class 'A'>, <class 'object'>)

D.mro()   # same, as a list
```

**Round Up :**

```python
class Vehicle:                          # superclass
    def __init__(self, make, speed):
        self.make = make
        self._speed = speed             # protected

    def describe(self):
        return f"{self.make} @ {self._speed}km/h"

    @classmethod
    def slow(cls, make):               # factory method
        return cls(make, 60)


class ElectricCar(Vehicle):            # subclass
    def __init__(self, make, speed, battery):
        super().__init__(make, speed)  # reuse parent init
        self.__battery = battery       # private

    def describe(self):
        base = super().describe()
        return f"{base}, battery={self.__battery}kWh"

    def charge(self):
        self.__battery = 100


v = Vehicle.slow("Toyota")
e = ElectricCar("Tesla", 200, 75)

print(v.describe())   # Toyota @ 60km/h
print(e.describe())   # Tesla @ 200km/h, battery=75kWh

isinstance(e, Vehicle)    # True
isinstance(e, ElectricCar)  # True
```

## 4.2. Methods & Constructors :

**Defining Methods Inside a Class :**
- Methods are functions defined inside a class body using `def`. The only structural difference from a regular function is the first parameter — `self`:
```python
class Dog:
    def bark(self):
        return "woof!"

    def run(self, distance):
        return f"ran {distance}m"

    def eat(self, food, amount):
        return f"ate {amount}g of {food}"
```
- Methods live on the class — they are shared by all instances. They only become bound to a specific object when called on one.

**The `self` Parameter — Always the First Argument :**
- `self` is a reference to the specific instance the method was called on. It is how a method knows which object's data to work with:
```python
class Counter:
    def set(self, value):
        self.value = value     # stored on THIS instance

    def increment(self):
        self.value += 1        # modifies THIS instance's value

    def get(self):
        return self.value      # reads THIS instance's value
        
a = Counter()
b = Counter()

a.set(10)
b.set(99)

a.increment()

a.get()   # 11 — only a was incremented
b.get()   # 99 — b untouched
```

>[!note]
>`self` is just a convention — Python passes the instance automatically. You could name it anything, but `self` is universal

**How Python Wires `self` Under the Hood :**
- Calling a method on an instance is syntactic sugar:
```python
class Dog:
    def bark(self):
        return f"{self.name} says woof"

rex = Dog()
rex.name = "Rex"

# These two calls are identical:
rex.bark()           # Python rewrites this as →
Dog.bark(rex)        # the instance is passed as the first argument
```

- The method on the class is an **unbound function**. Accessing it through an instance creates a **bound method** that already knows its `self`:
```python
rex.bark               # <bound method Dog.bark of <Dog object>>
Dog.bark               # <function Dog.bark at 0x...>  — unbound

rex.bark()             # ✅ no argument needed — self = rex
Dog.bark(rex)          # ✅ identical result
Dog.bark()             # ❌ TypeError: missing argument 'self'
```

**`__init__` — The Constructor :**
- `__init__` is called automatically the moment a new object is created. Its job is to initialize the instance's attributes:
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age  = age
        
alice = Person("Alice", 30)   # __init__ runs immediately
                               # self.name = "Alice"
                               # self.age  = 30
```

- The full creation sequence:
```
Person("Alice", 30)
       ↓
1. __new__()   — allocates memory, creates the object
       ↓
2. __init__()  — initialises attributes on the new object
       ↓
3. returns the fully constructed object → alice
```

>[!note]
>`__init__` never returns a value — returning anything other than `None` raises a `TypeError`.

**Default Parameter Values in `__init__` :**
```python
class Car:
    def __init__(self, make, speed=120, electric=False):
        self.make     = make
        self.speed    = speed
        self.electric = electric
        
Car("Toyota")                      # speed=120, electric=False
Car("Tesla",  electric=True)       # speed=120, electric=True
Car("BMW",    200)                 # speed=200, electric=False
Car("Rivian", 160, True)           # all three supplied
```

**Attributes Set Outside `__init__` :**
- You can add attributes to an object at any time — but it is strongly discouraged. Always declare all attributes in `__init__` for clarity and predictability:
```python
# ❌ Fragile — attribute may not exist yet
class Dog:
    def set_name(self, name):
        self.name = name

    def bark(self):
        return f"{self.name} says woof"   # AttributeError if set_name wasn't called

# ✅ Always initialise in __init__
class Dog:
    def __init__(self, name):
        self.name = name                  # guaranteed to exist

    def bark(self):
        return f"{self.name} says woof"
```

**Calling Methods — `obj.method()` :**
```python
class Rectangle:
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

    def perimeter(self):
        return 2 * (self.w + self.h)

    def scale(self, factor):
        self.w *= factor
        self.h *= factor
        return self        # returning self enables method chaining

    def describe(self):
        return f"{self.w} × {self.h}"
        
r = Rectangle(4, 5)

r.area()          # 20
r.perimeter()     # 18
r.scale(2)        # modifies r in place
r.area()          # 80

# We can use Method chaining when `return self`
r = Rectangle(3, 4)
r.scale(2).scale(3).describe()   # "18 × 24"
```

**Methods Calling Other Methods :**
- Methods can call each other via `self`:
```python
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

    def diameter(self):
        return self.radius * 2

    def summary(self):
        return (
            f"radius={self.radius}, "
            f"diameter={self.diameter()}, "   # calls self.diameter()
            f"area={self.area():.2f}"         # calls self.area()
        )
```

**Class vs Instance — What `self` Separates :**
```python
class Player:
    high_score = 0           # class attribute — shared by ALL players

    def __init__(self, name):
        self.name  = name    # instance attribute — unique to each player
        self.score = 0       # instance attribute

    def add_points(self, pts):
        self.score += pts
        if self.score > Player.high_score:
            Player.high_score = self.score   # update the shared record
            
p1 = Player("Alice")
p2 = Player("Bob")

p1.add_points(50)
p2.add_points(80)

p1.score          # 50
p2.score          # 80
Player.high_score # 80  — shared, updated by both players
```

**Round Up :**
```python
class BankAccount:
    interest_rate = 0.03                    # class attribute

    def __init__(self, owner, balance=0):   # constructor
        self.owner   = owner                # instance attribute
        self._balance = balance             # protected attribute

    def deposit(self, amount):              # instance method
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self._balance += amount
        return self                         # enables chaining

    def withdraw(self, amount):
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount
        return self

    def apply_interest(self):
        self._balance *= (1 + BankAccount.interest_rate)
        return self

    def balance(self):
        return self._balance

    def __str__(self):
        return f"Account({self.owner}, £{self._balance:.2f})"


acc = BankAccount("Alice", 1000)
acc.deposit(500).deposit(200).apply_interest()
print(acc)           # Account(Alice, £1761.00)
print(acc.balance()) # 1761.0
```

## 4.3. Introspection :

- Introspection means examining objects, classes, and their structure **at runtime** — asking Python "what are you, what do you have, and where did you come from?"

**`hasattr(obj, 'attr')` — Check if Attribute Exists :**
- Returns `True` if the attribute exists on the object (or its class chain), `False` otherwise:
```python
class Dog:
    species = "Canis familiaris"

    def __init__(self, name):
        self.name = name

    def bark(self):
        return "woof"

rex = Dog("Rex")

hasattr(rex, "name")      # True  — instance variable
hasattr(rex, "species")   # True  — class variable, found via lookup chain
hasattr(rex, "bark")      # True  — methods count too
hasattr(rex, "fly")       # False — doesn't exist anywhere
hasattr(rex, "__init__")  # True  — dunder methods included
```

- Safer than catching `AttributeError`:
```python
# ❌ verbose
try:
    value = obj.speed
except AttributeError:
    value = None

# ✅ clean
value = obj.speed if hasattr(obj, "speed") else None
```

>[!note]
>Under the hood, `hasattr` calls `getattr` and returns `False` if it raises `AttributeError` — so it respects `__getattr__` and properties.

**`getattr` — Read an Attribute by Name :**
```python
getattr(obj, name)             # basic — raises AttributeError if missing
getattr(obj, name, default)    # safe — returns default if missing
```

```python
class Car:
    def __init__(self, make, speed):
        self.make  = make
        self.speed = speed

c = Car("Toyota", 120)

getattr(c, "make")           # "Toyota"
getattr(c, "speed")          # 120
getattr(c, "color")          # AttributeError ❌
getattr(c, "color", "red")   # "red"  — default returned ✅
```

- Powerful for **dynamic attribute access** :
```python
fields = ["make", "speed", "color"]
for field in fields:
    print(f"{field}: {getattr(c, field, 'N/A')}")

# make:  Toyota
# speed: 120
# color: N/A
```

- Also works to call methods dynamically :
```python
method = getattr(c, "describe", None)
if callable(method):
    method()        # calls c.describe() if it exists
```

**`setattr` — Set an Attribute by Name :**
```python
setattr(obj, name, value)
```

```python
c = Car("Toyota", 120)

setattr(c, "color", "red")     # same as c.color = "red"
setattr(c, "speed", 200)       # same as c.speed = 200

c.color    # "red"
c.speed    # 200
```

- Useful when the attribute name is only known at runtime:
```python
data = {"make": "BMW", "speed": 250, "color": "black"}

for key, value in data.items():
    setattr(c, key, value)      # bulk-assign from a dict

# equivalent to:
# c.make  = "BMW"
# c.speed = 250
# c.color = "black"
```

**`delattr` — Delete an Attribute by Name :**
```python
delattr(obj, name)
```

```python
c = Car("Toyota", 120)
c.color = "red"

delattr(c, "color")    # removes color from c.__dict__
hasattr(c, "color")    # False

delattr(c, "make")     # removes make
c.__dict__             # {'speed': 120}

delattr(c, "speed")
delattr(c, "missing")  # AttributeError ❌ — must exist
```

**`__name__` — Class Name as a String :**
```python
class ElectricCar:
    pass

ElectricCar.__name__     # "ElectricCar"  — the class itself

e = ElectricCar()
type(e).__name__         # "ElectricCar"  — via the instance
e.__class__.__name__     # "ElectricCar"  — equivalent
```

>[!note]
>Note — `__name__` lives on the **class**, not the instance:
>```
>e.__name__         # AttributeError ❌ — instances don't have __name__
type(e).__name__   # ✅ correct way to get it from an instance
>```

**`__module__` — Where the Class Was Defined: **

```python
# file: vehicles.py
class Car:
    pass
```

```python
import vehicles

vehicles.Car.__module__    # "vehicles"
```

```python
# in the same file being run directly:
class Dog:
    pass

Dog.__module__    # "__main__"  — the entry-point module
```

**`__bases__` — Tuple of Direct Parent Classes:**

```python
class Animal: pass
class Flyable: pass
class Bird(Animal, Flyable): pass
class Parrot(Bird): pass

Bird.__bases__       # (<class 'Animal'>, <class 'Flyable'>)
Parrot.__bases__     # (<class 'Bird'>,)
Animal.__bases__     # (<class 'object'>,)  — every class inherits from object
object.__bases__     # ()  — object has no parents
```

- `__bases__` is only the **direct** parents. For the full chain use `__mro__`:
```python
Parrot.__mro__
# (<class 'Parrot'>, <class 'Bird'>, <class 'Animal'>,
#  <class 'Flyable'>, <class 'object'>)

Parrot.mro()     # same, as a plain list
```

- Other useful Introspection Tools :
	1. `type()` — what is this object? : 
	```python
	type(42)           # <class 'int'>
type("hello")      # <class 'str'>
type(rex)          # <class '__main__.Dog'>
type(Dog)          # <class 'type'>  — classes are instances of type
	```
	2. `isinstance()` — is it this type or a subclass? :
	```python
	isinstance(rex, Dog)     # True
	isinstance(rex, Animal)  # True  — Dog is a subclass of Animal
	isinstance(rex, str)     # False
	```
	3. `issubclass()` — is one class derived from another? :
	```python
	issubclass(Dog, Animal)   # True
issubclass(Dog, Dog)      # True  — a class is a subclass of itself
issubclass(str, object)   # True  — everything inherits from object
issubclass(Animal, Dog)   # False — parent is not a subclass of child
	```
	4. `dir()` — all attribute names including inherited ones :
	```python
	dir(rex)
	# ['__class__', '__dict__', '__init__', 'bark', 'name', 'species', ...]
	# includes everything from Dog and object
	```
	5. `vars()` — same as `__dict__` :
	```python
	vars(rex)       # {'name': 'Rex'}   — same as rex.__dict__
	vars(Dog)       # mappingproxy({...})  — same as Dog.__dict__
	```
	6. `callable()` — can it be called? :
	```python
	callable(rex.bark)     # True   — it's a method
	callable(rex.name)     # False  — it's a string
	callable(Dog)          # True   — classes are callable (they create instances)
	```

# 5. Miscellaneous : (~9 Questions - 22%)

## 5.1. List Comprehensions :

**Basic — `[expression for item in iterable]` :**
- A compact way to build a list by transforming every item in an iterable:
```python
# traditional loop
squares = []
for x in range(6):
    squares.append(x ** 2)

# comprehension — identical result, one line
squares = [x ** 2 for x in range(6)]
# [0, 1, 4, 9, 16, 25]
```
- The pattern always reads naturally left to right — "give me `x ** 2` for each `x` in `range(6)`".
```python
# works on any iterable
letters  = [c.upper() for c in "hello"]         # ['H','E','L','L','O']
lengths  = [len(w) for w in ["hi","hello","hey"]] # [2, 5, 3]
doubled  = [x * 2 for x in [1, 2, 3, 4]]        # [2, 4, 6, 8]
booleans = [bool(x) for x in [0, 1, "", "a"]]   # [False, True, False, True]
```

**With Condition — `[expr for item in iterable if condition]` :**
- The `if` clause filters — only items where the condition is `True` are processed:
```python
evens = [x for x in range(10) if x % 2 == 0]
# [0, 2, 4, 6, 8]

long_words = [w for w in ["hi","hello","hey","howdy"] if len(w) > 3]
# ["hello", "howdy"]

positives = [x for x in [-3, -1, 0, 2, 5] if x > 0]
# [2, 5]
```

- Condition and expression are independent — transform one thing, filter by another:
```python
# square only the odd numbers
[x**2 for x in range(10) if x % 2 != 0]
# [1, 9, 25, 49, 81]

# uppercase only non-empty strings
words = ["hello", "", "world", "", "!"]
[w.upper() for w in words if w]
# ["HELLO", "WORLD", "!"]
```

**`if / else` in the expression (ternary) — no filtering, transforms every item :**
- When `if/else` is in the **expression** part (before `for`), every item is kept — it selects between two values:
```python
# if condition AFTER for → filters (removes items)
[x for x in range(6) if x % 2 == 0]          # [0, 2, 4]

# if/else BEFORE for → transforms (keeps all items)
["even" if x % 2 == 0 else "odd" for x in range(6)]
# ["even", "odd", "even", "odd", "even", "odd"]

# both together — transform the kept items
[x**2 if x > 0 else 0 for x in [-1, 2, -3, 4] if x != 0]
# [0, 4, 0, 16]
```

**Nested — `[expr for x in outer for y in inner]` :**
- Equivalent to nested `for` loops — outer loop first, inner loop second:
```python
# nested loops
pairs = []
for x in [1, 2, 3]:
    for y in ["a", "b"]:
        pairs.append((x, y))

# comprehension — same result
pairs = [(x, y) for x in [1, 2, 3] for y in ["a", "b"]]
# [(1,'a'),(1,'b'),(2,'a'),(2,'b'),(3,'a'),(3,'b')]
```

**Flattening a list of lists:**
```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

flat = [n for row in matrix for n in row]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

**With a condition on the inner loop:**
```python
# all (x, y) pairs where x != y
[(x, y) for x in range(3) for y in range(3) if x != y]
# [(0,1),(0,2),(1,0),(1,2),(2,0),(2,1)]
```

**Nested comprehension — list of lists :**
- A comprehension that produces a list of lists (matrix transposition, grids):
```python
# 3×3 multiplication table
table = [[x * y for y in range(1, 4)] for x in range(1, 4)]
# [[1, 2, 3],
#  [2, 4, 6],
#  [3, 6, 9]]

# transpose a matrix
matrix    = [[1, 2, 3],
             [4, 5, 6]]

transposed = [[row[i] for row in matrix] for i in range(3)]
# [[1, 4],
#  [2, 5],
#  [3, 6]]
```

**Dictionary Comprehension — `{k: v for k, v in pairs}` :**
- Same idea applied to dictionaries — produces `{key: value}` pairs:
```python
# basic
squares = {x: x**2 for x in range(6)}
# {0:0, 1:1, 2:4, 3:9, 4:16, 5:25}

# from two lists using zip
keys   = ["a", "b", "c"]
values = [1,   2,   3  ]
d = {k: v for k, v in zip(keys, values)}
# {"a": 1, "b": 2, "c": 3}

# from an existing dict — transform values
prices    = {"apple": 1.0, "banana": 0.5, "cherry": 2.0}
discounted = {k: round(v * 0.9, 2) for k, v in prices.items()}
# {"apple": 0.9, "banana": 0.45, "cherry": 1.8}
```

- With a condition — filter entries:
```python
# keep only items over £1
expensive = {k: v for k, v in prices.items() if v > 1.0}
# {"apple": 1.0, "cherry": 2.0}  — banana excluded

# invert a dict (swap keys and values)
original = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in original.items()}
# {1: "a", 2: "b", 3: "c"}
```

**Set Comprehension — `{expr for item in iterable}` :**
- Same syntax as dict comprehension but without the colon — produces a set (unique values):
```python
{x**2 for x in [-2, -1, 0, 1, 2]}
# {0, 1, 4}  — duplicates removed automatically

{w.lower() for w in ["Hello","WORLD","hello","Python"]}
# {"hello", "world", "python"}
```

**Generator Expression — `(expr for item in iterable)` :**
- Parentheses instead of brackets — produces a lazy iterator, not a list. Values are computed one at a time on demand:
```python
gen = (x**2 for x in range(1000000))  # no memory cost yet
next(gen)    # 0
next(gen)    # 1

# useful directly inside functions that accept iterables
sum(x**2 for x in range(10))      # 285 — no intermediate list created
max(len(w) for w in ["hi","hello","hey"])  # 5
```

**Round Up :**
```python
data = [1, 2, 3, 4, 5, 6]

# list comprehension
evens_list = [x for x in data if x % 2 == 0]
# [2, 4, 6]

# set comprehension
evens_set  = {x for x in data if x % 2 == 0}
# {2, 4, 6}

# dict comprehension
evens_dict = {x: x**2 for x in data if x % 2 == 0}
# {2: 4, 4: 16, 6: 36}

# generator expression
evens_gen  = (x for x in data if x % 2 == 0)
# <generator object> — lazy, computed on demand
```
## 5.2. Lambda Function :

**Syntax — `lambda args: expression` :**
- A lambda is a small anonymous function defined in a single expression. It can take any number of arguments but can only contain **one expression** — no statements, no assignments, no `return` keyword:
```python
# regular function
def square(x):
    return x ** 2

# equivalent lambda
square = lambda x: x ** 2

square(5)    # 25
```

- The expression after `:` is always the return value — `return` is implicit.
```python
# zero arguments
greet   = lambda: "hello"

# one argument
double  = lambda x: x * 2

# multiple arguments
add     = lambda x, y: x + y
clamp   = lambda x, lo, hi: max(lo, min(x, hi))

# default argument values
power   = lambda x, n=2: x ** n

greet()            # "hello"
double(7)          # 14
add(3, 4)          # 7
clamp(15, 0, 10)   # 10
power(3)           # 9
power(3, 3)        # 27
```

**Anonymous — Used Once, Not Named :**
- The real purpose of lambdas is to be passed directly without needing a name:
```python
# ❌ naming a lambda — just use def instead
is_even = lambda x: x % 2 == 0

# ✅ def is clearer when you need a named function
def is_even(x):
    return x % 2 == 0

# ✅ lambda shines when passed directly — no name needed
nums = [3, 1, 4, 1, 5, 9, 2, 6]
nums.sort(key=lambda x: -x)    # sort descending, inline
```

- Lambdas cannot contain:
```python
lambda x: if x > 0: return x    # ❌ statements not allowed
lambda x: x = x + 1             # ❌ assignment not allowed
lambda x: print(x); x * 2       # ❌ multiple expressions not allowed

# for any of these — use def
```

**Passing Lambdas as Arguments :**
- Lambdas are most useful as throwaway functions passed to other functions:
```python
# `sorted()` and `list.sort()` — `key` argument
words = ["banana", "apple", "fig", "cherry", "date"]

sorted(words, key=lambda w: len(w))
# ["fig", "date", "apple", "banana", "cherry"]  — by length

sorted(words, key=lambda w: w[-1])
# sorted by last letter

people = [{"name": "Alice", "age": 30},
          {"name": "Bob",   "age": 25},
          {"name": "Carol", "age": 35}]

sorted(people, key=lambda p: p["age"])
# [Bob(25), Alice(30), Carol(35)]

sorted(people, key=lambda p: p["name"])
# [Alice, Bob, Carol]  — alphabetically
```

```python
# `min()` / `max()` — `key` argument
words = ["banana", "fig", "cherry"]

min(words, key=len)                       # "fig"
max(words, key=len)                       # "banana"
max(people, key=lambda p: p["age"])       # Carol
```

**`map(func, iterable)` — Apply to Each Element :**
- Applies a function to every item and returns a **lazy iterator**. Wrap in `list()` to materialise:

```python
nums = [1, 2, 3, 4, 5]

list(map(lambda x: x ** 2, nums))       # [1, 4, 9, 16, 25]
list(map(lambda x: x * 2, nums))        # [2, 4, 6, 8, 10]
list(map(lambda x: str(x), nums))       # ['1','2','3','4','5']
list(map(lambda x: x > 3, nums))        # [False,False,False,True,True]
```

- `map` with multiple iterables — zips them together:
```python
a = [1, 2, 3]
b = [10, 20, 30]

list(map(lambda x, y: x + y, a, b))    # [11, 22, 33]
list(map(lambda x, y: x * y, a, b))    # [10, 40, 90]
```

- `map` with a named function — lambdas aren't required:
```python
list(map(str.upper, ["hello", "world"]))    # ['HELLO', 'WORLD']
list(map(abs, [-1, -2, 3, -4]))             # [1, 2, 3, 4]
list(map(int, ["1", "2", "3"]))             # [1, 2, 3]
```

**`filter(func, iterable)` — Keep Where `True` :**
- Applies a function to every item and keeps only those where the result is truthy. Also returns a **lazy iterator**:
```python
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

list(filter(lambda x: x % 2 == 0, nums))    # [2, 4, 6, 8, 10]
list(filter(lambda x: x > 5, nums))         # [6, 7, 8, 9, 10]
list(filter(lambda x: x ** 2 > 10, nums))   # [4, 5, 6, 7, 8, 9, 10]
```

**Combining `map` and `filter` :**
- Chain them together — `filter` first to narrow down, then `map` to transform:
```python
nums = range(-5, 6)   # -5 to 5

# square only the positive numbers
list(map(lambda x: x**2,
         filter(lambda x: x > 0, nums)))
# [1, 4, 9, 16, 25]
```

- Reading inside-out gets hard — a comprehension is often clearer:
```python
# map + filter
result = list(map(lambda x: x**2, filter(lambda x: x > 0, nums)))

# equivalent comprehension — reads left to right
result = [x**2 for x in nums if x > 0]
```

**`map` / `filter` vs Comprehensions :**
- Both approaches are valid — choose based on context:
```python
nums = [1, 2, 3, 4, 5]

# map
list(map(lambda x: x * 2, nums))      # [2, 4, 6, 8, 10]
# comprehension
[x * 2 for x in nums]                 # [2, 4, 6, 8, 10]

# filter
list(filter(lambda x: x > 3, nums))   # [4, 5]
# comprehension
[x for x in nums if x > 3]            # [4, 5]
```
## 5.3. Closures :
- A closure is an inner function that **remembers variables from its enclosing scope** even after that outer function has finished and returned. The inner function carries those variables with it — they are captured, not copied:
```python
def outer():
    message = "hello"          # lives in outer's scope

    def inner():
        print(message)         # captures message from outer

    return inner               # return the function — not a call


fn = outer()                   # outer() runs and returns inner
                               # outer's local scope is gone — but message survives
fn()                           # "hello"  — inner still remembers message
```

- The returned `inner` function plus the captured variable `message` together form the **closure**.

**The Enclosing Scope Must Have Already Returned :**
- This is what makes closures interesting — the outer function is done, its stack frame is gone, yet the inner function still has access to its variables:
```python
def make_greeting(name):
    greeting = f"Hello, {name}!"     # local to make_greeting

    def greet():
        return greeting               # captured from enclosing scope

    return greet                      # make_greeting returns and exits


say_hi   = make_greeting("Alice")    # make_greeting is finished
say_hello = make_greeting("Bob")

say_hi()     # "Hello, Alice!"   — Alice's greeting is still alive
say_hello()  # "Hello, Bob!"     — Bob's is independent
```

>[!note]
>Each call to `make_greeting` creates a **new, independent closure** — `say_hi` and `say_hello` each have their own captured `greeting`.

**Inspecting a Closure :**
- Python exposes the captured variables on the `__closure__` attribute:
```python
def make_multiplier(n):
    def multiply(x):
        return x * n           # n is captured
    return multiply


triple = make_multiplier(3)

triple.__closure__                          # (<cell object at 0x...>,)
triple.__closure__[0].cell_contents        # 3  — the captured value

triple(5)     # 15
triple(10)    # 30
```

**Factory Functions — The Main Use Case :**
- Closures let you create specialized functions from a general template:
```python
def make_multiplier(n):
    def multiply(x):
        return x * n
    return multiply


double  = make_multiplier(2)
triple  = make_multiplier(3)
times10 = make_multiplier(10)

double(5)    # 10
triple(5)    # 15
times10(5)   # 50
```

```python
def make_power(exp):
    def power(base):
        return base ** exp
    return power


square = make_power(2)
cube   = make_power(3)

square(4)    # 16
cube(3)      # 27
```

**Callbacks :**
- Closures are natural callbacks — they carry their context with them:
```python
def make_logger(prefix):
    def log(message):
        print(f"[{prefix}] {message}")
    return log


info  = make_logger("INFO")
error = make_logger("ERROR")
debug = make_logger("DEBUG")

info("server started")      # [INFO] server started
error("connection lost")    # [ERROR] connection lost
debug("x = 42")            # [DEBUG] x = 42
```

**Data Hiding — State Without a Class :**
- Closures can encapsulate state that is completely inaccessible from the outside — no class needed:
```python
def make_counter(start=0):
    count = start              # private — no way to access directly

    def increment():
        nonlocal count
        count += 1
        return count

    def decrement():
        nonlocal count
        count -= 1
        return count

    def reset():
        nonlocal count
        count = start
        return count

    def value():
        return count

    return increment, decrement, reset, value


inc, dec, rst, val = make_counter(10)

inc()    # 11
inc()    # 12
inc()    # 13
dec()    # 12
val()    # 12
rst()    # 10
val()    # 10
```

>[!note]
>`count` is completely private — there is no way to reach it from outside except through the returned functions.

**`nonlocal` — Modify an Enclosing Variable :**
- By default, an inner function can **read** enclosing variables but cannot **assign** to them. Assigning without `nonlocal` creates a new local variable instead:
```python
def outer():
    x = 10

    def inner():
        x = 99        # ⚠️ creates a LOCAL x — does not touch outer's x
        print(x)      # 99

    inner()
    print(x)          # 10 — outer's x is unchanged


outer()
# 99
# 10
```

- `nonlocal` declares that the name refers to the enclosing scope's variable:
```python
def outer():
    x = 10

    def inner():
        nonlocal x    # ✅ refers to outer's x
        x = 99
        print(x)      # 99

    inner()
    print(x)          # 99 — outer's x was modified


outer()
# 99
# 99
```

- `nonlocal` walks up the scope chain — it finds the nearest enclosing scope that has that variable:
```python
def level1():
    x = 1

    def level2():
        x = 2                    # local to level2

        def level3():
            nonlocal x           # refers to level2's x (nearest enclosing)
            x = 99

        level3()
        print("level2:", x)      # 99 — level2's x modified

    level2()
    print("level1:", x)          # 1  — level1's x untouched


level1()
# level2: 99
# level1: 1
```

**`nonlocal` vs `global` :**

```python
x = "global"

def outer():
    x = "outer"

    def inner():
        global x      # refers to module-level x — skips outer entirely
        x = "changed globally"

    inner()
    print("outer:", x)    # "outer" — outer's x untouched

inner_fn = outer()
print("global:", x)       # "changed globally"
```

**The Late-Binding Trap :**
- Closures capture variables by **reference**, not by value. This catches many developers off guard in loops:
```python
# ❌ common mistake — all closures share the same i
funcs = [lambda: i for i in range(5)]

funcs[0]()    # 4  — not 0!
funcs[1]()    # 4  — not 1!
funcs[4]()    # 4  — all return 4 (the final value of i)
```

- All five lambdas capture the same `i` — and by the time they're called, the loop has finished and `i` is `4`.
- Fix — capture the current value with a default argument:
```python
# ✅ default argument captures value at definition time
funcs = [lambda i=i: i for i in range(5)]

funcs[0]()    # 0
funcs[1]()    # 1
funcs[4]()    # 4

# Or use a factory function:

# ✅ factory creates a new scope with its own i each time
def make_fn(i):
    return lambda: i

funcs = [make_fn(i) for i in range(5)]

funcs[0]()    # 0
funcs[3]()    # 3
```

**Closure vs Class — Choosing Between Them :**
```python
# Closure — lightweight, one concern
def make_counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

counter = make_counter()
counter()    # 1
counter()    # 2
```

```python
# Class — more structure, multiple behaviours, inspectable state
class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

counter = Counter()
counter.increment()    # 1
counter.count          # 1  — state is accessible
```
## 5.4. File I/O - Concepts :

**Opening Files — `open()` :**
```python
open(file, mode='r', encoding=None, buffering=-1, errors=None)
```

```python
f = open("data.txt", "r")          # open for reading (default)
f = open("data.txt", "w")          # open for writing
f = open("data.txt", "a")          # open for appending
f = open("data.txt", "rb")         # open for reading in binary mode
f = open("data.txt", "w", encoding="utf-8")  # explicit encoding
```

- Always close what you open — or better, use a `with` block:
```python
# ❌ manual close — easy to forget, skipped on exceptions
f = open("data.txt")
data = f.read()
f.close()

# ✅ with block — closes automatically, even on exceptions
with open("data.txt") as f:
    data = f.read()
```

**I/O Modes :**

| Mode   | Meaning          | File must exist?                       | Truncates?             |
| ------ | ---------------- | -------------------------------------- | ---------------------- |
| `'r'`  | Read             | ✅ yes — `FileNotFoundError` if missing | ❌                      |
| `'w'`  | Write            | ❌ created if missing                   | ✅ yes — erases content |
| `'a'`  | Append           | ❌ created if missing                   | ❌ writes at end        |
| `'x'`  | Exclusive create | ❌ — `FileExistsError` if exists        | n/a                    |
| `'r+'` | Read + write     | ✅ yes                                  | ❌                      |
| `'w+'` | Read + write     | ❌ created if missing                   | ✅ yes                  |
| `'a+'` | Read + append    | ❌ created if missing                   | ❌                      |
- For Binary modes — add `b` :
```python
'rb'   # read binary
'wb'   # write binary
'ab'   # append binary
'rb+'  # read + write binary
```

**Text Mode vs Binary Mode :**
- The fundamental split in file I/O:

```python
# Text mode ('r', 'w', 'a')
with open("data.txt", "r", encoding="utf-8") as f:
    content = f.read()      # str — decoded from bytes automatically
```

- Reads and writes **`str`** objects
- Python automatically **encodes/decodes** using the specified (or system default) encoding
- **Line endings are normalised** — `\r\n` (Windows) is converted to `\n` on read; `\n` is converted back to the platform default on write
- Supports iteration line by line

```python
# Binary mode ('rb', 'wb')
with open("image.png", "rb") as f:
    content = f.read()      # bytes — raw data, no decoding
```

- Reads and writes **`bytes`** objects
- **No encoding/decoding** — raw bytes, exactly as stored on disk
- **No line ending conversion** — `\r\n` stays `\r\n`
- Required for images, audio, video, PDFs, zip files, pickles

**File Handles vs Streams :**
- **File handle :**

- A **file handle** (also called a file object) is what `open()` returns — a Python object with methods for reading and writing. It wraps a specific file on disk:

```python
with open("data.txt") as f:
    print(type(f))           # <class '_io.TextIOWrapper'>
    print(f.name)            # 'data.txt'
    print(f.mode)            # 'r'
    print(f.encoding)        # 'utf-8'  (or system default)
    print(f.closed)          # False
    
f.closed                     # True — closed after with block exits
```

- A file handle has a **current position** — a cursor that advances as you read or write:

```python
with open("data.txt") as f:
    f.read(5)       # reads first 5 characters, cursor moves to position 5
    f.tell()        # 5  — current position
    f.read(5)       # reads next 5 characters
    f.tell()        # 10

    f.seek(0)       # move cursor back to beginning
    f.read(5)       # reads the same first 5 characters again

    f.seek(0, 2)    # seek to end (0 bytes from end)
    f.tell()        # total file size in bytes
```

- **Streams :**
- A **stream** is a more general concept — any object that supports sequential reading or writing, not necessarily backed by a file on disk. File handles are one kind of stream. Others include:

```python
import io

# in-memory text stream — behaves like a file but stores in RAM
buf = io.StringIO()
buf.write("hello ")
buf.write("world")
buf.seek(0)
buf.read()         # "hello world"

# in-memory binary stream
raw = io.BytesIO(b"\x00\x01\x02\x03")
raw.read(2)        # b'\x00\x01'
raw.read(2)        # b'\x02\x03'
```

- `StringIO` and `BytesIO` are useful for:
	1. Testing code that expects a file without touching the disk
	2. Building content in memory before writing it all at once
	3. Passing "file-like objects" to libraries that accept streams

**Common encodings :**

```python
encoding="utf-8"          # universal — use this almost always
encoding="utf-8-sig"      # utf-8 with BOM — handles Windows-generated files
encoding="latin-1"        # Western European — legacy files
encoding="ascii"          # 7-bit ASCII only
```
## 5.5. File I/O - Operations :

**`open(path, mode)` — Returns a File Object :**

```python
f = open("data.txt", "r")          # text read
f = open("data.txt", "w")          # text write — truncates
f = open("data.txt", "a")          # text append
f = open("data.txt", "rb")         # binary read
f = open("data.txt", "wb")         # binary write
f = open("data.txt", "r", encoding="utf-8")  # explicit encoding
```

- The returned file object exposes all read/write methods and tracks the current cursor position.

**`errno` — OS Error Codes :**

- When a file operation fails, Python raises `OSError` (or a subclass). The `errno` module gives named constants for the numeric error codes:

```python
import errno
import os

try:
    f = open("missing.txt", "r")
except OSError as e:
    print(e.errno)                  # 2
    print(e.strerror)               # No such file or directory
    print(e.filename)               # missing.txt

    if e.errno == errno.ENOENT:     # 2 — file not found
        print("File does not exist")
    elif e.errno == errno.EACCES:   # 13 — permission denied
        print("Permission denied")
    elif e.errno == errno.ENOSPC:   # 28 — no space left
        print("Disk is full")
```

- Common `errno` constants:

| Constant        | Code | Meaning                    |
| --------------- | ---- | -------------------------- |
| `errno.ENOENT`  | 2    | No such file or directory  |
| `errno.EACCES`  | 13   | Permission denied          |
| `errno.EEXIST`  | 17   | File already exists        |
| `errno.ENOSPC`  | 28   | No space left on device    |
| `errno.EISDIR`  | 21   | Is a directory, not a file |
| `errno.ENOTDIR` | 20   | Not a directory            |

- `OSError` subclasses map to the most common codes automatically:

```python
except FileNotFoundError:      # errno.ENOENT — no need to check e.errno
except PermissionError:        # errno.EACCES
except FileExistsError:        # errno.EEXIST
except IsADirectoryError:      # errno.EISDIR
```

**`file.read(n)` — Read n Bytes / Characters, or All :**

```python
with open("data.txt") as f:
    all_content = f.read()       # entire file as one string
    
with open("data.txt") as f:
    chunk = f.read(10)           # first 10 characters
    next_chunk = f.read(10)      # next 10 — cursor advances
    empty = f.read()             # "" — at end of file
```

- Reading in chunks — useful for large files:

```python
with open("large.txt") as f:
    while True:
        chunk = f.read(1024)     # 1 KB at a time
        if not chunk:            # empty string means EOF
            break
        process(chunk)
```

- Binary mode returns `bytes`:

```python
with open("image.png", "rb") as f:
    header = f.read(4)           # b'\x89PNG'
    rest   = f.read()            # remaining bytes
```

**`file.readline()` — Read One Line :**

- Reads up to and including the next `\n`. Returns an empty string `""` at end of file:
```python
with open("data.txt") as f:
    line1 = f.readline()         # "first line\n"
    line2 = f.readline()         # "second line\n"
    line3 = f.readline()         # "third line\n"
    eof   = f.readline()         # ""  — end of file
```

- Stripping the newline:
```python
with open("data.txt") as f:
    line = f.readline().rstrip("\n")    # removes trailing newline
```

- Reading until EOF manually:
```python
with open("data.txt") as f:
    while True:
        line = f.readline()
        if not line:             # "" is falsy — EOF
            break
        print(line, end="")
```

**`file.readlines()` — Read All Lines Into a List :**

- Returns a list where each element is one line including its `\n`:
```python
with open("data.txt") as f:
    lines = f.readlines()
    # ["first line\n", "second line\n", "third line\n"]

lines[0]           # "first line\n"
len(lines)         # 3

# strip newlines from every line
clean = [line.rstrip("\n") for line in lines]
# ["first line", "second line", "third line"]
```

- `readlines()` loads the entire file into memory. For large files, iterate the file object directly instead:
```python
# ❌ loads everything into memory
lines = f.readlines()
for line in lines:
    process(line)

# ✅ reads one line at a time — memory efficient
for line in f:
    process(line)
```

**`file.write(string)` — Write a String :**

- Writes the string and returns the number of characters written. Does **not** add a newline automatically:
```python
with open("output.txt", "w") as f:
    n = f.write("hello\n")     # returns 6 (5 chars + \n)
    f.write("world\n")         # returns 6

# output.txt contains:
# hello
# world
```

- Writing multiple lines:
```python
lines = ["alpha\n", "beta\n", "gamma\n"]

with open("output.txt", "w") as f:
    for line in lines:
        f.write(line)

# or — writelines() writes a list, no newlines added automatically
with open("output.txt", "w") as f:
    f.writelines(lines)
```

- Binary mode — write `bytes`:
```python
with open("data.bin", "wb") as f:
    f.write(b"\x00\x01\x02\x03")
    f.write(bytes([10, 20, 30]))
```

- Appending — cursor starts at end, existing content preserved:
```python
with open("log.txt", "a") as f:
    f.write("new entry\n")     # added after all existing content
```

**`file.close()` — Release the File :**

- Flushes any buffered data and releases the OS file handle:
```python
f = open("data.txt")
data = f.read()
f.close()               # must be called — even on error

f.closed                # True — safe to check
f.read()                # ValueError: I/O operation on closed file
```

- Manually closing is error-prone — if an exception occurs before `close()`, the file stays open:
```python
# ❌ close() skipped if read() raises an exception
f = open("data.txt")
data = f.read()         # exception here →
f.close()               # never reached
```

- The `with` block solves this entirely.

**`with open(...) as f:` — Context Manager :**

- The `with` statement guarantees the file is closed when the block exits — regardless of whether an exception occurred:
```python
with open("data.txt", "r") as f:
    data = f.read()
# file is closed here — automatically, always

f.closed    # True
```

- Under the hood, `with` calls `f.__enter__()` on entry and `f.__exit__()` on exit (which calls `f.close()`).

- Multiple files in one `with`:
```python
# open two files at once
with open("input.txt") as src, open("output.txt", "w") as dst:
    for line in src:
        dst.write(line.upper())
```

- Reading, processing, writing — the full pattern:
```python
with open("input.txt", encoding="utf-8") as src:
    lines = src.readlines()

processed = [line.strip().upper() for line in lines if line.strip()]

with open("output.txt", "w", encoding="utf-8") as dst:
    dst.writelines(line + "\n" for line in processed)
```

**Cursor Navigation — `seek()` and `tell()` :**
```python
with open("data.txt") as f:
    f.tell()             # 0 — start of file

    f.read(5)            # read 5 chars
    f.tell()             # 5 — cursor moved

    f.seek(0)            # back to start
    f.seek(5)            # jump to position 5
    f.seek(0, 0)         # same as seek(0) — from start
    f.seek(0, 1)         # seek 0 bytes from current position
    f.seek(0, 2)         # jump to end of file

    f.seek(0)
    f.read(3)            # reads first 3 chars again
```

**`bytearray` — Mutable Buffer for Binary I/O :**

- `bytes` is immutable. `bytearray` is its mutable equivalent — a buffer you can modify in place, ideal for binary I/O and protocol work:
```python
# creating bytearray
ba = bytearray(4)                  # bytearray(b'\x00\x00\x00\x00')
ba = bytearray([65, 66, 67])       # bytearray(b'ABC')
ba = bytearray(b"hello")           # bytearray(b'hello')
ba = bytearray("hello", "utf-8")   # bytearray(b'hello')
```

- Mutable — individual bytes can be changed:
```python
ba = bytearray(b"hello")
ba[0] = 72                 # bytearray(b'Hello')
ba[1:3] = b"EL"            # bytearray(b'HELlo')

ba.append(33)              # bytearray(b'HELlo!')
ba.extend(b" world")       # bytearray(b'HELlo! world')
del ba[0]                  # bytearray(b'ELlo! world')
```

- Convert between `bytes` and `bytearray`:
```python
b  = bytes(ba)       # bytearray → bytes (immutable copy)
ba = bytearray(b)    # bytes     → bytearray (mutable copy)
```

- Reading binary data into a `bytearray`:
```python
with open("image.png", "rb") as f:
    buf = bytearray(f.read())    # mutable buffer

# modify specific bytes
buf[0] = 0x89
buf[1:4] = b"PNG"

# write back
with open("image_modified.png", "wb") as f:
    f.write(buf)
```

- Reading directly into a pre-allocated `bytearray` with `readinto()` — zero copy:
```python
buf = bytearray(1024)         # pre-allocate 1 KB buffer

with open("data.bin", "rb") as f:
    while True:
        n = f.readinto(buf)    # reads into buf, returns bytes read
        if not n:
            break
        process(buf[:n])       # only process the bytes actually read
```

- `readinto()` avoids creating a new `bytes` object on every read — important in tight loops over large files.