number = eval(input("Enter any number to multiply: "))

print("Multiplication table for:", number)
for i in range(1, 11,):
    print(number,"x",i,"=", number * i)