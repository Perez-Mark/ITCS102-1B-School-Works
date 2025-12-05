#informations on the topics
from defs import *
def infoprint():
    print(black("==============================================================="))
    print(cyan("INFO ABOUT PRINT STATEMENT"))
    print(black("==============================================================="))
    print(black("---------------------------------------------------------------"))
    print(yellow("""
print() is a basic Python function used to show information on the screen.
It takes whatever you give it—like text, numbers, or the result of a calculation—and displays it to the user.
It is mainly used to check what your program is doing, show messages, or display results while the program runs.
"""))
    print(black("---------------------------------------------------------------"))

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
    print(cyan("STORING A VALUE IN A VARIABLE"))
    print(black("========================================"))
    print(black("----------------------------------------"))
    print(green("""
Code:
\tname = "Alice"
\tprint(name)
Output:
\tAlice
"""))
    print(black("----------------------------------------"))
    print(yellow("""This shows that a variable can hold text (called a “string”).
You put the text inside quotes"""))
    print(black("----------------------------------------"))

def examplevariables2():
    print(black("========================================"))
    print(cyan("STORING NUMBERS IN A VARIABLE"))
    print(black("========================================"))
    print(black("----------------------------------------"))
    print(green("""
Code:
\tage = 16
\tprint(age)
Output:
\t16
"""))
    print(black("----------------------------------------"))
    print(yellow("""Variables can also store numbers.
Numbers do NOT use quotes because they are real values you can calculate with."""))
    print(black("----------------------------------------"))

def examplevariables3():
    print(black("========================================"))
    print(cyan("CHANGING A VARIABLE’S VALUE"))
    print(black("========================================"))
    print(black("----------------------------------------"))
    print(green("""
Code:
\tx = 10
\tx = 20
\tprint(x)
Output:
\t20
"""))
    print(black("----------------------------------------"))
    print(yellow("""A variable is not permanent.
You can change it anytime, and Python uses the newest value."""))
    print(black("----------------------------------------"))

def examplevariables4():
    print(black("========================================"))
    print(cyan("USING VARIABLES INSIDE PRINT()"))
    print(black("========================================"))
    print(black("----------------------------------------"))
    print(green("""
Code:
\tmessage = "Hello!"
\tprint("The message is:", message)
Output:
\tThe message is: Hello!
"""))
    print(black("----------------------------------------"))
    print(yellow("""You can show the value of a variable by putting the variable name inside print().
Python prints whatever the variable contains."""))
    print(black("----------------------------------------"))

def examplevariables5():
    print(black("========================================"))
    print(cyan("DOING MATH WITH VARIABLES"))
    print(black("========================================"))
    print(black("----------------------------------------"))
    print(green("""
Code:
\ta = 5
\tb = 3
\tprint(a + b)
Output:
\t8
"""))
    print(black("----------------------------------------"))
    print(yellow("""If a variable has a number, you can do math with it.
Python solves the math first, then prints the answer."""))
    print(black("----------------------------------------"))

def examplevariables6():
    print(black("========================================"))
    print(cyan("COMBINING TEXT AND VARIABLES"))
    print(black("========================================"))
    print(black("----------------------------------------"))
    print(green("""
Code:
\tusername = "Mark"
\tscore = 95
\tprint("Player:", username, "Score:", score)
Output:
\tPlayer: Mark Score: 95
"""))
    print(black("----------------------------------------"))
    print(yellow("""You can print text and variable values together by separating them with commas.
Python will add spaces automatically."""))
    print(black("----------------------------------------"))

def examplevariables7():
    print(black("========================================"))
    print(cyan("USING MULTIPLE VARIABLES TOGETHER"))
    print(black("========================================"))
    print(black("----------------------------------------"))
    print(green("""
Code:
\tfirst = "Python"
\tsecond = "Programming"
\tprint(first, second)
Output:
\tPython Programming
"""))
    print(black("----------------------------------------"))
    print(yellow("""Variables help organize information.
You can store many values and print them in one line or multiple lines."""))
    print(black("----------------------------------------"))

