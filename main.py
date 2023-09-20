#validates a number is a valid integer
def validate_input():
    valid_input = False
    while valid_input == False:
        try: 
            guess = int(input("Enter a number between 1 and 100: "))
        except: 
            print("Not an integer. Enter a number between 1 and 100")
        else:
            valid_input = True
    return guess


import random
from art import logo
target_number  = random.randint(1,100)
lives = 0
#Prints Introduction
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100. Try to guess it!")
#Validates input to ensure proper difficulty is selected
valid_difficulty = False
while valid_difficulty == False:
    difficulty = input("Choose a difficulty. 'easy' for 10 lives, 'hard' for 5 lives: ")
    if difficulty == "easy":
        lives = 10
        valid_difficulty = True
    elif difficulty == "hard":
        lives = 5
        valid_difficulty = True
    else:
        print("Invalid difficulty, try again")
#Takes initial guess and initiates feedback loop
guess = validate_input()
number_guessed = False
#While at least 1 life and number isn't guessed
while lives > 0 and number_guessed == False:
    #checks if guess is between 1 and 100. Let's player re-input otherwise
    if (guess < 1) or (guess > 101):
        guess = input("Not an integer between 1 and 100, input a number between 1 and 100: ")
    else:
        #If guess is correct, ends game
        if guess == target_number:
            print(f"You got it! The answer was {target_number}.")
            number_guessed = True
        #If guess is too low, tells player, deducts a life, and prompts another guess
        elif guess < target_number:
            lives += -1
            print(f"Too Low! Lives remaining: {lives}")
            guess = validate_input()
        #If guess is too high, tells player, deducts a life, and prompts another guess
        elif guess > target_number:
            lives += -1
            print(f"Too High! Lives remaining: {lives}")
            
            guess = validate_input()
        #Error handling if for some reason none of the above checks work
        else:
            print("Error. You shouldn't see this")
            number_guessed = True




