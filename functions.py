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
        self.posVal = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.value == other.value and self.posVal == other.posVal

    def setValue(self, value):
        self.value = value if value else self.posVal[0]
        self.posVal = []
    
    def getValue(self):
        return self.value if self.value != None else 0

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