import sys
sys.path.append('.')

import unittest
# from Classes import cell
from Classes import sudoku
# import random

class TestStringMethods(unittest.TestCase):
    def setUp(self):
        self.sudoku = sudoku.Sudoku()

    def fillSudoku(self):
        try:
            self.sudoku.fillBoard([])
        except:
            e = sys.exc_info()[0]
            print(e)
            

if __name__ == '__main__':
    print("hola1")
    unittest.main()
    print("hola")