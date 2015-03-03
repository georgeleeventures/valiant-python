# File:    part4.py
# Author:  George Lee
# Date:    10/2/2014
# Section: 07 Lecture, 09 Discussion
# E-mail:  ge5@umbc.edu
# Description:
# This file contains python code needed to generate a pairwise
# sum array given the input of two arrays, each ended with 'end'
# respectively. Please enter a set of integers when prompted.

def welcome():
    print("Hello, This program will generate a pairwise sum array given")
    print("the input of two list of values. End each list by entering 'end.'")

# define our main function                                                      
def main():

    # show welcome message
    welcome()

    # blank array
    makeList = []
    makeList2 = []
    resultList = []
    # get user input
    userNum = input("Please, enter a number: ")
    # some static values to use in conditionals
    stopLooping = False
    stopLooping2 = False
    finalTotal = 0
    
    # append number entered to list.
    makeList.append(userNum)    
    
    # while loop to keep collecting numbers for first list
    while(stopLooping != True):
        userNum = input("Please, enter a number: ")
              
        # stop if user wishes to terminate, or add to list
        if(userNum == 'end'):
            stopLooping = True
        else:
            makeList.append(userNum)
           
    # second while loop to collect second list of ints       
    while(stopLooping2 != True):
        userNum = input("Please, enter a number: ")

        # stop if user wishes to terminate, or add to list
        if(userNum == 'end'):
            stopLooping2 = True
        else:
            makeList2.append(userNum)       
     
    # get length of arrays
    makeLength1 = len(makeList)
    makeLength2 = len(makeList2)
    
    # for loop to run comparison of two lists and determine if we need
    # a difference length and implode 0's, or if equal amt, we're good!
    if(makeLength1 < makeLength2):
        finalTotal = makeLength2
        differenceLength = makeLength2 - makeLength1
        for s in range(0, differenceLength):
            makeList.append(0)
    elif(makeLength1 > makeLength2):
        finalTotal = makeLength1
        differenceLength = makeLength1 - makeLength2
        for r in range(0, differenceLength):
            makeList2.append(0)            
    elif(makeLength1 == makeLength2):
        finalTotal = makeLength1

    # for loop to add the numbers of the two lists together.
    for i in range(0, finalTotal):
        # define variables and cast into ints so we're not adding str
        firstList = int(makeList[i])
        secondList = int(makeList2[i])
        addLists = firstList + secondList
        resultList.append(addLists)
    
    # print results
    print(resultList)
        
# run the app by calling main!        
main() 