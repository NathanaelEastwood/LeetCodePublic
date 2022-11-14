import math
from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        BoardComplete = False

        def checkPossible(row, column):  # checkPossible returns a list of values which can fit in a Sudoku square
            possibleNums = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
            for i in range(9):  # cycle through all numbers in that row
                if (board[row][i]) in possibleNums:
                    possibleNums.remove((board[row][i]))
            for i in range(9):  # cycle through all numbers in that column
                if (board[i][column]) in possibleNums:
                    possibleNums.remove((board[i][column]))
            boxRightCol = (math.floor(column / 3)) * 3  # finding the sub grid
            boxRightRow = (math.floor(row / 3)) * 3  # finding the sub grid
            for j in range(3):  # loop through columns within the inner box
                for k in range(3):  # loop through rows within the inner box
                    if (board[boxRightRow + k][boxRightCol + j]) in possibleNums:
                        possibleNums.remove((board[boxRightRow + k][boxRightCol + j]))
            return possibleNums

        def checkByElim(row, column):  # checkByElim needs to check to see if any other square in that set has the
            # potential to carry a number
            # this function needs to eliminate numbers if it's possible for them to go elsewhere
            """
            possibleNums = checkPossible(row, column)
            for possibleNumberToHandle in (checkPossible(row, column)):
                for i in range(9):  # cycle through all squares in that row to check it can't go there instead
                    if board[row][i] == "." and possibleNumberToHandle in checkPossible(row, i):
                        possibleNums.remove(possibleNumberToHandle)
                for i in range(9):  # cycle through all numbers in that column
                    if board[i][column] == "." and possibleNumberToHandle in checkPossible(i, column):
                        possibleNums.remove(possibleNumberToHandle)
                boxRightCol = (math.floor(column / 3)) * 3  # finding the sub grid
                boxRightRow = (math.floor(row / 3)) * 3  # finding the sub grid
                for j in range(3):  # loop through columns within the inner box
                    for k in range(3):  # loop through rows within the inner box
                        if board[boxRightRow+k][boxRightCol+j] == "." and possibleNumberToHandle in checkPossible(boxRightRow+k, boxRightCol+j):
                            possibleNums.remove(possibleNumberToHandle)
            return possibleNums
            """

        while not BoardComplete:
            for i in range(9):
                for j in range(9):
                    if board[j][i] == "." and len(checkPossible(j, i)) == 1:
                        print("Adding ", checkPossible(j, i)[0], "To position", j + 1, " , ", i + 1)
                        board[j][i] = checkPossible(j, i)[0]

        print(board)
