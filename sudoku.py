class Pair:
    def __init__(self, first, second):
        self.first = first
        self.second = second


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Solution
        # 1. Go to empty cells, row-by-row
        # 2. Attempt to solve that cell by checking if there are any valid numbers for that cell
        #   2a. Check every number in the submatrix, line, and row. Add them to a unique list, no dupes
        #   3a. If there is a number >=1 and <=9 that is NOT present in the array, that is the answer
        # 3. Proceed through each empty square, repeating from the start, until completely solved
        # Optimizations
        # 1. Weight each empty cell with the sum of digits already figured for it - return to cells with
        #    the highest weights first
        #    1a. Can be accomplished with a supplementary structure of map of pairs. [(X,Y), Z]        
        # 2. Check between every quad/row/column for a valid number, to skip some calcluations
        # 3. Only re-calculate row, quadrant, or column, if the next square you choose is in a different one
        # 4. Issue: can't solve when therea re squares with more than one potential answer. Need to implement
        #    memory for each empty square, so that I can reference all the possible solutions for each square
        #    and adjust them as I go. If a square has a possible answer that no other square in a row, column, or sub has, then that's the answer.

        solved_flag = False
        prev_x = 0
        prev_y = 0
        possibles = {}
        while solved_flag is False:
            # Collect all possible answers
            for y in range(9):
                for x in range(9):
                    if board[y][x] == ".":
                        possibles[(y,x)] = self.getPossibles(board, x, y, prev_x, prev_y)

                    prev_x = x
                    prev_y = y

            # Now do a pass checking for simple solves
            # If there's only one possible answer, just put it into the board
            for k, v in possibles.items():
                if len(v) == 1:
                    board[k[0]][k[1]] = v

            # Now check for more complicated solves using a search
            


            # Check to see if solved yet
            solved_flag = True
            for x in range(9):
                for y in range(9):
                    if board[y][x] == ".":
                        solved_flag = False

        print(board)
    
    def getPossibles(self, board: [List[List[str]]], x, y, prev_x, prev_y) -> None:
        unique_numbers = {}

        for i in range(1,10):
            unique_numbers["{}".format(i)] = False
        
        for k, v in self.checkRow(board, y).items():
            if v == True:
                unique_numbers[k] = v
        
        for k, v in self.checkColumn(board, x).items():
            if v == True:
                unique_numbers[k] = v
        
        for k, v in self.checkSubMatrix(board, x, y).items():
            if v == True:
                unique_numbers[k] = v

        possibles = []
        for k, v in unique_numbers.items():
            if flag == False:  # Aka, if this number isn't already found in the groupings, it's possible
                possibles.insert(v)

        return possibles
    
    def checkRow(self, board: [List[List[str]]], y):
        numbers = {}

        for i in range(9):
            if board[y][i] != ".":
                numbers[board[y][i]] = True

        return numbers
    
    def checkColumn(self, board: [List[List[str]]], x):
        numbers = {}

        for i in range(9):
            if board[i][x] != ".":
                numbers[board[i][x]] = True

        return numbers
    
    def checkSubMatrix(self, board: [List[List[str]]], x, y):
        numbers = {}

        if x >= 0 and x <= 2: 
            if y >= 0 and y <= 2: 
                numbers = self.searchSub(board, 0, 0)
            elif y >= 3 and y <= 5:
                numbers = self.searchSub(board, 0, 3)
            elif y >= 6 and y <= 8:
                numbers = self.searchSub(board, 0, 6)
        elif x >= 3 and x<= 5:
            if y >= 0 and y <= 2:
                numbers = self.searchSub(board, 3, 0)
            elif y >= 3 and y <= 5:  # Center
                numbers = self.searchSub(board, 3, 3)
            elif y >= 6 and y <= 8:  # Bottom Center
                numbers = self.searchSub(board, 3, 6)
        elif x >= 6 and x <= 8:  # Right Side
            if y>= 0 and y <= 2:  # Top Right
                numbers = self.searchSub(board, 6, 0)
            elif y >= 3 and y <= 5:  # Middle Right
                numbers = self.searchSub(board, 6, 3)
            elif y >= 6 and y <= 8:  # Bottom Right
                numbers = self.searchSub(board, 6, 6)

        return numbers
    
    def searchSub(self, board: [List[List[str]]], low_x, low_y):
        numbers = {}

        for y in range(low_y, low_y + 3):
            for x in range(low_x, low_x + 3):
                if board[y][x] != ".":
                    numbers[board[y][x]] = True
        
        return numbers
    
    def checkComplexSolves(self, board: [List[List[str]]], possibles):
        # Build a new list of possibles for the cell through process of elimination
        # If any other cell in a group has the same possible, we eliminate it (A bit of a shortcut)
        # If we are left with one possible, that's the answer
        
