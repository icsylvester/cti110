# A program that calculate meal price, tax and tip
# 6/7/17
# CTI-110 M2HW2 - Tip Tax Total
# India Sylvester
#

#get meal price
meal_price = float( input('How much was the meal consumed? : '))
#Calculate the tax of the meal
tax = meal_price * .07

#Add the two values together
total_price = tax + meal_price

#Calculate the tip, you should give the waitress
tip =  total_price * .18

#Calculate the total meal price
total_meal = tip + total_price

#Display the price, tax and tip
print('The total price is $', format(total_meal , ',.2f'))
print('This is with a meal price of $', format(meal_price , ',.2f'))
print('And a tax of $', format(tax , ',.2f'))
print('The combination of these two values is $', format(total_price , ',.2f'))
print('And you should tip this amount $', format(tip , ',.2f'))

