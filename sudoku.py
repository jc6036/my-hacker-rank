class Solution:
    # These vars are used in place of in-line calcluations in a couple of places to speed things up
    answerlist = ["0","1","2","3","4","5","6","7","8","9"]
    min_subgrouplist = [0,3,6]
    max_subgrouplist = [3,6,9]

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        self.solve(board, 0)

    def solve(self, board: List[List[str]], index: int):
        y = index // 9
        x = index % 9

        if board[y][x] == ".":
            for i in range(1, 10):
                if self.isValid(board, y, x, i):
                    board[y][x] = self.answerlist[i]  # Save our possily valid answer to the board

                    if y == 8 and x == 8:  # We are at the end, time to exit recursion                        
                        return True
                    
                    if self.solve(board, index + 1):  # Ensure we actually exit the recursion on solve
                        return True
                    
                    if i == 9:
                        board[y][x] = "."  # Before dropping out of this instance, reset the cell
                        return False
                else:
                    if i == 9:
                        board[y][x] = "."  # No valid answer, clear it
                        return False
        else:  # Pre-solved cell, skip it
            if y == 8 and x == 8:  # Unless we are at the end, in which case consider it done
                return True
            else:  # Otherwise yeah, skip
                if self.solve(board, index + 1) == True:
                    return True
    
    def isValid(self, board: List[List[str]], y: int, x: int, i: int):
        # Check Column grouping
        for check_x in range(9):
            if board[y][check_x] == self.answerlist[i]:
                return False
        # Check Row
        for check_y in range(9):
            if board[check_y][x] == self.answerlist[i]:
                return False

        # Check sub group
        for check_x in range(self.min_subgrouplist[x // 3], self.max_subgrouplist[x // 3]):
            for check_y in range(self.min_subgrouplist[y // 3], self.max_subgrouplist[y // 3]):
                if board[check_y][check_x] == self.answerlist[i]:
                    return False

        return True
