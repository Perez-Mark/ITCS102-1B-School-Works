number = eval(input("Choose any number: "))
sum = 1
for i in range(number,0,-1):
    sum *= i
print("The Factorial of",number,"Is",sum)