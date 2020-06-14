#!/usr/bin/env python3
# import pygame # library to generate the graphic interface
import numpy as np # library to handle matrices
import time # to set a delay between each iteration

import functions as tool
import latexToPDF as pdf

# https://www.conceptispuzzles.com/index.aspx?uri=puzzle/sudoku/techniques

# -Scanning techniques
# 1. Scanning in one direction:(basic + unique)
# 2. Scanning in two directions:(basic + unique)
# 3. Searching for Single Candidates: (unique)
# 4. Eliminating numbers from rows, columns and boxes: (pairs)
# 5. Searching for missing numbers in rows and columns: (basic)

# -Analyzing techniques:
# 1. Eliminating squares using Naked Pairs in a box (pairs two values)
# 2. Eliminating squares using Naked Pairs in rows and columns (pairs two values)
# 3. Eliminating squares using Hidden Pairs in rows and columns (unique)
# 4. Eliminating squares using X-Wing (X-Wing algo)


# https://www.learn-sudoku.com/advanced-techniques.html

# 1. X-Wing (X-Wing algo)
# 2. Sworldfish ()
# 3. XY Wing () 
# 4. Unique Rectangle () 
# 5. Extremely advanced techniques () 

# Sudoku vars:
grid = [[tool.Cell(x, y) for y in range(9)] for x in range(9)]
# data = [ #canonical (solved)
#     [9, 8, 4, 0, 3, 1, 0, 7, 2],
#     [6, 1, 0, 0, 0, 7, 0, 0, 0],
#     [2, 5, 7, 0, 0, 9, 8, 0, 0],
#     [3, 0, 0, 0, 6, 0, 0, 1, 0],
#     [0, 0, 0, 3, 7, 0, 9, 2, 0],
#     [0, 0, 9, 0, 0, 5, 0, 0, 0],
#     [0, 3, 0, 0, 0, 6, 0, 0, 0],
#     [0, 4, 5, 0, 1, 8, 0, 9, 6],
#     [1, 9, 6, 7, 0, 0, 2, 8, 0]
# ]
# data = [ # medium (solved)
#     [0, 0, 0, 7, 0, 0, 0, 0, 0],
#     [0, 0, 7, 0, 9, 0, 0, 1, 8],
#     [0, 0, 9, 6, 1, 0, 4, 3, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [7, 5, 0, 3, 2, 8, 0, 4, 9],
#     [4, 0, 2, 9, 0, 0, 0, 7, 5],
#     [0, 0, 6, 8, 0, 0, 0, 0, 0],
#     [0, 3, 0, 0, 0, 2, 0, 0, 0],
#     [9, 4, 0, 0, 0, 6, 0, 0, 2]
# ]
# data = [ # hard (solved)
#     [0, 0, 7, 0, 0, 0, 3, 0, 2],
#     [2, 0, 0, 0, 0, 5, 0, 1, 0],
#     [0, 0, 0, 8, 0, 1, 4, 0, 0],
#     [0, 1, 0, 0, 9, 6, 0, 0, 8],
#     [7, 6, 0, 0, 0, 0, 0, 4, 9],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 1, 0, 3, 0, 0, 0],
#     [8, 0, 1, 0, 6, 0, 0, 0, 0],
#     [0, 0, 0, 7, 0, 0, 0, 6, 3]
# ]

# data = [ # multiple solutions
#     [0, 0, 7, 0, 0, 0, 0, 0, 2],
#     [2, 0, 0, 0, 0, 5, 0, 1, 0],
#     [0, 0, 0, 8, 0, 1, 4, 0, 0],
#     [0, 1, 0, 0, 9, 6, 0, 0, 8],
#     [7, 6, 0, 0, 0, 0, 0, 4, 9],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 1, 0, 3, 0, 0, 0],
#     [8, 0, 1, 0, 6, 0, 0, 0, 0],
#     [0, 0, 0, 7, 0, 0, 0, 6, 3]
# ]

