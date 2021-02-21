# import sys
# sys.path.append('.')
from Classes import cell # Custom Class

class Sudoku():
    def __init__(self, board=None):
        self.board = [[cell.Cell(x, y) for y in range(9)] for x in range(9)] # Create the board
        self.remainingCells = set()
        if not board == None:
            self.fillBoard(board)
    
    def fillBoard(self, data):
        '''
        Fills the board with the elements given.

        data (list): List of integers or Cells (Or even both!) with the values desired. If some value = 0, the cell will be tagged as a remaining cell.
        '''
        if len(data) != 9 or len(data[0]) != 9:
            raise Exception("The data should be a 9x9 list")

        # If here, the data is correct
        for i in range(9):
            for j in range(9):
                if data[i][j] != 0:
                    if type(data[i][j]) is int:
                        self.board[i][j].setValue(data[i][j])
                    elif type(data[i][j]) is cell.Cell:
                        self.board[i][j].setValue(data[i][j].getValue())
                    # self.board[i][j].setValue(data[i][j], False, cleverCell=False)
                else:
                    self.remainingCells.add(self.board[i][j])
    

    # ******    Visualization / getters:    ******
    def toList(self):
        # return [[self.board[i][j] for j in range(9)] for i in range(9)]
        return self.board

    def getRemainingCells(self):
        return self.remainingCells()

    def print(self, arr=None, returnAsString=False):
        '''
        Prints with sudoku format the 9x9 list given.

        Given a 9x9 list of integers, prints on console the ASCII representation on the format used by this code.

        - arr (list): (optional) 9x9 list with integers or Cells.
        - returnAsString (boolean): (optional) if true: instead of printing, the string is returned.
        
        Please note that the axis are inverted compared with the programming convention.

        Returns:

        If returnAsString = True, the output is the string that should be printed.
        '''
        if arr == None: # If no list given
            arr = self.toList() # Use the objects list
        stringList = list()

        # First line
        r = []
        for j in range(0, 7, 3):
            r.append("".join([str(i+j) + " " for i in range(3)]))
        stringList.append("  C " + "  ".join(r))

        # Rest of the lines
        separador = "".join(["".join(["+"] + ["-" for i in range(7)]) for j in range(3)] + ["+"]) # divider
        stringList.append("R " + separador) # Start

        separador = "  " + separador

        for s in range(0, 9, 3): # For each sector
            for i in range(3): #For each row in each sector
                r = [str(i+s)] #Here the string of each line will be generated
                for j in range(0, 7, 3): # for each 3 numbers on a row-sector
                    r.append("|")
                    for k in range(3): # For each number in a row-sector
                        r.append(arr[i + s][j+k].__str__())
                r.append("|")
                stringList.append(" ".join(r))
            stringList.append(separador)

        string = "\n".join(stringList)
        if not returnAsString:
            print(string)
        else:
            return string


    # ******    Solver:    ******

    # https://www.conceptispuzzles.com/index.aspx?uri=puzzle/sudoku/techniques

    # -Scanning techniques
    # 1. Scanning in one direction:(basic + unique)
    # 2. Scanning in two directions:(basic + unique)
    # 3. Searching for Single Candidates: (unique)
    # 4. Eliminating numbers from rows, columns and boxes: (pairs)
    # 5. Searching for missing numbers in rows and columns: (basic)

    # -Analyzing techniques:
    # 1. Eliminating squares using Naked Pairs in a box (pairs two values)
    # 2. Eliminating squares using Naked Pairs in rows and columns (pairs two values)
    # 3. Eliminating squares using Hidden Pairs in rows and columns (unique)
    # 4. Eliminating squares using X-Wing (X-Wing algo)


    # https://www.learn-sudoku.com/advanced-techniques.html

    # 1. X-Wing (X-Wing algo)
    # 2. XY Wing (XY-Wing algo) 
    # 3. Unique Rectangle (Unique rectangle algo) 
    # 4. Sworldfish (swordfish)
    # 5. Extremely advanced techniques (??) 

    # - Triplets and Quads (onProgress)

    def findSolutions(self, solutions, arr=None):
        '''
        Gets the possible solution(s) of the given sudoku.

        Given a 9x9 integer list, all the possible solutions of the input are found using a classic implementation of a recursive algorithm.

        - arr (list): 9x9 integer list with the data of the current state of the sudoku
        - solutions (list) Nx9x9 with the solutions found. This works as a "output".
        
        Returns:

        list: the object solutions works as output
        '''
        if arr == None: # If no sudoku list given, use current
            arr = self.toList()
        # if type(arr[0][0]) is int:
        #     a = Sudoku(arr)
        #     arr = a.toList()

        for c in range(9): # For each colum
            for r in range(9): # For each row
                if arr[r][c] == 0: # If empty cell
                    for val in range(1,10): # For each possible value
                        valid = True # If the current value (val) is viable to be the correct value of the cell(x, y)
                        for i in range(9): # for each neighbour cell (row, col or 3by3)
                            rIndex = (r // 3) * 3 # R 3by3
                            cIndex = (c // 3) * 3 # C 3by3
                            if arr[r][i] == val or arr[i][c] == val or arr[rIndex + (i // 3)][cIndex + (i % 3)] == val:
                                # If neighbour already has the value val, this value can not be on this cell => val not valid
                                valid = False
                                break
                        if valid: # If the value val may be correct
                            arr[r][c].setValue(val, force=True) # Try to solve the sudoku using this value as correct
                            self.findSolutions(solutions, arr)
                            arr[r][c].setValue(0, force=True) # if here, the path wasn't good => undo move
                    return # If here, all posible valid combinations have been tested => end execution
        
        ## if here, solution founded
        newSolution = Sudoku(arr) # Create a new Sudoku object to clone the solution to a new object (current will be modified)
        if newSolution.validSolution(): # Check if solution founded is correct
            solutions.append(newSolution.toList()) # Add the current solution to the solution list

    def validSolution(self, arr=None):
        '''
        Check if the given sudoku is a valid solution

        Given a 9x9 Cell list, check if it forms a valid sudoku.

        - arr (list): (optional) 9x9 list (integer of Cell). If None given, the board from the object is used.

        Returns:
        boolean: whenever the input forms a valid sudoku

        Note: See the Cell class for more information about who this function works.
        '''
        if arr == None:
            arr = self.toList()
        elif type(arr[0][0]) is int:
            a = Sudoku(arr)
            arr = a.toList()
        elif any([not type(arr[i][j]) is cell.Cell for i in range(9) for j in range(9)]):
            raise Exception("The list given must be a list of Cells")

        for i in range(0, 9, 3):#3 by 3:
            for j in range(0, 9, 3):
                suma = 0
                for k in range(3):
                    for l in range(3):
                        suma = suma + arr[i + k][j + l].getValue()
                if(suma != 45):
                    return False
        for l in range(9):#lines:
            solCc = 0
            solCr = 0
            for i in range(9):
                solCc = solCc + arr[i][l].getValue()
                solCr = solCr + arr[l][i].getValue()
            if solCc != 45 or solCr != 45:
                return False
        return True

    def findSolutionWithSteps(self):
        correctSolution = []
        self.findSolutions(solutions=correctSolution) # Search possible solutions for the current sudoku
        print("hey!")
        if len(correctSolution) == 0:
            print("ups1")
            raise Exception("No solutions founded for the current sudoku.")
        if len(correctSolution) > 1: # If more than one possible solutions
            print("ups2")
            raise Exception("There are more than one possible solution.")

        # If here, there is only one possible solution. Let's find it



    def solver_basic(self):
        for cell in self.getRemainingCells(): # Values in row, col, 3by3
            if cell.getValue() != 0: continue # if during this loop, this cell got it's value defined, go to next one

            
    


if __name__ == "__main__":
    a = Sudoku()
    a.fillBoard([])
    data = [ # hard
        [0, 0, 7, 0, 0, 0, 3, 0, 2],
        [2, 0, 0, 0, 0, 5, 0, 1, 0],
        [0, 0, 0, 8, 0, 1, 4, 0, 0],
        [0, 1, 0, 0, 9, 6, 0, 0, 8],
        [7, 6, 0, 0, 0, 0, 0, 4, 9],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 3, 0, 0, 0],
        [8, 0, 1, 0, 6, 0, 0, 0, 0],
        [0, 0, 0, 7, 0, 0, 0, 6, 3]
    ]
    a.fillBoard(data)
