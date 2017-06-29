# A program that get grades and calculates the testing averages
# 6/29/17
# CTI-110 M5HW2 - Random Number Guessing Game
# India Sylvester

#import the random generator
import random

# Call the main function
def main():

    #generate a random number
    answer = random.randint(1,5)

    #Greet the user and get their input
    guess = int(input("Hey! Let's play a game! I am thinking of" +
                          " a number between 1 and 100. Can you" +
                          "guess it? : "))
        
    #for loop to max out the number of guess
    for i in range(1,6): 

        #If the user guesses correctly, then terminate the program
        correct = check_guess(guess, answer)
        #If correct answer was stated
        if (correct == True):
              #give the user back the total number of guesses
            print(" The total number of guesses were " + str(i))

            #give user the previous answer
            print("The answer was " + str(answer))
           #Stop program
            break
        else:
            int(input("Enter in another guess: "))
        
        #Ask user if they want to play again
                
    confirm = str(input("Do you want to play again? : "))

        #If they say yes
    if(confirm == "yes"):

            #loop it back to input
             int(input(" Enter in your guess: "))

        #terminate the program if they say no
    elif(confirm == "no"):
    

            #say a goodbye
            print(" Enjoy your day! ")

    #just incase they try to type anything other than the two confirmations
    else:
            print("Enter a yes or a no.")
            confirm = str(input("Do you want to play again? : "))
            
#Define the checking answer
def check_guess(crguess, answer):

    #if the answer is correct
    if(crguess == answer):

       #coingratulate the user 
        print("You guessed it!")
        
        return True

    #if the user was wrong
    else:
        #if number guess was too high
        if(crguess > answer):
             print("The number was too high. ")

        #if number guess was too low    
        else:
             print("The number was too low. ")
        return False
            
#call the main            
main()
