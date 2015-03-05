# File:    connectfour.py
# Author:  George Lee
# Date:    11/14/2014
# E-mail:  g@georgelee.co
# Web: georgelee.co
# Description:
# This is the game called connect four. The program will prompt
# the user to enter a column choice to put his/her piece in place.
# The system will continue to ask the user for a piece until either
# user has four pieces (x or o's) in a row in the following directions:
# vertical, diagonal, and horizontal.

# welcomeMessage() displays the welcome message for this game
# Input: None
# Output: Welcome message (Welcome to Connect Four!)
def welcomeMessage():
    print("Welcome to Connect Four!")

# moveIntent() processes and adds a users move to the 2d array.
# Input:  gameBoard (the 2d array), colNum (the users choice move), currentPlayer
# Output: gameBoard (modified 2d array), moveRow (the corresponding sublist change was made)
def moveIntent(gameBoard, colNum, currentPlayer):
    
    # customize playerId to fit our backend data types (eg. pl 1 is 1, pl 2 is -1)
    if(currentPlayer == 1):
        playerID = 1
    elif(currentPlayer == 2):
        playerID = -1
    
    # insertion colNum change to list standards of 1 less.
    listCol = colNum - 1
    
    # take gameBoard, and iterate backwards with reversed()
    # try to add playerID into the appropriate (colNum + 1) by checking if taken. if taken, just
    # go on and move up a level. User will not be able to move one up anyways because this fault
    # tolerant system would have prevented it earlier on in the app.
    # stop going if we found an open spot.
    stopGoing = False
    for rows in reversed(range(len(gameBoard))):
        while(gameBoard[rows][listCol] == 0 and stopGoing == False):
            stopGoing = True
            gameBoard[rows].pop(listCol)
            gameBoard[rows].insert(listCol, playerID)
            moveRow = rows
    
    return gameBoard, moveRow

# showBoard() prints the board in a user friendly format to the screen.
# Input:  gameBoard (the 2d array)
# Output: Just the gameboard in the user friendly format.
def showBoard(gameBoard):
    # we have the gameboard array and need to copy it for sake of sanity
    tempBoard = gameBoard[:]
    # for loop to go through board and change values on the run as necessary.
    for row in tempBoard:
        for moves in row:
            # conditions to change the values to show to user. 0=not used, 1=player 1, 2=player2
            if(moves == 0):
                showToUser = '_'
            elif(moves == 1):
                showToUser = 'x'
            elif(moves == -1):
                showToUser = 'o'
            print(showToUser, end="")
        print()
        
# checkWin() determines whether a move caused a win, or not a win by checking in several
# directions for 4 in a row, such as horizontal, vertical, and \ / diagonals.
# Input:  gameBoard (the 2d array), row, col (row and col reference users input)
# Output: Boolean- True for a win, False for not a win.
def checkWin(gameBoard, row, col):
    
    # check the left \ diagonal for 4
    topLeftDiag = int(checkInDirection(row,col,-1,-1, gameBoard))
    bottomLeftDiag = int(checkInDirection(row,col,1,1, gameBoard))

    # check the right / diagonal for 4
    topRightDiag = int(checkInDirection(row,col,-1,1, gameBoard))
    bottomRightDiag = int(checkInDirection(row,col,1,-1, gameBoard))

    # check the horizontal for 4
    leftSearch = int(checkInDirection(row,col,0,-1, gameBoard))
    rightSearch = int(checkInDirection(row,col,0,1, gameBoard))

    # check vertical for 4 (only need down because we're checking realtime)
    downSearch = int(checkInDirection(row,col,1,0, gameBoard))
    
    # default to not a win.
    isAWin = False
    
    # conditions to check if = 4, to then return that a player has connected 4.
    if(topLeftDiag + 1 + bottomLeftDiag >= 4):
        isAWin = True
    elif(topRightDiag + 1 + bottomRightDiag >= 4):
        isAWin = True
    elif(leftSearch + 1 + rightSearch >= 4):
        isAWin = True
    elif(downSearch + 1 >= 4):
        isAWin = True
    
    return isAWin
    
# checkInDirection() checks in a certain direction, such as vertical, diagonal, etc.
# through the use of traversal of the board with coordinates.
# Input:  gameBoard (the 2d array), row, col (row and col reference users input), deltaRow, and deltaCol
# Output: counter (total occurances in a certain direction)
def checkInDirection(row, col, deltaRow, deltaCol, gameBoard):
    
    col = col - 1
    playerID = gameBoard[row][col]
    currentRow = row + deltaRow
    currentCol = col + deltaCol

    counter = 0

    while(isInBounds(currentRow,currentCol,gameBoard) and gameBoard[currentRow][currentCol] == playerID):
        counter += 1
        currentRow += deltaRow
        currentCol += deltaCol
    
    return counter

# isInBounds(), a helper function, checks whether or not we are in bounds for the checkInDirection function.
# Input:  gameBoard (the 2d array), row, col (row and col reference users input)
# Output: Boolean, True or False
def isInBounds(row, col, gameBoard):
    return row >= 0 and row < len(gameBoard) and col >= 0 and col < len(gameBoard[0])

# isDraw() determines whether a game is a draw or not.
# Input:  gameBoard (the 2d array)
# Output: Boolean, True or False
def isDraw(gameBoard):
    # simple - go through board and if all filled up and there are no 0's, then its a draw.
    tempBoard = gameBoard[:]
    for row in tempBoard:
        for moves in row:
            if(moves == 0):
                return False
        return True
    
