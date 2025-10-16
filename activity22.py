import random
print("+++++++++++++")
print("Guessing game")
print("+++++++++++++")

ranval = random.randrange(1,5)
tries = 0

while True:
    num = eval(input("Guess a random number --> "))

    if ranval == num:
        tries += 1
        print(f"{num} is the right number YOU GUESS RIGHT!!!")
        break
    else:
        tries += 1
        print(f"{num} isnt the number You guess wrong")
        continue

print(f"You tried {tries} times")