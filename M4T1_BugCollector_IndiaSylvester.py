# A program that read the information of the bugs that were vollected in that day
# and displays it
# 6-14-17
# CTI-110 M4T1 - Bug Collector
# Your Name
#
# give the total a start value.
total = 0

# get the user to input the bugs collectedf in each day
for day in range (1,8):
    print ('Enter the bugs collected on day', day)
    #input 
    bugs = int(input())
    #add them to total
    total += bugs

#Display the total bugs
    print("You collected a total of ", total, " bugs.")
