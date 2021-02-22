class DataSudoku():
    def __init__(self, typeData):
    # def __init__(self, typeData, cell):
        self.type = typeData
        # self.cell = cell
        self.valuesDiscarted = None
        self.valuesCertain = None
    

    # ******    type Handle:    ******

    def typeConversor(self, t):
        switcher = {
            1: "therefore",
            2: "basic",
            3: "unique",
            4: "pairs",
            5: "delPairs",
            6: "X-Wing",
            7: "XY-Wing",
            8: "uniqueRectangle",
            9: "swordfish"
        }
        retu = switcher.get(t, "Data type not found")
        return retu in switcher
    
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

    