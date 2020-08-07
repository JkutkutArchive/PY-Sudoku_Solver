#!/usr/bin/env python3

import functions as tool
import latexToPDF as pdf
import input as inputData

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
# 2. XY Wing (XY-Wing algo) 
# 3. Unique Rectangle (Unique rectangle algo) 
# 4. Sworldfish (swordfish)
# 5. Extremely advanced techniques (??) 

# - Triplets and Quads

# Sudoku vars:
grid = [[tool.Cell(x, y) for y in range(9)] for x in range(9)]
data = inputData.data

# --------------------------    CODE    --------------------------

# Functions
def swordfish(v, pairs, iniPos, currentPos, cellToPosF, cells=[]):
    '''Finds a list of pairs valid to form a swordfish.
    
    - v (int): value that all pairs must have as their pair-value
    - pairs (list): list of pairs made on rows or columns (one type only)
    - iniPos (int): first cell's coordinate (therefore, the goal coordinate)
    - currentPos (int): current cell's coordinate
    - cellToPosF (function): function to get the coordinate of a cell (this way, this code can be used for rows and columns)
    - cells (list): To keep track of the path taken to make the loop (also the output)

    Returns:
    list: With the cells used to make this algorithm possible (cellsPos)
    '''

    if len(pairs) != 0: # If still pairs to search (and still running this algo)
        if iniPos == currentPos: # If loop made (may be a correct swordfish)
            return [] if len(cells) == 2 else cells # Return the sol only if it is not a double pair
        for p in pairs: # For the rest of the pairs
            if p[2] != v: continue # if different value, no possible to form it with this pair, go to the next one
            for i in range(2): # Try to continue the loop with both cells as connector
                if currentPos == cellToPosF(p[i]): # If I can continue this path with the first member of the pair
                    result = swordfish(v, pairs - set([p]), iniPos, cellToPosF(p[(i + 1) % 2]), cellToPosF, cells + [p[i], p[(i + 1) % 2]])
                    if len(result) > 0: return result # If correct swordfish found return that solution. Else, continue searching
    # If here, not possible or no more pairs to checks
    return []