def infooperators():
    print(black("==============================================================="))
    print(cyan("INFO ABOUT OPERATORS"))
    print(black("==============================================================="))
    print(black("---------------------------------------------------------------"))
    print(yellow("""Operators are symbols that tell Python to do an action.
They are used to work with numbers, compare values, or connect conditions.

Operators help Python add, subtract, compare, and check things in your code.
They make it possible to do math, make decisions, and control how your program works.
"""))
    print(black("---------------------------------------------------------------"))

def exampleoperators1():
    print(black("========================================"))
    print(cyan("ARITHMETIC OPERATORS"))
    print(black("========================================"))
    print(black("----------------------------------------"))
    print(green("""
Code:
\tprint(3 + 2)
\tprint(7 - 5)
\tprint(4 * 3)
\tprint(10 / 2)
\tprint(10 // 3)
\tprint(10 % 3)
\tprint(2 ** 3)

Output:
\t5
\t2
\t12
\t5.0
\t3
\t1
\t8
"""))
    print(black("----------------------------------------"))
    print(yellow("""Arithmetic Operators (+, -, *, /, //, %, **)

These operators do math.
Python calculates the result and gives back a number.

+ → Adds two numbers.

- → Subtracts the second number from the first.

* → Multiplies numbers.

/ → Divides numbers (result is always a float).

// → Floor division (divides and gives the whole number only).

% → Modulus (gives the remainder after division).

** → Exponent (first number raised to the power of the second)."""))
    print(black("----------------------------------------"))

def exampleoperators2():
    print(black("========================================"))
    print(cyan("ASSIGNMENT OPERATORS"))
    print(black("========================================"))
    print(black("----------------------------------------"))
    print(green("""
Code:
\tx = 10
\tx += 5
\tprint(x)

\ty = 20
\ty -= 3
\tprint(y)

\tz = 4
\tz *= 2
\tprint(z)

\ta = 9
\ta /= 3
\tprint(a)

Output:
\t15
\t17
\t8
\t3.0
"""))
    print(black("----------------------------------------"))
    print(yellow("""Assignment Operators (=, +=, -=, *=, /=, etc.)

These operators store a value into a variable or update it.
They help change variables in a shorter way.
                 
== → Checks if two values are equal.

!= → Checks if two values are not equal.

> → Checks if the first value is greater than the second.

< → Checks if the first value is less than the second.

>= → Checks if the first value is greater than or equal to the second.

<= → Checks if the first value is less than or equal to the second."""))
    print(black("----------------------------------------"))

def exampleoperators3():
    print(black("========================================"))
    print(cyan("COMPARISON OPERATORS"))
    print(black("========================================"))
    print(black("----------------------------------------"))
    print(green("""
Code:
\tprint(5 == 5)
\tprint(5 != 3)
\tprint(7 > 2)
\tprint(2 < 1)
\tprint(4 >= 4)
\tprint(3 <= 1)

Output:
\tTrue
\tTrue
\tTrue
\tFalse
\tTrue
\tFalse
"""))
    print(black("----------------------------------------"))
    print(yellow("""Comparison Operators (==, !=, >, <, >=, <=)

These operators compare two values.
The result is always True or False.

Compare values and check conditions.

== → Checks if two values are equal.

!= → Checks if two values are not equal.

> → Checks if the first value is greater than the second.

< → Checks if the first value is less than the second.

>= → Checks if the first value is greater than or equal to the second.

<= → Checks if the first value is less than or equal to the second."""))
    print(black("----------------------------------------"))

def exampleoperators4():
    print(black("========================================"))
    print(cyan("LOGICAL OPERATORS"))
    print(black("========================================"))
    print(black("----------------------------------------"))
    print(green("""
Code:
\tprint(True and False)
\tprint(True or False)
\tprint(not False)

Output:
\tFalse
\tTrue
\tTrue
"""))
    print(black("----------------------------------------"))
    print(yellow("""Logical Operators (and, or, not)

These operators combine conditions.
They help your program make decisions.

and → True only if both conditions are True.

or → True if at least one condition is True.

not → Reverses the value (True → False, False → True)."""))
    print(black("----------------------------------------"))

