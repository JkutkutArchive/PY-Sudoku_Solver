def printArray(arr, *delimeter):
    print(arrayToString(arr, *delimeter))

def arrayToString(arr, *delimeter):
    d = delimeter if delimeter else "\n"
    end = ""
    s = "["
    for subArr in arr:
        if isinstance(subArr, list):
            if isinstance(subArr[0], list):
                end = "\n"
            s = s + arrayToString(subArr, delimeter)
        else:
            s = s + str(subArr) # This is an element of the array
            d = ","
        s = s + ((d + " " if True else "") + end)
    return s[0:-(1 + len(d))] + "]"

class Cell():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.value = None
        self.posVal = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.data = ["Let's focus on the cell on the position (" + str(x) + ", " + str(y) + ")"]
    
    def __str__(self):
        return str(self.getValue())

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            if self.value == other.value and self.posVal == other.posVal:
                if self.data == other.data:
                    return True

        return False
        # return  and  and 
    
    def __hash__(self):
        return hash(self.x) ^ hash(self.y) # Because there is not 2 cells on the same coord

    def setValue(self, value):
        self.value = value
        self.posVal = None
        if(len(self.data) > 1):
            print(*self.data, sep = "\n")
    
    def getValue(self):
        return self.value if self.value != None else 0

    def getPosVal(self):
        return self.posVal
    
    def setPosVal(self, set):
        self.posVal = set

    def addData(self, dataArr):
        dataToAdd = ""
        print(dataArr[0])
        if "basic" in dataArr[0]:
            tipo = "3 by 3 sector"
            if "row" in dataArr[0]:
                tipo = "row"
            elif "col" in dataArr[0]:
                tipo = "col"
            # ELSE ERROR
            dataToAdd = "If we look at the " + tipo + " containing this cell, we know that this cell can not be " + str(dataArr[1]) + "."
        if "unique" in dataArr[0]:
            tipo = "3 by 3 sector"
            if "row" in dataArr[0]:
                tipo = "row"
            elif "col" in dataArr[0]:
                tipo = "col"
            dataToAdd = "If we look at the " + tipo + " containing this cell, we know that this cell should be " + str(dataArr[1]) + "."
            
        self.data.append(dataToAdd)

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