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