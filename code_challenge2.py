D = eval(input("How much are you gonna deposit: "))
print("The breakdown of the Deposit amount: ")

n1 = 1000
n2 = 500
n3 = 200
n4 = 100
n5 = 50
n6 = 20
n7 = 10
n8 = 5
n9 = 1

print(D // n1,"- 1000")
print((D % n1) // n2,"- 500")
print((D % n1 % n2) // n3,"- 200")
print((D % n1 % n2 % n3) // n4,"- 100")
print((D % n1 % n2 % n3 % n4) // n5,"- 50")
print((D % n1 % n2 % n3 % n4 % n5) // n6,"- 20")
print((D % n1 % n2 % n3 % n4 % n5 % n6) // n7,"- 10")
print((D % n1 % n2 % n3 % n4 % n5 % n6 % n7) // n8,"- 5")
print((D % n1 % n2 % n3 % n4 % n5 % n6 % n7 % n8) // n9,"- 1")