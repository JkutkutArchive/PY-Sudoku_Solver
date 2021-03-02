import sys
sys.path.append('.')

import unittest
import logging
import pytest
# from Classes import cell
from Classes import sudoku
# import random

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
                self.assertEqual(sud1Board[r][c].getValue(), 0)
                self.assertEqual(sud2Board[r][c].getValue(), board[r][c])

    def test_fillBoard(self):
        testSudoku = sudoku.Sudoku()
        boardTest = testSudoku.toList()

        spected = input.full()
        self.sudoku.fillBoard(spected)
        board = self.sudoku.toList()
        for r in range(9):
            for c in range(9):
                self.assertEqual(boardTest[r][c].getValue(), 0)
                self.assertEqual(board[r][c].getValue(), spected[r][c])
        
        spected2 = input.empty()
        self.sudoku.fillBoard(spected2)
        board2 = self.sudoku.toList()
        for r in range(9):
            for c in range(9):
                self.assertNotEqual(board2[r][c].getValue(), spected2[r][c])
                self.assertEqual(board2[r][c].getValue(), board[r][c].getValue())

    def test_printSudokuTest(self):
        self.sudoku.fillBoard(input.easy())
        self.maxDiff = None # To compare the whole output

        espected = "  C 0 1 2   3 4 5   6 7 8 \nR +-------+-------+-------+\n0 | 9 8 4 | 0 3 1 | 0 7 2 |\n1 | 6 1 0 | 0 0 7 | 0 0 0 |\n2 | 2 5 7 | 0 0 9 | 8 0 0 |\n  +-------+-------+-------+\n3 | 3 0 0 | 0 6 0 | 0 1 0 |\n4 | 0 0 0 | 3 7 0 | 9 2 0 |\n5 | 0 0 9 | 0 0 5 | 0 0 0 |\n  +-------+-------+-------+\n6 | 0 3 0 | 0 0 6 | 0 0 0 |\n7 | 0 4 5 | 0 1 8 | 0 9 6 |\n8 | 1 9 6 | 7 0 0 | 2 8 0 |\n  +-------+-------+-------+"

        self.assertEqual(self.sudoku.print(returnAsString=True), espected)

        self.sudoku.fillBoard(input.medium())
        self.assertEqual(self.sudoku.print(arr=input.easy(), returnAsString=True), espected)
        self.assertIsNone(self.sudoku.print())

    def test_validSolution(self):
        self.assertFalse(self.sudoku.validSolution())
        self.sudoku.fillBoard(input.full())
        self.assertTrue(self.sudoku.validSolution())
        self.assertTrue(self.sudoku.validSolution(input.full()))
        self.assertFalse(self.sudoku.validSolution(input.empty()))
        
    def test_findSolutions(self):
        # None solution
        noSolutionSudoku = sudoku.Sudoku(input.noSolution())
        noSolutionsFound = []
        noSolutionSudoku.findSolutions(noSolutionsFound)
        self.assertEqual(len(noSolutionsFound), 0)

        # One solution
        self.sudoku.fillBoard(input.full())
        solutions = []
        self.sudoku.findSolutions(solutions=solutions)
        self.assertEqual(len(solutions), 1)
        
        solutionSudoku = sudoku.Sudoku(solutions[0])
        self.assertTrue(solutionSudoku.validSolution())

        miniTests = [input.tripleSolutions(), input.hexSolutions()]
        spectedSolutions = [3, 6]

        # Multiple solutions
        for miniTest in range(len(miniTests)):

            sudoku2 = sudoku.Sudoku(miniTests[miniTest])
            solutionSudoku2 = []
            sudoku2.findSolutions(solutionSudoku2)
            
            self.assertEqual(len(solutionSudoku2), spectedSolutions[miniTest])
            solutionSudoku2Objects = [sudoku.Sudoku(i) for i in solutionSudoku2]
            
            for solutionObject in solutionSudoku2Objects:
                self.assertTrue(solutionObject.validSolution())
            
            #Check all solutions are unique
            for i in range(len(solutionSudoku2Objects) - 1):
                for j in range(i + 1, len(solutionSudoku2Objects)):
                    self.assertNotEqual(solutionSudoku2Objects[i], solutionSudoku2Objects[j])


    def test_findSolutionWithSteps(self):
        # Check invalid sudokus
        test = [
            sudoku.Sudoku(input.noSolution()),
            sudoku.Sudoku(input.tripleSolutions())
        ]

        exceptions = ["No solutions founded for the current sudoku.",\
                      "There are more than one possible solution."]
        for t in range(len(test)):
            with self.assertRaises(Exception) as context:
                test[t].findSolutionWithSteps()
            
            self.assertTrue(exceptions[t] in str(context.exception))

if __name__ == '__main__':
    print("Testing...")

    logging.basicConfig( stream=sys.stderr )
    logging.getLogger( "TestStringMethods.printSudokuTest" ).setLevel( logging.DEBUG )

    unittest.main()