def exampleoperators5():
    print(black("========================================"))
    print(cyan("IDENTITY OPERATORS"))
    print(black("========================================"))
    print(black("----------------------------------------"))
    print(green("""
Code:
\ta = [1, 2]
\tb = a
\tc = [1, 2]
\t
\tprint(a is b)
\tprint(a is c)
\tprint(a is not c)

Output:
\tTrue
\tFalse
\tTrue
"""))
    print(black("----------------------------------------"))
    print(yellow("""Identity Operators (is, is not)

These operators check if two variables point to the same object in memory.
(Not about value — about identity.)

is → True if both variables point to the same object.

is not → True if both variables point to different objects."""))
    print(black("----------------------------------------"))

def exampleoperators6():
    print(black("========================================"))
    print(cyan("MEMBERSHIP OPERATORS"))
    print(black("========================================"))
    print(black("----------------------------------------"))
    print(green("""
Code:
\tnumbers = [1, 2, 3, 4]
\tprint(3 in numbers)
\tprint(5 in numbers)
\tprint(5 not in numbers)

Output:
\tTrue
\tFalse
\tTrue
"""))
    print(black("----------------------------------------"))
    print(yellow("""Membership Operators (in, not in)

These operators check if a value is inside a list, string, or other group.

in → True if the value exists in the group.

not in → True if the value does NOT exist in the group."""))
    print(black("----------------------------------------"))

def infoconditionals():
    print(black("==============================================================="))
    print(cyan("INFO ABOUT CONDITIONALS"))
    print(black("==============================================================="))
    print(black("---------------------------------------------------------------"))
    print(yellow("""
Conditionals in Python let your program choose what to do by testing a condition; if the condition is
true, it runs one block of code, but if it is false, it can run another, helping your program make smart
decisions and react to different situations.

Conditionals help your program act differently based on:

✔ answers
✔ choices
✔ comparisons
✔ user input
✔ values in variables
"""))
    print(black("---------------------------------------------------------------"))

def exampleconditionals1():
    print(black("========================================"))
    print(cyan("IF STATEMENT"))
    print(black("========================================"))
    print(black("----------------------------------------"))
    print(green("""
Code:
\tx = 10
\tif x > 5:
\t    print("x is greater than 5")

Output:
\tx is greater than 5
"""))
    print(black("----------------------------------------"))
    print(yellow("""This shows how Python checks a condition.
If the condition is True, the code inside runs; if False, nothing happens."""))
    print(black("----------------------------------------"))

def exampleconditionals2():
    print(black("========================================"))
    print(cyan("IF + ELSE STATEMENT"))
    print(black("========================================"))
    print(black("----------------------------------------"))
    print(green("""
Code:
\tage = 15
\tif age >= 18:
\t    print("You are an adult")
\telse:
\t    print("You are a minor")

Output:
\tYou are a minor
"""))
    print(black("----------------------------------------"))
    print(yellow("""else runs only when the if condition is False.
This lets your program choose between two actions."""))
    print(black("----------------------------------------"))

def exampleconditionals3():
    print(black("========================================"))
    print(cyan("IF, ELIF, ELSE STATEMENT"))
    print(black("========================================"))
    print(black("----------------------------------------"))
    print(green("""
Code:
\tscore = 80
\tif score >= 90:
\t    print("Grade A")
\telif score >= 75:
\t    print("Grade B")
\telse:
\t    print("Grade C")

Output:
\tGrade B
"""))
    print(black("----------------------------------------"))
    print(yellow("""This allows multiple choices.
Python checks if first, then elif.
If none are True, else runs."""))
    print(black("----------------------------------------"))

def exampleconditionals4():
    print(black("========================================"))
    print(cyan("USING COMPARISON OPERATORS IN CONDITIONALS"))
    print(black("========================================"))
    print(black("----------------------------------------"))
    print(green("""
Code:
\tnumber = 0
\tif number == 0:
\t    print("The number is zero")

Output:
\tThe number is zero
"""))
    print(black("----------------------------------------"))
    print(yellow("""This shows that conditionals often use comparison operators (like >=, ==) to make decisions."""))
    print(black("----------------------------------------"))

