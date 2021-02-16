import sys
sys.path.append('.')

import unittest
from Classes import cell
import random

class TestStringMethods(unittest.TestCase):
    def setUp(self):
        self.cells = [[cell.Cell(x, y) for y in range(9)] for x in range(9)]

    def test_string_emptyCells(self):
        for c in self.cells:
            for cc in c:
                self.assertEqual(cc.__str__(), '0')
        
    # def test_string_ValuedCells(self):
    #     for c in self.cells:
    #         for cc in c:
    #             value = random.randint(1, 9)
    #             cc.setValue(value, False, False)
    #             self.assertEqual(cc.getValue, value)
    
            

if __name__ == '__main__':
    unittest.main()