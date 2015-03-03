# File:    part2.py
# Author:  George Lee
# Date:    10/2/2014
# Section: 07 Lecture, 09 Discussion
# E-mail:  ge5@umbc.edu
# Description:
# This file contains python code needed to determine how many duplicates
# are in a certain list. For example, input of 2,3,4,4,4,5 will return
# 3 as there are 3 4's in a row. -- subsequence of elements!

def welcome():
    print("This python program will determine how many duplicates are")
    print("in a certain list, but only the subseqence of elements.")
    print("Please enter integers only, and end list by entering 'end'.")

# define our main function                                                      
def main():

    # show welcome message.
    welcome()

    # blank user list and other values for placeholder.
    userList = []
    firstCount = 1
    longRun = 0
    userNumber = ""
    
    # loop to keep asking user for number until he/she enters end.
    while(userNumber != "end"):
        
        # collect user input
        userNumber = input("Please, enter a number: ")
        
        # append number to list if not end -- but cast to int instead of str                
        if (userNumber != "end"):
            userList.append(int(userNumber))
        
    # find the longest run with for loop. (0 to one less than userList)
    for e in range(0, len(userList) - 1):
            
        # record the same number for all intents and purposes and increment
        if (userList[e] == userList[e + 1]):
            
            firstCount += 1
                    
            # set longest run number and replace if necessary.
            if (firstCount > longRun):
                
                longRun = firstCount
        else:
            # fool didn't enter any identical numbers, so just return the count 1.
            firstCount = 1
                   
    # show result of longest run.
    print("The longest run was: " + str(longRun) + " long.")
        
# run the app by calling main!        
main()