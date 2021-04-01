import sys
sys.path.append('.')

import unittest
import logging
import pytest

from Classes.cell import Cell
from Classes.dataSudoku import DataSudoku
from Classes.typeHandler import TypeHandler
# import random

import input

class TestStringMethods(unittest.TestCase):
    def setUp(self):
        # self.typeHandler = TypeHandler()
        self.cell = Cell(0, 0)
        self.data = DataSudoku(TypeHandler.therefore(), self.cell, None)
    
    def test_typesExist(self):
        sw = TypeHandler.switcher
        
        errorNotFound = "Data type not found"
        notValidInput = "The input is not valid"
        for i in range(len(sw)):
            self.assertTrue(TypeHandler.validType(i))
            self.assertTrue(TypeHandler.typeConversor(i) != errorNotFound)
        
        self.assertEqual(TypeHandler.typeConversor(1 + len(sw)), notValidInput)
        self.assertEqual(TypeHandler.typeConversor(-1), notValidInput)

        for type in sw:
            typeIndex = TypeHandler.typeConversor(type) # int eq to type
            self.assertTrue(TypeHandler.validType(typeIndex))
            self.assertTrue(type == TypeHandler.typeConversor(typeIndex)) # check the conversor is circular

            for subType in ["row", "col", "3by3"]:
                typeIndex = TypeHandler.typeConversor(type + " " + subType) # int eq to type+subtype
                self.assertTrue(TypeHandler.validType(typeIndex))
                self.assertTrue(type + " " + subType == TypeHandler.typeConversor(typeIndex))
                
    def test_methodsExist(self):
        sw = TypeHandler.switcher
        subSw = TypeHandler.subSwitcher
        for type in sw:
            self.assertTrue(type in dir(TypeHandler))
        for subType in subSw:
            self.assertTrue("sub"+subType in dir(TypeHandler))






if __name__ == '__main__':
    print("Testing...")

    logging.basicConfig( stream=sys.stderr )
    logging.getLogger( "TestStringMethods.printSudokuTest" ).setLevel( logging.DEBUG )

    unittest.main()