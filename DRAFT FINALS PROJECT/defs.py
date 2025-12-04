#print statements, variables, operators, conditionals, loops, lists, and functions.
#The main menu and topics
import os
import platform
import shutil
#colors for the terminal text
def red(text):
    return f"\033[1;31m{text}\033[0m"

def green(text):
    return f"\033[1;32m{text}\033[0m"

def yellow(text):
    return f"\033[1;33m{text}\033[0m"

def blue(text):
    return f"\033[1;34m{text}\033[0m"

def cyan(text):
    return f"\033[1;36m{text}\033[0m"

def magenta(text):
    return f"\033[1;35m{text}\033[0m"

def black(text):
    return f"\033[1;30m{text}\033[0m"

def blinking(text):
    return f"\x1b[6m{text}\x1b[25m"

def reset():
    return f"\033[0m"
def center_text(text):
    terminal_size = shutil.get_terminal_size((80, 20))
    terminal_width = terminal_size.columns
    return text.center(terminal_width)
def center_block(text):
    terminal_size = shutil.get_terminal_size((80, 20))
    terminal_width = terminal_size.columns
    lines = text.split('\n')
    centered_lines = [line.center(terminal_width) for line in lines]
    return '\n'.join(centered_lines)
#the main menu
def MAINMENU():
    print(black("====================="))
    print(cyan("SELECT OPTIONS BELOW"))
    print(black("====================="))
    print(red("1 ")+black("- ")+cyan(" PRINT STATEMENT")+black("|"))
    print(red("2 ")+black("- ")+cyan(" VARIABLES      ")+black("|"))
    print(red("3 ")+black("- ")+cyan(" OPERATORS      ")+black("|"))
    print(red("4 ")+black("- ")+cyan(" CONDITIONALS   ")+black("|"))
    print(red("5 ")+black("- ")+cyan(" LOOPS          ")+black("|"))
    print(red("6 ")+black("- ")+cyan(" LISTS          ")+black("|"))
    print(red("7 ")+black("- ")+cyan(" FUNCTIONS      ")+black("|"))
    print(red("0 ")+black("- ")+cyan(" QUIT SYSTEM    ")+black("|"))
    print(black("====================="))
#the submenus and topics
def SUBMENU_PRINT():
    print(black("================================"))
    print(cyan("PRINT STATEMENT"))
    print(black("================================"))
    print(red("1 ")+black("- ")+cyan("INFO ABOUT PRINT STATEMENT")+black(" |"))
    print(red("2 ")+black("- ")+cyan("EXAMPLES OF PRINT STATEMENT")+black("|"))
    print(red("3 ")+black("- ")+cyan("MAKE YOUR OWN CODE         ")+black("|"))
    print(red("0 ")+black("- ")+cyan("BACK TO MAINMENU           ")+black("|"))
    print(black("================================"))
#the submenu for the examples of print statement
def SUBMENU_OFPRINT():
    print(black("========================================"))
    print(cyan("SELECT FROM THIS EXAMPLES"))
    print(black("========================================"))
    print(red("1 ")+black("- ")+cyan("PRINTING TEXT AND NUMBERS          ")+black("|"))
    print(red("2 ")+black("- ")+cyan("PRINTING TEXT AND NUMBERS TOGETHER ")+black("|"))
    print(red("3 ")+black("- ")+cyan("PRINTING A RESULT OF A MATH PROBLEM")+black("|"))
    print(red("4 ")+black("- ")+cyan("PRINTING MULTIPLE WORDS            ")+black("|"))
    print(red("5 ")+black("- ")+cyan("PRINTING USING VIRIABLES           ")+black("|"))
    print(red("6 ")+black("- ")+cyan("PRINTING MULTIPLE LINE USING \\n   ")+black(" |"))
    print(red("7 ")+black("- ")+cyan("PRINTING A BLOCK OF TEXT           ")+black("|"))
    print(red("0 ")+black("- ")+cyan("BACK TO MENU                       ")+black("|"))
    print(black("========================================"))
#the submenu for variables
def SUBMENU_VARIABLES():
    print(black("=============================="))
    print(cyan("VARIABLES"))
    print(black("=============================="))
    print(red("1 ")+black("- ")+cyan("INFO ABOUT VARIABLES     ")+black("|"))
    print(red("2 ")+black("- ")+cyan("EXAMPLES OF VARIABLES    ")+black("|"))
    print(red("3 ")+black("- ")+cyan("MAKE YOUR OWN CODE       ")+black("|"))
    print(red("0 ")+black("- ")+cyan("BACK TO MAINMENU         ")+black("|"))
    print(black("=============================="))
#the submenu for the examples of variables
def SUBMENU_OFVARIABLES():
    print(black("========================================"))
    print(cyan("SELECT FROM THIS EXAMPLES"))
    print(black("========================================"))
    print(red("1 ")+black("- ")+cyan("STORING TEXT IN A VARIABLE         ")+black("|"))
    print(red("2 ")+black("- ")+cyan("STORING NUMBERS IN A VARIABLE      ")+black("|"))
    print(red("3 ")+black("- ")+cyan("CHANGING A VARIABLE’S VALUE        ")+black("|"))
    print(red("4 ")+black("- ")+cyan("USING VARIABLES INSIDE PRINT()     ")+black("|"))
    print(red("5 ")+black("- ")+cyan("DOING MATH WITH VARIABLES          ")+black("|"))
    print(red("6 ")+black("- ")+cyan("COMBINING TEXT AND VARIABLES       ")+black("|"))
    print(red("7 ")+black("- ")+cyan("USING MULTIPLE VARIABLES TOGETHER  ")+black("|"))
    print(red("0 ")+black("- ")+cyan("BACK TO MENU                       ")+black("|"))
    print(black("========================================"))

def SUBMENU_OPERATORS():
    print("==============================")
    print("OPERATORS")
    print("==============================")

def SUBMENU_CONDITIONALS():
    print("==============================")
    print("CONDITIONALS")
    print("==============================")

def SUBMENU_LOOPS():
    print("==============================")
    print("LOOPS")
    print("==============================")

def SUBMENU_LISTS():
    print("==============================")
    print("LISTS")
    print("==============================")

def SUBMENU_FUNCTIONS():
    print("==============================")
    print("FUNCTIONS")
    print("==============================")

#checking if you have windows or any other os
# too cls or clear the terminal
def clear():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')