import Classes.typeHandler
import Classes.cell

# Format:
# [ID, VALUEs, CELLs]


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
# [     "uniqueRectangle", <CELLs>,  <VALUE>]
# [ "swordfish <SUBTYPE>", <CELLs>,  <VALUE>]; <SUBTYPE>=[row, col]





class DataSudoku():
    def __init__(self, typeData, cellsGiven=None, values=None):
        self.typeHandler = Classes.typeHandler.TypeHandler()
        
        if self.typeHandler.validType(typeData):
            self.type = typeData
        else:
            raise Exception("DataType not valid")

        if any([type(cellsGiven) is posType for posType in [Classes.cell.Cell, list]]):
            self.CELLs = cellsGiven
        else:
            raise Exception("The cell adressed is not a Cell")

        if any([type(values) is posType for posType in [int, list]]):
            self.VALUEs = values