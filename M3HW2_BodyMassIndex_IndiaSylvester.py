# A program that compares the users body mass to body mass standards 
# 6-13-17
# CTI-110 M3HW2 - Body Mass Index
# India Sylvester
#
# variables for BMI.
underweightBMI = 18.5
overweightBMI = 25


#get the height and weight from the user 
weight = float(input(' Enter in your weight: '))
height = float(input(' Enter in your height: '))

BMI = weight * ((703)/(height**2))
#compare BMI
if BMI <= underweightBMI:
    print('You are underwieight ')
elif BMI >= overweightBMI:
    print('You are overweight. ')
else:
    print('You are a normal weight. ')