def exampleconditionals5():
    print(black("========================================"))
    print(cyan("USING LOGICAL OPERATORS IN CONDITIONALS"))
    print(black("========================================"))
    print(black("----------------------------------------"))
    print(green("""
Code:
\tage = 20
\thas_id = True
\tif age >= 18 and has_id:
\t    print("Access granted")

Output:
\tAccess granted
"""))
    print(black("----------------------------------------"))
    print(yellow("""Here, more than one condition must be checked.
Logical operators (and, or) help combine conditions."""))
    print(black("----------------------------------------"))

def exampleconditionals6():
    print(black("========================================"))
    print(cyan("NESTED IF STATEMENTS(IF INSIDE ANOTHER IF"))
    print(black("========================================"))
    print(black("----------------------------------------"))
    print(green("""
Code:
\tusername = "admin"
\tpassword = "1234"
\tif username == "admin":
\t    if password == "1234":
\t        print("Login successful")
\t    else:
\t        print("Incorrect password")
\telse:
\t    print("Unknown username")

Output:
\tLogin successful
"""))
    print(black("----------------------------------------"))
    print(yellow("""This example shows decision-making inside a decision.
Useful when one condition depends on another."""))
    print(black("----------------------------------------"))

def infoloops():
    print(black("==============================================================="))
    print(cyan("INFO ABOUT LOOPS"))
    print(black("==============================================================="))
    print(black("---------------------------------------------------------------"))
    print(yellow("""
Loops let Python repeat actions automatically.
They help us avoid typing the same line many times.
We can repeat tasks until a condition changes or all items are used.
"""))
    print(black("---------------------------------------------------------------"))

def exampleloops1():
    print(black("========================================"))
    print(cyan("BASIC FOR LOOP"))
    print(black("========================================"))
    print(black("----------------------------------------"))
    print(green("""
Code:
\tfor i in range(5):
\t    print(i)

Output:
\t0
\t1
\t2
\t3
\t4
"""))
    print(black("----------------------------------------"))
    print(yellow("""range(5) tells Python to loop 5 times.  
The loop starts from 0 and goes up to 4.  
Each time the loop repeats, the value of i increases by 1,  
and Python prints that number.  
This is useful when we want to repeat something a fixed number of times."""))
    print(black("----------------------------------------"))

def exampleloops2():
    print(black("========================================"))
    print(cyan("FOR LOOP THROUGH A LIST"))
    print(black("========================================"))
    print(black("----------------------------------------"))
    print(green("""
Code:
\tanimals = ["cat", "dog", "bird"]
\t
\tfor a in animals:
\t    print(a)

Output:
\tcat
\tdog
\tbird
"""))
    print(black("----------------------------------------"))
    print(yellow("""The loop goes through every animal inside the list.  
Each time the loop runs, it picks one item from the list  
and stores it in the variable **a**.  
Then it prints the animal’s name.  
This is helpful when we want to process or show each item in a list."""))
    print(black("----------------------------------------"))

def exampleloops3():
    print(black("========================================"))
    print(cyan("BASIC WHILE LOOP"))
    print(black("========================================"))
    print(black("----------------------------------------"))
    print(green("""
Code:
\tx = 1
\t
\twhile x <= 3:
\t    print(x)
\t    x += 1

Output:
\t1
\t2
\t3
"""))
    print(black("----------------------------------------"))
    print(yellow("""The loop keeps running as long as the condition (x <= 3) is true.  
Python prints the value of x, then increases it by 1.  
Once x becomes 4, the condition is false, so the loop stops.  
This type of loop is useful when we want something to repeat  
until a changing condition becomes false."""))
    print(black("----------------------------------------"))

def exampleloops4():
    print(black("========================================"))
    print(cyan("WHILE LOOP WAITING FOR USER"))
    print(black("========================================"))
    print(black("----------------------------------------"))
    print(green("""
Code:
\tuser = ""
\t
\twhile user != "exit":
\t    user = input("Type exit to stop: ")

Output:
\t(keeps asking until user types exit)
"""))
    print(black("----------------------------------------"))
    print(yellow("""This loop continues asking the user for input.  
It only stops when the user types **"exit"**.  
This is useful when we want programs to wait for instructions  
or keep running until the user decides to stop."""))
    print(black("----------------------------------------"))