# Vars:
gameRunning = True
nIte = 0 # Number of iterations
nNoNewValues = 0 # Number of consecutive iterations with nNewValues = 0
tool.nNewValues = 0 # Number of cells defined on a single interation
print(tool.nNewValues) 


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

    if tool.nNewValues == 0: # If iteration without new values
        nNoNewValues = nNoNewValues + 1
        if nNoNewValues == 3: # If algo is not working 
            print("\n\n")
            print("Congratulations, you have found a sudoku this algorithm can not solve with steps")
            print("However, here is the solution:\n")
            tool.printSudoku(sol[0])
            break
    else: # Reset variables 
        nNoNewValues = 0 
        tool.nNewValues = 0

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
                    cell.removePosVal(otherValue)
                    values[0] = values[0] + [otherValue]
            if i != cell.x: # Cols (y=cte) -- If not the same cell
                otherValue = grid[i][cell.y].getValue()
                if otherValue != 0 and (otherValue in cell.getPosVal()):
                    cell.removePosVal(otherValue)
                    values[1] = values[1] + [otherValue]
            x = (cell.x // 3) * 3 + (i // 3)
            y = (cell.y // 3) * 3 + (i % 3)
            if cell.x != x or cell.y != y: # 3 by 3 -- If not the same cell
                otherValue = grid[x][y].getValue()
                if otherValue > 0 and (otherValue in cell.getPosVal()):
                    cell.removePosVal(otherValue)
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
    
    pairs = [set() for i in range(3)] # list with Sets with all pairs found on the sudoku (pairs = [set(row pairs, col pairs, 3by3 pairs)])
    
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

    
    # ----------    TRIPLETS AND QUADS   ----------
    # what is a triplet:
    #   - 3 cells on 3by3, row or col.
    #   - 3 values in game
    #   - at least 1 value on all cells, rest pairs:
    #       - 3 triple value
    #       - 2 triple value + pair
    #       - 1 triple value + 2 pairs (no double pair)
    # 
    # 
    # 
    # If all correct, those cells can only be these values



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
                    # print("X-Wing " + ["row", "col"][t] + " with value " + str(value) + " and pos " + str(i) + ":" + \
                    #     "\n  - p1: " + str(p1[0].getPos()) + ", " + str(p1[1].getPos()) + \
                    #     "\n  - p2: " + str(p2[0].getPos()) + ", " + str(p2[1].getPos()))
                    for j in range(9): # For each row or col
                        if t == 0: # X-Wing row
                            c = grid[j][p1[i].y] # Go on cols
                        else: # t == 1: X-Wing col
                            c = grid[p1[i].x][j] # Go on rows
                        if c != p1[i] and c != p2[i] and value in c.getPosVal(): # If c is not one on the cells on consideration and the value can be removed
                            print(c.getPos())
                            c.addData("X-Wing " + ["row", "col"][t], p1, p2, value) # Add Data
                            c.removePosVal(value) # Remove this value from possible values



    pv2Cells = [] # list of sets (1 per sector 3by3)
    for s in range(9): # for each sector
        sectorC = set() # here the cells of the sector will be stored
        for p in range(9): # for each cell on sector
            i = (s // 3) * 3 + (p // 3)
            j = (s % 3) * 3 + (p % 3)
            if len(grid[i][j].getPosVal()) == 2: # If value not defined and only 2 possible values
                sectorC.add(grid[i][j])
        pv2Cells.append(sectorC) # Add it to the rest of candidates


    # ----------    XY Wing   ----------
    # Row:
    #   - two cells (c1, c2) with a value v1
    #       - Not neccesary a PAIR from pairs 
    #       - On the same row
    #       - len(posVal) on both is 2 => (c1 and c2 can not share more than one posVal)
    #   - One of the members (c1) of the pair have another relation on the 3by3: (c1, c3) with value v2
    #       - c1 and c3 not neccesary a PAIR from pairs 
    #       - c3.x != c1.x (therefore, c3.x != c1.x)
    #       - len(c3.posVal) = 2
    #       - both c2 and c3 has as second posVal v3 in common
    #   If all OK: cells at (c3.x, T),, T = Sector(c2).y's can not be v2

    # Conclusion:
    #  - Cells: c1, c3, c2
    #  - Links by value:
    #    - v1: value in c1 and c2
    #    - v2: value in c1 and c3
    #    - v3: value in c2 and c3

    for s in range(9): # for each sector (len(pv2Cells))
        # print("\n----New Sector:----")
        for c1 in pv2Cells[s]: # For each possible c1
            for c3 in pv2Cells[s]: # Look for c3 (note that the pair (c1, c3) is formed as well as (c3, c1)) => always work based on c1 and c3
                if c3 == c1: continue # Skip the same cell
                if c3.x == c1.x: continue # If both cells on the same row, not valid 
                v2 = c1.getPosVal() & c3.getPosVal() # Get common possibles values
                if len(v2) != 1: continue# If no values in common or to many, continue to next one 
                # If here, c3 is valid
                v1 = next(iter(c1.getPosVal() - v2)) # Get v1 by removing v2 from possibles values of c1
                v3 = next(iter(c3.getPosVal() - v2)) # Get v3 by the method
                v2 = next(iter(v2)) # convert set to single value

                c2Sector = [(s + i) % 3 for i in range(1, 3, 1)] # Get the sectors to check (OJO: Row only)
                # print(str(s) + " -> " + str(c2Sector))
                for s2 in c2Sector: # for each sector in possible sectors for c2
                    for c2 in pv2Cells[s2]: # for each cell on possible sector of c2
                        if c2.x != c1.x: continue # If not on the same row, not valid
                        if v1 not in c2.getPosVal() or v3 not in c2.getPosVal(): continue # If the values of c2 does not make a valid XY-Wing, continue seaching 
                        # if here, c2 is valid => XY-Wing can be applied!! 
                        # print("\nFounded!!\nv1= " + str(v1) + "; v2 = " + str(v2)+ "; v3 = " + str(v3))
                        # print("c1: " + c1.cellToString(printValue=False, printData=False, printPairs=False))
                        # print("c3: " + c3.cellToString(printValue=False, printData=False, printPairs=False))
                        # print("c2: " + c2.cellToString(printValue=False, printData=False, printPairs=False))

                        for i in range(s2 * 3, s2 * 3 + 3): # for all cells at c3.x on the sector where is c2
                            cell = grid[c3.x][i]
                            if v3 in cell.getPosVal():
                                cell.addData("XY-Wing", [c1, c2, c3], [v1, v2, v3]) # Row
                                cell.removePosVal(v3)
                
                c2Sector = [(s // 3) * 3 + i for i in range(1, 3, 1)] # Get the sectors to check (OJO: Column only)
                for s2 in c2Sector: # for each sector in possible sectors for c2
                    for c2 in pv2Cells[s2]: # for each cell on possible sector of c2
                        if c2.y != c1.y: continue # If not on the same col, not valid
                        if v1 not in c2.getPosVal() or v3 not in c2.getPosVal(): continue # If the values of c2 does not make a valid XY-Wing, continue seaching 
                        # if here, c2 is valid => XY-Wing can be applied!! 

                        for i in range(s2 * 3, s2 * 3 + 3): # for all cells at c3.y on the sector where is c2
                            cell = grid[i][c3.y]
                            if v3 in cell.getPosVal():
                                cell.addData("XY-Wing", [c1, c2, c3], [v1, v2, v3]) # Row
                                cell.removePosVal(v3)


    # ----------    Unique rentangles   ----------
    # We look for:
    #   - 4 cells: c1, c2, c3, c4 
    #       - All has len(posVal) == 2 except 1 that has more (c4)
    #       - All has v1 and v2 as their values
    #       - c1 on same sector (s1) than c3
    #       - c2 on same sector (s2) than c4
    #   - Two options:
    #       - Row rect:
    #           - c1.y == c3.y and c2.y == c4.y
    #           - c1.x == c2.x and c3.x == c4.x
    #       - Col rect:
    #           - c1.x == c3.x and c2.x == c4.x
    #           - c1.y == c2.y and c3.y == c4.y


    sectorsToCheck = [[0],[-1,1]] # Based on the index (sector.x or sector.y you are), get how much you must move to check neighbours
    # for s in range(9): # for each sector (len(pv2Cells))
    for s1 in range(1, 2):
        for c1 in pv2Cells[s1]: # For each possible c1
            v = c1.getPosVal().copy() # Get v1 and v2 on a set
            for c3 in pv2Cells[s1]:
                if c1 == c3: continue # Skip itself
                if v != c3.getPosVal(): continue # They must have exacly 2 identical posValues
                # If here, may be valid c3 (depends on position in relation with c1)

                if c1.y == c3.y: # Row rect:    
                    for m in sectorsToCheck[(s1 % 3) % 2]: # for each move to go to a possible s2
                        for c2 in pv2Cells[s1 - m]: # for each possible c2 in possible s2
                            if c2.x != c1.x: continue
                            if v != c2.getPosVal(): continue # Not valid possible values for v2
                            #If here, c2 is valid
                            c4 = grid[c3.x][c2.y]
                            if v >= c4.getPosVal(): continue # If at least does not contain the values in v, not correct v4
                            # If here, we have a Unique rectangle!!
                            c4.addData("Unique rectangle", [c1, c2, c3], list(v)) # add the data
                            print(c4.cellToString(printValue=True))
                            for vn in v: c4.removePosVal(vn) # Remove the values
                            # print("\nFounded!!\nv = " + str(v))
                            # print("c1: " + c1.cellToString(printValue=False, printData=False, printPairs=False))
                            # print("c3: " + c3.cellToString(printValue=False, printData=False, printPairs=False))
                            # print("c2: " + c2.cellToString(printValue=False, printData=False, printPairs=False))
                            # print("c4: " + c4.cellToString(printValue=False, printData=False, printPairs=False))


    # ----------    Swordfish   ----------
    # -Row: 
    #   - Looking for 2 row pairs: p1, p2 
    #       - p1.x != p2.x
    #       - both pairs are made based on the same value: v
    #       - one of the cells in each pair has to be alinged on the same column
    #   - That way, each cell on that colum can not be that value v
    # THIS CODE MAY BE SUTIABLE FOR X-WING?

    # pairss = pairs[0:2].copy()
    f = [lambda x: x.y, lambda x: x.x]
    for i in range(2):
        while len(pairs[i]) > 3:
            p = pairs[i].pop() # Remove and return element to pairs
            value = p[2]
            result = swordfish(value, pairs[i], p[0].y, p[1].y, f[i])
            if len(result) == 0: continue # If not valid swordfish, continue
            # If here, there is a valid swordfish on the coordinates "coordinates"
            result = list(p[0:2]) + result # result + pair of cells
            # print([c.getPos() for c in result])
            coordinates = set([c.y for c in result])
            # print(coordinates)
            for coord in coordinates: # For each valid coordinate
                for j in range(9): # for all the line/col
                    cell = grid[j][coord]
                    if cell in result: continue # skip the cells used to make this algorithm
                    if value in cell.getPosVal(): # If the value can be removed from posVal
                        cell.addData("Swordfish row", result, coordinates, value) # ["Swordfish <TYPE>", result, coordinates, v]
                        cell.removePosVal(value) # Remove it from there
                        # print(cell.cellToString())


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
                print(grid[int(response[0])][int(response[1])].cellToString())

print("\nThank you for using this code. I hope you liked it.")
print("If you want to see more code like this, visit\n\nhttps://github.com/Jkutkut/Jkutkut-projects\n\n")