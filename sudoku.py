class Pair:
    def __init__(self, first, second):
        self.first = first
        self.second = second

class Solution:
    weight_map = {}

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

        self.initWeightMap()
        solved_flag = False
        prev_x = 0
        prev_y = 0
        while solved_flag is False:
            for coords, weight in reversed(self.weight_map.copy().items()):
                x = coords.first
                y = coords.second
                if board[x][y] == ".":
                    board[x][y] = self.attemptSolve(board, x, y, prev_x, prev_y)

                prev_x = x
                prev_y = y

            solved_flag = True
            for coords, weight in self.weight_map.items():
                if weight != "9":
                    solved_flag = False

        print(board)
    
    def attemptSolve(self, board: [List[List[str]]], x, y, prev_x, prev_y) -> None:
        possible_numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        unique_numbers = {}

        for i in range(9):
            unique_numbers[i] = False

        if y != prev_y:
            for num, flag in self.checkRow(board, x).items():
                unique_numbers[num] = flag
        
        if x != prev_x:
            for num, flag in self.checkColumn(board, y).items():
                unique_numbers[num] = flag
        
        if (x >= 3 and prev_x <= 2) or \
           (x >= 6 and prev_x <= 5) or \
           (y >= 3 and prev_y <= 2) or \
           (y >= 6 and prev_y <= 5):
            for num, flag in self.checkSubMatrix(board, x, y).items():
                unique_numbers[num] = flag
        
        count = 0
        for num, flag in unique_numbers.items():
            if flag == True:
                count = count + 1
        self.weight_map[Pair(x,y)] = count

        if count == 8:
            for num, flag in unique_numbers.items():
                if flag == False:
                    return "{}".format(num)

        return "."
    
    def checkRow(self, board: [List[List[str]]], x):
        numbers = {}

        for i in range(9):
            if board[x][i] != ".":
                numbers[board[x][i]] = True

        return numbers
    
    def checkColumn(self, board: [List[List[str]]], y):
        numbers = {}

        for i in range(9):
            if board[i][y] != ".":
                numbers[board[i][y]] = True

        return numbers
    
    def checkSubMatrix(self, board: [List[List[str]]], x, y):
        numbers = {}

        if x >= 0 and x<= 2:  # Left Hand Side
            if y >= 0 and y <= 2:  # Upper Left
                numbers = self.searchSub(board, 0, 0)
            elif y >= 3 and y <= 5:  # Middle Left
                numbers = self.searchSub(board, 0, 3)
            elif y >= 6 and y <= 8:  # Bottom Left
                numbers = self.searchSub(board, 0, 6)
        elif x >= 3 and x<= 5:  # Center
            if y >= 0 and y <= 2:  # Top Center
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

        for i in range(low_x,3):
            for z in range(low_y,3):
                if board[i][z] != ".":
                    numbers[board[i][z]] = True
        
        return numbers

    def initWeightMap(self):
        for x in range(9):
            for y in range(9):
                self.weight_map[Pair(x,y)] = 0
