#informations on the topics
from defs import *
def infoprint():
    print(center_text(black("===============================================================")))
    print(center_text(cyan("INFO ABOUT PRINT STATEMENT")))
    print(center_text(black("===============================================================")))
    print(center_text(black("---------------------------------------------------------------")))
    print(center_block(yellow("""
print() is a basic Python function used to show information on the screen.
It takes whatever you give it—like text, numbers, or the result of a calculation—and displays it to the user.
It is mainly used to check what your program is doing, show messages, or display results while the program runs.
""")))
    print(center_text(black("---------------------------------------------------------------")))

def exampleprint1():
    print(black("========================================"))
    print(cyan("PRINTING TEXT AND NUMBERS"))
    print(black("========================================"))
    print(black("----------------------------------------"))
    print(green("""
Print text
Code:
\tprint("Hello!")
Output:
\tHello!

Print numbers
Code:
\tprint(25)
\tprint(2025)
Output:
\t25
\t2025
"""))
    print(black("----------------------------------------"))
    print(yellow("""These examples show that print() can display different kinds of information on the screen.
You can print text (inside quotes) or numbers (without quotes).
Python will show them exactly as they are."""))
    print(black("----------------------------------------"))
def exampleprint2():
    print(black("========================================"))
    print(cyan("PRINTING TEXT AND NUMBERS TOGETHER"))
    print(black("========================================"))
    print(black("----------------------------------------"))
    print(green("""
Code:
\tprint("My age is:", 15)
Output:
\tMy age is: 15
"""))
    print(black("----------------------------------------"))
    print(yellow("""This shows that print() can display text and numbers in one line.
You separate them with commas, and Python automatically spaces them and puts them together."""))
    print(black("----------------------------------------"))

def exampleprint3():
    print(black("========================================"))
    print(cyan("PRINTING THE RESULT OF A MATH PROBLEM"))
    print(black("========================================"))
    print(black("----------------------------------------"))
    print(green("""
Code:
\tprint(10 + 5)
\tprint(8 * 3)
Output:
\t15
\t24
"""))
    print(black("----------------------------------------"))
    print(yellow("""Here, print() shows the result of a calculation.
Python solves the math first, then prints the answer.
So you can use print() to check or display math results."""))
    print(black("----------------------------------------"))

def exampleprint4():
    print(black("========================================"))
    print(cyan("PRINTING MULTIPLE WORDS"))
    print(black("========================================"))
    print(black("----------------------------------------"))
    print(green("""
Code:
\tprint("Python", "is", "cool")
Output:
\tPython is cool
"""))
    print(black("----------------------------------------"))
    print(yellow("""When you put several items inside print(), separated by commas,
Python prints them with spaces between each item.
This makes it easy to print multiple words or values in one line."""))
    print(black("----------------------------------------"))
    
def exampleprint5():
    print(black("========================================"))
    print(cyan("PRINTING USING VIRIABLES"))
    print(black("========================================"))
    print(black("----------------------------------------"))
    print(green("""
Code:
\tname = "Alex"
\tage = 16
\tprint("Name:", name)
\tprint("Age:", age)
Output:
\tName: Alex
\tAge: 16
"""))
    print(black("----------------------------------------"))
    print(yellow("""This shows that print() can display the value stored inside a variable.
Instead of printing text only, you can print the data your program is using (like name or age)."""))
    print(black("----------------------------------------"))
    
def exampleprint6():
    print(black("========================================"))
    print(cyan("PRINTING MULTIPLE LINE USING \\n "))
    print(black("========================================"))
    print(black("----------------------------------------"))
    print(green("""
Code:
\tprint("Line 1\\nLine 2\\nLine 3")
Output:
\tLine 1
\tLine 2
\tLine 3
"""))
    print(black("----------------------------------------"))
    print(yellow("""The \\n means “new line.”
When Python sees it, it moves the text to the next line.
This example shows you how to print several lines using only one print() statement."""))
    print(black("----------------------------------------"))

