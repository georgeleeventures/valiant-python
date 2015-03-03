# File:    part1.py
# Author:  George Lee
# Date:    10/2/2014
# Section: 07 Lecture, 09 Discussion
# E-mail:  ge5@umbc.edu
# Description:
# This file contains python code necessary to echo out a square in width 
# numbers and height rows. an example would be input of 4 w and 2h:
# 1 2 3 4
# 5 6 7 8
# Thus, we see there are numbers following a 4 by 2 box made up with numbers.

# define welcome message
def welcome():
    print("Hello. This python program will create a box using an input")
    print("of two numbers, height and width. Please enter integers only.")
    print("The box will subsequently be made out of the numbers conforming")
    print("to the entered standards and boundaries.")

# define our main function                                                      
def main():

    # show welcome message.
    welcome()
    
    # collect user input for the height and width
    userWidth = int(input("Please, enter a width value (integer): "))
    userHeight = int(input("Please, enter a height value (integer):"))
    
    # increment value
    countNum = 1

    # for loop that will print out numbers of range based on user input
    for x in range(1, userHeight + 1):
        for i in range(1, userWidth + 1):
            
            # output the square based on conditions specified by user.
            print(countNum, end = " ")
            
            # count num - increment so we can display set of numbers
            countNum += 1
            
        # print to serve a line between     
        print("")
        
# run the app by calling main!        
main()