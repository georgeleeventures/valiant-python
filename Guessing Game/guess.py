# File:    guess.py
# Author:  George Lee
# Date:    11/8/2014
# E-mail:  g@georgelee.co
# Web: georgelee.co
# © Copyright 2014 George Lee / georgelee.co. All Rights Reserved
# Description:
# This program is a game.
# You will need to guess the contents of a word
# file and subsequently play with another user.
# Guessing wrong has no penalty, but if it already
# exists, you lose a point.

# welcome() displays the welcome 
# Input:  none
# Output: welcome statement to welcome the user to the game.
def welcome():
    print("Welcome to the letter guessing game. This is a two player game. Enter a word file to begin.")

# getFileName() gets the file name from the user to process
# Input:  none
# Output: getInput, the filename.
def getFileName():
    getInput = input("Enter the name of your word file: ")
    return getInput

# processFile() processes/cleans the file and returns the result
# Input:  rawFile -- the file raw from the user input.
# Output: listOfWords, the contents in a list.
def processFile(rawFile):        
    listOfWords = []
    # for loop 
    for line in rawFile:
        # strip all \n from content
        sanitize = line.strip('\n')
        if(sanitize != ""):
            listOfWords.append(sanitize)
    return listOfWords

# currentRound() returns the current round given a game index
# Input:  gameIndexNum - unprocessed raw index number.
# Output: gameIndexNum, the current game round after incrementing.
def currentRound(gameIndexNum):
    # always 1 more than the index since list starts at 0.
    return gameIndexNum + 1    

# currentScore() shows the current score of player 1 and player 2
# Input:  playerOneScore, playerTwoScore - score numbers for players.
# Output: print statement detailing the player scores in a readable format
def currentScore(playerOneScore, playerTwoScore):
    print("----------------")
    print("The score for Player 1 is:", playerOneScore)
    print("The score for Player 2 is:", playerTwoScore)
    print("----------------")
    print()

# userWinner() shows the final score and calculates the winner of the game.
# Input:  playerOneScore, playerTwoScore - score numbers for players.
# Output: print statement detailing the final score and game result (who wins?)    
def userWinner(playerOneScore, playerTwoScore):
    
    print("THE FINAL SCORE IS:")
    currentScore(playerOneScore, playerTwoScore)
    # conditions to determine winner based on p1 and p2 scores
    if(playerOneScore > playerTwoScore):
        print("Player 1 WINS!")
    elif(playerTwoScore > playerOneScore):
        print("Player 2 WINS!")
    elif(playerOneScore == playerTwoScore):
        print("The game is a draw.")

# showCurrentWord() shows the current word with underscores so the user knows
# how many blanks need to be filled/guessed. 
# Input:  correctLetters, guessedCorrect - two lists that will be cross reference.
# Output: unvalidatedWord - a raw, unprocessed list of words with underscores.
def showCurrentWord(correctLetters, guessedCorrect):
    
    showCurrentWordStatus = correctLetters[:]
    unvalidatedWord = len(correctLetters) * ['_']
    # check the letters guessed correctly with the correct list. 
    for guessIndex in range(0, len(showCurrentWordStatus)):
        currentLetter = showCurrentWordStatus[guessIndex]
        for eachLetter in range(0, len(guessedCorrect)):
            if(currentLetter == guessedCorrect[eachLetter]):
                # guessIndex holds all indexes that should be exposed in word.
                # currentLetter holds the actual letter that needs to replace _
                # first, we will remove the first _ with the .pop method
                unvalidatedWord.pop(guessIndex)
                # now, we will insert the currentLetter with the guessLetter index.
                unvalidatedWord.insert(guessIndex, currentLetter)

    return unvalidatedWord

# showCurrentWordToUser() processes the unvalidatedWord from previous function and
# formats it in a manner a human would prefer to read, with spaces in between each letter
# Input:  correctLetters, guessedCorrect - two lists that will be cross reference.
# Output: print statement (toshowUser) detailing the current word in a readable format.
def showCurrentWordToUser(correctLetters, guessedCorrect):
    unvalidatedWord = showCurrentWord(correctLetters, guessedCorrect)
    # simple for loop to render the final product with end="" so to put everything together
    print()
    for toShowUser in unvalidatedWord:
        print(toShowUser, end=" ")
    print("\n")

