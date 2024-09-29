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
        # If we find no valid num, do nothing, allow iteration through range of 0-8, but return False if we run out of options (back on first solve index w no answer)

        if self.solve(board, 0, -1) == False:
            print("Error with given input.")
        else:
            print(board)

    def solve(self, board: List[List[str]], index, first_solve):
        if index <= 8:
            y = 0
            x = index
        else:
            y = index // 8
            x = index - (y * 8)
            if index % 8 == 0:
                y = y - 1
                x = 8

        if board[y][x] == ".":
            if first_solve < 0:
                first_solve = index
            for i in range(1, 10):
                valid = True
                # Check Column grouping
                for check_x in range(9):
                    if board[y][check_x] == "{}".format(i):
                        valid = False
                        break
                # Check Row
                for check_y in range(9):
                    if board[check_y][x] == "{}".format(i):
                        valid = False
                        break
                # Check sub group
                for check_x in range((x // 3)*3, (((x // 3)*3) + 3)):
                    for check_y in range((y // 3)*3, (((y // 3)*3) + 3)):
                        if board[check_y][check_x] == "{}".format(i):
                            valid = False
                            break

                if valid == True:
                    board[y][x] = "{}".format(i)  # Save our possily valid answer to the board

                    if y == 8 and x == 8:  # We are at the end, time to exit recursion
                        return True
                    
                    if self.solve(board, index + 1, first_solve) == True:  # Ensure we actually exit the recursion on solve
                        return True

                if valid == False and i == 9:
                    board[y][x] = "."  # No valid answer, clear it

                    if index == first_solve:  # No valid answer for first open cell, bad sudoku, kill it
                        return False
        else:  # Pre-solved cell, skip it
            if y == 8 and x == 8:  # Unless we are at the end, in which case consider it done
                return True
            else:  # Otherwise yeah, skip
                self.solve(board, index + 1, first_solve)
