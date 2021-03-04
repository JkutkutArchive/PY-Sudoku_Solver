from testing.anidated_Files.class2 import Class2


class Class1():
    def __init__(self):
        print("created class1 object")

    def tellTheType(self, obj):
        if type(obj) is Class1:
            return "same as Class1"
        elif type(obj) is Class2:
            return "Class2"