# getUserInput() gets, validates, and returns a users input.
# Input: message, minimum (chars), maximum (chars, optional), gameBoard (list optional)
# Output: userInput -- all clean and sanitized
def getUserInput(message, minimum, maximum = None, gameBoard = None):
        
    userInput = input(message)

    while(userInput < minimum or userInput.isdigit() == False or (maximum != None and userInput > maximum) or (isValidMove(gameBoard, userInput) == False)):
        userInput = input("Please enter a valid choice: ")
    
    return userInput

# createGameBoard(), creates the 2d array based game board.
# Input:  totalRows (from user input), totalColumns (from user input)
# Output: outer, the entire array created.
def createGameBoard(totalRows, totalColumns):

    outer = []
    
    # create our 2d array with nested loops based on requirements.
    # for loop - rows first so we can establish number of inner arrays we need
    for i in range(totalRows):
        inner = []
        # and finally, the number of columns so we can pack this into the big array.
        for e in range(totalColumns):
            inner.append(0)
        outer.append(inner)
   
    return outer

# switchPlayer() switches the player to the opposite player
# Input:  currentPlayer, the current player
# Output: currentPlayer, the opposite player
def switchPlayer(currentPlayer):
    if(currentPlayer == 1):
        currentPlayer = 2
    elif(currentPlayer == 2):
        currentPlayer = 1
    return currentPlayer

# isValidMove() checks whether or not a move is valid
# Input:  gameBoard (the 2d game array), userCol (column user wants to enter)
# Output: Boolean, True or False
def isValidMove(gameBoard, userCol):
    if(gameBoard == None):
        return True
    else:
        userCol = int(userCol) - 1
        # check whether or not user selection has already been selected and is full.
        for rows in gameBoard:
            # check if user input exceeds bounds
            if(userCol > len(rows)):
                return False
            # if not, check if already taken.
            elif(rows[userCol] == -1 or rows[userCol] == 1):
                return False
            return True

# runGameSystem() is the main game controller that controls the game, switches users, and calls other functions
# Input:  currentPlayer, gameBoard, isGameComplete, gameCompleteType
# Output: currentPlayer, gameBoard, isGameComplete, gameCompleteType
def runGameSystem(currentPlayer, gameBoard, isGameComplete, gameCompleteType):
    
    # whose turn is it?
    print("Player", str(currentPlayer) + "'s turn:")
    
    # calculate total possible columns based on a gameboard length to santize input.
    maxMove = len(gameBoard[0])
    
    # some input validation:
    # minimum to enter is 1, as logical, and more specified as needed.
    userMove = getUserInput("Please enter a move: ", '1', str(maxMove), gameBoard)
    userMove = int(userMove)  

    # passed? good. now we pass the user move to moveIntent() 
    gameBoard, moveRow = moveIntent(gameBoard, userMove, currentPlayer)
    
    # assume game is not complete and change it as necessary
    isGameComplete = False
    
    # check if user is a winner.
    isWinner = checkWin(gameBoard, moveRow, userMove)
    
    #check if game is a draw
    isGameDraw = isDraw(gameBoard)
    
    # conditionals to determine win/draw: gamecompletetype- 1(win) 2= draw else switch player.
    if(isWinner == True):
        isGameComplete = True
        gameCompleteType = 1
    elif(isGameDraw == True):
        isGameComplete = True
        gameCompleteType = 2
    else:
        # continue and switch player.
        currentPlayer = switchPlayer(currentPlayer)
   
    return currentPlayer, gameBoard, isGameComplete, gameCompleteType

# main() is the main operator of this app
# Input:  None
# Output: None
def main():
    
    # show the welcome message
    welcomeMessage()
    
    # WHILE loop to continue the game unless user wants to stop playing
    stopGame = False
    while (stopGame == False):
        # get number of rows and number of columns
        totalRows = getUserInput("Please enter a number of rows: ", '5')
        totalColumns = getUserInput("Please enter a number of columns: ", '5')
        totalRows = int(totalRows)
        totalColumns = int(totalColumns)
        
        # create the game board array via function
        gameBoard = createGameBoard(totalRows, totalColumns)
    
        # set user turn default, booleans, and game complete type.
        currentPlayer = 1
        isGameComplete = False
        gameCompleteType = 0
                
        # now that gameboard is set, we need to ask user for his/her move as long as its not solved
        while (isGameComplete == False):
            # show the board to the user.
            showBoard(gameBoard)
            
            # call our main function to run the game.
            currentPlayer, gameBoard, isGameComplete, gameCompleteType = runGameSystem(currentPlayer, gameBoard, isGameComplete, gameCompleteType)
        
            if(isGameComplete == True):
                if(gameCompleteType == 1):
                    # show the board one last time and show winner.
                    showBoard(gameBoard)
                    print()
                    print("Player", currentPlayer, "wins!")
                    print()
                elif(gameCompleteType == 2):
                    # show the board one last time and show draw.
                    showBoard(gameBoard)
                    print()
                    print("The game is a draw!")
                    print()
    
        # at the end of game here, we need to ask user if he/she wants to play new game.
        restartGame = ''
        allowedInputs = ['y','n']
        while(restartGame not in allowedInputs):
            restartGame = input("Would you like to play again (y/n): ")
            print()
        if(restartGame == 'y'):
            stopGame = False
        elif(restartGame == 'n'):
            stopGame = True    

# call our app!
main()