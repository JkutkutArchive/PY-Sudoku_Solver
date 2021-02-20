

def sudokuSolution(data, solutions):
    '''
    Gets the possible solution(s) of the given sudoku.

    Given a 9x9 integer list, all the possible solutions of the input are found using a classic implementation of a recursive algorithm.

    - data (list): 9x9 integer list with the data of the current state of the sudoku
    - solutions (list) Nx9x9 with the solutions found. This works as a "output".
    '''
    for x in range(9): # For each colum
        for y in range(9): # For each row
            if data[x][y] == 0: # If empty cell
                for val in range(1,10): # For each possible value
                    valid = True # If the current value (val) is viable to be the correct value of the cell(x, y)
                    for i in range(9): # for each neighbour cell (row, col or 3by3)
                        xIndex = (x // 3) * 3 # X 3by3
                        yIndex = (y // 3) * 3 # Y 3by3
                        if data[x][i] == val or data[i][y] == val or data[xIndex + (i // 3)][yIndex + (i % 3)] == val:
                            # If neighbour already has the value val, this value can not be on this cell => val not valid
                            valid = False
                            break
                    if valid: # If the value val may be correct
                        data[x][y] = val # Try to solve the sudoku using this value as correct
                        sudokuSolution(data, solutions)
                        data[x][y] = 0 # if here, the path wasn't good => undo move
                return # If here, all posible valid combinations have been tested => end execution
    
    ## if here, solution founded
    solutions.append([[ele for ele in row] for row in data]) # Add the current solution to the solution list