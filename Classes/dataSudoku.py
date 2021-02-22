from logging import raiseExceptions
from unittest.case import skipIf
from Classes import cell

class DataSudoku():
    def __init__(self, typeData, cellGiven, extraInfo):
        if TypeHandler().validType(typeData):
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
        # self.switcher = {
        #     1: "therefore",
        #     2: "basic",
        #     3: "unique",
        #     4: "pairs",
        #     5: "delPairs",
        #     6: "X-Wing",
        #     7: "XY-Wing",
        #     8: "uniqueRectangle",
        #     9: "swordfish"
        # }
        methods = [f for f in TypeHandler.__dict__ if not f.startswith("__")]
        i = 0
        self.methodsToIgnore = ["vaidType", "typeConversor"]
        for f in methods:
            if any([f == skipM for skipM in self.methodsToIgnore]):
                continue
            self.switcher[i] = f
            i = i + 1

    def validType(self, typeData) -> bool:
        return typeData <= len(self.switcher)
    
    def typeConversor(self, t) -> str:
        retu = self.switcher.get(t, "Data type not found")
        return retu
    
    def therefore(self):
        return 1
    def basic(self):
        return 2
    def unique(self):
        return 3
    def pairs(self):
        return 4
    def delPair(self):
        return 5
    def xWing(self):
        return 6
    def xyWing(self):
        return 7
    def uniqueRectangle(self):
        return 8
    def swordfish(self):
        return 9