# data = [ # X-Wing
#     [0, 0, 3, 8, 0, 0, 5, 1, 0],
#     [0, 0, 8, 7, 0, 0, 9, 3, 0],
#     [1, 0, 0, 3, 0, 5, 7, 2, 8],
#     [0, 0, 0, 2, 0, 0, 8, 4, 9],
#     [8, 0, 1, 9, 0, 6, 2, 5, 7],
#     [0, 0, 0, 5, 0, 0, 1, 6, 3],
#     [9, 6, 4, 1, 2, 7, 3, 8, 5],
#     [3, 8, 2, 6, 5, 9, 4, 7, 1],
#     [0, 1, 0, 4, 0, 0, 6, 9, 2]
# ]

data = [ # XY-Wing
    [8, 0, 0, 3, 6, 0, 9, 0, 0],
    [0, 0, 9, 0, 1, 0, 8, 6, 3],
    [0, 6, 3, 0, 8, 9, 0, 0, 5],
    [9, 2, 4, 6, 7, 3, 1, 5, 8],
    [3, 8, 6, 9, 5, 1, 7, 2, 4],
    [5, 7, 1, 8, 2, 4, 3, 9, 6],
    [4, 3, 2, 1, 9, 6, 5, 8, 7],
    [6, 9, 8, 5, 3, 7, 0, 0, 0],
    [0, 0, 0, 2, 4, 8, 6, 3, 9]
]

# data = [ # expert
#     [0, 0, 0, 0, 0, 0, 9, 2, 6],
#     [0, 7, 0, 0, 9, 0, 8, 5, 0],
#     [0, 0, 1, 0, 0, 0, 0, 0, 0],
#     [0, 0, 3, 0, 0, 0, 5, 0, 0],
#     [8, 6, 0, 0, 0, 0, 0, 0, 0],
#     [5, 0, 4, 8, 0, 0, 0, 9, 0],
#     [0, 4, 0, 0, 2, 1, 0, 0, 0],
#     [6, 0, 0, 0, 0, 0, 0, 3, 0],
#     [0, 0, 0, 0, 4, 7, 0, 0, 0]
# ]

# data = [ # epmty
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0]
# ]

# --------------------------    CODE    --------------------------

# Vars:
gameRunning = True
nIte = 0

#-------    Update matrices    -------
print("Searching for solutions...")
sol = []
tool.sudokuSolution(data, sol)
tool.sol = sol[0]
tool.grid = grid

for i in range(9):
    for j in range(9):
        if data[i][j] != 0:
            grid[i][j].setValue(data[i][j], False, cleverCell=False)

#-------    Analice data    -------
if len(sol) == 0:
    print("There is no possible solution to this data :(")
    gameRunning = False
elif len(sol) == 1:
    print("Solution founded\n")
    tool.printSudoku(sol[0])
    while True:
        response = input("\nDo you want to see the steps to solve it? [yes/no]")
        if "y" in response:
            gameRunning = True
            pdf.init(data) # Start the pdf
            break
        elif "n" in response:
            gameRunning = False
            break   
else:
    print("Multiple solutions founded. All of them are:")
    pdf.init(data)
    for sols in sol: 
        print("\n")
        tool.printSudoku(sols)
        pdf.addSudokuOnLaTeX(sols, data)
    pdf.endFile(None, data)
    gameRunning = False

