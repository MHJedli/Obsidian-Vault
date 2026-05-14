#!/usr/bin/env python3
"""
PCAP-31-03 Practice Exam - Easy Level
50 Questions covering fundamental Python concepts
"""

import random

class PCAPExamEasy:
    def __init__(self):
        self.score = 0
        self.total_questions = 50
        self.questions = [
            {
                "question": "What is the output of: print(type(5))?",
                "options": ["A) <class 'int'>", "B) <class 'float'>", "C) <class 'str'>", "D) int"],
                "answer": "A"
            },
            {
                "question": "Which keyword is used to define a function in Python?",
                "options": ["A) function", "B) def", "C) func", "D) define"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(3 + 2 * 2)?",
                "options": ["A) 10", "B) 7", "C) 8", "D) 12"],
                "answer": "B"
            },
            {
                "question": "Which of the following is a mutable data type?",
                "options": ["A) tuple", "B) string", "C) list", "D) int"],
                "answer": "C"
            },
            {
                "question": "What does the len() function return?",
                "options": ["A) The type of object", "B) The length of an object", "C) The value of object", "D) The memory address"],
                "answer": "B"
            },
            {
                "question": "What is the correct way to create a comment in Python?",
                "options": ["A) // comment", "B) /* comment */", "C) # comment", "D) -- comment"],
                "answer": "C"
            },
            {
                "question": "What is the output of: print('Hello' + 'World')?",
                "options": ["A) Hello World", "B) HelloWorld", "C) Error", "D) Hello+World"],
                "answer": "B"
            },
            {
                "question": "Which operator is used for exponentiation in Python?",
                "options": ["A) ^", "B) **", "C) ^^", "D) pow"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(10 // 3)?",
                "options": ["A) 3.33", "B) 3", "C) 4", "D) 3.0"],
                "answer": "B"
            },
            {
                "question": "Which keyword is used to create a class in Python?",
                "options": ["A) class", "B) Class", "C) define", "D) struct"],
                "answer": "A"
            },
            {
                "question": "What is the output of: print(bool(0))?",
                "options": ["A) True", "B) False", "C) 0", "D) None"],
                "answer": "B"
            },
            {
                "question": "Which method is used to add an element to the end of a list?",
                "options": ["A) add()", "B) append()", "C) insert()", "D) extend()"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print('Python'[0])?",
                "options": ["A) P", "B) Python", "C) y", "D) Error"],
                "answer": "A"
            },
            {
                "question": "Which statement is used to exit a loop prematurely?",
                "options": ["A) exit", "B) stop", "C) break", "D) return"],
                "answer": "C"
            },
            {
                "question": "What is the output of: print(5 == 5.0)?",
                "options": ["A) False", "B) True", "C) Error", "D) None"],
                "answer": "B"
            },
            {
                "question": "Which keyword is used to handle exceptions in Python?",
                "options": ["A) catch", "B) except", "C) handle", "D) error"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(list(range(3)))?",
                "options": ["A) [1, 2, 3]", "B) [0, 1, 2]", "C) [0, 1, 2, 3]", "D) [1, 2]"],
                "answer": "B"
            },
            {
                "question": "Which method converts a string to lowercase?",
                "options": ["A) lowercase()", "B) lower()", "C) toLower()", "D) casefold()"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(10 % 3)?",
                "options": ["A) 3", "B) 1", "C) 0", "D) 3.33"],
                "answer": "B"
            },
            {
                "question": "Which of the following is NOT a valid variable name?",
                "options": ["A) _var", "B) var1", "C) 1var", "D) var_1"],
                "answer": "C"
            },
            {
                "question": "What is the output of: print(type([]))?",
                "options": ["A) <class 'list'>", "B) <class 'array'>", "C) <class 'tuple'>", "D) list"],
                "answer": "A"
            },
            {
                "question": "Which keyword is used to import a module?",
                "options": ["A) include", "B) import", "C) require", "D) using"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(not True)?",
                "options": ["A) True", "B) False", "C) 0", "D) 1"],
                "answer": "B"
            },
            {
                "question": "Which method removes the last element from a list?",
                "options": ["A) remove()", "B) delete()", "C) pop()", "D) clear()"],
                "answer": "C"
            },
            {
                "question": "What is the output of: print('abc' * 2)?",
                "options": ["A) abc2", "B) abcabc", "C) abc abc", "D) Error"],
                "answer": "B"
            },
            {
                "question": "Which function is used to get input from the user?",
                "options": ["A) input()", "B) get()", "C) read()", "D) scan()"],
                "answer": "A"
            },
            {
                "question": "What is the output of: print(len('Hello'))?",
                "options": ["A) 4", "B) 5", "C) 6", "D) Error"],
                "answer": "B"
            },
            {
                "question": "Which operator is used for string concatenation?",
                "options": ["A) &", "B) +", "C) .", "D) ,"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(True and False)?",
                "options": ["A) True", "B) False", "C) 1", "D) 0"],
                "answer": "B"
            },
            {
                "question": "Which method is used to find the index of an element in a list?",
                "options": ["A) find()", "B) search()", "C) index()", "D) locate()"],
                "answer": "C"
            },
            {
                "question": "What is the output of: print(int('10'))?",
                "options": ["A) '10'", "B) 10", "C) 10.0", "D) Error"],
                "answer": "B"
            },
            {
                "question": "Which keyword is used to define a conditional statement?",
                "options": ["A) when", "B) if", "C) condition", "D) check"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(2 ** 3)?",
                "options": ["A) 6", "B) 8", "C) 9", "D) 23"],
                "answer": "B"
            },
            {
                "question": "Which of the following is an immutable data type?",
                "options": ["A) list", "B) dict", "C) set", "D) tuple"],
                "answer": "D"
            },
            {
                "question": "What is the output of: print(abs(-5))?",
                "options": ["A) -5", "B) 5", "C) 0", "D) Error"],
                "answer": "B"
            },
            {
                "question": "Which method is used to split a string into a list?",
                "options": ["A) divide()", "B) split()", "C) separate()", "D) break()"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(True or False)?",
                "options": ["A) True", "B) False", "C) 1", "D) None"],
                "answer": "A"
            },
            {
                "question": "Which function is used to convert a value to a string?",
                "options": ["A) string()", "B) str()", "C) toString()", "D) convert()"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print([1, 2, 3][1])?",
                "options": ["A) 1", "B) 2", "C) 3", "D) Error"],
                "answer": "B"
            },
            {
                "question": "Which keyword is used to skip the current iteration of a loop?",
                "options": ["A) skip", "B) next", "C) continue", "D) pass"],
                "answer": "C"
            },
            {
                "question": "What is the output of: print(max([1, 5, 3]))?",
                "options": ["A) 1", "B) 3", "C) 5", "D) 9"],
                "answer": "C"
            },
            {
                "question": "Which method is used to join elements of a list into a string?",
                "options": ["A) join()", "B) concat()", "C) merge()", "D) combine()"],
                "answer": "A"
            },
            {
                "question": "What is the output of: print(float(5))?",
                "options": ["A) 5", "B) 5.0", "C) '5.0'", "D) Error"],
                "answer": "B"
            },
            {
                "question": "Which operator is used to check if a value is in a sequence?",
                "options": ["A) contains", "B) in", "C) has", "D) exists"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(min([5, 2, 8]))?",
                "options": ["A) 2", "B) 5", "C) 8", "D) 15"],
                "answer": "A"
            },
            {
                "question": "Which method is used to remove whitespace from both ends of a string?",
                "options": ["A) trim()", "B) strip()", "C) clean()", "D) remove()"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(sum([1, 2, 3]))?",
                "options": ["A) 123", "B) 6", "C) [1, 2, 3]", "D) Error"],
                "answer": "B"
            },
            {
                "question": "Which keyword is used to define a variable that refers to nothing?",
                "options": ["A) null", "B) None", "C) nil", "D) empty"],
                "answer": "B"
            },
            {
                "question": "What is the output of: print(round(3.7))?",
                "options": ["A) 3", "B) 3.7", "C) 4", "D) 4.0"],
                "answer": "C"
            },
            {
                "question": "Which method is used to count occurrences of an element in a list?",
                "options": ["A) count()", "B) occurrences()", "C) frequency()", "D) number()"],
                "answer": "A"
            }
        ]
    
    def run_exam(self):
        print("=" * 60)
        print("PCAP-31-03 PRACTICE EXAM - EASY LEVEL")
        print("=" * 60)
        print(f"Total Questions: {self.total_questions}")
        print("Instructions: Enter A, B, C, or D for each question")
        print("=" * 60)
        print()
        
        for i, q in enumerate(self.questions, 1):
            print(f"Question {i}/{self.total_questions}")
            print(q["question"])
            for option in q["options"]:
                print(option)
            
            while True:
                answer = input("\nYour answer: ").strip().upper()
                if answer in ['A', 'B', 'C', 'D']:
                    break
                print("Invalid input. Please enter A, B, C, or D.")
            
            if answer == q["answer"]:
                self.score += 1
                print("✓ Correct!\n")
            else:
                print(f"✗ Incorrect. The correct answer is {q['answer']}\n")
            
            print("-" * 60)
        
        self.show_results()
    
    def show_results(self):
        percentage = (self.score / self.total_questions) * 100
        print("\n" + "=" * 60)
        print("EXAM RESULTS")
        print("=" * 60)
        print(f"Score: {self.score}/{self.total_questions}")
        print(f"Percentage: {percentage:.2f}%")
        
        if percentage >= 70:
            print("Status: PASS ✓")
        else:
            print("Status: FAIL ✗")
        
        print("=" * 60)

if __name__ == "__main__":
    exam = PCAPExamEasy()
    exam.run_exam()
