import random 

print("_________________________________HANGMAN_________________________________")

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', 
'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

                                                                
fruits = ["apple", "banana", "pineapple", "grapefruit", "kiwi", "mango", 
          "peach", "papaya", "plum", "raspberry", "strawberry", "watermelon"]

fruit = random.choice(fruits)

chances = len(fruit)+2

stage = 6

guesses = ""

while(chances > 0):
    
    loss = 0
    
    for i in fruit:
        if i in guesses:
            print(i,end="")
        else:
            print("_",end="")
            loss += 1
        
    print()
            
    if loss == 0:
        print("YOU WON THIS MATCH!!")
        break

    guess = input("Enter the character: ")
    guesses += guess

    if guess not in fruit:
        chances -= 1
        print(stages[stage])
        stage -= 1
    
    if chances == 0:
        print("You have lost all your chances")