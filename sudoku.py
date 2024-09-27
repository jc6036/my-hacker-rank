class Pair:
    def __init__(self, first, second):
        self.first = first
        self.second = second


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        solved_flag = False
        prev_x = 0
        prev_y = 0

        # Collect all possible answers into a map of [y,x][str[]]
        possibles = {}
        for y in range(9):
            for x in range(9):
                if board[y][x] == ".":
                    possibles[(y,x)] = self.getPossibles(board, x, y, prev_x, prev_y)

                prev_x = x
                prev_y = y

        while solved_flag is False:
            # Now analyze each square and perform a process of elimination on possibles for that
            # square. If you get down to 1 possible left, that's the answer.
            # If an answer is found, eliminate that answer from the possibles in that cells groups
            board = self.solvePossibles(board, possibles)

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
            if v == False:  # Aka, if this number isn't already found in the groupings, it's possible
                possibles.append(k)

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
            elif y >= 3 and y <= 5: 
                numbers = self.searchSub(board, 3, 3)
            elif y >= 6 and y <= 8: 
                numbers = self.searchSub(board, 3, 6)
        elif x >= 6 and x <= 8: 
            if y>= 0 and y <= 2: 
                numbers = self.searchSub(board, 6, 0)
            elif y >= 3 and y <= 5:
                numbers = self.searchSub(board, 6, 3)
            elif y >= 6 and y <= 8:
                numbers = self.searchSub(board, 6, 6)

        return numbers
    
    def searchSub(self, board: [List[List[str]]], low_x, low_y):
        numbers = {}

        for y in range(low_y, low_y + 3):
            for x in range(low_x, low_x + 3):
                if board[y][x] != ".":
                    numbers[board[y][x]] = True
        
        return numbers
    
    def solvePossibles(self, board: [List[List[str]]], possibles):
        for y in range(9):
            for x in range(9):
                if board[y][x] == ".":
                    tracker = possibles[(y,x)].copy()

                    # Solve singles first before doing any possibility checkoff
                    if len(tracker) == 1:
                        board[y][x] = tracker[0]
                        possibles.pop((y,x))
                        possibles = self.adjustPossibles(tracker[0], possibles, x, y)
                        continue

                    # Go through process of elminiation to figure out the only number a cell could be within a single group
                    tracker = self.solveGroups(board, tracker, possibles, x, y)

                    if len(tracker) == 1:
                        board[y][x] = tracker[0]
                        possibles.pop((y,x))
                        possibles = self.adjustPossibles(tracker[0], possibles, x, y)

                    # Naked doubles implementation

        return board
    
    def solveGroups(self, board: [List[List[str]]], tracker, possibles, x, y):
        #  Check each group for cells where there is a possible that is not in any other cell in the group - that's the answer
        if len(tracker) > 0:
            rowCheck = self.solveRows(board, tracker.copy(), possibles, y, x)
            if len(rowCheck) == 1:
                return rowCheck
        
            colCheck = self.solveColumns(board, tracker.copy(), possibles, x, y)
            if len(colCheck) == 1:
                return colCheck

            subCheck = self.solveSubMatrix(board, tracker.copy(), possibles, x, y)
            if len(subCheck) == 1:
                return subCheck

        return tracker
    
    def solveRows(self, board: [List[List[str]]], tracker, possibles, y, x):
        for i in range(9):
            if board[y][i] == "." and i != x:
                for v in possibles[(y,i)]:
                    for z in range(len(tracker)):
                        if v == tracker[z]:
                            tracker.pop(z)
                            break
        
        return tracker
    
    def solveColumns(self, board: [List[List[str]]], tracker, possibles, x, y):
        for i in range(9):
            if board[i][x] == "." and i != y:
                for v in possibles[(i,x)]:
                    for z in range(len(tracker)):
                        if v == tracker[z]:
                            tracker.pop(z)
                            break
        
        return tracker
    
    def solveSubMatrix(self, board, tracker, possibles, x, y):
        if x >= 0 and x <= 2: 
            if y >= 0 and y <= 2: 
                tracker = self.solveSub(board, tracker, possibles, 0, 0, x, y)
            elif y >= 3 and y <= 5:
                tracker = self.solveSub(board, tracker, possibles, 0, 3, x, y)
            elif y >= 6 and y <= 8:
                tracker = self.solveSub(board, tracker, possibles, 0, 6, x, y)
        elif x >= 3 and x<= 5:
            if y >= 0 and y <= 2:
                tracker = self.solveSub(board, tracker, possibles, 3, 0, x, y)
            elif y >= 3 and y <= 5: 
                tracker = self.solveSub(board, tracker, possibles, 3, 3, x, y)
            elif y >= 6 and y <= 8: 
                tracker = self.solveSub(board, tracker, possibles, 3, 6, x, y)
        elif x >= 6 and x <= 8: 
            if y>= 0 and y <= 2: 
                tracker = self.solveSub(board, tracker, possibles, 6, 0, x, y)
            elif y >= 3 and y <= 5:
                tracker = self.solveSub(board, tracker, possibles, 6, 3, x, y)
            elif y >= 6 and y <= 8:
                tracker = self.solveSub(board, tracker, possibles, 6, 6, x, y)
        
        return tracker
    
    def solveSub(self, board, tracker, possibles, low_x, low_y, x, y):
        for arr_y in range(low_y + 3):
            for arr_x in range(low_x + 3):
                if board[arr_y][arr_x] == "." and not (arr_y == y and arr_x == x):
                    for i in possibles[(arr_y,arr_x)]:
                        for z in range(len(tracker)):
                            if i == tracker[z]:
                                tracker.pop(z)
                                break
        
        return tracker
    
    def adjustPossibles(self, answer, possibles, x, y):
        for k, v in possibles.items():
            if k[0] == y or k[1] == x:
                for i in range(len(v)):                    
                    if v[i] == answer:
                        v.pop(i)
                        break
            
            # God I HATE this - fix immediately after its working
            if (k[0] >= 0 and k[0] <= 2) and (y >= 0 and y <= 2):
                if(k[1] >= 0 and k[1] <= 2) and (x >= 0 and x <= 2):
                    for i in range(len(v)):
                        if v[i] == answer:
                            v.pop(i)
                            break
                elif(k[1] >= 3 and k[1] <= 5) and (x >= 3 and x <= 5):
                    for i in range(len(v)):
                        if v[i] == answer:
                            v.pop(i)
                            break
                elif(k[1] >= 6 and k[1] <= 8) and (x >= 6 and x <= 8):
                    for i in range(len(v)):
                        if v[i] == answer:
                            v.pop(i)
                            break
            elif (k[0] >= 3 and k[0] <= 5) and (y >= 3 and y <= 5):
                if(k[1] >= 0 and k[1] <= 2) and (x >= 0 and x <= 2):
                    for i in range(len(v)):
                        if v[i] == answer:
                            v.pop(i)
                            break
                elif(k[1] >= 3 and k[1] <= 5) and (x >= 3 and x <= 5):
                    for i in range(len(v)):
                        if v[i] == answer:
                            v.pop(i)
                            break
                elif(k[1] >= 6 and k[1] <= 8) and (x >= 6 and x <= 8):
                    for i in range(len(v)):
                        if v[i] == answer:
                            v.pop(i)
                            break
            elif (k[0] >= 6 and k[0] <= 8) and (y >= 6 and y <= 8):
                if(k[1] >= 0 and k[1] <= 2) and (x >= 0 and x <= 2):
                    for i in range(len(v)):
                        if v[i] == answer:
                            v.pop(i)
                            break
                elif(k[1] >= 3 and k[1] <= 5) and (x >= 3 and x <= 5):
                    for i in range(len(v)):
                        if v[i] == answer:
                            v.pop(i)
                            break
                elif(k[1] >= 6 and k[1] <= 8) and (x >= 6 and x <= 8):
                    for i in range(len(v)):
                        if v[i] == answer:
                            v.pop(i)
                            break

        return possibles
