
# A program that calculates test averages
# 06/27/2017
# CTI-110 M5HW1 - Test Average and Grade
# India Sylvester
#
def main():

    testscore1 = float(input('Enter the first test score: '))
    testscore2 = float(input('Enter the second test score: '))
    testscore3 = float(input('Enter the third test score: '))
    testscore4 = float(input('Enter the fourth test score: '))
    testscore5 = float(input('Enter the fifth test score: '))

    calc_avg(testscore1, testscore2, testscore3, testscore4, testscore5)
    score_return(avg())

def calc_avg(score1, score2, score3, score4, score5):
        total = score1 + score2 + score3 + score4 + score5
        avg = total/5
        print(avg)
        score_return(avg)

def score_return(score):
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

main()
