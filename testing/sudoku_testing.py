import sys
from types import resolve_bases
sys.path.append('.')

import unittest
import logging
import pytest
import random

from Classes.sudoku import Sudoku
from Classes.cell import Cell
from Classes.dataSudoku import DataSudoku
from Classes.typeHandler import TypeHandler



import input

class TestStringMethods(unittest.TestCase):
    def setUp(self):
        self.sudoku = Sudoku()

    def test_initClass(self):
        sud1 = Sudoku()
        board = input.swordfish()
        sud2 = Sudoku(board)

        sud1Board = sud1.toList()
        sud2Board = sud2.toList()

        for r in range(9):
            for c in range(9):
                self.assertEqual(sud1Board[r][c].getValue(), 0)
                self.assertEqual(sud2Board[r][c].getValue(), board[r][c])

    def test_fillBoard(self):
        for spected in [input.full(), input.empty(), input.easy()]:
            self.sudoku.fillBoard(spected)
            board = self.sudoku.toList()
            for r in range(9):
                for c in range(9):
                    self.assertEqual(board[r][c].getValue(), spected[r][c])

    def test_printSudokuTest(self):
        self.sudoku.fillBoard(input.easy())
        self.maxDiff = None # To compare the whole output

        espected = "  C 0 1 2   3 4 5   6 7 8 \nR +-------+-------+-------+\n0 | 9 8 4 | 0 3 1 | 0 7 2 |\n1 | 6 1 0 | 0 0 7 | 0 0 0 |\n2 | 2 5 7 | 0 0 9 | 8 0 0 |\n  +-------+-------+-------+\n3 | 3 0 0 | 0 6 0 | 0 1 0 |\n4 | 0 0 0 | 3 7 0 | 9 2 0 |\n5 | 0 0 9 | 0 0 5 | 0 0 0 |\n  +-------+-------+-------+\n6 | 0 3 0 | 0 0 6 | 0 0 0 |\n7 | 0 4 5 | 0 1 8 | 0 9 6 |\n8 | 1 9 6 | 7 0 0 | 2 8 0 |\n  +-------+-------+-------+"

        self.assertEqual(self.sudoku.print(returnAsString=True), espected)

        self.sudoku.fillBoard(input.medium())
        self.assertNotEqual(self.sudoku.print(returnAsString=True), espected)
        self.assertEqual(self.sudoku.print(arr=input.easy(), returnAsString=True), espected)
        # self.assertIsNone(self.sudoku.print())

    def test_validSolution(self):
        self.assertFalse(self.sudoku.validSolution())
        self.sudoku.fillBoard(input.full())
        self.assertTrue(self.sudoku.validSolution())
        self.assertTrue(self.sudoku.validSolution(input.full()))
        self.assertFalse(self.sudoku.validSolution(input.empty()))
        
    def test_findSolutions(self):
        # None solution
        noSolutionSudoku = Sudoku(input.noSolution())
        noSolutionsFound = []
        noSolutionSudoku.findSolutions(noSolutionsFound)
        self.assertEqual(len(noSolutionsFound), 0)

        # One solution
        self.sudoku.fillBoard(input.full())
        solutions = []
        self.sudoku.findSolutions(solutions=solutions)
        self.assertEqual(len(solutions), 1)
        
        solutionSudoku = Sudoku(solutions[0])
        self.assertTrue(solutionSudoku.validSolution())

        miniTests = [input.tripleSolutions(), input.hexSolutions()]
        spectedSolutions = [3, 6]

        # Multiple solutions
        for miniTest in range(len(miniTests)):

            sudoku2 = Sudoku(miniTests[miniTest])
            solutionSudoku2 = []
            sudoku2.findSolutions(solutionSudoku2)
            
            self.assertEqual(len(solutionSudoku2), spectedSolutions[miniTest])
            solutionSudoku2Objects = [Sudoku(i) for i in solutionSudoku2]
            
            for solutionObject in solutionSudoku2Objects:
                self.assertTrue(solutionObject.validSolution())
            
            #Check all solutions are unique
            for i in range(len(solutionSudoku2Objects) - 1):
                for j in range(i + 1, len(solutionSudoku2Objects)):
                    self.assertNotEqual(solutionSudoku2Objects[i], solutionSudoku2Objects[j])

    def test_getRemainingCells(self):
        test = [
            Sudoku(input.empty()),
            Sudoku(input.easy()),
            Sudoku(input.full())
        ]
        spected = [81, 43, 0]
        for i in range(len(test)):
            self.assertEqual(len(test[i].remainingCells), spected[i]) # Before update
            self.assertEqual(len(test[i].getRemainingCells()), spected[i]) # With update


    def test_findSolutionWithSteps_1(self):
        # Check invalid sudokus
        test = [
            Sudoku(input.noSolution()),
            Sudoku(input.tripleSolutions())
        ]

        exceptions = ["No solutions founded for the current sudoku.",\
                      "There are more than one possible solution."]
        for t in range(len(test)):
            with self.assertRaises(Exception) as context:
                test[t].findSolutionWithSteps()
            
            self.assertTrue(exceptions[t] in str(context.exception))

    def test_findSolutionWithSteps_easy(self):
        self.sudoku.fillBoard(input.easy())
        self.assertTrue(self.sudoku.findSolutionWithSteps())

    def test_solver_basic_easy(self):
        self.sudoku.fillBoard(input.easy())

        solutions = []
        self.sudoku.findSolutions(solutions)
        self.assertEqual(len(solutions), 1)
        
        somethingDone = self.sudoku.solver_basic_loop()
        self.assertTrue(somethingDone)

    def test_solver_basic_rowCol3by3(self):
        # Easy sudoku
        easyS = Sudoku(input.easy())

        tests = [
            easyS.toList()[1][2],
            easyS.toList()[3][3],
        ]
        espected = [
            [
                set([6, 1, 7]),
                set([4, 7, 9, 5, 6]),
                set([9, 8, 4, 6, 1, 2, 5, 7])
            ],
            [
                set([3, 6, 1]),
                set([3, 7]),
                set([6, 3, 7, 5])
            ]
        ]
        # easyS.print()
        for i in range(len(tests)):
            for j in range(3):
                result = easyS.solver_basic_rowCol3by3(tests[i], j)
                self.assertEqual(espected[i][j], result)
        # easyS.print()

    def test_solver_unique(self):
        self.sudoku.fillBoard(input.unique())
        board = self.sudoku.toList()
        print()
        self.sudoku.print()

        tests = [
            board[4][5],
            board[6][4],
            board[1][2]
        ]
        expectedType = [
            0,
            1,
            2
        ]
        expectedValue = [
            6,
            2,
            6
        ]

        # r, c = 3, 3
        # # for i in range(r, r + 3):
        # #     for j in range(c, c + 3):
        # #         print(board[i][j].toString())

        # c = 4
        # for i in range(9):
        #     print(board[i][c].toString())

        for i in range(len(tests)):
            for j in range(3):
                t = self.sudoku.solver_unique_rowCol3by3(tests[i], j)
                if expectedType[i] == j:
                    # print("---------")
                    # print(tests[i].toString())
                    # print(f"type: {expectedType[i]}, expectedValue: {expectedValue[i]}, got: {t}")
                    # print("---------")
                    self.assertEqual(t, expectedValue[i])
                else:
                    # print("++++")
                    # print(j)
                    # print("++++")
                    self.assertIsNone(t)
        

if __name__ == '__main__':
    print("Testing...")

    logging.basicConfig( stream=sys.stderr )
    logging.getLogger( "TestStringMethods.printSudokuTest" ).setLevel( logging.DEBUG )

    unittest.main()