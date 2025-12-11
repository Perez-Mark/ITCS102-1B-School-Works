from defs import *
from information import *
import time

clear()
print(black("================================"))
print(cyan(blinking("WELCOME TO MY FINAL PROJECT CODE")))
print(black("================================"))
print(cyan("This program teaches Python basics."))
print(cyan("Use number keys to navigate menus."))
print(cyan("Explore topics, see examples, or write your own code."))
print(black("================================"))
#new indicator for the messenge ones you selected 7 topics
listindicator = []
listrep = ['a','b','c','d','e','f','g']
name = ""
while name.strip() == "":
    name = input("\033[1;36mWhats Your name?\033[0m \033[1;32m")
print("\033[1;90m================================\033[0m")
hi = input(cyan(f"Hello {name.title()} Do you want to run the code? (yes/no)") + ":\033[1;32m ").lower()
print(black("================================="))
time.sleep(0.5)
#indicator if youve gone to a topic
#indicator = 0

#if the messange was shown, its false if not
done_messange = False
while True:
    if hi == 'yes':
        while True:
            clear()
            
            
            #Some text when you go in or out of the menus
            #if indicator == 0:
            #    print(f"Hello! {name.title()}")
            #elif indicator >= 1 and indicator <= 6 or indicator >= 8 :
            #    print(f"Welcome back {name.title()}")
            #elif indicator == 7:
            #    print(f"You selected 7 topics hope you \nlearned something new :> {name.title()}")

            MAINMENU()
            if not done_messange and set(listindicator) == set(listrep):
                print(f"\033[0mYou selected 7 topics \nhope you learned \nsomething new {name.title()}!")
                print("=====================")
                done_messange = True

            choose = input(cyan("Choose Options above: ")+"\033[1;31m")
            print("\033[0m")

            if choose == '1':
                if 'a' not in listindicator:
                    listindicator.insert(0,'a')
                while True:
                    clear()
                    SUBMENU_PRINT()
                    choose = input(cyan("Choose Options above: ")+"\033[1;31m")
                    print("\033[0m")
                    if choose == '1':
                        clear()
                        infoprint()
                        pause = input("Press enter to go back")
                        time.sleep(0.3)
                    elif choose == '2':
                        clear()
                        while True:
                            clear()
                            SUBMENU_OFPRINT()
                            choose = input(cyan("Choose Options above: ")+"\033[1;31m")
                            print("\033[0m")
                            if choose == '1':
                                clear()
                                exampleprint1()
                                pause = input("Press enter to go back")
                                time.sleep(0.3)
                                continue
                            elif choose == '2':
                                clear()
                                exampleprint2()
                                pause = input("Press enter to go back")
                                time.sleep(0.3)
                                continue
                            elif choose == '3':
                                clear()
                                exampleprint3()
                                pause = input("Press enter to go back")
                                time.sleep(0.3)
                                continue
                            elif choose == '4':
                                clear()
                                exampleprint4()
                                pause = input("Press enter to go back")
                                time.sleep(0.3)
                                continue
                            elif choose == '5':
                                clear()
                                exampleprint5()
                                pause = input("Press enter to go back")
                                time.sleep(0.3)
                                continue
                            elif choose == '6':
                                clear()
                                exampleprint6()
                                pause = input("Press enter to go back")
                                time.sleep(0.3)
                                continue
                            elif choose == '7':
                                clear()
                                exampleprint7()
                                pause = input("Press enter to go back")
                                time.sleep(0.3)
                                continue
                            elif choose == '0':
                                print("GOING BACK")
                                break
                            else:
                                print(red("invalid"))
                                time.sleep(0.2)
                                continue
                    elif choose == '3':
                        while True:
                            clear()
                            CODER()
                            choose = input(cyan("Choose Options above: ")+"\033[1;31m")
                            print("\033[0m")
                            if choose == '1':
                                clear()
                                open_user_editor()
                                pause = input("Press enter to go back")
                                time.sleep(0.3)
                                continue
                            elif choose == '2':
                                clear()
                                run_user_file()
                                pause = input("Press enter to go back")
                                time.sleep(0.3)
                                continue
                            elif choose == '0':
                                print("GOING BACK")
                                time.sleep(0.5)
                                break

                             
                    elif choose == '0':
                        clear()
                        print(black("======================"))
                        print(cyan("GOING BACK TO MAINMENU"))
                        print(black("======================"))
                        time.sleep(1)
                        break
                    else:
                        print(red("invalid"))
                        time.sleep(0.2)
                        continue

            elif choose == '2':
                if 'b' not in listindicator:
                    listindicator.insert(1,'b')
                while True:
                    clear()
                    SUBMENU_VARIABLES()
                    choose = input(cyan("Choose Options above: ")+"\033[1;31m")
                    print("\033[0m")
                    if choose == '1':
                        clear()
                        infovariables()
                        pause = input("Press enter to go back")
                        time.sleep(0.3)
                    elif choose == '2':
                        clear()
                        while True:
                            clear()
                            SUBMENU_OFVARIABLES()
                            choose = input(cyan("Choose Options above: ")+"\033[1;31m")
                            print("\033[0m")
                            if choose == '1':
                                clear()
                                examplevariables1()
                                pause = input("Press enter to go back")
                                time.sleep(0.3)
                            elif choose == '2':
                                clear()
                                examplevariables2()
                                pause = input("Press enter to go back")
                                time.sleep(0.3)
                            elif choose == '3':
                                clear()
                                examplevariables3()
                                pause = input("Press enter to go back")
                                time.sleep(0.3)
                            elif choose == '4':
                                clear()
                                examplevariables4()
                                pause = input("Press enter to go back")
                                time.sleep(0.3)
                            elif choose == '5':
                                clear()
                                examplevariables5()
                                pause = input("Press enter to go back")
                                time.sleep(0.3)
                            elif choose == '6':
                                clear()
                                examplevariables6()
                                pause = input("Press enter to go back")
                                time.sleep(0.3)
                            elif choose == '7':
                                clear()
                                examplevariables7()
                                pause = input("Press enter to go back")
                                time.sleep(0.3)
                            elif choose == '0':
                                print("GOING BACK")
                                time.sleep(0.5)
                                break
                            else:
                                print(red("invalid"))
                                time.sleep(0.2)
                                continue
                    elif choose == '3':
                        while True:
                            clear()
                            CODER()
                            choose = input(cyan("Choose Options above: ")+"\033[1;31m")
                            print("\033[0m")
                            if choose == '1':
                                clear()
                                open_user_editor()
                                pause = input("Press enter to go back")
                                time.sleep(0.3)
                                continue
                            elif choose == '2':
                                clear()
                                run_user_file()
                                pause = input("Press enter to go back")
                                time.sleep(0.3)
                                continue
                            elif choose == '0':
                                print("GOING BACK")
                                time.sleep(0.5)
                                break
                    elif choose == '0':
                        clear()
                        print(black("======================"))
                        print(cyan("GOING BACK TO MAINMENU"))
                        print(black("======================"))
                        time.sleep(1)
                        break
                    else:
                        print(red("invalid"))
                        time.sleep(0.2)
                        continue
                    
            elif choose == '3':
                if 'c' not in listindicator:
                    listindicator.insert(2,'c')
                while True:
                    clear()
                    SUBMENU_OPERATORS()
                    choose = input(cyan("Choose Options above: ")+"\033[1;31m")
                    print("\033[0m")
                    if choose == '1':
                        clear()
                        infooperators()
                        pause = input("Press enter to go back")
                        time.sleep(0.3)
                    elif choose == '2':
                        clear()
                        while True:
                            clear()
                            SUBMENU_OFOPERATORS()
                            choose = input(cyan("Choose Options above: ")+"\033[1;31m")
                            print("\033[0m")
                            if choose == '1':
                                clear()
                                exampleoperators1()
                                pause = input("Press enter to go back")
                                time.sleep(0.3)
                                continue
                            elif choose == '2':
                                clear()
                                exampleoperators2()
                                pause = input("Press enter to go back")
                                time.sleep(0.3)
                                continue
                            elif choose == '3':
                                clear()
                                exampleoperators3()
                                pause = input("Press enter to go back")
                                time.sleep(0.3)
                                continue
                            elif choose == '4':
                                clear()
                                exampleoperators4()
                                pause = input("Press enter to go back")
                                time.sleep(0.3)
                                continue
                            elif choose == '5':
                                clear()
                                exampleoperators5()
                                pause = input("Press enter to go back")
                                time.sleep(0.3)
                                continue
                            elif choose == '6':
                                clear()
                                exampleoperators6()
                                pause = input("Press enter to go back")
                                continue
                            elif choose == '0':
                                print("GOING BACK")
                                time.sleep(0.5)
                                break
                    elif choose == '3':
                        while True:
                            clear()
                            CODER()
                            choose = input(cyan("Choose Options above: ")+"\033[1;31m")
                            print("\033[0m")
                            if choose == '1':
                                clear()
                                open_user_editor()
                                pause = input("Press enter to go back")
                                time.sleep(0.3)
                                continue
                            elif choose == '2':
                                clear()
                                run_user_file()
                                pause = input("Press enter to go back")
                                time.sleep(0.3)
                                continue
                            elif choose == '0':
                                print("GOING BACK")
                                time.sleep(0.5)
                                break
                    elif choose == '0':
                        clear()
                        print(black("======================"))
                        print(cyan("GOING BACK TO MAINMENU"))
                        print(black("======================"))
                        time.sleep(1)
                        break
                    else:
                        print(red("invalid"))
                        time.sleep(0.2)
                        continue
            elif choose == '4':
                if 'd' not in listindicator:
                    listindicator.insert(3,'d')
                while True:
                    clear()
                    SUBMENU_CONDITIONALS()
                    choose = input(""+cyan("Choose Options above: ")+"\033[1;31m")
                    print("\033[0m")
                    if choose == '1':
                        clear()
                        infoconditionals()
                        pause = input("Press enter to go back")
                        time.sleep(0.3)
                        continue
                    elif choose == '2':
                        clear()
                        while True:
                            clear()
                            SUBMENU_OFCONDITIONALS()
                            choose = input(cyan("Choose Options above: ")+"\033[1;31m")
                            print("\033[0m")
                            if choose == '1':
                                clear()
                                exampleconditionals1()
                                pause = input("Press enter to go back")
                                time.sleep(0.3)
                                continue
                            elif choose == '2':
                                clear()
                                exampleconditionals2()
                                pause = input("Press enter to go back")
                                time.sleep(0.3)
                                continue
                            elif choose == '3':
                                clear()
                                exampleconditionals3()
                                pause = input("Press enter to go back")
                                time.sleep(0.3)
                                continue
                            elif choose == '4':
                                clear()
                                exampleconditionals4()
                                pause = input("Press enter to go back")
                                time.sleep(0.3)
                                continue
                            elif choose == '5':
                                clear()
                                exampleconditionals5()
                                pause = input("Press enter to go back")
                                time.sleep(0.3)
                                continue
                            elif choose == '6':
                                clear()
                                exampleconditionals6()
                                pause = input("Press enter to go back")
                                time.sleep(0.3)
                                continue
                            elif choose == '0':
                                print("GOING BACK")
                                time.sleep(0.5)
                                break
                            else:
                                print(red("invalid"))
                                time.sleep(0.2)
                                continue
                    elif choose == '3':
                        while True:
                            clear()
                            CODER()
                            choose = input(cyan("Choose Options above: ")+"\033[1;31m")
                            print("\033[0m")
                            if choose == '1':
                                clear()
                                open_user_editor()
                                pause = input("Press enter to go back")
                                time.sleep(0.3)
                                continue
                            elif choose == '2':
                                clear()
                                run_user_file()
                                pause = input("Press enter to go back")
                                time.sleep(0.3)
                                continue
                            elif choose == '0':
                                print("GOING BACK")
                                time.sleep(0.5)
                                break
                    elif choose == '0':
                        clear()
                        print(black("======================"))
                        print(cyan("GOING BACK TO MAINMENU"))
                        print(black("======================"))
                        time.sleep(1)
                        break
                    else:
                        print(red("invalid"))
                        time.sleep(0.2)
                        continue
            elif choose == '5':
                if 'e' not in listindicator:
                    listindicator.insert(4,'e')
                while True:
                    clear()
                    SUBMENU_LOOPS()
                    choose = input(""+cyan("Choose Options above: ")+"\033[1;31m")
                    print("\033[0m")
                    if choose == '1':
                        clear()
                        infoloops()
                        pause = input("Press enter to go back")
                        time.sleep(0.3)
                        continue
                    elif choose == '2':
                        clear()
                        while True:
                            clear()
                            SUBMENU_OFLOOPS()
                            choose = input(cyan("Choose Options above: ")+"\033[1;31m")
                            print("\033[0m")
                            if choose == '1':
                                clear()
                                exampleloops1()
                                pause = input("Press enter to go back")
                                time.sleep(0.3)
                                continue
                            elif choose == '2':
                                clear()
                                exampleloops2()
                                pause = input("Press enter to go back")
                                time.sleep(0.3)
                                continue
                            elif choose == '3':
                                clear()
                                exampleloops3()
                                pause = input("Press enter to go back")
                                time.sleep(0.3)
                                continue
                            elif choose == '4':
                                clear()
                                exampleloops4()
                                pause = input("Press enter to go back")
                                time.sleep(0.3)
                                continue
                            elif choose == '5':
                                clear()
                                exampleloops5()
                                pause = input("Press enter to go back")
                                time.sleep(0.3)
                                continue
                            elif choose == '6':
                                clear()
                                exampleloops6()
                                pause = input("Press enter to go back")
                                time.sleep(0.3)
                                continue
                            elif choose == '0':
                                print("GOING BACK")
                                time.sleep(0.5)
                                break
                            else:
                                print(red("invalid"))
                                time.sleep(0.2)
                                continue
                    elif choose == '3':
                        while True:
                            clear()
                            CODER()
                            choose = input(cyan("Choose Options above: ")+"\033[1;31m")
                            print("\033[0m")
                            if choose == '1':
                                clear()
                                open_user_editor()
                                pause = input("Press enter to go back")
                                time.sleep(0.3)
                                continue
                            elif choose == '2':
                                clear()
                                run_user_file()
                                pause = input("Press enter to go back")
                                time.sleep(0.3)
                                continue
                            elif choose == '0':
                                print("GOING BACK")
                                time.sleep(0.5)
                                break
                    elif choose == '0':
                        clear()
                        print(black("======================"))
                        print(cyan("GOING BACK TO MAINMENU"))
                        print(black("======================"))
                        time.sleep(1)
                        break
                    else:
                        print(red("invalid"))
                        time.sleep(0.2)
                        continue
            elif choose == '6':
                if 'f' not in listindicator:
                    listindicator.insert(5,'f')
                while True:
                    clear()
                    SUBMENU_LISTS()
                    choose = input(""+cyan("Choose Options above: ")+"\033[1;31m")
                    print("\033[0m")
                    if choose == '1':
                        clear()
                        infolists()
                        pause = input("Press enter to go back")
                        time.sleep(0.3)
                        continue
                    elif choose == '2':
                        clear()
                        while True:
                            clear()
                            SUBMENU_OFLISTS()
                            choose = input(cyan("Choose Options above: ")+"\033[1;31m")
                            print("\033[0m")
                            if choose == '1':
                                clear()
                                examplelists1()
                                pause = input("Press enter to go back")
                                time.sleep(0.3)
                                continue
                            elif choose == '2':
                                clear()
                                examplelists2()
                                pause = input("Press enter to go back")
                                time.sleep(0.3)
                                continue
                            elif choose == '3':
                                clear()
                                examplelists3()
                                pause = input("Press enter to go back")
                                time.sleep(0.3)
                                continue
                            elif choose == '4':
                                clear()
                                examplelists4()
                                pause = input("Press enter to go back")
                                time.sleep(0.3)
                                continue
                            elif choose == '5':
                                clear()
                                examplelists5()
                                pause = input("Press enter to go back")
                                time.sleep(0.3)
                                continue
                            elif choose == '6':
                                clear()
                                examplelists6()
                                pause = input("Press enter to go back")
                                time.sleep(0.3)
                                continue
                            elif choose == '0':
                                print("GOING BACK")
                                time.sleep(0.5)
                                break
                            else:
                                print(red("invalid"))
                                time.sleep(0.2)
                                continue
                    elif choose == '3':
                        while True:
                            clear()
                            CODER()
                            choose = input(cyan("Choose Options above: ")+"\033[1;31m")
                            print("\033[0m")
                            if choose == '1':
                                clear()
                                open_user_editor()
                                pause = input("Press enter to go back")
                                time.sleep(0.3)
                                continue
                            elif choose == '2':
                                clear()
                                run_user_file()
                                pause = input("Press enter to go back")
                                time.sleep(0.3)
                                continue
                            elif choose == '0':
                                print("GOING BACK")
                                time.sleep(0.5)
                                break
                    elif choose == '0':
                        clear()
                        print(black("======================"))
                        print(cyan("GOING BACK TO MAINMENU"))
                        print(black("======================"))
                        time.sleep(1)
                        break
                    else:
                        print(red("invalid"))
                        time.sleep(0.2)
                        continue
            elif choose == '7':
                if 'g' not in listindicator:
                    listindicator.insert(6,'g')
                while True:
                    clear()
                    SUBMENU_FUNCTIONS()
                    choose = input(""+cyan("Choose Options above: ")+"\033[1;31m")
                    print("\033[0m")
                    if choose == '1':
                        clear()
                        infofunctions()
                        pause = input("Press enter to go back")
                        time.sleep(0.3)
                        continue
                    elif choose == '2':
                        clear()
                        while True:
                            clear()
                            SUBMENU_OFFUNCTIONS()
                            choose = input(cyan("Choose Options above: ")+"\033[1;31m")
                            print("\033[0m")
                            if choose == '1':
                                clear()
                                examplefunctions1()
                                pause = input("Press enter to go back")
                                time.sleep(0.3)
                                continue
                            elif choose == '2':
                                clear()
                                examplefunctions2()
                                pause = input("Press enter to go back")
                                time.sleep(0.3)
                                continue
                            elif choose == '3':
                                clear()
                                examplefunctions3()
                                pause = input("Press enter to go back")
                                time.sleep(0.3)
                                continue
                            elif choose == '4':
                                clear()
                                examplefunctions4()
                                pause = input("Press enter to go back")
                                time.sleep(0.3)
                                continue
                            elif choose == '5':
                                clear()
                                examplefunctions5()
                                pause = input("Press enter to go back")
                                time.sleep(0.3)
                                continue
                            elif choose == '6':
                                clear()
                                examplefunctions6()
                                pause = input("Press enter to go back")
                                time.sleep(0.3)
                                continue
                            elif choose == '0':
                                print("GOING BACK")
                                time.sleep(0.5)
                                break
                            else:
                                print(red("invalid"))
                                time.sleep(0.2)
                                continue
                    elif choose == '3':
                        while True:
                            clear()
                            CODER()
                            choose = input(cyan("Choose Options above: ")+"\033[1;31m")
                            print("\033[0m")
                            if choose == '1':
                                clear()
                                open_user_editor()
                                pause = input("Press enter to go back")
                                time.sleep(0.3)
                                continue
                            elif choose == '2':
                                clear()
                                run_user_file()
                                pause = input("Press enter to go back")
                                time.sleep(0.3)
                                continue
                            elif choose == '0':
                                print("GOING BACK")
                                time.sleep(0.5)
                                break
                    elif choose == '0':
                        clear()
                        print(black("======================"))
                        print(cyan("GOING BACK TO MAINMENU"))
                        print(black("======================"))
                        time.sleep(1)
                        break
                    else:
                        print(red("invalid"))
                        time.sleep(0.2)
                    continue
            elif choose == '0':
                print("QUITING SYSTEM")
                break
            else:
                print(red("invalid"))
                continue
        break
    elif hi == 'no':
        print(f"Ok Goodbye {name.title() }:D")
        break
    else:
        print(red("invalid"))
        hi = input("Type yes or no: ").lower()
        continue