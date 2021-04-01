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
        self.cell = Cell(0, 0)
        self.data = DataSudoku(TypeHandler.therefore(), self.cell, None)
        
    def test_initdataInvalid(self):
        testInvalid = [
            ["", self.cell, None],
            [None, self.cell, None],
            [100, self.cell, None],
            [-1, self.cell, None],
            [TypeHandler.therefore(), "", set()],
            [TypeHandler.therefore(), {}, 2],
            [TypeHandler.therefore(), set(), ""],
            [TypeHandler.therefore(), self.cell, {}],
        ]
        exceptions = [
            "DataType not valid",
            "DataType not valid",
            "DataType not valid",
            "DataType not valid",
            "Cells given not valid",
            "Cells given not valid",
            "Values given not valid",
            "Values given not valid"
        ]

        for t in range(len(testInvalid)):
            with self.assertRaises(Exception) as context:
                DataSudoku(*testInvalid[t])
            self.assertTrue(exceptions[t] in str(context.exception))
        
        exception = "Subtype not valid"
        with self.assertRaises(Exception) as context:
            DataSudoku(len(TypeHandler.switcher) - 0.25, subType=0.25)
            self.assertEqual(exception, context.exception)
        
    def test_initdataValid(self):
        testValid = [
            [TypeHandler.therefore(), self.cell, set([1,2])],
            [1, set([self.cell, self.cell]), set([1,2])],
            [1, set([self.cell, self.cell]), 3],
            [1]
        ]

        for t in range(len(testValid)):
            try:
                DataSudoku(*testValid[t])
            except:
                self.assertFalse(True)
            self.assertTrue(True)
        
        try:
            DataSudoku(1, subType=0.25)
        except:
            raise Exception("Special creation failed")
        
    def test_getIndexType(self):
        indices = [
            [0, None],
            [0, 0.25],
        ]
        for case in indices:
            d = DataSudoku(case[0], subType=case[1])
            
            self.assertEqual(d.getType(), case[0])
            
            if case[1] == None:
                case[1] = 0.0
            self.assertEqual(d.getSubType(), case[1])
            self.assertEqual(d.getFullType(), sum(case))

    def test_getNameType(self):
        indices = [
            [0, None],
            [0, 0.25],
        ]
        for case in indices:
            d = DataSudoku(case[0], subType=case[1])
            
            self.assertEqual(d.getTypeName(), TypeHandler.typeConversor(case[0]))
            
            if case[1] == None:
                case[1] = 0.0
            else:
                self.assertEqual(d.getSubTypeName(), TypeHandler.subTypeConversor(case[1]))
            

            self.assertEqual(d.getFullTypeName(), TypeHandler.typeConversor(sum(case)))






if __name__ == '__main__':
    print("Testing...")

    logging.basicConfig( stream=sys.stderr )
    logging.getLogger( "TestStringMethods.printSudokuTest" ).setLevel( logging.DEBUG )

    unittest.main()