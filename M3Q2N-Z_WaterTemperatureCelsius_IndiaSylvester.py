# (M3Q2N-Z) A program that compares the water temperature to the state of water in celcius
# 6-13-17
#  CTI-110 M3Q2N-Z - Water Temperaturwe in celcius
#  India Sylvester
#
# Define main function
#IT's a little tricky, but I'll get the hang of it. 
def main():
    print ('Temperature')

#if you call the function
if  __name__ == "__main__":
    # list of variable that define what temperature the state difference
    icetemp = 0
    steamtemp = 100


    #get the temp of water
    temp = float(input('Enter the temperature in degrees (Celcius) of the water temperature: '))


    #compare the water temp
    if temp <= icetemp:
        print('The state of water is solid, therefore it is ice. ')
    elif temp > steamtemp:
        print('The state of water is a gas, therefore it is steam. ')
    else:
        print('The state of water is a liquid, there for it is liquid water')
else:
    ("Try again.")
