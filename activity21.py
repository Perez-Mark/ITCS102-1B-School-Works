
isDirty = ""
sum = 0

check = input("type the word (perez)")
check += isDirty
print(isDirty)
while isDirty == "dirty":
    confirm = input("Do you want to keep washing (yes/no)").lower()

    if confirm == 'yes':
        sum += 1
        print("continuing Washing")
        continue
    else:
        print("Stoping Washing")
        break
print(f"Youve washed {sum}")