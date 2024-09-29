class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Backtracking brute force algorithm
        # Go to each cell on the board
        # For every empty cell, set empty cell flag and attempt to solve
        # Solve - Insert a number starting from 1 to 9, until we find a valid number
        # If we find a valid num, recurse call solve(index + 1) - if on last cell, return True
        # If we find no valid num, return False - this will totally exit the recursion on a bad puzzle


        for y in range(9):
            for x in range(9):

    def solve(self, board: List[List[str]], index, first_solve):
        if index <= 8:
            y = 0
            x = index
        else:
            y = y // 8
            x = index - (y * 8)

        empty_cell = False
        if board[y][x] == ".":
            empty_cell = True
            valid = True
            if first_solve < 0:
                first_solve = index
            for i in range(9):
                # Check Column grouping
                for check_x in range(9):
                    if board[y][check_x] == "{}".format(i):
                        valid = False
                # Check Row
                for check_y in range(9):
                    if board[check_y][x] == "{}".format(i):
                        valid = False
                # Check sub group
                for check_x in range(x // 3, ((x // 3) + 3)):
                    for check_y in range(y // 3, ((y // 3) + 3)):
                        if board[check_y][check_x] == "{}".format(i):
                            valid = False
        
        if empty_cell == False:
            solve(board, index + 1, first_solve)
            
        if valid == True:
            if y = 8 and x = 8:
                return True

            solve(board, index + 1, first_solve)

        if valid == False:
            return False
