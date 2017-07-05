# A program that converts kilometers to miles
# 06/26/17
# CTI-110 M5T1_KilometerConverter 
# India Sylvester
#

#This program converts kilometers to miles
CONVERSION_FACTOR = 0.6214

# main function gets a distance in kilometers and calls the main
def main():

    #Get the distance in kilometers
    kilometers= float(input('Enter a distance in kilometers: '))

    #display the distance converted to miles
    show_miles(kilometers)
                  
def show_miles(km):

    #Calculate miles.
    miles = km * 0.6214

    #display the miles.
    print(km, 'kilometers equals', miles, 'miles.')

#Call the main function
main()
