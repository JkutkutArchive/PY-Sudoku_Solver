def checkSol(arr):
    '''
    Check if the given sudoku is a valid solution

    Given a 9x9 Cell list, check if it forms a valid sudoku.

    - arr (list): 9x9 Cell list

    Returns:
    boolean: whenever the input forms a valid sudoku

    Note: See the Cell class for more information about who this function works.
    '''
    for i in range(0, 9, 3):#3 by 3:
        for j in range(0, 9, 3):
            suma = 0
            ele = []
            for k in range(3):
                for l in range(3):
                    suma = suma + arr[k + i][l + j].getValue()
                    ele = ele + [arr[k + i][l + j].getValue()]
            if(suma != 45):
                return False
    for l in range(9):#lines:
        solCc = 0
        solCr = 0
        for i in range(9):
            solCc = solCc + arr[i][l].getValue()
            solCr = solCr + arr[l][i].getValue()
        if solCc != 45 or solCr != 45:
            return False
    return True


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