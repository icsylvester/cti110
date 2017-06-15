# A program that displays the total amout of calories burned in 30 minutes
# 6-15-17
# CTI-110 M4T1 - Calories
# India Sylvester
#
# give the total a start value.
total = 0

# get the calories the user burned
for minutes in range (0,31,5):
    #Get the calories per 5 minutes burned and calculate that total
    calories = 4.2 * 5
    #Display the calories burned
    print("Calories burned in " + str(minutes) + " is " + str(total))
    #increment
    total += calories