def exampleprint7():
    print(black("========================================"))
    print(cyan("PRINTING A BLOCK OF TEXT"))
    print(black("========================================"))
    print(black("----------------------------------------"))
    print(green("""
Code:
\tprint(\"\"\"
\tThis is a long message.
\tYou can write many lines here.
\tPython will print it exactly the same.
\t\"\"\")
Output:
\tThis is a long message.
\tYou can write many lines here.
\tPython will print it exactly the same
"""))
    print(black("----------------------------------------"))
    print(yellow("""Triple quotes (\""") let you write many lines inside one print().
Python prints the text exactly the same way, including line breaks.
This is useful for long messages or formatted text."""))
    print(black("----------------------------------------"))

def infovariables():
    print(black("==============================================================="))
    print(cyan("INFO ABOUT VARIABLES"))
    print(black("==============================================================="))
    print(black("---------------------------------------------------------------"))
    print(yellow("""
A variable is a name that stores a value.
It works like a box where you keep information so you can use it later in your program.

A variable can store different kinds of data, like text, numbers, or results.   
You can change the value of a variable anytime, and Python will remember the new one.

Variables help you:

Save information

Reuse the information

Make your code easier to read and update

You choose the variable name, and Python will keep the value connected to that name.
"""))
    print(black("---------------------------------------------------------------"))

def examplevariables1():
    print(black("========================================"))
    print("STORING A VALUE IN A VARIABLE")
    print(black("========================================"))
    print(black("----------------------------------------"))
    print("""
Code:
\tname = "Alice"
\tprint(name)
Output:
\tAlice
""")
    print(black("----------------------------------------"))
    print("""This shows that a variable can hold text (called a “string”).
You put the text inside quotes""")
    print(black("----------------------------------------"))

def examplevariables2():
    print(black("========================================"))
    print("STORING NUMBERS IN A VARIABLE")
    print(black("========================================"))
    print(black("----------------------------------------"))
    print("""
Code:
\tage = 16
\tprint(age)
Output:
\t16
""")
    print(black("----------------------------------------"))
    print("""Variables can also store numbers.
Numbers do NOT use quotes because they are real values you can calculate with.""")
    print(black("----------------------------------------"))

def examplevariables3():
    print(black("========================================"))
    print("CHANGING A VARIABLE’S VALUE")
    print(black("========================================"))
    print(black("----------------------------------------"))
    print("""
Code:
\tx = 10
\tx = 20
\tprint(x)
Output:
\t20
""")
    print(black("----------------------------------------"))
    print("""A variable is not permanent.
You can change it anytime, and Python uses the newest value.""")
    print(black("----------------------------------------"))

def examplevariables4():
    print(black("========================================"))
    print("USING VARIABLES INSIDE PRINT()")
    print(black("========================================"))
    print(black("----------------------------------------"))
    print("""
Code:
\tmessage = "Hello!"
\tprint("The message is:", message)
Output:
\tThe message is: Hello!
""")
    print(black("----------------------------------------"))
    print("""You can show the value of a variable by putting the variable name inside print().
Python prints whatever the variable contains.""")
    print(black("----------------------------------------"))

def examplevariables5():
    print(black("========================================"))
    print("DOING MATH WITH VARIABLES")
    print(black("========================================"))
    print(black("----------------------------------------"))
    print("""
Code:
\ta = 5
\tb = 3
\tprint(a + b)
Output:
\t8
""")
    print(black("----------------------------------------"))
    print("""If a variable has a number, you can do math with it.
Python solves the math first, then prints the answer.""")
    print(black("----------------------------------------"))

def examplevariables6():
    print(black("========================================"))
    print("COMBINING TEXT AND VARIABLES")
    print(black("========================================"))
    print(black("----------------------------------------"))
    print("""
Code:
\tusername = "Mark"
\tscore = 95
\tprint("Player:", username, "Score:", score)
Output:
\tPlayer: Mark Score: 95
""")
    print(black("----------------------------------------"))
    print("""You can print text and variable values together by separating them with commas.
Python will add spaces automatically.""")
    print(black("----------------------------------------"))

def examplevariables7():
    print(black("========================================"))
    print("USING MULTIPLE VARIABLES TOGETHER")
    print(black("========================================"))
    print(black("----------------------------------------"))
    print("""
Code:
\tfirst = "Python"
\tsecond = "Programming"
\tprint(first, second)
Output:
\tPython Programming
""")
    print(black("----------------------------------------"))
    print("""Variables help organize information.
You can store many values and print them in one line or multiple lines.""")
    print(black("----------------------------------------"))

