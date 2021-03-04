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
    
    def test_typeHandlerT1(self):
        sw = self.typeHandler.switcher
        
        errorNotFound = "Data type not found"
        for i in range(len(sw)):
            self.assertTrue(self.typeHandler.validType(i))
            self.assertTrue(self.typeHandler.typeConversor(i) != errorNotFound)
        self.assertEqual(self.typeHandler.typeConversor(1 + len(sw)), errorNotFound)
        self.assertEqual(self.typeHandler.typeConversor(-1), errorNotFound)





if __name__ == '__main__':
    print("Testing...")

    logging.basicConfig( stream=sys.stderr )
    logging.getLogger( "TestStringMethods.printSudokuTest" ).setLevel( logging.DEBUG )

    unittest.main()