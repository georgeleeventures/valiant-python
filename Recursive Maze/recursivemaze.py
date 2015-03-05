# File:    recursivemaze.py
# Author:  George Lee
# Date:    11/21/2014
# E-mail:  g@georgelee.co
# Web: georgelee.co
# © Copyright 2014 George Lee / georgelee.co. All Rights Reserved
# Description:
# This app solves mazes based on a command line input and uses
# recursion among other python techniques to do so.
# You must enter the filename and a set of two integers after
# running this script in python. The first 2 integers will
# represent start, while second set will be the final destination
# You'll either get results or nothing at all.

import sys

# printPath() shows the path of the maze to the user.
# Input: path (list of tuples)
# Output: line in for loop, basically all tuples in the list.
def printPath(path):
    for line in path:
        print(line)

# isInPath() returns a boolean whether or not a coordinate tuple is already in the path list
# Input: coordinateTuple, currentPath
# Output: Boolean, True if in path, otherwise, False.
def isInPath(coordinateTuple, currentPath):
    if(coordinateTuple in currentPath):
        return True
    else:
        return False

# searchMazeRecurse() determines recursively whether or not there is a path existant to solve maze.
# Input: maze (3d maze list), path_so_far (list of tuples where we've been), finish_pos (final intended destination)
# Output: Boolean, True or False depending on whether or not results were found.
def searchMazeRecurse(maze, path_so_far, finish_pos):

    # get our current position in maze by taking tuple value at end of path so far list.
    currentPosition = path_so_far[-1]
    
    # break up the position coordinate tuple. (?,?) - get with index 0 and 1. X = row, Y = column
    xPosition = int(currentPosition[0])
    yPosition = int(currentPosition[1])

    # define our specific box by taking 3D array and looking into specific row and column.
    mazeBox = maze[xPosition][yPosition]
    
    # Check all 4 sides of box, and append to list. If we're not done, pop off the last one on path_so_far.
    
    # check right side and make sure we have not been there yet.
    if(yPosition + 1 < len(maze[0]) and int(mazeBox[0]) == 0 and isInPath((xPosition, yPosition + 1), path_so_far) == False):
        path_so_far.append((xPosition, yPosition + 1))
        if(searchMazeRecurse(maze, path_so_far, finish_pos) == False):
           path_so_far.pop()
    # check bottom side and make sure we have not been there yet.
    if(xPosition + 1 < len(maze) and int(mazeBox[1]) == 0 and isInPath((xPosition + 1, yPosition), path_so_far) == False):
        path_so_far.append((xPosition + 1, yPosition))
        if(searchMazeRecurse(maze, path_so_far, finish_pos) == False):
            path_so_far.pop()     
    # check left side and make sure we have not been there yet.
    if(yPosition - 1 >= 0 and int(mazeBox[2]) == 0 and isInPath((xPosition, yPosition - 1), path_so_far) == False):
        path_so_far.append((xPosition, yPosition - 1))
        if(searchMazeRecurse(maze, path_so_far, finish_pos) == False):
            path_so_far.pop()
    # check top side and make sure we have not been there yet.
    if(xPosition - 1 >= 0 and int(mazeBox[3]) == 0 and isInPath((xPosition - 1, yPosition), path_so_far) == False):
        path_so_far.append((xPosition - 1, yPosition))
        if(searchMazeRecurse(maze, path_so_far, finish_pos) == False):
            path_so_far.pop()

    # are we done or not? Run comparison and return boolean true/false.
    if(path_so_far[-1] == finish_pos):
        return True
    return False

# searchMaze() bootstraps and handles parameters
# Input: maze (3d list), start_pos (list of tuples), finish_pos (end position)
# Output: path_so_far (a list of tuples indicating path), or None if no results found.
def searchMaze(maze, start_pos, finish_pos):
    
    # make the blank list and add our most current position/start position to it.
    path_so_far = []
    path_so_far.append(start_pos)

    # start the recursive maze search. Pass maze array, pathsofar array and finish position.
    searchRun = searchMazeRecurse(maze, path_so_far, finish_pos)
    if(searchRun == True):
        return path_so_far
    else:
        return None

