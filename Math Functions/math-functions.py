# File:    mathfunctions.py
# Author:  George Lee
# Date:    3/30/2015
# E-mail:  g@georgelee.co
# Web: georgelee.co
# © Copyright 2014 George Lee / georgelee.co. All Rights Reserved
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

def main():
	print(getMax([2,4,7]))
	print(getMin([2,4,7]))
	print(getMean([2,4,7]))

main()