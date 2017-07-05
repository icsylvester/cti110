# A program that converts feet to inches
# 6/26/17
# CTI-110 M5T2_FeetToInches 
# India Sylvester
#


#Constant for inches per foot
INCHES_PER_FOOT =12

#main function
def main():
    #Get a number of feet from the user
    feet = int(input('Enter a number of feet: '))

    #Convert that to inches
    print(feet, 'equals', feet_to_inches(feet), 'inches.')

#The feet_to_inches function converts feels to inches 
def feet_to_inches(feet):
    return feet * INCHES_PER_FOOT

#Call the main function.
main()
