# A program that compares the user grade to grading standards
# 6-12-17
#  CTI-110 M3LAB - Debugging
# India Sylvester
#
# list of variable that define what it takes to get a letter grade
A_score = 90
B_score = 80
C_score = 70
D_score = 60
F_score = 50

#get the score for the course
score = int(input('Enter the grade you received for the course: '))


#compare grades
if score >= A_score:
    print('Your grade is an A. ')
elif score >= B_score:
    print('Your grade is an B. ')
elif score >= C_score:
    print('Your grade is an C. ')
elif score >= D_score:
    print('Your grade is an D. ')
else:
    print('Your grade is an F. ')
