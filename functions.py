import latexToPDF as pdf
sol = []
grid = []

def printSudoku(arr):
    print(*["  Y "] + [str(i) + " " for i in range(3)] + ["  "] + [str(3+i) + " " for i in range(3)] + ["  "] + [str(6+i) + " " for i in range(3)], sep = "")
    print(*["X +"] + ["-" for i in range(23)] + ["+"], sep = "")#start

    for i in range(3): #rows
        t = [str(i) + " |"] + arr[i][0:3] + ["|"] + arr[i][3:6] + ["|"] + arr[i][6:9] + ["|"]
        print(*t, sep = " ")

    print(*["  "]+["".join(["+"] + ["-" for i in range(7)]) for j in range(3)] + ["+"], sep = "")#3 by 3 separators

    for i in range(3, 6): #rows
        t = [str(i) + " |"] + arr[i][0:3] + ["|"] + arr[i][3:6] + ["|"] + arr[i][6:9] + ["|"]
        print(*t, sep = " ")

    print(*["  "]+["".join(["+"] + ["-" for i in range(7)]) for j in range(3)] + ["+"], sep = "")#3 by 3 separators

    for i in range(6, 9): #rows
        t = [str(i) + " |"] + arr[i][0:3] + ["|"] + arr[i][3:6] + ["|"] + arr[i][6:9] + ["|"]
        print(*t, sep = " ")

    print(*["  +"] + ["-" for i in range(23)] + ["+"], sep = "")#end

