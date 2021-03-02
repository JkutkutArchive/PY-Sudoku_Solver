import sys
sys.path.append('.')

import unittest
import logging
import pytest

from Classes import dataSudoku
from Classes import cell
from Classes import sudoku
# import random

import input

class TestStringMethods(unittest.TestCase):
    def setUp(self):
        self.typeHandler = dataSudoku.TypeHandler()
        self.cell = cell.Cell(0, 0)
        self.data = dataSudoku.DataSudoku(self.typeHandler.therefore(), self.cell, None)
    
    def test_typeHandler(self):
        sw = self.typeHandler.switcher
        
        errorNotFound = "Data type not found"
        for i in range(len(sw)):
            self.assertTrue(self.typeHandler.validType(i))
            self.assertTrue(self.typeHandler.typeConversor(i) != errorNotFound)
        self.assertEqual(self.typeHandler.typeConversor(1 + len(sw)), errorNotFound)
        self.assertEqual(self.typeHandler.typeConversor(-1), errorNotFound)

    
    def test_initdata(self):        
        testInvalid = [
            ["", self.cell, []],
            [None, self.cell, []],
            [100, self.cell, []],
            [-1, self.cell, []],
            [self.typeHandler.therefore(), None, []],
            [self.typeHandler.therefore(), {}, []],
        ]
        exceptions = [
            "DataType not valid",
            "DataType not valid",
            "DataType not valid",
            "DataType not valid",
            "The cell adressed is not a Cell",
            "The cell adressed is not a Cell"
        ]

        testValid = [
            [self.typeHandler.therefore(), self.cell, []],
            [1, self.cell, []]
        ]

        for t in range(len(testInvalid)):
            with self.assertRaises(Exception) as context:
                dataSudoku.DataSudoku(*testInvalid[t])
            self.assertTrue(exceptions[t] in str(context.exception))
        
        for t in range(len(testValid)):
            try:
                dataSudoku.DataSudoku(*testValid[t])
            except:
                self.assertFalse(True)
            self.assertTrue(True)
        
        






if __name__ == '__main__':
    print("Testing...")

    logging.basicConfig( stream=sys.stderr )
    logging.getLogger( "TestStringMethods.printSudokuTest" ).setLevel( logging.DEBUG )

    unittest.main()