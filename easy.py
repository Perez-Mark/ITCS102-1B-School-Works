for i in range(1,6,1):
    for x in range(6,i,-1):
        print(" ",end="")
    for y in range(1,i*2,1):
        print("*",end="")
    print()

for c in range(1,6,1):
    for h in range(c,7,1):
        print("", end="")
    for m in range(0,c,1):
        print(c, end="")
    print()