# import sys
# sys.path.append('.')
from Classes import cell # Custom Class

class Sudoku():
    def __init__(self):
        self.board = [[cell.Cell(x, y) for y in range(9)] for x in range(9)] # Create the board
        self.remainingCells = set()
    
    def fillBoard(self, data):
        super() # Reset the class
        if len(data) != 9 or len(data[0]) != 9:
            raise Exception("The data should be a 9x9 list")

        # If here, the data is correct
        for i in range(9):
            for j in range(9):
                if data[i][j] != 0:
                    self.board[i][j].setValue(data[i][j])
                    # self.board[i][j].setValue(data[i][j], False, cleverCell=False)
                else:
                    self.remainingCells.add(self.board[i][j])


    def validSolution(self, arr):
        '''
        Check if the given sudoku is a valid solution

        Given a 9x9 Cell list, check if it forms a valid sudoku.

        - arr (list): 9x9 Cell list

        Returns:
        boolean: whenever the input forms a valid sudoku

        Note: See the Cell class for more information about who this function works.
        '''
        for i in range(0, 9, 3):#3 by 3:
            for j in range(0, 9, 3):
                suma = 0
                ele = []
                for k in range(3):
                    for l in range(3):
                        suma = suma + arr[k + i][l + j].getValue()
                        ele = ele + [arr[k + i][l + j].getValue()]
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

    def findSolutions(self, data, solutions):
        '''
        Gets the possible solution(s) of the given sudoku.

        Given a 9x9 integer list, all the possible solutions of the input are found using a classic implementation of a recursive algorithm.

        - data (list): 9x9 integer list with the data of the current state of the sudoku
        - solutions (list) Nx9x9 with the solutions found. This works as a "output".
        
        Returns:

        list: the object solutions works as output
        '''
        if data == None: # If no sudoku list given, use current
            data = self.toList()

        for x in range(9): # For each colum
            for y in range(9): # For each row
                if data[x][y] == 0: # If empty cell
                    for val in range(1,10): # For each possible value
                        valid = True # If the current value (val) is viable to be the correct value of the cell(x, y)
                        for i in range(9): # for each neighbour cell (row, col or 3by3)
                            xIndex = (x // 3) * 3 # X 3by3
                            yIndex = (y // 3) * 3 # Y 3by3
                            if data[x][i] == val or data[i][y] == val or data[xIndex + (i // 3)][yIndex + (i % 3)] == val:
                                # If neighbour already has the value val, this value can not be on this cell => val not valid
                                valid = False
                                break
                        if valid: # If the value val may be correct
                            data[x][y] = val # Try to solve the sudoku using this value as correct
                            self.findSolutions(data, solutions)
                            data[x][y] = 0 # if here, the path wasn't good => undo move
                    return # If here, all posible valid combinations have been tested => end execution
        
        ## if here, solution founded
        solutions.append([[ele for ele in row] for row in data]) # Add the current solution to the solution list
    

    # ******    Visualization:    ******
    def toList(self):
        return [[self.board[i][j] for j in range(9)] for i in range(9)]

    def print(self, arr=None, returnAsString=False):
        '''
        Prints with sudoku format the 9x9 list given.

        Given a 9x9 list of integers, prints on console the ASCII representation on the format used by this code.

        - arr (list): 9x9 list with integers

        Please note that the axis are inverted compared with the programming convention.
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
                        r.append(arr[i][j+k].__str__())
                r.append("|")
                stringList.append(" ".join(r))
            stringList.append(separador)

        string = "\n".join(stringList)
        if not returnAsString:
            print(string)
        else:
            return string



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