def exampleloops5():
    print(black("========================================"))
    print(cyan("USING BREAK IN LOOPS"))
    print(black("========================================"))
    print(black("----------------------------------------"))
    print(green("""
Code:
\tfor i in range(10):
\t    if i == 5:
\t        break
\t    print(i)

Output:
\t0
\t1
\t2
\t3
\t4
"""))
    print(black("----------------------------------------"))
    print(yellow("""The loop was supposed to run from 0 to 9,  
but **break** stops the loop completely when i reaches 5.  
This is helpful when we want to cancel a loop early  
when a certain condition is met."""))
    print(black("----------------------------------------"))

def exampleloops6():
    print(black("========================================"))
    print(cyan("USING CONTINUE IN LOOPS"))
    print(black("========================================"))
    print(black("----------------------------------------"))
    print(green("""
Code:
\tfor i in range(6):
\t    if i == 3:
\t        continue
\t    print(i)

Output:
\t0
\t1
\t2
\t4
\t5
"""))
    print(black("----------------------------------------"))
    print(yellow("""The loop runs from 0 to 5,  
but when i equals 3, **continue** tells Python to skip that step.  
The loop does not print 3 but continues running normally.  
This is useful when we want to ignore or skip specific values  
without stopping the entire loop."""))
    print(black("----------------------------------------"))

def infolists():
    print(black("==============================================================="))
    print(cyan("INFO ABOUT LISTS"))
    print(black("==============================================================="))
    print(black("---------------------------------------------------------------"))
    print(yellow("""
A list is a container that can store many values in one variable.
Lists can hold numbers, text, or mixed types.
We can read, update, add, or remove values from a list.
"""))
    print(black("---------------------------------------------------------------"))

def examplelists1():
    print(black("========================================"))
    print(cyan("CREATING A LIST"))
    print(black("========================================"))
    print(black("----------------------------------------"))
    print(green("""
Code:
\tfruits = ["apple", "banana", "mango"]
\tprint(fruits)

Output:
\t['apple', 'banana', 'mango']
"""))
    print(black("----------------------------------------"))
    print(yellow("""fruits stores three items inside square brackets.
Printing the list shows everything inside it."""))
    print(black("----------------------------------------"))

def examplelists2():
    print(black("========================================"))
    print(cyan("ACCESSING LIST VALUES"))
    print(black("========================================"))
    print(black("----------------------------------------"))
    print(green("""
Code:
\tfruits = ["apple", "banana", "mango"]
\tprint(fruits[0])

Output:
\tapple
"""))
    print(black("----------------------------------------"))
    print(yellow("""Index 0 refers to the first item.
Lists begin counting at zero.
This allows us to pick specific stored data."""))
    print(black("----------------------------------------"))

def examplelists3():
    print(black("========================================"))
    print(cyan("CHANGING LIST ITEMS"))
    print(black("========================================"))
    print(black("----------------------------------------"))
    print(green("""
Code:
\tfruits = ["apple", "banana", "mango"]
\tfruits[1] = "orange"
\tprint(fruits)

Output:
\t['apple', 'orange', 'mango']
"""))
    print(black("----------------------------------------"))
    print(yellow("""Lists can be edited.
We replaced the second item with orange."""))
    print(black("----------------------------------------"))

def examplelists4():
    print(black("========================================"))
    print(cyan("ADDING ITEMS TO A LIST"))
    print(black("========================================"))
    print(black("----------------------------------------"))
    print(green("""
Code:
\tfruits = ["apple", "banana"]
\tfruits.append("cherry")
\tprint(fruits)

Output:
\t['apple', 'banana', 'cherry']
"""))
    print(black("----------------------------------------"))
    print(yellow("""append adds a new item to the end of the list,
allowing the list to grow."""))
    print(black("----------------------------------------"))

def examplelists5():
    print(black("========================================"))
    print(cyan("REMOVING ITEMS FROM A LIST"))
    print(black("========================================"))
    print(black("----------------------------------------"))
    print(green("""
Code:
\tfruits = ["apple", "banana", "mango"]
\tfruits.remove("banana")
\tprint(fruits)

Output:
\t['apple', 'mango']
"""))
    print(black("----------------------------------------"))
    print(yellow("""remove deletes the matching item.
This updates the list by taking something out."""))
    print(black("----------------------------------------"))

