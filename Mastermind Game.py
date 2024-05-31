import random 

number = random.randint(1000,10000)
print(number)

user_no = int(input("Enter the number: ")) 
if number == user_no:
    print("Great! You guessed the number in just 1 try! You're a Mastermind!")
else:
    ctr = 0
    while(user_no != number):
        ctr = 1
        count = 0
        user_no = str(user_no)
        number = str(number)
        correct = ['X']*4
        
        for i in range(0, 4):
            if user_no[i] == number[i]:
                count += 1
                correct[i] = user_no[i]
        print(correct)
        ctr+=1
        
        if user_no == number:
            print("You've become a Mastermind!")
            print("It took you only", ctr, "tries.")
            break 
        
        print("Not quite the number. But you did get ",count, " digit(s) correct!")
        user_no = int(input("Enter your next choice of numbers: "))
        
    


        