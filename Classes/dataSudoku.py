from logging import raiseExceptions
from unittest.case import skipIf
from Classes import cell

class DataSudoku():
    def __init__(self, typeData, cellGiven, extraInfo):
        self.typeHandler = TypeHandler()
        if self.typeHandler.validType(typeData):
            self.type = typeData
        else:
            raise Exception("DataType not valid")

        if type(cellGiven) is cell.Cell:
            self.cell = cellGiven
        else:
            raise Exception("The cell adressed is not a Cell")

        self.extraInfo = extraInfo
    

    # ******    type Handle:    ******

class TypeHandler():
    def __init__(self):
        self.switcher = {}
        methods = [f for f in TypeHandler.__dict__ if not f.startswith("__")]
        i = 0
        self.methodsToIgnore = ["validType", "typeConversor"]
        for f in methods:
            if any([f == skipM for skipM in self.methodsToIgnore]):
                continue
            self.switcher[i] = f
            i = i + 1

    def validType(self, typeData) -> bool:
        if not type(typeData) is int:
            return False
        if typeData < 0:
            return False
        if typeData > len(self.switcher):
            return False
        return True
    
    def typeConversor(self, t) -> str:
        retu = self.switcher.get(t, "Data type not found")
        return retu
    
    def therefore(self):
        return 0
    def basic(self):
        return 1
    def unique(self):
        return 2
    def pairs(self):
        return 3
    def delPair(self):
        return 4
    def xWing(self):
        return 5
    def xyWing(self):
        return 6
    def uniqueRectangle(self):
        return 7
    def swordfish(self):
        return 8