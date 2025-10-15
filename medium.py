num = eval(input("enter your number here --> "))

for i in range(1,11,1):
    for y in range(1,num+1,1):
        print(f"{i} x {y} = {i * y}", end = "\t")
    print()

for c in range(1,6,1):
    for x in range(6,) 