name = input("Whats your name: ")
sum = 0
odd = ""
print("ODD NUMBER SUMMARATION, press 0 to stop")
while True:
    num = eval(input("Input a randum number: "))
    if num == 0:
        print("Program has Stoped")
        break

    elif num % 2 == 1:
        print(f"ODD NUMBER DETECTED, code continues") 
        sum += num
        odd += str(num) + " "
        continue

    elif num % 2 == 0:
        print(f"EVEN NUMBER DETECTED, code continues")
        continue
    
    else:
        print("Not a number")
        break

print(f"hello {name}, The sum of all ODD number is {sum}")
print(f"ODD numbers detected included the ff {odd}")