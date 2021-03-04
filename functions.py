import latexToPDF as pdf
sol = []
grid = []
# nNewValues = 0 


# ## Prints the status of the arguments (errors)
# def pError(**kwargs):
#     '''
#     Console logs the error(s) given
#     '''
#     print("***ERROR***".center(30))
#     print(kwargs)
#     print("***END ERROR***".center(30))

#   --------------------------------    METHODS     --------------------------------
def tellCells(cell, cleverCell=True): # When a cell defines its value, this function is called to update the rest
    value = cell.getValue()
    for i in range(9):
        if i != cell.y: # Row
            c = grid[cell.x][i]
            if c.getValue() != value and value in c.getPosVal():
                c.addData("basic row", [value])
                c.removePosVal(value, cleverCell=cleverCell)
        if i != cell.x: # Col
            c = grid[i][cell.y]
            if c.getValue() != value and value in c.getPosVal():
                c.addData("basic col", [value])
                c.removePosVal(value, cleverCell=cleverCell)
        x = (cell.x // 3) * 3 + (i // 3)
        y = (cell.y // 3) * 3 + (i % 3)
        if i != cell.x or i != cell.y: # 3by3
            c = grid[x][y]
            if c.getValue() != value and value in c.getPosVal():
                c.addData("basic 3 by 3", [value])
                c.removePosVal(value, cleverCell=cleverCell)