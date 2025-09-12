name = input("Whats your name?: ")
fee = eval(input("Whats your fare fee?: "))
ifstudent = input("Are you a student?: (yes/no) ").lower()

if ifstudent == 'yes':
    discount = fee * 0.20
    discounted = fee - discount
    print("\nHello",name,)
    print("Your discounted fare fee is:",discounted)
else:
    print("\nHello",name)
    print("Your fare fee is:",fee)