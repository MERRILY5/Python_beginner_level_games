import random

print("______________RULES______________\nLower - Enter the starting number\nEnter the end number\n______________Level______________")
print("Easy - e (10 chances)\nMedium - m  (7 chances)\nHard - h (5 chances)\n")



lower = int(input("Enter the lower number: "))
higher = int(input("Enter the higher number: "))

guess = random.randint(lower,higher)


while(True):
    level = input("\nEnter your level: ").lower()
    if level == 'e':
        guesses = 10
        break
    elif level == 'm':
        guesses = 7
        break
    elif level == 'h':
        guesses = 5
        break
    else:
        print("Give correct input")
        
print("____________________________________________________________")

i=guesses
while(i):
    num=int(input("Enter the number: "))
    guesses -= 1
    if num > guess:
        print("Number is High")
        print(f"Guesses left: {guesses}")
    elif num < guess:
        print("Number is Low")
        print(f"Guesses left: {guesses}")
    else:
        print("Number is guessed")
        break
    if guesses == 0:
        print(f"YOU lOST ALL YOUR CHANCES! And the random number is {guess}")
        break