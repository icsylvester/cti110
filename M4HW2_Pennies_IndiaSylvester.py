# A program that counts the amount of pennies accumulative over a user declares.
# 6-19-17
# CTI-110 M4HW2 - Pennies for Pay 
# India Sylvester
#
# give the total a start value.
total  = 0
#penny intial value
penny = 1

# prompt the user to give the amount of days being counted.
days = int(input("Enter the amount of days that pennies are being collected: "))

# get the pennies accumulated.
for time in range (1,days):

#Calculate the pennies 
  penny *= 2.0
  

#Display the pennies collected
dollar = penny / 100
             
print("Pennies earned in " + str(days) + " is $" + str(dollar))
