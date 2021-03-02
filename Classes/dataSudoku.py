from Classes import cell

class DataSudoku():
    def __init__(self, typeData, cellGiven, details):
        self.typeHandler = TypeHandler()
        if self.typeHandler.validType(typeData):
            self.type = typeData
        else:
            raise Exception("DataType not valid")

        if type(cellGiven) is cell.Cell:
            self.cell = cellGiven
        else:
            raise Exception("The cell adressed is not a Cell")

        self.details = details
    

    # ******    type Handle:    ******

class TypeHandler():
    def __init__(self):
        self.switcher = [
            "therefore",
            "basic",
            "unique",
            "pairs",
            "delPairs",
            "delPair",
            "xWing",
            "xyWing",
            "uniqueRectangle",
            "swordfish"
        ]
        for i in range(len(self.switcher)):
            exec("self." + self.switcher[i] + " = lambda: " + str(i))


    def validType(self, typeData) -> bool:
        if not type(typeData) is int:
            return False
        if typeData < 0:
            return False
        if typeData > len(self.switcher):
            return False
        return True
    
    def typeConversor(self, t) -> str:
        if type(t) is str:
            for i in range(len(self.switcher)):
                if self.switcher[i] == t:
                    return i
            return "Data type not found"
        elif self.validType(t):
            return self.switcher[t]
        else:    
            return "Data type not found"