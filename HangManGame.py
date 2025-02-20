import random

hangmanStages = [
    """
       ------
       |    |
       |    
       |    
       |    
       |    
      ---   
    """,
    """
       ------
       |    |
       |    O
       |    
       |    
       |    
      ---   
    """,
    """
       ------
       |    |
       |    O
       |    |
       |    
       |    
      ---   
    """,
    """
       ------
       |    |
       |    O
       |   /|
       |    
       |    
      ---   
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |    
       |    
      ---   
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / 
       |    
      ---   
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |    
      ---   
    """,
]

lists = {

    "FRUITS": [
    "Apple", "Banana", "Orange", "Mango", "Grapes",
    "Pineapple", "Strawberry", "Blueberry", "Watermelon", "Cherry",
    "Peach", "Pear", "Kiwi", "Papaya", "Pomegranate"
    ],

    "ANIMALS": [
    "Lion", "Tiger", "Elephant", "Giraffe", "Zebra",
    "Kangaroo", "Panda", "Dolphin", "Eagle", "Wolf",
    "Rabbit", "Crocodile", "Bear", "Owl", "Horse"
    ],

    "CARTOONS": [
    "MickeyMouse", "SpongeBobSquarePants", "TomandJerry", "ScoobyDoo", "BugsBunny",
    "TheSimpsons", "RickandMorty", "LooneyTunes", "Popeye", "DoratheExplorer",
    "TeenTitans", "Ben10", "AvatarTheLastAirbender", "PhineasandFerb", "TheFlintstones"
    ]
}   

selectedListName = random.choice(list(lists.keys()))
selectedList = lists[selectedListName]
selectedWord = random.choice(selectedList).upper()

secretWord = len(selectedWord) * "_"
print(secretWord)
print(selectedWord)
print("")

print(f"Welcome to Hangman Game! The Category is: {selectedListName}")

input("Press Enter to Start!")

print(f"That is your secret Word: {secretWord }")

chances = 6
stage = 0

print(f"Let`s play Hangman! You have {chances} to get the correct word" )
print(hangmanStages[0])
while chances > 0:
    guess = input("Guess a letter: ").upper()
    if guess in selectedWord:
        print("Correct Guess!")
        secretWord = list(secretWord)
        for i in range(len(selectedWord)):
            if selectedWord[i] == guess:
                secretWord[i] = guess
        secretWord = "".join(secretWord)
        print(secretWord)
    else:
        print("Wrong Guess!")
        chances -= 1

        print(hangmanStages[stage + 1])
        stage += 1
        
        print(f"Chances Left: {chances}")
        
    if "_" not in secretWord:
        print("Congratulations! You Won!")
        break

if "_"  in secretWord:    
    print("Game Over!")
    print(f"The correct word was: {selectedWord}")  






















# input("Press Enter to Exit!")