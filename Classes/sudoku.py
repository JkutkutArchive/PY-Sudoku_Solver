# import sys
# sys.path.append('.')
from Classes import dataSudoku as dS
from Classes.dataSudoku import TypeHandler as tH
from Classes import cell # Custom Class

class Sudoku():
    def __init__(self, board=None):
        self.board = [[cell.Cell(x, y, self) for y in range(9)] for x in range(9)] # Create the board
        self.remainingCells = set()
        if not board == None:
            self.fillBoard(board)

        self.getRemainingCells(forced=True)
    
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
                else:
                    self.remainingCells.add(self.board[i][j])
    

    # ******    Visualization / getters:    ******
    def toList(self):
        # return [[self.board[i][j] for j in range(9)] for i in range(9)]
        return self.board

    def getRemainingCells(self, forced=False):
        if forced:
            oldCells = set([c for r in self.toList() for c in r])
        else:
            oldCells = self.remainingCells
        self.remainingCells = set()
        for c in oldCells:
            if c.getValue() == 0:
                self.remainingCells.add(c)

        return self.remainingCells

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
    # 1. Scanning in one direction:(basic + unique) (solver_basic())
    # 2. Scanning in two directions:(basic + unique) (solver_basic())
    # 3. Searching for Single Candidates: (unique) (solver_basic())
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
        solutionSudoku = Sudoku(self.toList())
        solutionSudoku.findSolutions(solutions=correctSolution) # Search possible solutions for the current sudoku
        if len(correctSolution) == 0:
            raise Exception("No solutions founded for the current sudoku.")
        if len(correctSolution) > 1: # If more than one possible solutions
            raise Exception("There are more than one possible solution.")

        # If here, there is only one possible solution. Let's find it
        
        iteration = 0
        while True:
            print("Iteration nº" + str(iteration))
            iteration = iteration + 1

            if self.solver_basic():
                continue
            # if self.solver_unique():
            #     continue

            # If here, either we have solve it or we can not solve it
            break
        
        print("exit at iteration nº" + str(iteration - 1))
        return self.validSolution()


    def solver_basic(self):
        '''
        This code tries to find values of the cells using basic scanning techniques.
        '''
        cellWithValueDefined = False
        for cell in self.getRemainingCells(): 
            if cell.getValue() != 0: continue # if during this loop, this cell got it's value defined, go to next one

            # ----------    BASIC   ----------
            values = [] # Values in row, col, 3by3
            typeH = tH()
            tipos = ["row", "col", "3by3"]

            for i in range(3):
                values = self.solver_basic_rowCol3by3(cell, i)
                if len(values) == 0:
                    continue
                else:
                    values = set(values)
                # data = dS.DataSudoku(typeH.basic() + 0.25 * i, values)
                
                cell.removePosVal(values)
                # cell.addData(data)
                if len(cell.getPosVal()) == 1: # We got the value
                    cell.setValue(list(cell.getPosVal())[0])
                    cellWithValueDefined = True
                    break
        return cellWithValueDefined
    
    def solver_basic_rowCol3by3(self, cell, type):
        board = self.toList()
        valuesToRemove = []
        if type == 0 or type == "row":
            for i in range(9): # For each row, col and 3by3
                # Rows (r=cte) -- If not the same cell
                if i != cell.gC():
                    otherValue = board[cell.gR()][i].getValue()
                    # if otherCell has it's value defined and that value is possible value of Cell
                    if otherValue != 0 and (otherValue in cell.getPosVal()):                        
                        # Add the othervalue to the list of values to remove
                        valuesToRemove.append(otherValue)
        
        elif type == 1 or type == "col":
            for i in range(9): # For each col
                # Cols (c=cte) -- If not the same cell
                if i != cell.gR(): 
                    otherValue = board[i][cell.gC()].getValue()
                    if otherValue != 0 and (otherValue in cell.getPosVal()):
                        valuesToRemove.append(otherValue)
        
        elif type == 2 or type == "3by3":    
            for i in range(9): # For each 3by3    
                # 3 by 3 -- If not the same cell
                r = (cell.gR() // 3) * 3 + (i // 3)
                c = (cell.gC() // 3) * 3 + (i % 3)
                if cell.gR() != r or cell.gC() != c: # If not same cell
                    otherValue = board[r][c].getValue()
                    if otherValue != 0 and (otherValue in cell.getPosVal()):
                        valuesToRemove.append(otherValue)
        return valuesToRemove

    def solver_basic_unique(self):
        pass
        # ----------    UNIQUE   ----------
        # unique = [set([i for i in range(1, 10, 1)]) for i in range(3)] # unique row, col, 3by3
        # for i in range(9):
        #     if i != cell.y: # for each piece on the row (x=cte) -- if not same cell
        #         valueToFilter = grid[cell.x][i].getPosVal() # Set with values on other cell
        #         if grid[cell.x][i].getValue() != 0: # If looking at cell with defined value, valueToFilter should be the actual value
        #             valueToFilter = set([grid[cell.x][i].value]) # valueToFilter => numbers here are not unique on our cell
        #         unique[0] = unique[0].difference(valueToFilter) # All common are not unique => del them
        #     if i != cell.x: # for each piece on the Col (y=cte) -- if not same cell
        #         valueToFilter = grid[i][cell.y].getPosVal() # Set with possible values of other cell
        #         if grid[i][cell.y].getValue() != 0: # If looking at cell with defined value, valueToFilter should be the actual value
        #             valueToFilter = set([grid[i][cell.y].value]) # valueToFilter => numbers here are not unique on our cell                
        #         unique[1] = unique[1].difference(valueToFilter) # All common are not unique => del them
        #     x = (cell.x // 3) * 3 + (i // 3)
        #     y = (cell.y // 3) * 3 + (i % 3)
        #     if cell.x != x or cell.y != y:
        #         valueToFilter = grid[x][y].getPosVal() # Set with values on other cell
        #         if grid[x][y].getValue() != 0: # If looking at cell with defined value, valueToFilter should be the actual value
        #             valueToFilter = set([grid[x][y].value]) # valueToFilter => numbers here are not unique on our cell
        #         unique[2] = unique[2].difference(valueToFilter) # All common are not unique => del them

        # if len(unique[0]) == 1: # If only one value is unique -> should be the value
        #     uniqueValue = list(unique[0])[0]
        #     if uniqueValue in cell.getPosVal(): # if this value is a possible one, make it the value of the cell (This should always be true)
        #         cell.addData("unique row", uniqueValue)
        #         cell.setValue(uniqueValue)
        #         discoveryMade = True
        #         continue
        #     else:
        #         print("ERROR at unique row")
        # if len(unique[1]) == 1: # If only one value is unique -> should be the value
        #     uniqueValue = list(unique[1])[0]
        #     if uniqueValue in cell.getPosVal(): # if this value is a possible one, make it the value of the cell (This should always be true)
        #         cell.addData("unique col", uniqueValue)
        #         cell.setValue(uniqueValue)
        #         discoveryMade = True
        #         continue
        #     else:
        #         print("ERROR at unique col")
        # if len(unique[2]) == 1: # If only one value is unique -> should be the value
        #     uniqueValue = list(unique[2])[0]
        #     if uniqueValue in cell.getPosVal(): # if this value is a possible one, make it the value of the cell (This should always be true)
        #         cell.addData("unique 3 by 3", uniqueValue)
        #         cell.setValue(uniqueValue)
        #         discoveryMade = True
        #         continue
        #     else:
        #         print("ERROR at unique 3 by 3")

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
