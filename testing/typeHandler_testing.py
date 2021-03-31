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
        self.typeHandler = TypeHandler()
        self.cell = Cell(0, 0)
        self.data = DataSudoku(self.typeHandler.therefore(), self.cell, None)
    
    def test_typesExist(self):
        sw = self.typeHandler.switcher
        
        errorNotFound = "Data type not found"
        notValidInput = "The input is not valid"
        for i in range(len(sw)):
            self.assertTrue(self.typeHandler.validType(i))
            self.assertTrue(self.typeHandler.typeConversor(i) != errorNotFound)
        
        self.assertEqual(self.typeHandler.typeConversor(1 + len(sw)), notValidInput)
        self.assertEqual(self.typeHandler.typeConversor(-1), notValidInput)

        for type in sw:
            typeIndex = self.typeHandler.typeConversor(type) # int eq to type
            self.assertTrue(self.typeHandler.validType(typeIndex))
            self.assertTrue(type == self.typeHandler.typeConversor(typeIndex)) # check the conversor is circular

            for subType in ["row", "col", "3by3"]:
                typeIndex = self.typeHandler.typeConversor(type + " " + subType) # int eq to type+subtype
                self.assertTrue(self.typeHandler.validType(typeIndex))
                self.assertTrue(type + " " + subType == self.typeHandler.typeConversor(typeIndex))
                
    
    # def test_subTypeExist(self):
    #     subSw = self.typeHandler.subSwitcher

    #     for i in range(len(subSw)):






if __name__ == '__main__':
    print("Testing...")

    logging.basicConfig( stream=sys.stderr )
    logging.getLogger( "TestStringMethods.printSudokuTest" ).setLevel( logging.DEBUG )

    unittest.main()