# File:    functions.py
# Author:  George Lee
# Date:    4/15/2015
# E-mail:  g@georgelee.co
# Web: georgelee.co
# © Copyright 2015 George Lee / georgelee.co. All Rights Reserved
# Description:
# This program will, given input, take the goldback decomposition, tell you the
# greatest common divisor of two numbers, tell you if the number is perfect, 
# tell you the prime factors, and show you nice menu altogether. Trust me,
# this assignment is the most outlandish that I have ever seen. 
# Have fun though and please, enter integers only or i will throw a 
# nasty but generic error message at you. Cheers!

# GCD() takes two integers and return the largest number that evenly 
# divides both integers.
# Input:  num1, the first number inputted and num2, the second number inputted
# Output: the largest number that evenly divides both intgers.
def GCD(num1, num2):
    # first, we're gonna find the smaller number and set that var.
    if(num2 > num1):
        # second number is smaller.
        smallNum = num2
    elif(num1 > num2):
        # first number is smaller.
        smallNum = num1
    else:
        # both the same, so just default to num1
        smallNum = num1
        
    divisorNum = 1
    # for loop to determine which number is the greatest common divisor.
    for e in range(1, smallNum + 1):
        # confusing, but here we check if BOTH nums can cleanly divide the current num e.
        if((num1 % e == 0) and (num2 % e == 0)):
           # set divisorNum var to e IF conditions met. Replace when bigger one is found
           divisorNum = e
    
    return divisorNum

# isPerfect() takes a single integer and returns True is the number is equal to 
# half the sum of all of its positive divisors, and false otherwise.
# Input:  num1, the first number inputted
# Output: True or False boolean based on whether the number is perfect or not.
def isPerfect(num1):
    
    divisibleNums = []
    # first, let's take the num and check every number less than it.
    for i in range(1, num1 + 1):
        if(num1 % i == 0):
            # append to a list for my sanity -.-
            divisibleNums.append(i)
    
    # list divisiblenums holds the divisible nums, so let's sum them up quickly.
    sumOfDivisible = sum(divisibleNums)
          
    # now, let's divide the number by two as per the property of a "perfect number"
    halvedResult = sumOfDivisible / 2
    
    # conditionals to run through and check if halvedresult equals original number.
    if(halvedResult == num1):
        return True
    else:
        return False

# isNumPrime() will be our helper function so we can easily loop 
# through later and find whether or not a number is prime.
# Input:  theNumberTested, the number being tested for primeness
# Output: True or False boolean based on whether the number is prime or not.
def isNumPrime(theNumberTested):

    # loop to check every number from 2 to my num too see if prime.
    for l in range(2, theNumberTested):
        if(theNumberTested % l == 0):
            return False        
    return True

# goldbach() takes a single, positive even integer greater 
# than 4 and returns two primes, the sum of which is that num1.
# Input:  num1, the number being tested for goldbach
# Output: firstPrime, secondPrime -- two numbers that are prime
# and add up to the originally entered number.
def goldbach(num1):
    

        primesOfNum = []
        # get all the primes in a list through a for loop
        for g in range(1, num1 + 1):
            if(isNumPrime(g) == True):
                primesOfNum.append(g)

        #primes are in the list, so now we can add each num and the next num to
        # check if it will equal the original num. If equal, return those two.
        for i in range(0, len(primesOfNum) - 1):
            numPart = primesOfNum[i]
            for e in range(0, len(primesOfNum) - 1):
                check = numPart + primesOfNum[e]
                # do our check from the nested loop values
                if(check == num1):
                    firstPrime = numPart
                    secondPrime = primesOfNum[e]
                
        return firstPrime, secondPrime    
         
# primeFactors() takes a single, positive integer and returns
# a list of all the prime factors of that integer.
# Input:  num1, the number being run to check for prime factors
# Output: primeFactorList, a list of primes of the number.
def primeFactors(num1):
    
    primeList = []
    # for loop to check numbers that are prime from 1 to num1+1
    for e in range(1, num1 + 1):
        if(isNumPrime(e) == True):
            # the e is prime!
            primeList.append(e)

    primeFactorList = []
    # for loop and if stmt: num1 % i to get PRIME factors from list.
    # and finally append to the final list to return.
    for i in primeList:
        if(num1 % i == 0):
            primeFactorList.append(i)
        
    return primeFactorList

# getMenu() prints a pre-set menu.
# a list of all the prime factors of that integer.
# Input:  none
# Output: list of options for user.
def getMenu():
    #just a space between menu output between each program run by the user
    print("")
    print("Please enter a choice:")
    print("1. Greatest common divisor")
    print("2. Perfect number check")
    print("3. Goldbach decomposition")
    print("4. Prime Factors")
    print("5. Quit")


# getNumber() prints message, and then asks the user for a number.
# If the number is less than min, the function will loop, continuing
# to ask the user for a number until the user enters  a number larger 
# than min. The function then returns that number
# Input:  message for user to see, minimum value of input
# Output: numInput, a sanitized and clean input
def getNumber(message, minimum): 
    # print the message, and then as the user for the number    
    numInput = int(input(message))
    
    while(numInput < minimum):
        print("Number entered is not acceptable!")
        numInput = int(input(message))
    
    return numInput
    
# welcomeMessage() prints welcome message to user.
# Input:  none
# Output: welcome message
def welcomeMessage():
    print("Welcome! This program will prompt you to enter a number,")
    print("and ask you to select a certain program choice.")
    print("After selecting, follow directions and receive results.")
    
# define our main function.
def main():
    # show the welcome message and set program selection var to default
    welcomeMessage()
    userSelection = 0
    
    # while loop to keep going unless user wants to quit.
    while(userSelection != 5):

        getMenu()
        
        # get user selection of a certain program.
        userSelection = int(input(""))
    
        # use a list of allowed inputs, just for my sanity.
        allowedInputs = [1,2,3,4,5]
        while(userSelection not in allowedInputs):
            userSelection = int(input("Selection Invalid! Please enter a valid selection: "))
    
        # conditionals so we can do what the user wants to run.
        if(userSelection == 1):
            # collect inputs from user - positive will do for GCD
            numInput = getNumber('Please enter a positive integer: ', 1)
            numInput2 = getNumber('Please enter a positive integer: ', 1)
            
            largestDivisor = GCD(numInput, numInput2)
            print("The greatest common divisor of", numInput, "and", numInput2, "is:", largestDivisor)
            
        elif(userSelection == 2):
            # get input from user
            numInput = getNumber('Please enter a positive integer: ', 1)
            
            # basic conditionals to print custom message to user.
            if(isPerfect(numInput) == True):
                print(numInput, "is a perfect number.")
            elif(isPerfect(numInput) == False):
                print(numInput, "is not a perfect number.")
                
        elif(userSelection == 3):
            # get the input from user, but we need positive int GREATER THAN 4 and is EVEN!
            numInput = getNumber('Please enter an even positive integer greater than 4: ', 4)

            while(numInput % 2 != 0):
                # not even, so reprompt user.
                print("Number is not even and is not acceptable.")
                numInput = getNumber('Please enter an even positive integer greater than 4: ', 4)
                
            goldBachPrimes = goldbach(numInput)
            # return result, and use indexes to show individual numbers.
            print("The goldbach decomposition of", numInput, "is", goldBachPrimes[0], "and", goldBachPrimes[1])
            
        elif(userSelection == 4):
            # collect user input for Prime Factors. Positive int will do.
            numInput = getNumber('Please enter a positive integer: ', 1)
    
            print("The prime factors of", numInput, "are", primeFactors(numInput))

     
    print("Quitting...")
# call main and run our app!
main()
