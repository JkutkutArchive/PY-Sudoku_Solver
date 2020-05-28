sol = []

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


#   --------------------------------    CLASSES     --------------------------------
class Cell():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.value = None
        self.posVal = set([i for i in range(1, 10, 1)])
        self.data = []
    
    def __str__(self):
        return str(self.getValue())

    def __eq__(self, other):
        if self.getPos() != other.getPos(): # If different coordinates
            return False # In theory, when well used this class, this should be the only condition used
        if self.value != other.value and self.getPosVal() != other.getPosVal():
            return False
        if self.data != other.data:
            return False
        return True 
    
    def __hash__(self):
        return hash(self.x) ^ hash(self.y) # Because there is not 2 cells on the same coord

    def setValue(self, value, *noPrint):
        self.value = value
        self.posVal = None
        self.addData(["therefore"])
        if not noPrint:
            print(*self.dataToText(), sep = "\n")
            if self.value == sol[self.x][self.y]:
                print("\n" + "CORRECT".center(40) + "\n")
            else:
                import main
                main.gameRunning = False
                print("\n" + ("ERROR, NOT CORRECT VALUE -> " + str(sol[self.x][self.y])).center(40) + "\n")
    
    def getValue(self):
        return self.value if self.value != None else 0

    def setPosVal(self, set):
        self.posVal = set

    def getPosVal(self):
        return self.posVal

    def getPos(self):
        return (self.x, self.y)

    def addData(self, *dataArr):
        key = dataArr[0]
        if "basic" in key or "pairs one cell" == key: # If basic type or pair, can be merged to the previous data
            for d in self.data: # Search for it
                if key == d[0]: # If exacly the same data type
                    if "pairs one cell" == key and d[1] == dataArr[1]:
                        return
                    elif "basic" in key: # Basic type
                        d[1].extend(dataArr[1]) # Update the previous data (Basic: row, col, 3by3)
                        return # end Execution
        self.data.append(dataArr) # If not founded or not basic, add it as new data
    
    def dataToText(self):
        s = ["Let's focus on the cell on the position (" + str(self.x) + ", " + str(self.y) + ")"]
        for d in self.data:
            dataToAdd = ""
            if "therefore" in d[0]:
                dataToAdd = "Therefore, the value of this cell is " + str(self.value) + "."
            elif "basic" in d[0]:
                tipo = d[0][6:]
                dataToAdd = "If we look at the " + tipo + " on this cell, this cell can not be " + str(d[1]) + "."
            elif "unique" in d[0]:
                tipo = "3 by 3 sector"
                if "row" in d[0]:
                    tipo = "row"
                elif "col" in d[0]:
                    tipo = "col"
                dataToAdd = "If we look at the " + tipo + " containing this cell, we know that this cell should be " + str(d[1]) + "."
            elif "pairs" in d[0]:
                if "one" in d[0]:
                    if "val" in d[0]:
                        dataToAdd = "Having on mind that one of the cells " + str(d[1].getPos()) + " and " + str(d[2].getPos()) + " is a " + str(d[3]) + ", this cell can not be " + str(d[3]) + "."
                    elif "cell" in d[0]:
                        dataToAdd = "This cell and " + str(d[1].getPos()) + " are linked. Value " + str(d[2]) + " is on one of these 2 cells."
                if "two" in d[0]:
                    dataToAdd = "If we take a look, this and the " + str(d[1].getPos()) + " cell are eather " + str(d[2]) + ". Both cells can only be these values."
            s.append(dataToAdd)
        return s

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