# File:    math-functions.py
# Author:  George Lee
# Date:    3/30/2015
# E-mail:  g@georgelee.co
# Web: georgelee.co
# © Copyright 2015 George Lee / georgelee.co. All Rights Reserved
# Description:
# This program contains simple math functions that get the maximum
# minimum, average/mean

def getMax(myList):
    maxVal = 0
        for e in myList:
            if(e > maxVal):
                maxVal = e
        return maxVal

def getMin(myList):
    minVal = myList[0]
        for e in myList:
            if(e < minVal):
                minVal = e
        return minVal

def getMean(myList):
    total = 0
    average = 0
    for e in myList:
        total += e
        average = total/len(myList)
    return average

def getMedian(myList):
    # bubble sort!
    isSorted = False
        
        while(isSorted != True):
            isSorted = True
                
                for b in range(0, len(myList) - 1):
                    
                    if(myList[b] > myList[b+1]):
                        
                        isSorted = False
                            
                            larger = myList[b]
                                smaller = myList[b+1]
                                myList[b+1] = larger
                                myList[b] = smaller
        
        sortedList = myList
        
    return (myList[len(sortedList) // 2])



def main():
    print(getMax([2,4,7]))
        print(getMin([2,4,7]))
        print(getMean([2,4,7]))
        print(getMedian([10, 11, 13, 15, 16, 23, 26]))

main()