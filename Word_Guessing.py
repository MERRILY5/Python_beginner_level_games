import random

words = ["variables", "loops", "functions", "arrays", "objects", "recursion","inheritance",
         "polymorphism", "debugging", "syntax", "algorithms", "compilation"]

word = random.choice(words)

chances = len(word)+2

guesses = ""

while(chances > 0):
    
    loss = 0
    
    for i in word:
        if i in guesses:
            print(i,end=" ")
        else:
            print("_",end=" ")
            loss += 1
        
    if loss == 0:
        print(f"\n You Won!!, The word is {word}")
        break
    
    print()
    guess = input("Enter the character: ")
    guesses += guess
    
    if guess not in word:
        chances -= 1
    print(f"Wrong, only {chances} left")
        
    if chances == 0:
        print(f"You Lost!! The word is {word}")  
    
        
        