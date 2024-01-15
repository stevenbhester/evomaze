"""
The object of this game is to guess the animal/fungus that the computer chose.
The user does this by providing guesses.
The computer then compares the taxonomy of the users guess to the taxonomy of the computers choice.
The user gets to see which parts of the taxonomical heirarchy were correct and where they were off.
"""

#OUTLINE
"""
Computer chooses animal
Rules are displayed to the user
Retrieve the taxonomy of chosen animal
->User guesses (input)
|   check input for special characters
|   compare input to animal
|       if true, they win
|   retreive taxonomy of input animal
|   compare top level
|       while currentLevel is the same between chosen and input, display in UI (highlighted in blue)
|       move to next level
|       corectBranches++
|       when the while statement fails
|           display branch in UI (in black)
|           move to next level
|           incorrectBranches++
|   guesses++
|   On the left, print the input, correctBranches, and incorrectBranches
-<
"""

#ADD LATER
"""
Difficulties
Leaderboard
"""

import random
#import checkGuess
#import userGuess

#CHOOSE ANIMAL
#Choose an organism from a list of organisms in a list in which all choices are findable on Wikipedia
organism = ["Cow", "Chicken", "Human"]
master = random.choice(organism)
print(master)

#Display rules to user
#print("Hello and welcome to the maze of evolution! The object of this game is to guess the organism that the computer chose.")
#print("Once you guess an organism, the computer will check to see how closely your guess matches the taxonomy of the correct organism")
#print("You will then get to see the parts of the taxonomy tree that match, and where they are different. With this info, you're ready to make your next guess!")
#print("Once you get the right organism, make sure to put your name on the leaderboard!")


#Retrieve the taxonomy of the computer's organism
"""
Add the code with API and all here
Set the taxonomy as a list with each level being it's own item. List is 7 items long. Called masterTaxonomy[]
    Kingdom
    Division/Phylum
    Class
    Order
    Family
    Genus
    Species
"""
#set inccorect guesses to zero in case they get it right on the first guess
incorrectGuesses = 0
guessList = []
guess = " "

#call the user guess (currently located here for testing)
def userGuess():
    #Get user input for their guess
    global guess
    global guessList
    #CHANGE THIS FROM GLOBAL IN HERE - BAD PRACTICE
    guess = input("What do you think the organism is? ")
    #check for special characters
    specialCharacters = "!@#$%^&*()-+?_=,<>/"
    if any(c in specialCharacters for c in guess):
        print("Please do not inclue any special characters in your guess")
        #for now we will assume that the user follows the rules and doesn't include any special characters the second time
        #eventually we will need to DOUBLE CHECK
        guess = input("What do you think the organism is? ")
        print("Awesome, you guessed", guess, "which is a valid guess")
        guessList.append(guess)
        return guess, guestList
    else:
        print("Awesome, you guessed", guess, "which is a valid guess")
        guessList.append(guess)
        return guess, guessList
userGuess()


#Compare their guess to the correct master answer
def checkGuess(guess,master):
    global incorrectGuesses
    #CHANGE THIS FROM GLOBAL IN HERE - BAD PRACTICE
    if guess.lower() == master.lower():
        print("Congrats! You guessed the right organism! It took ", incorrectGuesses + 1, "guesses.")
        exit()
    elif guess.lower() != master.lower():
        incorrectGuesses = incorrectGuesses + 1
        print("Unfortunately,", guess, "was wrong. Try again!")
        #need to find a way to call userguess() in here
        return guess
checkGuess(guess, master)
#print("guess was", guess, "master was", master, "incorrect guesses were", incorrectGuesses)
print("Number of incorrect guesses was", incorrectGuesses)


#Retreive taxonomy of input animal
"""
Add the code with API and all here
Set the taxonomy as a list with each level being it's own item. List is 7 items long. Called guessTaxonomy[]
    Kingdom
    Division/Phylum
    Class
    Order
    Family
    Genus
    Species
"""

#Compare levels
#def compareGuess():
    #while contents of guessTaxonomy[x] == contents of masterTaxonomy[x]
        #display contents of guessTaxonomy[x] in UI (highlighted in blue)
        #corectBranches++
        #x++
        #correctBranches = x
    #for x, x<masterTaxonomy.len(), x++:
    #   display contents of guessTaxonomy[x] in UI (in black)
    #   incorrectBranches++
    #incorrectGuesses++


#Print the list of guesses on the left side of the screen
