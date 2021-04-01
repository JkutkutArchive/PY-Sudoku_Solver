import Classes.typeHandler
import Classes.cell

# ["therefore"]
# ["basic <TYPE>", <VALUE>]
# ["unique <TYPE>", <VALUE>]
# ["pairs (two) <TYPE>", MATECELL, <VALUE>]
# ["delPair <TYPE> value", <MATECELL.pos()>, <VALUE>]
# ["X-Wing <TYPE>", p1, p2, value]; <TYPE>=[row, col]
# ["XY-Wing <TYPE>", [c1, c2, c3], [v1, v2, v3]]
# ["UniqueRectangle", [c1, c2, c3], <VALUE>]
# ["Swordfish <TYPE>", result, coordinates, v]

# [                <TYPE>, <CELLs>, <VALUEs>]
# [           "therefore",    NONE,     NONE]
# [     "basic <SUBTYPE>",    NONE, <VALUEs>]
# [    "unique <SUBTYPE>",    NONE, <VALUEs>]
# [     "pairs <SUBTYPE>", <CELLs>, <VALUEs>]
# [           "Pairs_two",  <CELL>,  <VALUE>]
# [   "delPair_set_value",  <CELL>,  <VALUE>]
# ["delPair_remove_value",  <CELL>,  <VALUE>]
# [    "xWing <SUBTYPE>", <CELLs>,  <VALUE>]; <SUBTYPE>=[row, col]
# [             "xyWing", <CELLs>, <VALUEs>]
# [     "UniqueRectangle", <CELLs>,  <VALUE>]
# [ "swordfish <SUBTYPE>", <CELLs>,  <VALUE>]; <SUBTYPE>=[row, col]


class DataSudoku():
    def __init__(self, typeData, cellsGiven=None, values=None, subType=None):
        self.typeHandler = Classes.typeHandler.TypeHandler()
        
        if self.typeHandler.validType(typeData):
            self.type = typeData
        else:
            raise Exception("DataType not valid")

        if subType != None:
            if subType > 0 and subType < 1 and self.typeHandler.validType(self.type + subType):
                self.subType = subType
            else:
                raise Exception("Subtype not valid")
        else:
            self.subType = 0

        validInput = lambda inputed, specialType: \
            any([type(inputed) is posType for posType in [specialType, list, set, type(None)]])

        if validInput(cellsGiven, Classes.cell.Cell):
            self.CELLs = cellsGiven
        else:
            raise Exception("Cells given not valid")
            # raise Exception("Cells given not valid:\n" + str(cellsGiven))

        if validInput(values, int):
            self.VALUEs = values
        else:
            raise Exception("Values given not valid")
            # raise Exception("Values given not valid" + str(values))

    # GETTERS

    def getFullType(self):
        return self.type + self.subType
    
    def getType(self):
        return self.type

    def getSubType(self):
        return self.subType
    
    def getFullName(self):
        return self.typeHandler.typeConversor(self.getFullType())
    
    def getTypeName(self):
        return self.typeHandler.typeConversor(self.getType())
    
    def getSubTypeName(self):
        return self.typeHandler.subTypeConversor(self.getSubType())
    
    def getCells(self):
        return self.CELLs
    
    def getValues(self):
        return self.VALUEs

    # SETTERS

    def addValues(self, values):
        if type(values) is set:
            self.VALUEs.update(values)
        else: 
            raise Exception("The input must be a set")