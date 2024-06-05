import random

l=[]

def getNumber():

    num = ''
    
    for i in range(4):
        number = random.randint(1,8)
        if number in l:
            l.append(number+1)
        else:
            l.append(number)   

    for i in l:
        num = num + str(i)

    return int(num)

print(getNumber())


while True:
    guess = int(input("Guess: "))
    bull = 0
    cows = 0 
    guess = str(guess)
    if len(guess) == 1:
        guess = "000"+guess         
    l2=[int(i) for i in guess]   
    for i,j in zip(l,l2):
        if j in l:
            if j == i:
                bull += 1
            else:
                cows += 1
                
    if bull == 4:
        print("You have guessed it!")
        break
    print(f"Bulls : {bull}  || Cows : {cows}")
    bull = 0
    cows = 0
                
                
