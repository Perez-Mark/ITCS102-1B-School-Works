sum = 0
for y in range(10):
    number = eval(input("Put any number: "))
    if number % 2 != 0:
      sum += number
print("The sum of all odd number is", sum)