class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        self.solve(board, 0, -1)

    def solve(self, board: List[List[str]], index, first_solve):
        y = index // 9
        x = index % 9

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
                    
                    if i == 9:
                        board[y][x] = "."  # Before dropping out of this instance, reset the cell
                        return False

                if valid == False and i == 9:
                    board[y][x] = "."  # No valid answer, clear it

                    if index == first_solve:  # No valid answer for first open cell, bad sudoku, kill it
                        return False
        else:  # Pre-solved cell, skip it
            if y == 8 and x == 8:  # Unless we are at the end, in which case consider it done
                return True
            else:  # Otherwise yeah, skip
                if self.solve(board, index + 1, first_solve) == True:
                    return True
