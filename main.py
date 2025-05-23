"""
Testing Code. Explaining to Mack how IDE works


"""
"""
import random

#Declare variables
computerNumb = random.randint(1,10)
numbGuess = 0


playTime = 1
while playTime == 1:
    userGuess = int(input("Guess a number between 1 and 10: "))
    numbGuess = numbGuess + 1
    if computerNumb == userGuess:
        print("That is correct!")
        playTime = 0
    else:
        print("That was not correct. Try again.")
        

print("Thank you for playing!")
print(f"You solved {numbGuess} guesses!")
"""
"""
Number Guessing Game: Project 1

This program should allow a user guess a number that was geneated by the computer.

Required:
Computer picks a new number each time the game is ran
User is able to see wether they guessed correctly or not
User should be prompted with the left and right limits of the game


Bonus options:
Make it so there are different difficulties the user selects before the game
Make it so the user is able to choose to exit the game or restart when failed

"""

# imports
import random

# introduction to the game
numbGuesses = 0
highRange = 0
print("Hello Player,  \nWelcome to the number guessing game")

# Start the game
continueGame = "yes"
while continueGame == "yes":
    difficultyInput = input("What difficulty would you like to play? \n(please type easy or hard) ").lower()

    if difficultyInput == "easy":
        numbGuesses = 5
        highRange = 10
    elif difficultyInput == "hard":
        numbGuesses = 3
        highRange = 50
    else:
        print("Invalid Response! Please reset the game.")

    print(
        f"You have selected {difficultyInput} mode \n \nYou have {numbGuesses} guesses \nThe computer will guess a number between 1 and {highRange}")

    secretNumb = random.randint(1, highRange)

    while numbGuesses > 0:
        userGuess = input("What is your guess? ")
        userGuess = int(userGuess)
        if userGuess == secretNumb:
            print("Congradulations! You found the secret number!")
            numbGuesses = 0
            victoryStatus = 1
        else:
            print("That was not the secret number")
            numbGuesses = numbGuesses - 1
            victoryStatus = 2

    if victoryStatus == 1:
        continueGame = input("Would you like to play again? \n(Please say yes or no) ").lower()

    else:
        print(f"The secret number was {secretNumb}")
        continueGame = input("Would you like to play again? \n(Please say yes or no) ").lower()