while gameRunning:
    #-------    Update matrix    -------
    cells = set() # Set with all undone cells
    for i in range(9):
        for j in range(9):
            if grid[i][j].getValue() == 0:
                cells.add(grid[i][j])
    
    if len(cells) == 0: # All cells filled => DONE :D
        print("\n")
        print(" Sudoku finished  ".center(40, "-"))
        print("\nHere is the solution:\n")
        tool.printSudoku(grid)
        print("\nThe solution is " + ("" if tool.checkSol(grid) else "IN") + "CORRECT")
        gameRunning = False
        print("Generating PDF with the steps to solve this sudoku:")
        pdf.endFile(grid, data) # Make the conclusion of the PDF and render the file
        print("PDF generated with all the steps")
        break # Exit the program

    nIte = nIte + 1
    print("\n\n-----------    Iteration "+ str(nIte) +"   ------------\n")
    print("Missing cells: " + str(len(cells)))
    tool.printSudoku(grid)
    pdf.newIteration(grid, data)
    print()

    discoveryMade = False # If at this iteration we discover the value of some cell, this become true

    # ------------------------------    actual algorithm   ------------------------------
    for cell in cells: # Check 3 by 3, row and col
        if cell.getValue() != 0: continue # if during this loop, this cell got it's value defined, go to next one
        # ----------    BASIC   ----------
        values = [[], [], []] # Values in row, col, 3by3

        for i in range(9):
            if i != cell.y: # Rows (x=cte) -- If not the same cell
                otherValue = grid[cell.x][i].getValue()
                if otherValue != 0 and (otherValue in cell.getPosVal()):
                    cell.removePosVal(otherValue, cleverCell=False)
                    values[0] = values[0] + [otherValue]
            if i != cell.x: # Cols (y=cte) -- If not the same cell
                otherValue = grid[i][cell.y].getValue()
                if otherValue != 0 and (otherValue in cell.getPosVal()):
                    cell.removePosVal(otherValue, cleverCell=False)
                    values[1] = values[1] + [otherValue]
            x = (cell.x // 3) * 3 + (i // 3)
            y = (cell.y // 3) * 3 + (i % 3)
            if cell.x != x or cell.y != y: # 3 by 3 -- If not the same cell
                otherValue = grid[x][y].getValue()
                if otherValue > 0 and (otherValue in cell.getPosVal()):
                    cell.removePosVal(otherValue, cleverCell=False)
                    values[2] = values[2] + [otherValue]

        if len(values[0]) > 0: # Row
            cell.addData("basic row", values[0])
        if len(values[1]) > 0: # Col 
            cell.addData("basic col", values[1])
        if len(values[2]) > 0: # 3by3
            cell.addData("basic 3 by 3", values[2])

        if len(cell.getPosVal()) == 1: # We got the value
            cell.setValue(list(cell.getPosVal())[0])
            discoveryMade = True
            continue

        # ----------    UNIQUE   ----------
        unique = [set([i for i in range(1, 10, 1)]) for i in range(3)] # unique row, col, 3by3
        for i in range(9):
            if i != cell.y: # for each piece on the row (x=cte) -- if not same cell
                valueToFilter = grid[cell.x][i].getPosVal() # Set with values on other cell
                if grid[cell.x][i].getValue() != 0: # If looking at cell with defined value, valueToFilter should be the actual value
                    valueToFilter = set([grid[cell.x][i].value]) # valueToFilter => numbers here are not unique on our cell
                unique[0] = unique[0].difference(valueToFilter) # All common are not unique => del them
            if i != cell.x: # for each piece on the Col (y=cte) -- if not same cell
                valueToFilter = grid[i][cell.y].getPosVal() # Set with possible values of other cell
                if grid[i][cell.y].getValue() != 0: # If looking at cell with defined value, valueToFilter should be the actual value
                    valueToFilter = set([grid[i][cell.y].value]) # valueToFilter => numbers here are not unique on our cell                
                unique[1] = unique[1].difference(valueToFilter) # All common are not unique => del them
            x = (cell.x // 3) * 3 + (i // 3)
            y = (cell.y // 3) * 3 + (i % 3)
            if cell.x != x or cell.y != y:
                valueToFilter = grid[x][y].getPosVal() # Set with values on other cell
                if grid[x][y].getValue() != 0: # If looking at cell with defined value, valueToFilter should be the actual value
                    valueToFilter = set([grid[x][y].value]) # valueToFilter => numbers here are not unique on our cell
                unique[2] = unique[2].difference(valueToFilter) # All common are not unique => del them

        if len(unique[0]) == 1: # If only one value is unique -> should be the value
            uniqueValue = list(unique[0])[0]
            if uniqueValue in cell.getPosVal(): # if this value is a possible one, make it the value of the cell (This should always be true)
                cell.addData("unique row", uniqueValue)
                cell.setValue(uniqueValue)
                discoveryMade = True
                continue
            else:
                print("ERROR at unique row")
        if len(unique[1]) == 1: # If only one value is unique -> should be the value
            uniqueValue = list(unique[1])[0]
            if uniqueValue in cell.getPosVal(): # if this value is a possible one, make it the value of the cell (This should always be true)
                cell.addData("unique col", uniqueValue)
                cell.setValue(uniqueValue)
                discoveryMade = True
                continue
            else:
                print("ERROR at unique col")
        if len(unique[2]) == 1: # If only one value is unique -> should be the value
            uniqueValue = list(unique[2])[0]
            if uniqueValue in cell.getPosVal(): # if this value is a possible one, make it the value of the cell (This should always be true)
                cell.addData("unique 3 by 3", uniqueValue)
                cell.setValue(uniqueValue)
                discoveryMade = True
                continue
            else:
                print("ERROR at unique 3 by 3")

    # ---------------------    advanced algorithm   ---------------------

    # ----------    PAIRS   ----------
    # Format:
    #   - "pair cell": This cell is part of a pair
    #   - "pair val" : This cell is affected by a pair of cells
    
    pairs = [set() for i in range(3)] # Set with all pairs found on the sudoku
    
    for t in range(3): # For each type of zone: 0 = row, 1 = col, 2 = 3by3
        for z in range(9): # For each row, col or 3by3 => for each zone
            candidates = [] # set of pairs on this zone
            valuesToTest = set([i for i in range(1, 10, 1)]) # Values that is possible to make a pair with
            for i in range(8): # for each cell in zone but last one
                if len(valuesToTest) == 0: # If not more values to test, go to next zone
                    break
                cC1 = [ # Coordinates of cell1
                    [z, i], # Row: [cte, i]
                    [i, z], # Col: [i, cte]
                    [(z // 3) * 3 + (i // 3), (z % 3) * 3 + (i % 3)] # 3by3 [row(sector) + row(i), col(sector) + col(i)]
                ]
                cell1 = grid[cC1[t][0]][cC1[t][1]]
                if cell1.getValue() != 0: # If cell1 has defined value
                    valuesToTest.discard(cell1.getValue()) # No pair can be formed with this value, remove it from possible values
                else: # If cell1 has no value defined
                    for val in cell1.getPosVal(): # For values to test that are on cell1.posVal
                        if val not in valuesToTest: # If not on this set, this val can not form any pairs
                            continue # Go to the next val
                        posCandidates = set() # Collection of posible candidates
                        for j in range(i + 1, 9): # For the rest of the cells on the zone
                            cC2 = [ # Coordinates of cell2
                                [z, j], # Row
                                [j, z], # Col
                                [(z // 3) * 3 + (j // 3), (z % 3) * 3 + (j % 3)] # 3by3
                            ]
                            cell2 = grid[cC2[t][0]][cC2[t][1]]
                            if cell2.getValue() == 0 and val in cell2.getPosVal(): # if cell2 has no value defined and has that val
                                posCandidates.add(cell2) # This candidate has this val as posVal
                        
                        if len(posCandidates) != 1: # If more than one or no one with this val => no pair
                            valuesToTest.discard(val) # remove this value, because it can not form any valid pair
                            continue # Go to the next val
                        else: # If only one cell with same val (no one on the zone has this val except cell1 and cell2)
                            # We have a valid pair.
                            cell2 = list(posCandidates)[0]
                            if t != 2 or (cell1.x != cell2.x and cell1.y != cell2.y): # If not in 3by3 or (not horizontal nor vertical in 3by3)
                                # print("Pair " + ["ROW", "COL", "3BY3"][t] + " founded with the value " + str(val) + ": " + str(cell1.getPos()) + ", " + str(cell2.getPos()))
                                cell1.addData("pairs cell", cell2, val)
                                cell2.addData("pairs cell", cell1, val)
                                cell1.addPair(cell2, val)
                                cell2.addPair(cell1, val)
                                candidates.append((cell1, cell2, val)) # Added

                                if t == 2: continue # if 3by3, skip this last part
                                # if here: all cells on the line can not be this value
                                for k in range(9): # for all cells on line (1º = same cell => start at 2º)
                                    cC = [ # Coordinates of cell
                                        [z, j], # Row
                                        [j, z], # Col
                                    ]
                                    cell = grid[cC2[t][0]][cC2[t][1]]
                                    if (cell != cell1) and (cell != cell2) and cell.getValue() == 0 and (val in cell.getPosVal()):
                                        cell.addData("pairs val", cell1, cell2, val)
                                        cell.removePosVal(val)
            pairs[t].update(candidates) # Add the candidates to pairs
            i = 0
            while i < len(candidates):
                c1 = set(candidates[i][0:2]) # pair of 2 cells
                n = 0 # ocurrences of the same pair
                for j in range(i + 1, len(candidates)): # for the rest of candidates pairs
                    c2 = set(candidates[j][0:2]) #
                    if c1 == c2: n = n + 1 # Count the times the pair c1 is repeated
                if n == 1: # if there are exacly 2 times the pair c1 is founded => Double pair
                    values = [candidates[i][2], candidates[i + 1][2]] # The values
                    cells = list(c1)
                    # print("** VALID DOUBLE PAIR: cells: " + str(cells[0].getPos()) + ", " + str(cells[1].getPos()) + "; values: " + str(candidates[i][2]) + ", " + str(candidates[i+1][2]))
                    cells[0].addData("pairs two", cells[1], values) 
                    cells[0].setPosVal(set(values)) # Update the possible values
                    cells[1].addData("pairs two", cells[0], values)
                    cells[1].setPosVal(set(values)) # Update the possible values
                    i = i + 1
                elif n > 1:
                    i = i + n - 1 # Skip all pairs not valid on next iteration
                i = i + 1

    # print(pairs)
    # ----------    X Wing   ----------
    # Row:
    #   - 2 pairs
    #   - With the same value
    #   - On diferent rows
    #       - but same col coordinates (forming rectangle): pair1 = ((1, 2), (1, 5), 4) and pair2 = ((4, 2), (4, 5), 4)
    #   - These does not form col pairs

    for t in range(2): # For each type of X-Wing: 0 = Row; 1 = Col
        for p1 in pairs[t]: # For each pair made on a Row or Col (format of p: (cell1, cell2, value))
            value = p1[2]
            matches = [set(), set()] # sets with valid 
            for p2 in pairs[t]: # For the rest of the pairs
                if p1 == p2: continue # If same pair, go to next one
                if p2[2] != value: continue # If not same value, go to next one
                if t == 0 and (p1[0].y != p2[0].y or p1[1].y != p2[1].y): continue # If not on the same column when using X-Wing row, next one
                if t == 1 and (p1[0].x != p2[0].x or p1[1].x != p2[1].x): continue # If not on the same row when using X-Wing col, next one
                for i in range(2):
                    if (p1[i], p2[i], value) not in pairs[(t + 1) % 2]: # If (0=right, 1=left) side is not linked on al col pair
                        matches[i].add(p2)
            for i in range(2):
                if len(matches[i]) == 1: # If only one match
                    p2 = next(iter(matches[i])) # Get the pair
                    print("X-Wing " + ["row", "col"][t] + " with value " + str(value) + " and pos " + str(i) + ":" + \
                        "\n  - p1: " + str(p1[0].getPos()) + ", " + str(p1[1].getPos()) + \
                        "\n  - p2: " + str(p2[0].getPos()) + ", " + str(p2[1].getPos()))
                    for j in range(9): # For each row or col
                        if t == 0: # X-Wing row
                            c = grid[j][p1[i].y] # Go on cols
                        else: # t == 1: X-Wing col
                            c = grid[p1[i].x][j] # Go on rows
                        if c != p1[i] and c != p2[i] and value in c.getPosVal(): # If c is not one on the cells on consideration and the value can be removed
                            print(c.getPos())
                            c.addData("X-Wing " + ["row", "col"][t], p1, p2, value) # Add Data
                            c.removePosVal(value) # Remove this value from possible values

    # ----------    XY Wing   ----------
    # Row:
    #   - two cells (c1, c2) with a value v1 (NOT NECCESARRY A PAIR)
    #       - No multiple pairs on this pair (???)
    #       - len(posVal) on both is 2
    #   - One of the members (c1) of the pair have another relation on a 3by3 pair: (c1, c3) with value v2 (NOT SURE IF PAIR)
    #       - c3.x != c1.x (therefore, c3.x != c1.x)
    #       - len(c3.posVal) = 2
    #       - both c2 and c3 has as second posVal v2
    #   If all OK: cells at (c3.x, T),, T = Sector(c2).y's can not be v2

    # for p in pairs[0]:
    #     if p[0].getPos() == (0, 2): print("no worries")
    #     if len(p[0].getPosVal()) > 2 or len(p[1].getPosVal()) > 2: continue # len(posVal) on both should be 2
    #     singlePair = True
    #     for i in range(9):
    #         if i == p[2]: continue # Skip the same pair
    #         if (p[0], p[1], i) in pairs[0]:
    #             singlePair = False
    #             break
    #     if not singlePair: continue # If double pair (pair with more than one value), go to next pair
    #     v1 = p[2]
    #     posV2 = [next(iter(p[i].getPosVal() - set([v1]))) for i in range(2)] # Get possible values of v2
    #     print("Pair Row" + str(p[0].getPos()) + " and " + str(p[1].getPos()) + " with value " + str(value) + \
    #         "\n  " + str(p[0].getPosVal()) + " --- " + str(p[1].getPosVal()) + \
    #         "\n  v1: " + str(v1) + "; posV2: " + str(posV2))
    #     c3pair = None
    #     for posC3 in pairs[2]: # for each pair made on a 3by3
    #         v2 = posC3[2] # Theoretical value of v2
    #         if p[0] in posC3 and v2 in posV2: # If pair (c1, c3) with a valid v2 value
    #             # c3pair = posC3
    #             # print("Pair Row" + str(p[0].getPos()) + " and " + str(p[1].getPos()) + " with value " + str(value) + \
    #             #     "\n  " + str(p[0].getPosVal()) + " --- " + str(p[1].getPosVal()) + \
    #             #     "\n  v1: " + str(v1) + "; posV2: " + str(posV2))
    #             print("founded")






    response = input("Continue?")
    # response = ""
    if response == "exit" or response == "e":
        gameRunning = False
        pdf.toPDF() # Render the pdf file
    elif "viewData" in response: 
        while True:
            response = input("Cell?")
            if "e" in response: # exit, e, ex
                break
            else: # 58 => view data on the cell (5,8)
                print(*grid[int(response[0])][int(response[1])].dataToText(), sep="\n")
                print(*grid[int(response[0])][int(response[1])].posVal, sep=", ")
                print(grid[int(response[0])][int(response[1])].value)

print("\nThank you for using this code. I hope you liked it.")
print("If you want to see more code like this, visit\nhttps://github.com/Jkutkut/Jkutkut-projects")