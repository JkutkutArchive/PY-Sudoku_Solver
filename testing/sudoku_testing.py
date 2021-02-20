import sys
sys.path.append('.')

import unittest
import logging
import pytest
# from Classes import cell
from Classes import sudoku
# import random

import sudokuFunctions
import input

class TestStringMethods(unittest.TestCase):
    def setUp(self):
        self.sudoku = sudoku.Sudoku()

    # def test_fillSudoku(self):
    #     try:
    #         self.sudoku.fillBoard([])
    #     except:
    #         e = sys.exc_info()[0]
    #         print(e)
    #     self.assertTrue(False)

    def test_printSudokuTest(self):
        self.sudoku.fillBoard(input.easy())
        self.maxDiff = None # To compare the whole output

        espected = \
"  C 0 1 2   3 4 5   6 7 8 \n\
R +-------+-------+-------+\n\
0 | 9 8 4 | 0 3 1 | 0 7 2 |\n\
1 | 6 1 0 | 0 0 7 | 0 0 0 |\n\
2 | 2 5 7 | 0 0 9 | 8 0 0 |\n\
  +-------+-------+-------+\n\
3 | 3 0 0 | 0 6 0 | 0 1 0 |\n\
4 | 0 0 0 | 3 7 0 | 9 2 0 |\n\
5 | 0 0 9 | 0 0 5 | 0 0 0 |\n\
  +-------+-------+-------+\n\
6 | 0 3 0 | 0 0 6 | 0 0 0 |\n\
7 | 0 4 5 | 0 1 8 | 0 9 6 |\n\
8 | 1 9 6 | 7 0 0 | 2 8 0 |\n\
  +-------+-------+-------+"

        self.assertEqual(self.sudoku.print(returnAsString=True), espected)

        self.sudoku.fillBoard(input.medium())
        self.assertEqual(self.sudoku.print(arr=input.easy(), returnAsString=True), espected)
        self.assertIsNone(self.sudoku.print())

if __name__ == '__main__':
  print("Testing...")

  logging.basicConfig( stream=sys.stderr )
  logging.getLogger( "TestStringMethods.printSudokuTest" ).setLevel( logging.DEBUG )
  
  unittest.main()