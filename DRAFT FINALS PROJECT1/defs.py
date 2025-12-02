#print statements, variables, operators, conditionals, loops, lists, and functions.
#The main menu and topics
import os
import platform
#colors for the terminal text
def red(text):
    return f"\033[1;91m{text}\033[0m"

def green(text):
    return f"\033[1;92m{text}\033[0m"

def yellow(text):
    return f"\033[1;93m{text}\033[0m"

def blue(text):
    return f"\033[1;94m{text}\033[0m"

def cyan(text):
    return f"\033[1;96m{text}\033[0m"

def magenta(text):
    return f"\033[1;95m{text}\033[0m"

def black(text):
    return f"\033[1;90m{text}\033[0m"

def white(text):
    return f"\033[1;97m{text}\033[0m"

def blinking(text):
    return f"\x1b[6m{text}\x1b[25m"

def reset():
    return f"\033[0m"



#the main menu
def MAINMENU():
    print(black("====================="))
    print(cyan("SELECT OPTIONS BELOW"))
    print(black("====================="))
    print(red("1 ")+black("- ")+cyan("PRINT STATEMENT"))
    print(red("2 ")+black("- ")+cyan("VARIABLES"))
    print(red("3 ")+black("- ")+cyan("OPERATORS"))
    print(red("4 ")+black("- ")+cyan("CONDITIONALS"))
    print(red("5 ")+black("- ")+cyan("LOOPS"))
    print(red("6 ")+black("- ")+cyan("LISTS"))
    print(red("7 ")+black("- ")+cyan("FUNCTIONS"))
    print(red("0 ")+black("- ")+cyan("QUIT SYSTEM"))
    print(black("====================="))
#the submenus and topics
def SUBMENU_PRINT():
    print(black("================================"))
    print(cyan("PRINT STATEMENT"))
    print(black("================================"))
    print(red("1 ")+black("- ")+cyan("INFO ABOUT PRINT STATEMENT"))
    print(red("2 ")+black("- ")+cyan("EXAMPLES OF PRINT STATEMENT"))
    print(red("3 ")+black("- ")+cyan("MAKE YOUR OWN CODE"))
    print(red("0 ")+black("- ")+cyan("BACK TO MAINMENU"))
    print(black("================================"))
#the submenu for the examples of print statement
def SUBMENU_OFPRINT():
    print(black("========================================"))
    print(cyan("SELECT FROM THIS EXAMPLES"))
    print(black("========================================"))
    print(red("1 ")+black("- ")+cyan("PRINTING TEXT AND NUMBERS"))
    print(red("2 ")+black("- ")+cyan("PRINTING TEXT AND NUMBERS TOGETHER"))
    print(red("3 ")+black("- ")+cyan("PRINTING A RESULT OF A MATH PROBLE"))
    print(red("4 ")+black("- ")+cyan("PRINTING MULTIPLE WORDS"))
    print(red("5 ")+black("- ")+cyan("PRINTING USING VIRIABLES"))
    print(red("6 ")+black("- ")+cyan("PRINTING MULTIPLE LINE USING \\n"))
    print(red("7 ")+black("- ")+cyan("PRINTING A BLOCK OF TEXT"))
    print(red("0 ")+black("- ")+cyan("BACK TO MENU"))
    print(black("========================================"))
#the submenu for variables
def SUBMENU_VARIABLES():
    print(black("=============================="))
    print(cyan("VARIABLES"))
    print(black("=============================="))
    print(red("1 ")+black("- ")+cyan("INFO ABOUT VARIABLES"))
    print(red("2 ")+black("- ")+cyan("EXAMPLES OF VARIABLES"))
    print(red("3 ")+black("- ")+cyan("MAKE YOUR OWN CODE"))
    print(red("0 ")+black("- ")+cyan("BACK TO MAINMENU"))
    print(black("=============================="))
