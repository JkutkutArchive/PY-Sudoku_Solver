import Classes.typeHandler
import Classes.cell


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