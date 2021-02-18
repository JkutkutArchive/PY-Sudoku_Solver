# import sys
# sys.path.append('.')
from Classes import cell # Custom Class

class Sudoku():
    def __init__(self):
        self.board = [[cell.Cell(x, y) for y in range(9)] for x in range(9)] # Create the board
        self.remainingCells = set()
    
    def fillBoard(self, data):
        super() # Reset the class
        if len(data) != 9 or len(data[0]) != 9:
            raise Exception("The data should be a 9x9 list")

        # If here, the data is correct
        for i in range(9):
            for j in range(9):
                if data[i][j] != 0:
                    self.board[i][j].setValue(data[i][j], False, cleverCell=False)
                else:
                    self.remainingCells.add(self.board[i][j])


if __name__ == "__main__":
    a = Sudoku()
    a.fillBoard([])
    data = [ # hard
        [0, 0, 7, 0, 0, 0, 3, 0, 2],
        [2, 0, 0, 0, 0, 5, 0, 1, 0],
        [0, 0, 0, 8, 0, 1, 4, 0, 0],
        [0, 1, 0, 0, 9, 6, 0, 0, 8],
        [7, 6, 0, 0, 0, 0, 0, 4, 9],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 3, 0, 0, 0],
        [8, 0, 1, 0, 6, 0, 0, 0, 0],
        [0, 0, 0, 7, 0, 0, 0, 6, 3]
    ]
    a.fillBoard(data)
