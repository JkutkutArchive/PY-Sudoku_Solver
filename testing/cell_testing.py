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
    
    def test_parentSudoku(self):
        self.testCells = [[cell.Cell(x, y) for y in range(9)] for x in range(9)]

        for c in range(9):
            for cc in range(9):
                self.assertIsNone(self.testCells[c][cc].sudoku)
                self.assertEqual(self.cells[c][cc].sudoku, self.sudokuBoard)

    def test_toString(self):
        r = random.Random()
        
        values = [[r.randint(0, 9) for _ in range(9)] for __ in range(9)]
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
            (cell.Cell(r.randint(0,9), r.randint(0,9)), r.randint(1,9)) for _ in range(9)
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

                pairIndices = [r.randint(0, 8) for _ in range(r.randint(0, 8))]
                for i in pairIndices:
                    self.cells[c][cc].addPair(pairs[i][0], pairs[i][1])
                
                self.assertTrue(pairs_test(self.cells[c][cc], pairIndices, argToString[0]))
                self.assertTrue(pairs_test(self.cells[c][cc], pairIndices, argToString[3]))
                self.assertFalse(pairs_test(self.cells[c][cc], pairIndices, argToString[-3]))
                self.assertFalse(pairs_test(self.cells[c][cc], pairIndices, argToString[-1]))


                # PosVal
                value2Remove = r.randint(1, 9)
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


    def test_string_emptyCells(self):
        r = random.Random()
        for c in self.cells:
            for cc in c:
                # No value
                self.assertEqual(cc.__str__(), '0')

                # Value defined
                value = r.randint(1, 9)
                cc.setValue(value)
                self.assertEqual(cc.getValue(), value)
                self.assertEqual(cc.__str__(), str(value))
                
    
            

if __name__ == '__main__':
    unittest.main()