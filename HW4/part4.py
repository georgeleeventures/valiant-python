# File:    part4.py
# Author:  George Lee
# Date:    10/2/2014
# Section: 07 Lecture, 09 Discussion
# E-mail:  ge5@umbc.edu
# Description:
# This file contains python code needed to sort the provided static
# list. Enter a number and the list will be sorted.

def welcome():
    print("Hello, this python program will sort a user input value")
    print("into a list such that the list will continue to be from")
    print("smallest to largest, without using the sort method.")
    
# define our main function                                                      
def main():

    welcome()

    # homework provided list
    myList = [1, 9, 16, 24]
    
    # collect user input
    userNumber = int(input("Please, enter a number: "))
    
    if(userNumber <= myList[0]):
        myList.insert(0, userNumber)
    elif(userNumber >= myList[0] and userNumber < myList[1]):
        myList.insert(1, userNumber)
    elif(userNumber >= myList[1] and userNumber < myList[2]):
        myList.insert(2, userNumber)
    elif(userNumber >= myList[2] and userNumber < myList[3]):
        myList.insert(3, userNumber)        
    elif(userNumber >= myList[3]):
        myList.insert(4, userNumber)
                   
    print(myList)
    
# run the app by calling main!        
main()