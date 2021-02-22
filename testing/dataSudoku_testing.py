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
        self.data = dataSudoku.DataSudoku(dataSudoku.TypeHandler().therefore(), cell.Cell(0, 0), None)
        self.typeHandler = dataSudoku.TypeHandler()
    
    def test_typeHandler(self):
        sw = self.typeHandler.switcher
        ignore = self.typeHandler.methodsToIgnore
        for i in range(len(sw)):
            self.assertFalse(all([sw[i] == skipM for skipM in ignore]))

    
    def test_initdata(self):
        self.assertTrue(True)
        
        # testInvalid = [
        #     [None, None, None],
        #     ["", cell.Cell(0,0), []],
        #     [dataSudoku.TypeHandler.therefore(), cell.Cell(0, 0), []],
        # ]
        # exceptions = [
        #     "DataType not valid",
        #     "DataType not valid",
        #     "The cell adressed is not a Cell"
        # ]

        # testValid = [
        #     [100, cell.Cell(0,0), None],
        #     [1, cell.Cell(0,0), []]
        # ]

        # for t in range(len(testInvalid)):
        #     with self.assertRaises(Exception) as context:
        #         dataSudoku.DataSudoku(*testInvalid[t])
            
        #     self.assertTrue(exceptions[t] in str(context.exception))





if __name__ == '__main__':
    print("Testing...")

    logging.basicConfig( stream=sys.stderr )
    logging.getLogger( "TestStringMethods.printSudokuTest" ).setLevel( logging.DEBUG )

    unittest.main()