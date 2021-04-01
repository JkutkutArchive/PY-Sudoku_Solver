import Classes.typeHandler as TH
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

        if TH.TypeHandler.validType(typeData):
            self.type = int(typeData)
            self.subType = typeData // 0.25
        else:
            raise Exception("DataType not valid")

        if subType != None:
            if subType > 0 and subType < 1 and TH.TypeHandler.validType(self.type + subType):
                self.subType = subType
            else:
                raise Exception("Subtype not valid")
        else:
            self.subType = 0.0

        # function to evaluate if the specifified input is valid or not
        validInput = lambda inputed, specialType: \
            any([type(inputed) is posType for posType in [specialType, list, set, type(None)]])

        if validInput(cellsGiven, Classes.cell.Cell):
            self.CELLs = cellsGiven
        else:
            raise Exception("Cells given not valid")
            # raise Exception("Cells given not valid:\n" + str(cellsGiven)) # Debug

        if validInput(values, int):
            self.VALUEs = values
        else:
            raise Exception("Values given not valid")
            # raise Exception("Values given not valid" + str(values)) # Debug

    def __eq__(self, other) -> bool:
        if not type(other) is DataSudoku:
            return False
        if not self.type == other.type or not self.subType == other.subType:
            return False
        
        if not self.VALUEs == other.VALUEs or not self.CELLs == other.CELLs:
            return False

        return True

    def __hash__(self) -> int:
        valH, cellH = 0, 0
        if type(self.VALUEs) is int:
            valH = hash(self.VALUEs)
        elif not self.VALUEs == None:
            for val in self.VALUEs:
                valH = valH ^ hash(val)
        if type(self.CELLs) is Classes.cell.Cell:
            cellH = hash(self.CELLs)
        elif not  self.CELLs == None:
            for cell in self.CELLs:
                cellH = cellH ^ hash(cell)

        return hash(self.type) ^ hash(self.subType) ^ valH ^ cellH

    # GETTERS

    def getFullType(self) -> float:
        '''
        Returns: the full type as a float number
        '''
        return self.type + self.subType
    
    def getType(self) -> int:
        '''
        Returns: the type as a int number
        '''
        return self.type

    def getSubType(self) -> float:
        '''
        Returns: the subType as a int float
        '''
        return self.subType
    
    def getFullTypeName(self) -> str:
        '''
        Returns: Full name of the Type as a string
        '''
        return TH.TypeHandler.typeConversor(self.getFullType())
    
    def getTypeName(self) -> str:
        '''
        Returns: Name of the Type as a string
        '''
        return TH.TypeHandler.typeConversor(self.getType())
    
    def getSubTypeName(self) -> str:
        '''
        Returns: name of the subType as a string
        '''
        return TH.TypeHandler.subTypeConversor(self.getSubType())
    
    def getCells(self):
        '''
        Returns: cells stored
        '''
        return self.CELLs
    
    def getValues(self):
        '''
        Returns: values stored
        '''
        return self.VALUEs

    # SETTERS

    def addValues(self, values) -> None:
        '''
        Add the values to the current values.
        values (set(int) or list[int]): values to add to the current set
        '''
        validInput = lambda values, specialType: \
            type(values) is specialType and \
            all([type(v) is int for v in values]) and \
            all([v > 0 and v < 10 for v in values])

        if self.VALUEs == None: # Clone the input (if valid)
            if type(values) is int:
                self.VALUEs = values
            if type(values) is list and validInput(values, list):
                self.VALUEs = values.copy()
            elif type(values) is set and validInput(values, set):
                self.VALUEs = set(values)
            else:
                raise Exception("The input must be a set(int), list[int] or int")

        elif type(self.VALUEs) is int:
            self.VALUEs = set(self.VALUEs)
            self.VALUEs.update(set(values))  
        
        elif type(self.VALUEs) is set:
            if validInput(values, set):
                self.VALUEs.update(values)
            else: 
                raise Exception("The input must be a set of integers")
        
        elif type(self.VALUEs) is list:
            if validInput(values, list):
                for v in values:
                    if not v in self.VALUEs:
                        self.VALUEs.append(v)
            else: 
                raise Exception("The input must be a list of integers")