# readMazeFile() reads and processes the input text file into a 3d list.
# Input: filename, the user entered filename from 
# Output: mazeArray (3d array), mazeRows (total number of rows), mazeCol (total number of columns in maze)
def readMazeFile(filename):
    # first, lets open the file
    openMaze = open(filename, 'r')
    # read first line and get rows/columns
    readFirst = openMaze.readline()
    getRowCol = readFirst.split()
    mazeRows = int(getRowCol[0])
    mazeCol = int(getRowCol[1])
    
    mazeArray = []
    mazeLine = []
    for line in openMaze:
        splitLine = line.split()
        # ONLY take the lines that have more than 2 values
        if(len(splitLine) > 2):
            mazeLine.append(splitLine)
        if(len(mazeLine) % mazeCol == 0):
            mazeArray.append(mazeLine)
            # reset mazeline, and start over.
            mazeLine = []

    # don't forget to close the file for optimal mem conservation!
    openMaze.close()
    
    return mazeArray, mazeRows, mazeCol

# processCommandLineArgs() takes in a reads the command line inputs from user using 
# sys.argv and changes them into appropriate formats.
# Input: None 
# Output: filename (str), startPos (tuple), finishPos (tuple)
def processCommandLineArgs():
    # sys.argv[0] = path to file, sys.argv[1] = input file, sys.argv[2-5] = integers
    # we only want 1-5.
    
    # need additional checking other than length? hope not.
    if(len(sys.argv) != 6):
        filename = None
        startPos = None
        finishPos = None
    else:
        filename = sys.argv[1]
        startPos = int(sys.argv[2]), int(sys.argv[3])
        finishPos = int(sys.argv[4]), int(sys.argv[5])
        
    return filename, startPos, finishPos

# printGreeting() prints a greeting to the user.
# Input: None 
# Output: welcome message printed to user.
def printGreeting():
    print("Welcome. This program will solve mazes using a recursive search algorithm.")
    print("Running maze search...")

# incorrectSystemArguments() prints a message to user if command line arguments were 
# entered incorrectly. The message is detailed and tells user the format.
# Input: None 
# Output: error message shown to user if entered info incorrectly.
def incorrectSystemArguments():
    print("Apologies, but you have not specified the proper inputs necessary for this app to solve a maze.")
    print("Please make sure that you specify a filename followed by 4 positive integer digits that are each")
    print("separated by spaces in order to indicate the start position (first 2 digits) and")
    print("end position (last 2 digits). Run the app again, and please specify PROPER inputs.")
    

# main() is the lifeblood of this app and runs everything, calls everything, etc..
# Input: None 
# Output: Result printed to user, either a result of coordinates or a message saying no result.
def main():
    
    # process the command line arguments supplied 
    filename, startPos, finishPos = processCommandLineArgs()

    # stop, terminate app, and notify user if filename is not there, or other input is missing.
    if(filename == None or startPos == None or finishPos == None or startPos[0] < 0 or startPos[1] < 0 or finishPos[0] < 0 or finishPos[1] < 0):
        incorrectSystemArguments()
    else:
        # show user the greeting.
        printGreeting()
        # take in the user file through command line args (sys.argv and read
        mazeData, mazeRows, mazeCols = readMazeFile(filename)
        # only do the search if the coordinates actually exist. Otherwise, just show no solution.
        if(startPos[0] > (mazeRows - 1) or startPos[1] > (mazeCols - 1) or finishPos[0] > (mazeRows - 1) or finishPos[1] > (mazeCols - 1)):
            searchResult = None
        else:
            # call searchMaze with the appropriate data.
            searchResult = searchMaze(mazeData, startPos, finishPos)
            
        # conditionals to check searchResult. We'll either have a list of tuples, or None type.
        # if we fail, just show no sol. msg, and ignore the printpath request on line 201.
        if(searchResult == None):
            resultMessage = "no solution was found!"
        else:
            resultMessage = "the following solution path was found:"
        print("Results:", resultMessage)
        
        # show the path using printPath if there was a result list returned.
        if(searchResult != None):
            printPath(searchResult)
   
# run our app!           
main()
