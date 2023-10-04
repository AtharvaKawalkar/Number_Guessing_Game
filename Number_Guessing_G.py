#Number Guessing Game
import random
import Number_Guessing_G_art

Easy_level_turns = 10
Hard_level_turns = 5
print(Number_Guessing_G_art.logo)
print("Welcome to Number Guessing Game")
print("I'm thinking of number between 1 to 100 and you have to guess")
print("Choose a difficulty level. Easy level has 10 attempts while hard one has only 5")
rand = random.randint(0,100)

def difficulty():
    choice = input("Type 'easy' or 'hard' : ").lower()
    if(choice == 'easy'):
        attempts = Easy_level_turns
        print("You have 10 attempts to guess the correct number")
    else:
        attempts = Hard_level_turns
        print("You have 5 attempts to guess the correct number")
    return attempts

def game():
    attempts = difficulty()
    while(attempts>0):
        guess = int(input("Make a guess : "))
        if(guess == rand):
            print(f"You got it. The number was {rand}")
            break
        elif(guess>rand):
            print("Too High")
            print("Guess again")
            print(f"You have {attempts-1} attempts remaining")
            attempts -= 1
        else:
            print("Too Low")
            print("Guess again")
            print(f"You have {attempts-1} attempts remaining")
            attempts -= 1

    if(attempts == 0):
        print("You've ran out of guesses. You Lose")

game()