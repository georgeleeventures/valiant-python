# File:    make-triangle.py
# Author:  George Lee
# Date:    4/15/2015
# E-mail:  g@georgelee.co
# Web: georgelee.co
# © Copyright 2015 George Lee / georgelee.co. All Rights Reserved
# Description:
# This contains python code necessary to generate a triangle based on input
# of how many rows we want the triangle to be (height). Please, only numeric
# inputs or I will have to take legal action against you for trying to 
# manipulate the system... Just kidding. But please, just integers.

# define our main function
def main():

    #welcome
    print("Welcome! This python program will create a triangle given an input")
    print("height value. Please, integers only!")

    # collect user input for the height
    userNum = int(input("Please enter the height of the triangle: "))

    # specify the type of symbol we want to use, in this case, an asterick *
    symbolType = "*"

    # loop that will print out the triangle given restriction.
    for i in range(0, userNum):
        
        # output the triangle based on conditions specified by user.
        print(symbolType)
        
        # increment symbolType so to keep adding * in the range of 0-input.
        symbolType += "*"
# run the app by calling main!        
main()