def sudokuSolution(data, solutions):
    for x in range(9):
        for y in range(9):
            if data[x][y] == 0:
                for val in range(1,10):
                    valid = True
                    for i in range(9):
                        xIndex = (x // 3) * 3
                        yIndex = (y // 3) * 3
                        if data[x][i] == val or data[i][y] == val or data[xIndex + (i // 3)][yIndex + (i % 3)] == val:
                            valid = False
                            break
                    if valid:
                        data[x][y] = val
                        sudokuSolution(data, solutions)
                        data[x][y] = 0 #if here, the path wasn't good => undo move
                return
    ## if here, solution founded
    solutions.append([[ele for ele in row] for row in data])

# Check if the given sudoku is a valid solution
def checkSol(arr):
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

## Prints the status of the arguments (errors)
def pError(**kwargs):
    print("***ERROR***".center(30))
    print(kwargs)
    print("***END ERROR***".center(30))

#   --------------------------------    METHODS     --------------------------------
def tellCells(cell, cleverCell=True): # When a cell defines its value, this function is called to update the rest
    value = cell.getValue()
    for i in range(9):
        if i != cell.y: # Row
            c = grid[cell.x][i]
            if c.getValue() != value and value in c.getPosVal():
                c.addData("basic row", [value])
                c.removePosVal(value, cleverCell=cleverCell)
        if i != cell.x: # Col
            c = grid[i][cell.y]
            if c.getValue() != value and value in c.getPosVal():
                c.addData("basic col", [value])
                c.removePosVal(value, cleverCell=cleverCell)
        x = (cell.x // 3) * 3 + (i // 3)
        y = (cell.y // 3) * 3 + (i % 3)
        if i != cell.x or i != cell.y: # 3by3
            c = grid[x][y]
            if c.getValue() != value and value in c.getPosVal():
                c.addData("basic 3 by 3", [value])
                c.removePosVal(value, cleverCell=cleverCell)
        

#   --------------------------------    CLASSES     --------------------------------
class Cell():
    def __init__(self, x, y):
        self.x = x # Position on the grid (row)
        self.y = y # Position on the grid (element in row/column)
        self.value = None # Value of the cell (Now, undefined)
        self.posVal = set([i for i in range(1, 10, 1)]) # Possible values of the cell
        self.pairs = set() # Set with tuple with the linked cell and the value: "(<Cell>, <Value>)"
        self.data = [] # Here all the conclusions made by the algo will be stored here to dispay it later
    
    def __str__(self):
        return str(self.getValue()) # Just print the value of the cell calling the method "getValue()"

    def cellToString(self):
        return "Cell " + str(self.getPos()) + \
            "\n - Value: " + str(self.getValue()) + \
            "\n - PosVal: " + str(self.getPosVal()) + \
            "\n - Pairs: " + "".join(["\n    - Pair with " + str(p[0].getPos()) + " -> " + str(p[1]) for p in self.pairs]) + \
            "\n - Data: " + "".join(["\n    - " + str(d) for d in self.dataToText()])

    def __eq__(self, other, exactComparation=False): # Enable us to compare it to other cells or to integers by the value
        if type(other) == int: # if comparing to an integer
            return self.getValue() == other # Return if the values are the same
        
        if self.getPos() != other.getPos(): # If cells on different coordinates
            return False # In theory, when well used this class, this should be the only condition used (position unique for each cell)
        
        if exactComparation: # If selected, the fucntion will make a full comparantion
            # (If used this class correctly, this next ifs should never be necessary)
            if self.value != other.value and self.getPosVal() != other.getPosVal(): # If different values on those variables
                return False
            if self.data != other.data: # If the data stored is different
                return False
        return True # If here, they are exacly equal
    
    def __hash__(self): # Enables to generate a hash to use this class on sets
        return hash(self.x) ^ hash(self.y) # This make the hash unique because there is not 2 cells on the same coordinates

    # ******    GETTERS AND SETTERS:    ******
    def setValue(self, value, printData=True, cleverCell=True):
        if self.getValue() != 0: return # if already called, do not continue
        # if value != sol[self.x][self.y]: # If not correct value
        #     raise Exception(("ERROR, NOT CORRECT VALUE -> Cell" + str(self.getPos()) + " is not " + str(value) + ", is " + str(sol[self.x][self.y])).center(40))
        self.value = value # Set the value of the cell to the one given 
        self.posVal.clear() # Therefore, there are no possible values left => clear the set of possible values
        self.addData("therefore") # Add to the data array the data to say that the value is the given 
        if printData: # If selected to print the data
            d = self.dataToText() # Data on text format
            print(*[""] + d, sep = "\n") # Print all the data
            pdf.printDataOnLaTeX(d) # Add this data to the pdf
        self.tellPairs() # Notify all linked cells that the value has been defined
        tellCells(self, cleverCell=cleverCell) # update the cells on the grid of this change in value
        if value != sol[self.x][self.y]: # If not correct value
            print("\n\n\n ERROR: \n"+self.cellToString())
            raise Exception(("ERROR, NOT CORRECT VALUE -> Cell" + str(self.getPos()) + " is not " + str(value) + ", is " + str(sol[self.x][self.y])).center(40))
                
    def getValue(self): # Returns the value of the cell. If not defined, return 0
        return self.value if self.value != None else 0

    def setPosVal(self, set): # Redefine the possible values of the cells
        self.posVal = set # Save the given set as the possible values (Warning, set not copied)

    def getPosVal(self): # Returns the set with the possible values.
        return self.posVal

    def removePosVal(self, value, cleverCell=True):
        self.getPosVal().discard(value) # this cell can no longer be the value "value"
        for p in self.pairs: # for each pair in this cell (format of p: tuple(cell, value))
            if p[1] == value: # If there is a pair with this value => the mate should be this value
                p[0].addData("delPair set value", self.getPos(), value) # Add the data
                p[0].setValue(value) # Set the value
                break
        if cleverCell and len(self.getPosVal()) == 1: # If cleverCell on and only one possible value
            self.setValue(next(iter(self.getPosVal())))


    def setPairs(self, ps):
        self.pairs = ps

    def getPairs(self):
        return self.pairs

    def getPos(self): # returns a tuple with the coordinates (row, column)
        return (self.x, self.y)

    # ******    PAIRS:    ******
    def addPair(self, other, value): # Add the new pair on a tuple with the value in common
        self.getPairs().add((other, value)) # If already in, nothing happends

    def tellPairs(self): # when value is defined, this method is called to tell all pairs this event has occured
        for p in self.getPairs(): # for each pair-mate tuple
            # print(p)
            p[0].delPair(self, self.value) # Tell the mate pair there is no pair relation anymore
        self.pairs.clear() # Once done, do not store them anymore
    
    def delPair(self, matePair, mateValue): # Executed when matePair gets its value defined
        if self.getValue() != 0: return # If already with value, do nothing

        # print(str(self.getPosVal()) + " --- " + str(mateValue))
        self.getPosVal().discard(mateValue) # If linked and mateValue now defined => this cell can not be mateValue
        self.addData("delPair remove value", matePair.getPos(), mateValue) # The cell (matePair.pos) has now the value v1 and these cells are linked, so this cell can not be v1
        # self.pairs.discard((matePair, mateValue))
        for p in self.getPairs(): # for each mate linked with this cell
            cell = p[0] # mate cell linked
            v = p[1] # value that make the link
            if cell == matePair: continue # Skip the pair
            if v == mateValue: # if "cell" has same value-relation as mate (the one who called this) => "cell" has that value
                cell.addData("delPair set value", self.getPos(), mateValue) # The cell (self.pos) is no longer matevalue and these cells were linked, so the value of this cell is matevalue
                cell.setValue(v) # Set the value
            if len(self.pairs) == 0: return # If setting the value of cell makes me change my value. Stop

        if len(self.getPosVal()) == 1: # We have the value
            self.setValue(next(iter(self.getPosVal())))






    # ******    DATA:    ******
    def addData(self, *dataArr): # Add data. If already added, do not duplicate the info
        if dataArr not in self.data: # If this data not added yet
            key = dataArr[0] # This first element represents the type of data
            if "basic" in key: # If key is the type "basic": row, col or 3by3
                for d in self.data: # Search for it
                    if key == d[0]: # If data on d has exacly the same data type
                        d[1].extend(dataArr[1]) # Update the previous data (Basic: row, col, 3by3)
                        return # end Execution
            
            elif "cell" in key: # "pair one cell" is eq to: "pair row cell" and "pair col cell"
                for d in self.data:
                    if "cell" in d[0] and dataArr[1:] == d[1:]: # If the data entered now has already been added
                        return # Do not added
            self.data.append(dataArr) # If not founded or not basic, add it as new data

    def dataToText(self): # Return a array of strings with the data ready to be red.
        s = ["Let's focus on the cell on the position " + str(self.getPos())] # Start by giving the position of the cell
        for d in self.data: # For each data piece stored on the array
            key = d[0] # Type of data on this piece d
            dataToAdd = "" # Here the data of this piece will be stored based on the key (then added to s)
            if "therefore" == key:
                dataToAdd = "Therefore, the value of this cell is " + str(self.value)
            elif "basic" in key: # Format: ["basic <TYPE>", <VALUE>]
                tipo = key[6:] # only enter the <TYPE>
                dataToAdd = "If we look at the " + tipo + " on this cell, this cell can not be " + str(d[1]) + "."
            elif "unique" in key: # Format: ["unique <TYPE>", <VALUE>]
                tipo = key[6:] # only enter the <TYPE>
                dataToAdd = "If we look at the " + tipo + " containing this cell, we know that this cell should be " + str(d[1]) + " because no one this " + tipo + " can be this value."
            elif "pairs" in key:
                if "two" in key:
                    dataToAdd = "If we take a look, this and the " + str(d[1].getPos()) + " cell are eather " + str(d[2]) + ". Both cells can only be these values."
                # elif "one" in key or "row" in key or "col" in key: # If type of pair: 3by3, row or col
                else: # If type of pair: 3by3, row or col
                    if "val" in key:
                        dataToAdd = "Having on mind that one of the cells " + str(d[1].getPos()) + " and " + str(d[2].getPos()) + " is a " + str(d[3]) + ", this cell can not be " + str(d[3]) + "."
                    elif "cell" in key:
                        dataToAdd = "This cell and " + str(d[1].getPos()) + " are linked. Value " + str(d[2]) + " is on one of these 2 cells."
                
            elif "delPair" in key:
                if "remove" in key:
                    dataToAdd = "The cell " + str(d[1]) + " has now the value " + str(d[2]) + " and these cells are linked, so this cell can not be " + str(d[2])
                elif "set" in key:
                    dataToAdd = "The cell " + str(d[1]) + " is no longer " + str(d[2]) + " and these cells were linked, so the value of this cell is " + str(d[2])

            s.append(dataToAdd) # Add it to the array with the rest
        return s # Return all the data on text format

class color():
    def __init__(self):
        self.BG = (25, 25, 25)
        self.GRID = (128, 128, 128)
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.DBLUE = (0, 153, 255) # L'
        self.LBLUE = (102, 255, 255) # Straight
        self.PURPLE = (153, 51, 255) # T
        self.GREEN = (102, 255, 102) #skew
        self.YELLOW = (255, 255, 102) #square
        self.ORANGE = (255, 102, 0) # L
        self.RED = (255, 80, 80) # Skew'