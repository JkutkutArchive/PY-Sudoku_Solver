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
        self.subSwitcher = [
            "row",
            "col",
            "3by3"
        ]
        for i in range(len(self.subSwitcher)):
            exec("self." + self.subSwitcher[i] + " = lambda: " + str((i + 1) * 0.25))

    def validType(self, typeData) -> bool:
        if not type(typeData) is int:
            return False
        if typeData < 0:
            return False
        if typeData > len(self.switcher):
            return False
        return True
    
    def typeConversor(self, t) -> str or int:
        '''
        Transforms the input to the equivalent type (str -> int and int -> str).

        Input:
        t (int|str): type to convert.

        Returns:
        (str|int): equivalent type.
        '''
        if type(t) is str:
            for i in range(len(self.switcher)):
                if t in self.switcher[i]:
                    subType = 0
                    for subT in range(len(self.subSwitcher)):
                        if t in self.subSwitcher[subT]:
                            subType = (t + 1) * 0.25
                    return i + subType
            return "Data type not found"

        elif self.validType(t):
            subType = ""
            if t % 1 != 0:
                indexSubType = (t % 1) // 0.25
                subType = " " + self.subSwitcher[indexSubType]
            return self.switcher[t] + subType
        else:    
            return "The input is not valid"