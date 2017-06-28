# A program that get grades and calculates the testing averages
# 6/28/17
# CTI-110 M5HW1 - Test Average and Grade
# India Sylvester

# Call the main function
def main():

    #Ask the user for each of the five test scores
    testscore1 = float(input('Enter the first test score: '))
    testscore2 = float(input('Enter the second test score: '))
    testscore3 = float(input('Enter the third test score: '))
    testscore4 = float(input('Enter the fourth test score: '))
    testscore5 = float(input('Enter the fifth test score: '))

    #Print out the letter grade for the first test
    print("The letter grade of the first test")
    score_return(testscore1)

    #Print out the letter grade for the second test
    print("The letter grade of the second test")
    score_return(testscore2)

     #Print out the letter grade for the third test
    print("The letter grade of the third test")
    score_return(testscore3)

     #Print out the letter grade for the fourth test
    print("The letter grade of the fourth test")
    score_return(testscore4)

     #Print out the letter grade for the fifth test
    print("The letter grade of the fifth test")
    score_return(testscore5)

    #Call the calc_avg function, so it will display.
    print("You're average test score is")
    calc_avg(testscore1, testscore2, testscore3, testscore4, testscore5)
   

#Define the calc_avg function
def calc_avg(score1, score2, score3, score4, score5):

        #Formula to calculate the sum of the test scores
        total = score1 + score2 + score3 + score4 + score5

        #the average formula for the test average
        avg = total/5

        #print the avg
        print(avg)

        #call the score return fucntion and display it
        print("You're average test score as a letter grade")
        score_return(avg)

        


#Define the score_return function
def score_return(score):

    #intialize the minimum for each score
    A_score = 90
    B_score = 80
    C_score = 70
    D_score = 60
    F_score = 50


    #compare grades
    if score >= A_score:
        print('Your test grade is an A. ')
    elif score >= B_score:
        print('Your test grade is an B. ')
    elif score >= C_score:
        print('Your test grade is an C. ')
    elif score >= D_score:
        print('Your test grade is an D. ')
    else:
        print('Your test grade is an F. ')

#end of the function
main()
