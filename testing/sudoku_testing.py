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

    def test_initClass(self):
        sud1 = sudoku.Sudoku()
        board = input.swordfish()
        sud2 = sudoku.Sudoku(board)

        sud1Board = sud1.toList()
        sud2Board = sud2.toList()

        for r in range(9):
            for c in range(9):
                self.assertEquals(sud1Board[r][c].getValue(), 0)
                self.assertEquals(sud2Board[r][c].getValue(), board[r][c])


    def test_fillSudoku(self):
        testSudoku = sudoku.Sudoku()
        boardTest = testSudoku.toList()

        spected = input.hard()
        self.sudoku.fillBoard(spected)
        board = self.sudoku.toList()
        for r in range(9):
            for c in range(9):
                self.assertEquals(boardTest[r][c].getValue(), 0)
                self.assertEquals(board[r][c].getValue(), spected[r][c])

    def test_printSudokuTest(self):
        self.sudoku.fillBoard(input.easy())
        self.maxDiff = None # To compare the whole output

        espected = "  C 0 1 2   3 4 5   6 7 8 \nR +-------+-------+-------+\n0 | 9 8 4 | 0 3 1 | 0 7 2 |\n1 | 6 1 0 | 0 0 7 | 0 0 0 |\n2 | 2 5 7 | 0 0 9 | 8 0 0 |\n  +-------+-------+-------+\n3 | 3 0 0 | 0 6 0 | 0 1 0 |\n4 | 0 0 0 | 3 7 0 | 9 2 0 |\n5 | 0 0 9 | 0 0 5 | 0 0 0 |\n  +-------+-------+-------+\n6 | 0 3 0 | 0 0 6 | 0 0 0 |\n7 | 0 4 5 | 0 1 8 | 0 9 6 |\n8 | 1 9 6 | 7 0 0 | 2 8 0 |\n  +-------+-------+-------+"

        self.assertEqual(self.sudoku.print(returnAsString=True), espected)

        self.sudoku.fillBoard(input.medium())
        self.assertEqual(self.sudoku.print(arr=input.easy(), returnAsString=True), espected)
        self.assertIsNone(self.sudoku.print())

if __name__ == '__main__':
    print("Testing...")

    logging.basicConfig( stream=sys.stderr )
    logging.getLogger( "TestStringMethods.printSudokuTest" ).setLevel( logging.DEBUG )

    unittest.main()