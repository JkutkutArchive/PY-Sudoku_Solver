class Class2():
    def __init__(self):
        print("created class2 object")
    def tellTheType(self, obj):
        if type(obj) is Class1:
            return "Class1"
        elif type(obj) is Class2:
            return "same as Class2"