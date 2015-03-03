    #empty list from the user                                                 
def main():
    userList = []

    sameCounter = 1
    userInput = ""

    longestRun = 0

    #gets values from user until end                                          
    while userInput != "end":
        userInput = input("Enter a number: ")

        #adds values to list until end                                        
        if userInput != "end":
            userList.append(int(userInput))

    #determines the longest run                                               
    for x in range(0, len(userList) - 1):

            #keeps track of same number                                       
        if userList[x] == userList[x + 1]:

            sameCounter += 1

            if sameCounter > longestRun:
                    #determines the longest run                               
                longestRun  = sameCounter

            #no repeating number                                              
        else:

            sameCounter = 1

    print(longestRun)
main()