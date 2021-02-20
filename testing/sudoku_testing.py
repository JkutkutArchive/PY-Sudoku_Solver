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
        # sudoku.fillBoard(input.easy())
        # sudoku.fillBoard(input.medium())
        # sudoku.print()
        
        logging.basicConfig()
        log = logging.getLogger("LOG")
        log.warning("Hola")
        # log = logging.getLogger("TestStringMethods.printSudokuTest")
        # log.debug("debug message")
        

#         self.assertEqual(captured.out,"  C 0 1 2   3 4 5   6 7 8 \
# R +-----------------------+\
# 0 | 9 8 4 | 0 3 1 | 0 7 2 |\
# 1 | 6 1 0 | 0 0 7 | 0 0 0 |\
# 2 | 2 5 7 | 0 0 9 | 8 0 0 |\
#   +-------+-------+-------+\
# 3 | 3 0 0 | 0 6 0 | 0 1 0 |\
# 4 | 0 0 0 | 3 7 0 | 9 2 0 |\
# 5 | 0 0 9 | 0 0 5 | 0 0 0 |\
#   +-------+-------+-------+\
# 6 | 0 3 0 | 0 0 6 | 0 0 0 |\
# 7 | 0 4 5 | 0 1 8 | 0 9 6 |\
# 8 | 1 9 6 | 7 0 0 | 2 8 0 |\
#   +-----------------------+")
        self.assertEqual(1,2)

if __name__ == '__main__':
  print("Testing...")

  logging.basicConfig( stream=sys.stderr )
  logging.getLogger( "TestStringMethods.printSudokuTest" ).setLevel( logging.DEBUG )
  
  unittest.main()