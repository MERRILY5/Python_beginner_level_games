import random

l=[0]

chance = input("Enter 'F' to take the first chance, Enter 'S' to take the second chance: ").lower()

def loop(l,number):
    
    for i in range(1,number+1):
        j=l[-1]+1
        l.append(j)
    return l
 
def user(l):
    while True: 
        if l[-1] >= 21:
            a ="\nYOU WON AND COMPUTER LOST!!" 
            break
        print("_____Your chance_____")
        x = True
        while x :
            number = int(input("Enter the number between 1-4: "))
            if number > 0 and number <= 4:
                print(f"User: {loop(l,number)}")
                computer(l)
                x = False
            else:
                print("Enter proper number between 1 to 4")
    return a

def computer(l):
    while True:
        if l[-1] >= 21:
            b ="\nYOU LOST AND COMPUTER WIN!!"
            break      
        number = random.randint(1,4)
        if number > 0 and number <= 4:
            print("_____Computer chance_____")
            print(f"Computer:{loop(l,number)}")
            user(l)
    return b
           
if chance == "f":
    print(user(l))
else:
    print(computer(l))
 
 

    