#the submenu for the examples of variables
def SUBMENU_OFVARIABLES():
    print(black("========================================"))
    print(cyan("SELECT FROM THIS EXAMPLES"))
    print(black("========================================"))
    print(red("1 ")+black("- ")+cyan("STORING TEXT IN A VARIABLE"))
    print(red("2 ")+black("- ")+cyan("STORING NUMBERS IN A VARIABLE"))
    print(red("3 ")+black("- ")+cyan("CHANGING A VARIABLE’S VALUE"))
    print(red("4 ")+black("- ")+cyan("USING VARIABLES INSIDE PRINT()"))
    print(red("5 ")+black("- ")+cyan("DOING MATH WITH VARIABLES"))
    print(red("6 ")+black("- ")+cyan("COMBINING TEXT AND VARIABLES"))
    print(red("7 ")+black("- ")+cyan("USING MULTIPLE VARIABLES TOGETHER"))
    print(red("0 ")+black("- ")+cyan("BACK TO MENU"))
    print(black("========================================"))

def SUBMENU_OPERATORS():
    print(black("=============================="))
    print(cyan("OPERATORS"))
    print(black("=============================="))
    print(red("1 ")+black("- ")+cyan("INFO ABOUT OPERATORS"))
    print(red("2 ")+black("- ")+cyan("EXAMPLES OF OPERATORS"))
    print(red("3 ")+black("- ")+cyan("MAKE YOUR OWN CODE"))
    print(red("0 ")+black("- ")+cyan("BACK TO MAINMENU"))
    print(black("=============================="))

def SUBMENU_OFOPERATORS():
    print(black("========================================"))
    print(cyan("SELECT FROM THIS EXAMPLES"))
    print(black("========================================"))
    print(red("1 ")+black("- ")+cyan("ARITHMETIC OPERATORS"))
    print(red("2 ")+black("- ")+cyan("ASSIGNMENT OPERATORS"))
    print(red("3 ")+black("- ")+cyan("COMPARISON OPERATORS"))
    print(red("4 ")+black("- ")+cyan("LOGICAL OPERATORS"))
    print(red("5 ")+black("- ")+cyan("IDENTITY OPERATORS"))
    print(red("6 ")+black("- ")+cyan("MEMBERSHIP OPERATORS"))
    print(red("0 ")+black("- ")+cyan("BACK TO MENU"))
    print(black("========================================"))


def SUBMENU_CONDITIONALS():
    print(black("=============================="))
    print(cyan("CONDITIONALS"))
    print(black("=============================="))
    print(red("1 ")+black("- ")+cyan("INFO ABOUT CONDITIONALS"))
    print(red("2 ")+black("- ")+cyan("EXAMPLES OF CONDITIONALS"))
    print(red("3 ")+black("- ")+cyan("MAKE YOUR OWN CODE"))
    print(red("0 ")+black("- ")+cyan("BACK TO MAINMENU"))
    print(black("=============================="))

def SUBMENU_OFCONDITIONALS():
    print(black("========================================"))
    print(cyan("SELECT FROM THIS EXAMPLES"))
    print(black("========================================"))
    print(red("1 ")+black("- ")+cyan("BASIC IF STATEMENT"))
    print(red("2 ")+black("- ")+cyan("IF + ELSE STATEMENT"))
    print(red("3 ")+black("- ")+cyan("IF, ELIF, ELSE STATEMENT"))
    print(red("4 ")+black("- ")+cyan("USING LOGICAL OPERATORS"))
    print(red("5 ")+black("- ")+cyan("NESTED IF STATEMENTS(IF INSIDE ANOTHER IF)"))
    print(red("0 ")+black("- ")+cyan("BACK TO MENU"))
    print(black("========================================"))

def SUBMENU_LOOPS():
    print(black("=============================="))
    print(cyan("LOOPS"))
    print(black("=============================="))

def SUBMENU_LISTS():
    print(black("=============================="))
    print(cyan("LISTS"))
    print(black("=============================="))

def SUBMENU_FUNCTIONS():
    print(black("=============================="))
    print(cyan("FUNCTIONS"))
    print(black("=============================="))

#checking if you have windows or any other os
# too cls or clear the terminal
def clear():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')