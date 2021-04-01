class TypeHandler():
    '''
    This class enables to control the type of data asociated with a discovery on a sudoku cell
    '''

    # Lambda functions
    switcher = [ # Posible methods (part 1/2 -> Type)
        "therefore",
        "basic",
        "unique",
        "pairs",
        "Pairs_two",
        "delPair_set_value",
        "delPair_remove_value",
        "xWing",
        "xyWing",
        "UniqueRectangle",
        "swordfish"
    ]

    for i in range(len(switcher)): # For each possible method (part 1)
            exec(switcher[i] + " = lambda: " + str(i)) # Create the method

    subSwitcher = [ # Possible methods (part 2/2 -> subType)
        "row",
        "col",
        "3by3"
    ]

    for i in range(len(subSwitcher)): # For each subMethod
        exec("sub" + subSwitcher[i] + " = lambda: " + str((i + 1) * 0.25)) # cretate it

    # Methods

    @classmethod
    def validType(cls, typeData) -> bool:
        '''
        Check whenever the input is a valid type of this class
        
        Valid type: a integer greater than 0 and less than the number of methods

        Returns: Result of the check
        '''
        
        if not type(typeData) is int and not type(typeData) is float or \
            typeData < 0 or \
            typeData > len(cls.switcher): 
            return False
        return True
    
    @classmethod
    def validSubType(cls, subTypeData) -> bool:
        return all([
            type(subTypeData) is float,
            subTypeData > 0,
            subTypeData < 1,
            subTypeData % 0.25 == 0
        ])

    @classmethod
    def typeConversor(cls, t) -> str or int:
        '''
        Transforms the input to the equivalent type (str -> int and int -> str).

        Input:
        t (int|str): type to convert.

        Returns:
        (str|int): equivalent type.
        '''
        if type(t) is str: # If string given -> output a int
            # OPTIMICE WITH SPLIT
            for i in range(len(cls.switcher)): # For each possible type
                if cls.switcher[i] in t: # If type found
                    subType = 0
                    for subT in range(len(cls.subSwitcher)): # For each possible subtype
                        if cls.subSwitcher[subT] in t: # If subtype found
                            subType = (subT + 1) * 0.25
                    return i + subType # Return int type
            return "Data type not found" # If not found, return this

        elif cls.validType(t): # If valid integer given -> output str
            subType = ""
            if t % 1 != 0: # If decimal value, there is a subtype required
                indexSubType = int((t % 1) // 0.25) - 1
                t = t // 1
                subType = cls.subSwitcher[indexSubType] # If subtype, it will follow this syntax: "<type> <subtype>"
            return cls.switcher[int(t)] + " " + subType # Return the type
        else:    
            return "The input is not valid" # If not valid input, return this

    
    @classmethod
    def subTypeConversor(cls, st) -> str or int:
        if type(st) is str: # If string given -> output a int
            if st in cls.subSwitcher:
                return (cls.subSwitcher.index(st) + 1) * 0.25
            else:
                raise Exception("Subtype not found")
        elif cls.validSubType(st): # If valid integer given -> output str
            return cls.subSwitcher[int(st // 0.25)]
        else:
            raise Exception("The input is not valid")