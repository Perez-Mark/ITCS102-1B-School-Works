
import os
import json
studentlist = {}

while True:
    print("SELECT FROM THE FOLLOWING OPTIONS")
    print("A - ADD STUDENT RECORD")
    print("B - PRINT ALL STUDENT RECORD")
    print("C - SEARCH STUDENT RECORD")
    print("D - DELETE STUDENT RECORD")
    print("E - EDIT STUDENT RECORD")
    print("F - EXPORT STUDENT RECORD")
    print("G - IMPORT STUDENT RECORD")
    print("X - EXIT SYSTEM")

    choice = input("SELECT OPTIONS ABOVE: ").lower()
        
    if choice == 'a':
        os.system('cls')
        print("ADDING STUDENT")
        id_no = input("Please input student id number: ")
        first_name = input("Please input student firstname: ").upper()
        last_name = input("Please input student lastname: ").upper()
        age = eval(input("Please input student age: "))
        course = input("Please input student course").upper()
        section = input("Please input student's section").upper()
        

        studentlist[id_no] = [first_name, last_name, age, course, section]
        continue

    elif choice == 'b':
        os.system('cls')
        for i,j in studentlist.items():
            print(f"STUDENT ID - {i}, INFORMATION - {j}")
        continue
    elif choice == 'c':
        os.system('cls')
        print("SEARCH STUDENT RECORD")

        search_id = input("Input Student ID for search").lower()

        for each_id in studentlist.keys():
            if search_id in studentlist.keys():
                print(f"RECORD FOUND for ID {search_id}")
                for i in studentlist[search_id]:
                    print(f" --- {i}")
            else:
                print("NO RECORDS FOUND")
                break
        continue
    elif choice == 'd':
        print("DELETE STUDENT RECORD")

        search_id = input("Input Student ID for search").lower()

        for each_id in studentlist.keys():
            if search_id in studentlist.keys():
                print(f"RECORD FOUND for ID {search_id}")
                for i in studentlist[search_id]:    
                    print(f" --- {i}")
                studentlist.pop[search_id]
            else:
                print("NO RECORDS FOUND")
                break
        continue
    elif choice == 'e':
        search_id = input("Input Student ID for search").lower()

        for each_id in studentlist.keys():
            if search_id in studentlist.keys():
                print(f"RECORD FOUND for ID {search_id}")
                for i in studentlist[search_id]:
                    print(f" --- {i}")
                print("EDITING STUDENT INFORMATION")

                first_name = input("Please input student firstname: ").upper()
                last_name = input("Please input student lastname: ").upper()
                age = eval(input("Please input student age: "))
                course = input("Please input student course").upper()
                section = input("Please input student's section").upper()
                
                studentlist[search_id][0] = first_name
                studentlist[search_id][1] = last_name
                studentlist[search_id][2] = age
                studentlist[search_id][3] = course
                studentlist[search_id][4] = section

                print("DATA UPDATED")
            else:
                print("NO RECORD FOUND")
        continue
    elif choice == 'f':
        os.system('cls')
        print("EXPORT STUDENT DATA")
        with open('student_record.json','w') as new_file:
            json.dump(studentlist,new_file, indent=4 ) 

            print("\n\nDATA EXPORTED TO JSON")
        continue
    elif choice == 'g':
        os.system('cls')
        print("EXPORT STUDENT DATA")
        with open('student_record.json','r') as new_file:
            imported_student = json.load(new_file)

        studentlist = imported_student
        print("\n\nDATA IMPORTED TO JSON")
        continue
    elif choice == 'x':
        print("EXITING SYSTEM")
        break
    else:
        print("invalid")
