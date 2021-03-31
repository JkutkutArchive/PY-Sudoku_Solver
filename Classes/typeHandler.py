class TypeHandler():
    '''
    This class enables to control the type of data asociated with a discovery on a sudoku cell
    '''
    def __init__(self):
        self.switcher = [ # Posible methods (part 1/2)
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
        for i in range(len(self.switcher)): # For each possible method (part 1)
            exec("self." + self.switcher[i] + " = lambda: " + str(i)) # Create the method
        
        self.subSwitcher = [ # Possible methods (part 2/2)
            "row",
            "col",
            "3by3"
        ]
        for i in range(len(self.subSwitcher)): # For each subMethod
            exec("self.sub" + self.subSwitcher[i] + " = lambda: " + str((i + 1) * 0.25)) # cretate it

    def validType(self, typeData) -> bool:
        '''
        Check whenever the input is a valid type of this class
        
        Valid type: a integer greater than 0 and less than the number of methods

        Returns: Result of the check
        '''
        
        if not type(typeData) is int or \
            typeData < 0 or \
            typeData > len(self.switcher): 
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
        if type(t) is str: # If string given -> output a int
            for i in range(len(self.switcher)): # For each possible type
                if t in self.switcher[i]: # If type found
                    subType = 0
                    for subT in range(len(self.subSwitcher)): # For each possible subtype
                        if t in self.subSwitcher[subT]: # If subtype found
                            subType = (t + 1) * 0.25
                    return i + subType # Return int type
            return "Data type not found" # If not found, return this

        elif self.validType(t): # If valid integer given -> output str
            subType = ""
            if t % 1 != 0: # If decimal value, there is a subtype required
                indexSubType = (t % 1) // 0.25
                subType = " " + self.subSwitcher[indexSubType] # If subtype, it will follow this syntax: "<type> <subtype>"
            return self.switcher[t] + subType # Return the type
        else:    
            return "The input is not valid" # If not valid input, return this