# showUserTurn() runs the users turn, prompts the user to enter a guess and adds points
# if guess is right, subtracts if guessed a previously guessed letter, or switches the 
# user if he/she guessed wrong or guessed existing letter. Vars are self explanatory.
# Input:  currentPlayer, playerOneScore, playerTwoScore, guessedLetters, correctLetters, guessedCorrect, wordIsSolved.
# Output: playerOneScore, playerTwoScore, currentPlayer, guessedLetters, correctLetters, guessedCorrect, wordIsSolved
def showUserTurn(currentPlayer, playerOneScore, playerTwoScore, guessedLetters, correctLetters, guessedCorrect, wordIsSolved):  
    # change to opposite user when needed:
    if(currentPlayer == 1):
        oppositePlayer = 2
    elif(currentPlayer == 2):
        oppositePlayer = 1
    print("Player", format(currentPlayer) + "'s turn")
    currentScore(playerOneScore, playerTwoScore)
    # get input from user and check if it is within requirements
    playerInput = input("Enter a letter:").upper()
    limitInput = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    while (playerInput not in limitInput or len(playerInput) > 1 or playerInput == ''):
        print("Invalid input. Please only enter a single letter.")
        playerInput = input("Enter a letter:").upper()
    #conditionals so we can process user inputs, change scores, and change stuff depending on
    # whether or not the word is inside the word, or if the word has already been guessed.
    if(playerInput in guessedLetters):
        # player has stupidly guessed a letter already guessed. Penalty 1 Pt! and Change users!
        if(currentPlayer == 1):
            playerOneScore -= 1
        elif(currentPlayer == 2):
            playerTwoScore -= 1
        currentPlayer = oppositePlayer
        print("The letter", playerInput,"has already been selected.")
    elif(playerInput in correctLetters):
        # add to correct letters
        guessedCorrect.append(playerInput)
        numberOfOccurance = correctLetters.count(playerInput)
        # give user a point for correct guess
        if(currentPlayer == 1):
            playerOneScore += numberOfOccurance
        elif(currentPlayer == 2):
            playerTwoScore += numberOfOccurance
    elif(playerInput not in correctLetters):
        # tell and change user if user guessed letter that isnt there, but don't deduct points
        print("No letter:", playerInput, "in the word")
        currentPlayer = oppositePlayer
    # show the current status of the word
    showCurrentWordToUser(correctLetters, guessedCorrect)
    # add to the guessed list - regardless if right or wrong.
    guessedLetters.append(playerInput)
    # check if the word has been solved and if so, reset our list vars to null, and set wordissolved to true
    if('_' not in showCurrentWord(correctLetters, guessedCorrect)):
        wordIsSolved = True
        correctLetters = []
        guessedLetters = []
        guessedCorrect = []
    return playerOneScore, playerTwoScore, currentPlayer, guessedLetters, correctLetters, guessedCorrect, wordIsSolved

def main():
    # show user welcome message
    welcome()
    # List variables that will be changed later.
    currentWord = []
    correctLetters = []
    guessedLetters = []
    guessedCorrect = []
    playerOneScore = 0
    playerTwoScore = 0
    # default to player 1
    currentPlayer = 1
    # get the filename from user
    fileName = getFileName()    
    # open the file
    rawFile = open(fileName, "r")
    # parse file, remove \n and remove blanks and put into list by calling function
    listOfWords = processFile(rawFile)
    # for each game, we will do the following.
    for game in range(0, len(listOfWords)):
        # show the current round.
        roundNum = str(currentRound(game))
        print("Round:", roundNum)
        # store game word into a readily accessible list, and store it
        currentWord.append(listOfWords[game].upper())
        # for loop to create correct letters list.
        for letter in listOfWords[game]:
            correctLetters.append(letter.upper())  
        # show the current status of the word
        showCurrentWordToUser(correctLetters, guessedCorrect)                         
        # only continue if the word is not solved.
        wordIsSolved = False  
        # while loop to keep user going if word is not solved
        while(wordIsSolved == False):
            playerOneScore, playerTwoScore, currentPlayer, guessedLetters, correctLetters, guessedCorrect, wordIsSolved = showUserTurn(currentPlayer, playerOneScore, playerTwoScore, guessedLetters, correctLetters, guessedCorrect, wordIsSolved)                           
    # show final score, message, and the winner.
    userWinner(playerOneScore, playerTwoScore)
    
main()
