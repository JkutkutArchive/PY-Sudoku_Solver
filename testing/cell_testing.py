import sys
sys.path.append('.')

import unittest
from Classes import cell
from Classes import sudoku
import random

class TestStringMethods(unittest.TestCase):
    def setUp(self):
        self.sudokuBoard = sudoku.Sudoku()
        self.cells = self.sudokuBoard.toList()
        self.r = random.Random()
    
    def test_parentSudoku(self):
        self.testCells = [[cell.Cell(x, y) for y in range(9)] for x in range(9)]

        for c in range(9):
            for cc in range(9):
                self.assertIsNone(self.testCells[c][cc].sudoku)
                self.assertEqual(self.cells[c][cc].sudoku, self.sudokuBoard)
    
    def test_init(self):
        coords = [
            [-1,  0],
            [0,  -1],
            [-1, -1],
            [0, 9],
            [9, 0], # 4
            ["a", 0],
            [None, None],
            [0, "a"],
            [set(), "a"],
            [0, set()], # 9
            [0, 0, 2],
            [0, 0, "a"],
            [0, 0, cell.Cell(0, 0)] # 12
        ]
        exceptions = [
            "r and c must be between 0 and 8",
            "r and c must be integers",
            "parentSudoku must be a Sudoku object"
        ]
        for t in range(len(coords)):
            with self.assertRaises(Exception) as context:
                cell.Cell(*coords[t])

            if t <= 4:
                exceptionToUse = exceptions[0]
            elif t <= 9:
                exceptionToUse = exceptions[1]
            else:
                exceptionToUse = exceptions[2]
            
            self.assertTrue(exceptionToUse in str(context.exception))
    
    def test_string(self):
        for c in self.cells:
            for cc in c:
                # No value
                self.assertEqual(cc.__str__(), '0')

                # Value defined
                value = self.r.randint(1, 9)
                cc.setValue(value)
                self.assertEqual(cc.getValue(), value)
                self.assertEqual(cc.__str__(), str(value))
    
    def test_toString(self):        
        values = [[self.r.randint(1, 9) for _ in range(9)] for __ in range(9)]
        argToString = [
            [ True,  True,  True,  True],
            [ True, False, False, False],
            [False,  True, False, False],
            [False, False,  True, False],
            [False, False, False,  True],
            [False,  True,  True,  True],
            [ True, False,  True,  True],
            [ True,  True, False,  True],
            [ True,  True,  True, False],
            [False, False, False, False],
        ]

        pairs = [
            (cell.Cell(self.r.randint(0,8), self.r.randint(0,8)), self.r.randint(1,9)) for _ in range(9)
        ]


        position_Test = lambda c, spected, arg: (
            c.getPos().__str__() in c.toString(*arg) and
            spected == c.getPos())
        
        value_Test = lambda c, spected, arg: (
            str(c.getValue()) in c.toString(*arg) and
            "Value:" in c.toString(*arg) and
            c.getValue() == spected
        )
        
        posVal_Test1 = lambda c, notSpected, arg: (
            all([str(x) in c.toString(*arg) for x in c.getPosVal()]) and
            not notSpected in c.getPosVal() and
            "PosVal" in c.toString(*arg) and
            c.getPosVal() == set([x for x in range(1, 10) if not x == notSpected])
        )
        
        posVal_Test2 = lambda c, arg: (
            "PosVal: set()" in c.toString(*arg) and
            len(c.getPosVal()) == 0
        )

        pairs_test = lambda c, indices, arg: (
            all([("- Pair with " + str(pairs[indices[i]][0].getPos()) + " -> " + str(pairs[indices[i]][1])) in c.toString(*arg) for i in range(len(indices))]) and
            "Pairs:" in c.toString(*arg)
        )

        data_test = lambda c, arg: (True)
        # ++++++++++++++++++++++ MISSING ++++++++++++++++++++++ 
        


        for c in range(9):
            for cc in range(9):
                pos = (c, cc)
                
                
                self.assertTrue(position_Test(self.cells[c][cc], pos, argToString[0])) # Check position correct
                self.assertTrue(position_Test(self.cells[c][cc], pos, argToString[-1])) # Check always appear

                # Pairs
                
                self.assertTrue(pairs_test(self.cells[c][cc], [], argToString[0]))
                self.assertTrue(pairs_test(self.cells[c][cc], [], argToString[3]))
                self.assertFalse(pairs_test(self.cells[c][cc], [], argToString[-3]))
                self.assertFalse(pairs_test(self.cells[c][cc], [], argToString[-1]))

                pairIndices = [self.r.randint(0, 8) for _ in range(self.r.randint(0, 8))]
                for i in pairIndices:
                    self.cells[c][cc].addPair(pairs[i][0], pairs[i][1])
                
                self.assertTrue(pairs_test(self.cells[c][cc], pairIndices, argToString[0]))
                self.assertTrue(pairs_test(self.cells[c][cc], pairIndices, argToString[3]))
                self.assertFalse(pairs_test(self.cells[c][cc], pairIndices, argToString[-3]))
                self.assertFalse(pairs_test(self.cells[c][cc], pairIndices, argToString[-1]))


                # PosVal
                value2Remove = self.r.randint(1, 9)
                self.cells[c][cc].removePosVal(value2Remove)

                self.assertTrue(posVal_Test1(self.cells[c][cc], value2Remove, argToString[0])) # Check posVal appears correct
                self.assertTrue(posVal_Test1(self.cells[c][cc], value2Remove, argToString[2])) # Check posVal appears correct
                self.assertFalse(posVal_Test1(self.cells[c][cc], value2Remove, argToString[-4])) # Check posVal does not appear
                self.assertFalse(posVal_Test1(self.cells[c][cc], value2Remove, argToString[-1])) # Check posVal does not appear

                self.cells[c][cc].setValue(values[c][cc])

                self.assertTrue(posVal_Test2(self.cells[c][cc], argToString[0])) # Check posVal appears correct
                self.assertTrue(posVal_Test2(self.cells[c][cc], argToString[2])) # Check posVal appears correct
                self.assertFalse(posVal_Test2(self.cells[c][cc], argToString[-4])) # Check posVal does not appear
                self.assertFalse(posVal_Test2(self.cells[c][cc], argToString[-1])) # Check posVal does not appear


                # Value
                self.assertTrue(value_Test(self.cells[c][cc], values[c][cc], argToString[1])) # Check value appears correct
                self.assertFalse(value_Test(self.cells[c][cc], values[c][cc], argToString[-5])) # Check value does not appear
                self.assertFalse(value_Test(self.cells[c][cc], values[c][cc], argToString[-1])) # Check value does not appear

    def test_eq(self):
        for c in self.cells:
            for cc in c:
                # Fails:
                self.assertNotEqual(cc, None)
                
                exception = "The object to compare to with this cell is not valid"
                for test in ["a", set(), []]:
                    with self.assertRaises(Exception) as context:
                        cc == test
                    self.assertEqual(exception, str(context.exception))
                
                # Correct
                self.assertEqual(cc, cc.getValue())
                self.assertEqual(cc, cc)

                # Incorrect
                value = self.r.randint(1, 9)

                methods = [
                    ".setValue(value)",
                    ".removePosVal(value)"
                    # "" // DATA
                ]
                # ++++++++++++++++++++++ MISSING ++++++++++++++++++++++ 
                for i in range(len(methods)):
                    testCell = cell.Cell(cc.gR(), cc.gC())
                    
                    self.assertEqual(cc, testCell)

                    eval("testCell" + methods[i])
                    self.assertNotEqual(cc, testCell)
                
                testCell = cell.Cell(0, 0)
                testCell.r = -1
                testCell.c = -1
                self.assertNotEqual(cc, testCell)
                
    
    # ******    GETTERS AND SETTERS:    ******
    def test_setGetValue(self):

        # setting with int
        self.assertEqual(self.cells[0][0].getValue(), 0)
        value = self.r.randint(1, 9)
        self.cells[0][0].setValue(value)
        self.assertEqual(self.cells[0][0].getValue(), value)

        # Second time setting value
        valueNotAplied = ((value + self.r.randint(1,5)) % 9) + 1
        
        self.cells[0][0].setValue(valueNotAplied) # This should do nothing
        self.assertNotEqual(self.cells[0][0].getValue(), valueNotAplied)
        self.assertEqual(self.cells[0][0].getValue(), value)

        self.cells[0][0].setValue(valueNotAplied, force=True) # forced => should work
        self.assertEqual(self.cells[0][0].getValue(), valueNotAplied)

        # setting with Cell
        self.cells[0][1].setValue(value)
        self.cells[0][2].setValue(self.cells[0][1])
        self.assertEqual(self.cells[0][2].getValue(), value)

        # Exceptions
        test = [None, 10, 0]
        exception = [
            "Can not set the value of the cell. Value not valid.",
            "The value must be between 1 and 9"
        ]
        for t in range(len(test)):
            with self.assertRaises(Exception) as context:
                self.cells[1][t].setValue(test[t])
                
                currentException = exception[0] if t == 0 else exception[1]
                self.assertTrue(currentException in str(context.exception))
            
    def test_setGetRemovePosVal(self):
        # Get
        self.assertEqual(self.cells[0][0].posVal, self.cells[0][0].getPosVal())

        # Remove values
        self.assertEqual(len(self.cells[0][0].getPosVal()), 9)
        value = self.r.randint(1, 9)
        self.cells[0][0].removePosVal(value)
        self.assertFalse(value in self.cells[0][0].getPosVal())
        self.assertEqual(len(self.cells[0][0].getPosVal()), 8)

        # Remove it again (should ignore)
        self.cells[0][0].removePosVal(value)
        self.assertFalse(value in self.cells[0][0].getPosVal())
        self.assertEqual(len(self.cells[0][0].getPosVal()), 8)

        # Remove a not valid value
        self.cells[0][0].removePosVal(None)
        self.cells[0][0].removePosVal("s")
        self.cells[0][0].removePosVal(set())
        self.cells[0][0].removePosVal(-1)
        self.assertEqual(len(self.cells[0][0].getPosVal()), 8)

        s = set([self.r.randint(1,9) for _ in range(self.r.randint(1,8))])

        self.assertEqual(self.cells[1][0].getPosVal(), self.cells[1][1].getPosVal())
        self.cells[1][0].setPosVal(s)
        self.assertEqual(self.cells[1][0].getPosVal(), s)
        self.assertNotEqual(self.cells[1][0].getPosVal(), self.cells[1][1].getPosVal())

    def test_getPosRowCol(self):
        for i in range(9):
            for j in range(9):
                self.assertEqual(self.cells[i][j].getPos(), (i, j))
                self.assertEqual(self.cells[i][j].getRow(), i)
                self.assertEqual(self.cells[i][j].gR(), i)
                self.assertEqual(self.cells[i][j].getCol(), j)
                self.assertEqual(self.cells[i][j].gC(), j)


if __name__ == '__main__':
    unittest.main()