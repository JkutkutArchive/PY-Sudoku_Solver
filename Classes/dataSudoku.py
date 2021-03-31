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
# [           "pairs two",  <CELL>,  <VALUE>]
# [   "delPair set value",  <CELL>,  <VALUE>]
# ["delPair remove value",  <CELL>,  <VALUE>]
# [    "X-Wing <SUBTYPE>", <CELLs>,  <VALUE>]; <SUBTYPE>=[row, col]
# [             "XY-Wing", <CELLs>, <VALUEs>]
# [     "UniqueRectangle", <CELLs>,  <VALUE>]
# [ "Swordfish <SUBTYPE>", <CELLs>,  <VALUE>]; <SUBTYPE>=[row, col]





class DataSudoku():
    def __init__(self, typeData, cellGiven, details):
        self.typeHandler = Classes.typeHandler.TypeHandler()
        
        if self.typeHandler.validType(typeData):
            self.type = typeData
        else:
            raise Exception("DataType not valid")

        if type(cellGiven) is Classes.cell.Cell:
            self.cell = cellGiven
        else:
            raise Exception("The cell adressed is not a Cell")

        self.details = details