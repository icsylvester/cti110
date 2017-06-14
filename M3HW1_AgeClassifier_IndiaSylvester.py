# A program that compares the user age to age standards
# 6-13-17
# CTI-110 M3HW1 - Age Classifier
# India Sylvester
#
# vaiables for ages
infantyr = 1
childyr = 13
teenageryr = 19


#get the age of the user
age = float(input('(Disclaimer: if you are before a year you can put a decimal. Example: .5 is 6 months)'+
                  'Enter how old you are: '))


#compare grades
if age <= infantyr:
    print('You are an infant. ')
elif age <= childyr:
    print('You are a child. ')
elif age <= teenageryr:
    print('You are a teenager. ')
else:
    print('You are an adult. ')
