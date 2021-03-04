import Classes.typeHandler as tH
import Classes.cell as c

TypeHandler = tH.TypeHandler
Cell = c.Cell

class DataSudoku():
    def __init__(self, typeData, cellGiven, details):
        self.typeHandler = TypeHandler()
        
        if self.typeHandler.validType(typeData):
            self.type = typeData
        else:
            raise Exception("DataType not valid")

        if type(cellGiven) is Cell:
            self.cell = cellGiven
        else:
            raise Exception("The cell adressed is not a Cell")

        self.details = details