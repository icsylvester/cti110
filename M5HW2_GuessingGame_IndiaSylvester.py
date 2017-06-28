# A program that get grades and calculates the testing averages
# 6/28/17
# CTI-110 M5HW2 - Random Number Guessing Game
# India Sylvester

#import the random generator
import random

# Call the main function
def main():
    
    guess = int(input(" Enter your guess in the range of 0 and 100: "))

    check_guess(guess)

def check_guess(crguess):

    answer = random.randrange(100)
    
    if(crguess == answer):
        print("You guessed it")
    else:
        total = 0
        for i in range(1, 100):
            print("Try again")
            tries = int(input("Enter in your guess: "))
            
            total += tries

main()
