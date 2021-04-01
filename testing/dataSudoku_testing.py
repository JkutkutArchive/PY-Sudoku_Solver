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
        self.data = DataSudoku(TypeHandler.therefore())
        
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

    def test_addValues(self):
        data2 = DataSudoku(TypeHandler.therefore(), values=set([1, 2]))
        data3 = DataSudoku(TypeHandler.therefore(), values=[1, 2])

        # invalid values
        invalid = [
            [1, "a", 3],
            set(["a"]),
            "",
            None
        ]
        ex = [
            "The input must be a set(int), list[int] or int",
            "The input must be a set of integers",
            "The input must be a list of integers"
        ]

        # empty values
        for t in invalid:
            with self.assertRaises(Exception) as context:
                self.data.addValues(t)
            self.assertEqual(ex[0], str(context.exception))

        # not empty values
        for t in range(len(invalid)):
            with self.assertRaises(Exception) as context:
                data2.addValues(t)
            self.assertEqual(ex[1], str(context.exception))

            with self.assertRaises(Exception) as context:
                data3.addValues(t)
            self.assertEqual(ex[2], str(context.exception))

        
        # Valid values
        valid = [
            [i for i in range(1, 4)],
            [i for i in range(4, 7)],
            [i for i in range(1, 7)],
        ]
        spectedLen = [
            3,
            6,
            6
        ]

        for i in range(len(valid)):
            try:
                self.data.addValues(set(valid[i]))
                self.assertEqual(spectedLen[i], len(self.data.getValues()))
            except:
                # print(f"{spectedLen[i]} -- {self.data.getValues()}")
                self.assertFalse(True)
            try:
                data2.addValues(set(valid[i]))
                self.assertEqual(spectedLen[i], len(data2.getValues()))
            except:
                self.assertFalse(True)
            try:
                data3.addValues(valid[i])
                self.assertEqual(spectedLen[i], len(data2.getValues()))
            except:
                self.assertFalse(True)

        for test in valid:
            with self.assertRaises(Exception) as context:
                data2.addValues(test)
            self.assertEqual(ex[1], str(context.exception))
            with self.assertRaises(Exception) as context:
                data3.addValues(set(test))
            self.assertEqual(ex[2], str(context.exception))
            






if __name__ == '__main__':
    print("Testing...")

    logging.basicConfig( stream=sys.stderr )
    logging.getLogger( "TestStringMethods.printSudokuTest" ).setLevel( logging.DEBUG )

    unittest.main()