def examplelists6():
    print(black("========================================"))
    print(cyan("LOOPING THROUGH A LIST"))
    print(black("========================================"))
    print(black("----------------------------------------"))
    print(green("""
Code:
\tfruits = ["apple", "banana", "mango"]
\t
\tfor f in fruits:
\t    print(f)

Output:
\tapple
\tbanana
\tmango
"""))
    print(black("----------------------------------------"))
    print(yellow("""The loop reads and prints each value in the list.
This is useful when working with many stored items."""))
    print(black("----------------------------------------"))

def infofunctions():
    print(black("==============================================================="))
    print(cyan("INFO ABOUT FUNCTIONS"))
    print(black("==============================================================="))
    print(black("---------------------------------------------------------------"))
    print(yellow("""
A function is a reusable block of code that performs a task.
Functions help keep programs organized and reduce repetition.
We define a function once and call it whenever we need it.
"""))
    print(black("---------------------------------------------------------------"))

def examplefunctions1():
    print(black("========================================"))
    print(cyan("BASIC FUNCTION"))
    print(black("========================================"))
    print(black("----------------------------------------"))
    print(green("""
Code:
\tdef greet():
\t    print("Hello!")
\t
\tgreet()

Output:
\tHello!
"""))
    print(black("----------------------------------------"))
    print(yellow("""def creates the function.
Calling greet() runs the stored code."""))
    print(black("----------------------------------------"))

def examplefunctions2():
    print(black("========================================"))
    print(cyan("FUNCTION WITH PARAMETERS"))
    print(black("========================================"))
    print(black("----------------------------------------"))
    print(green("""
Code:
\tdef greet(name):
\t    print("Hello", name)
\t
\tgreet("Alex")

Output:
\tHello Alex
"""))
    print(black("----------------------------------------"))
    print(yellow("""The function accepts a value through the parameter name,
letting it greet different people."""))
    print(black("----------------------------------------"))

def examplefunctions3():
    print(black("========================================"))
    print(cyan("FUNCTION THAT RETURNS A VALUE"))
    print(black("========================================"))
    print(black("----------------------------------------"))
    print(green("""
Code:
\tdef add(a, b):
\t    return a + b
\t
\tresult = add(5, 3)
\tprint(result)

Output:
\t8
"""))
    print(black("----------------------------------------"))
    print(yellow("""return sends a result back.
The function adds two numbers and returns the answer."""))
    print(black("----------------------------------------"))

def examplefunctions4():
    print(black("========================================"))
    print(cyan("FUNCTION WITH MULTIPLE ACTIONS"))
    print(black("========================================"))
    print(black("----------------------------------------"))
    print(green("""
Code:
\tdef user_info(name, age):
\t    print("Name:", name)
\t    print("Age:", age)
\t
\tuser_info("John", 18)

Output:
\tName: John
\tAge: 18
"""))
    print(black("----------------------------------------"))
    print(yellow("""Functions can run many lines of code.
This one prints related information."""))
    print(black("----------------------------------------"))

def examplefunctions5():
    print(black("========================================"))
    print(cyan("CALLING A FUNCTION MANY TIMES"))
    print(black("========================================"))
    print(black("----------------------------------------"))
    print(green("""
Code:
\tdef welcome():
\t    print("Welcome back!")
\t
\twelcome()
\twelcome()

Output:
\tWelcome back!
\tWelcome back!
"""))
    print(black("----------------------------------------"))
    print(yellow("""One function can be reused over and over,
which saves time and avoids repeating code."""))
    print(black("----------------------------------------"))

def examplefunctions6():
    print(black("========================================"))
    print(cyan("FUNCTION WITH DECISION MAKING"))
    print(black("========================================"))
    print(black("----------------------------------------"))
    print(green("""
Code:
\tdef check_age(age):
\t    if age >= 18:
\t        return True
\t    else:
\t        return False
\t
\tprint(check_age(20))

Output:
\tTrue
"""))
    print(black("----------------------------------------"))
    print(yellow("""The function checks a condition and returns True or False based on it.
Returning values lets other parts of the program react to the answer."""))
    print(black("----------------------------------------"))