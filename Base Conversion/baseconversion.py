# File:    baseconversion.py
# Author:  George Lee
# Date:    11/2/2014
# E-mail:  g@georgelee.co
# Web: georgelee.co
# Description:
# This program will read the contents of a text file and 
# will write out the ASCII values of each alphaNumeric 
# character in a user selected numeric base.

# changeBase() takes an int as param and base as param and returns a change
# of the integer to some requested base form. This will only support bases under
# 10 for now, because we have not casted this to an indexable list required for expansion
# Input:  numParam, the integer and baseParam, the chosen base to convert to.
# Output: the input integer converted to the selected base.
def changeBase(numParam, baseParam):
    # if numparam is not alphanumeric, we will just skip it and return ..
    # otherwise, we will process the number and get the base change form.
    if(numParam != '..'):
        # take our number and mod the base.
        numModBase = numParam % baseParam
        
        # conditionals to manipulate the numbers and handle computations as needed.
        # ie) in case the number is 0, we need to handle the problem by returning ''
        if numParam == 0:
            return ''
        elif numParam <= 1:
            return str(numParam)
        else:
            # a bit of recursion down here, hope you won't mind.
            # we need to call our function, do division but also pass over the
            # base to change to, and not forget to concatenate the last numModBase
            return str(changeBase(numParam // baseParam, baseParam)) + str(numModBase)
    else:
        return '..'
    
# formatResult() takes a number and will either keep the number as is or 
# change the number to two dots (..) if it is determined to not be 
# alphanumeric. Just for this assignment.
# Input:  number, the integer to check
# Output: either the number itself of two dots .. if not alphanumeric.
def formatResult(number):
    
    number = int(number)
    # only return the number IF the number satisfies alphanumeric,
    # otherwise, we will just return two dots for all intents and purposes.
    if(number >= 65 and number <= 90) or (number >= 48 and number <= 57) or (number >= 97 and number <= 122):
        return number
    else:
        return '..'

def main():

    # get the filename from the user.
    fileName = input("Enter the name of the file: ")
    
    userBase = ''
    # ask the user what base he/she wants to convert to and stop at nothing to get a proper response.
    while(userBase < '2' or userBase > '9' or userBase.isdigit() == False):
        userBase = input("Enter a base between 2 to 9: ")
        
    # open the file as read/write, and create new file per specifications
    inputFile = open(fileName, "r")
    newFileName = str(userBase)+'_'+fileName
    outputFile = open(newFileName, "w")
    
    # read the entire file as a string
    fileContents = inputFile.read()
    convertedList = []
    
    # for loop to read the entire inputfile as a string.
    for i in fileContents:    
        # format the numbers and change nonalphanumeric to ..
        formatMutation = formatResult(ord(i))
        
        # finally, change applicable nums to user chosen base (cast userbase to int!)
        mutateNumber = changeBase(formatMutation, int(userBase))
        
        # strip leading zeros so everything looks nice
        mutateNumber.lstrip('0')
        
        # append the changed number to the convertedlist list
        convertedList.append(mutateNumber)
    
    # writing to file, but this is a bit confusing!!
    for i in range(1, len(convertedList)+1):      
        outputFile.write(convertedList[i-1] + " ")

        # append a new line at every 5th result.        
        if(i % 5 == 0):
            outputFile.write('\n')

    # we gotta close our inputs and outputs for efficiency
    inputFile.close()
    outputFile.close()
    
    # we're done! show the user the success message
    print("Done. Use cat to see the file:", newFileName)
    
# call main and run our app
main()