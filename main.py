#!/usr/bin/env python3
# import pygame # library to generate the graphic interface
import numpy as np # library to handle matrices
import time # to set a delay between each iteration
import math as m

import functions as tool

# https://www.conceptispuzzles.com/index.aspx?uri=puzzle/sudoku/techniques

# add:

# -Scanning techniques
# 1. Scanning in one direction:(rows and cols-> solved)
# 2. Scanning in two directions:(rows and cols-> solved)
# 3. Searching for Single Candidates: (actual method for 1,2 -> posVal.length = 1)
# 4. Eliminating numbers from rows, columns and boxes: (Analize -> changeProduced)
# 5. Searching for missing numbers in rows and columns: (unique rows & cols)

# -Analyzing techniques:
# 1. Eliminating squares using Naked Pairs in a box
# 2. Eliminating squares using Naked Pairs in rows and columns
# 3. Eliminating squares using Hidden Pairs in rows and columns
# 4. Eliminating squares using X-Wing(difficult puzzle)


# Sudoku vars:
# grid = np.matrix([[tool.Cell(x, y) for y in range(9)] for x in range(9)])
grid = [[tool.Cell(x, y) for y in range(9)] for x in range(9)]
data = [ #canonical
    [9, 8, 4, 0, 3, 1, 0, 7, 2],
    [6, 1, 0, 0, 0, 7, 0, 0, 0],
    [2, 5, 7, 0, 0, 9, 8, 0, 0],
    [3, 0, 0, 0, 6, 0, 0, 1, 0],
    [0, 0, 0, 3, 7, 0, 9, 2, 0],
    [0, 0, 9, 0, 0, 5, 0, 0, 0],
    [0, 3, 0, 0, 0, 6, 0, 0, 0],
    [0, 4, 5, 0, 1, 8, 0, 9, 6],
    [1, 9, 6, 7, 0, 0, 2, 8, 0]
]

# sol = [
#     [9, 8, 4, 5, 3, 1, 6, 7, 2],
#     [6, 1, 3, 8, 2, 7, 5, 4, 9],
#     [2, 5, 7, 6, 4, 9, 8, 3, 1],
#     [3, 7, 8, 9, 6, 2, 4, 1, 5],
#     [5, 6, 1, 3, 7, 4, 9, 2, 8],
#     [4, 2, 9, 1, 8, 5, 7, 6, 3],
#     [8, 3, 2, 4, 9, 6, 1, 5, 7],
#     [7, 4, 5, 2, 1, 8, 3, 9, 6],
#     [1, 9, 6, 7, 5, 3, 2, 8, 4]
# ]


# data = [ #contiune adding techniques
#     [3, 8, 9, 4, 6, 1, 0, 0, 0],
#     [7, 1, 5, 8, 0, 2, 4, 3, 6],
#     [2, 0, 4, 0, 3, 7, 9, 1, 8],
#     [0, 3, 6, 7, 2, 9, 0, 4, 1],
#     [9, 2, 0, 6, 0, 4, 5, 7, 3],
#     [1, 4, 7, 3, 5, 8, 6, 9, 2],
#     [6, 7, 1, 2, 4, 5, 3, 8, 9],
#     [8, 5, 0, 9, 7, 0, 1, 0, 4],
#     [4, 9, 0, 1, 0, 0, 0, 0, 0],
# ]
# data = [ # contiune adding techniques
#     [0, 0, 9, 2, 0, 3, 8, 0, 0],
#     [0, 0, 0, 0, 0, 9, 0, 0, 0],
#     [4, 0, 8, 6, 0, 5, 1, 0, 3],
#     [0, 0, 0, 0, 0, 0, 9, 0, 4],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 5, 0, 2],
#     [0, 0, 6, 5, 0, 2, 3, 0, 7],
#     [0, 0, 1, 0, 0, 0, 0, 0, 0],
#     [0, 0, 5, 4, 0, 8, 6, 0, 0],
# ]

# --------------------------    CODE    --------------------------

# Vars:
gameRunning = True

#-------    Update matrices    -------
sol = []
tool.sudokuSolution(data, sol)

for i in range(9):
    for j in range(9):
        if data[i][j] != 0:
            grid[i][j].setValue(data[i][j], False)

if len(sol) == 0:
    print("There is no possible solution to this data :(")
    gameRunning = False
elif len(sol) == 1:
    print("Solution founded")
    while True:
        response = input("Do you want to see the steps to solve it? [yes/no]")
        if "y" in response:
            gameRunning = True
            break
        elif "n" in response:
            print("Okay, here is the solution:\n\n")
            tool.printSudoku(sol[0])
            gameRunning = False
            break
else:
    print("Multiple solutions founded. All of them are:")
    for sols in sol: 
        print("\n")
        tool.printSudoku(sols)
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
        print("\nHere is the solution:")
        tool.printSudoku(grid)
        print("\nThe solution is " + ("" if tool.checkSol(grid) else "IN") + "CORRECT")
        gameRunning = False
        break

    print()
    print("    Iteration    ".center(40,"-"))
    print()
    tool.printSudoku(grid)
    print()

    # ------------------------------    actual algorithm   ------------------------------
    for cell in cells: # Check 3 by 3, row and col
        values = [[], [], []] # Values in row, col, 3by3
        
        for i in range(9):
            if i != cell.y: # Rows (x=cte) -- If not the same cell
                otherValue = grid[cell.x][i].getValue()
                if otherValue > 0 and (otherValue in cell.getPosVal()):
                    cell.getPosVal().remove(otherValue)
                    values[0] = values[0] + [otherValue]
            if i != cell.x: # Cols (y=cte) -- If not the same cell
                otherValue = grid[i][cell.y].getValue()
                if otherValue > 0 and (otherValue in cell.getPosVal()):
                    cell.getPosVal().remove(otherValue)
                    values[1] = values[1] + [otherValue]
            x = (cell.x // 3) * 3 + (i // 3)
            y = (cell.y // 3) * 3 + (i % 3)
            if cell.x != x or cell.y != y: # 3 by 3 -- If not the same cell
                otherValue = grid[x][y].getValue()
                if otherValue > 0 and (otherValue in cell.getPosVal()):
                    cell.getPosVal().remove(otherValue)
                    values[2] = values[2] + [otherValue]

        if len(values[0]) > 0: # Row
            cell.addData(["basic row", values])
        if len(values[1]) > 0: # Col 
            cell.addData(["basic col", values])
        if len(values[2]) > 0: # 3by3
            cell.addData(["basic 3 by 3", values])

        if len(cell.getPosVal()) == 1: # We got the value
            cell.setValue(list(cell.getPosVal())[0])
            break



        #----------------------------

        values = []
        unique = set([i for i in range(1, 10, 1)])
        for i in range(9): # for each piece on the row (x=cte)
            if i != cell.x: # if not same cell
                valueToFilter = grid[cell.x][i].getPosVal() # Set with values on other cell
                if grid[cell.x][i].getValue() != None: # If looking at cell with defined value, valueToFilter should be the actual value
                    valueToFilter = set([grid[cell.x][i].value])                    
                # valueToFilter => numbers here are not unique on our cell
                unique = unique.difference(valueToFilter) # All common are not unique => del them            
        if len(unique) == 1: # If only one value is unique -> should be the value
            uniqueValue = list(unique)[0]
            if uniqueValue in cell.getPosVal(): # if this value is a possible one, make it the value of the cell (This should always be true)
                cell.addData(["unique row", uniqueValue])
                cell.setValue(uniqueValue)
                break
            else:
                print("ERROR at unique row")

        values = []
        unique = set([i for i in range(1, 10, 1)])
        for i in range(9): # for each piece on the Col (y=cte)
            if i != cell.x: # if not same cell
                valueToFilter = grid[i][cell.y].getPosVal() # Set with possible values of other cell
                if grid[i][cell.y].getValue() != None: # If looking at cell with defined value, valueToFilter should be the actual value
                    valueToFilter = set([grid[i][cell.y].value])                    
                # valueToFilter => numbers here are not unique on our cell
                unique = unique.difference(valueToFilter) # All common are not unique => del them
        if len(unique) == 1: # If only one value is unique -> should be the value
            uniqueValue = list(unique)[0]
            if uniqueValue in cell.getPosVal(): # if this value is a possible one, make it the value of the cell (This should always be true)
                cell.addData(["unique col", uniqueValue])
                cell.setValue(uniqueValue)
                break
            else:
                print("ERROR at unique col")

        values = []
        unique = set([i for i in range(1, 10, 1)])
        for i in range(3):
            for j in range(3):
                x = m.floor(cell.x / 3) * 3 + i
                y = m.floor(cell.y / 3) * 3 + j
                if cell.x != x or cell.y != y:
                    valueToFilter = grid[x][y].getPosVal() # Set with values on other cell
                    if grid[x][y].getValue() != None: # If looking at cell with defined value, valueToFilter should be the actual value
                        valueToFilter = set([grid[x][y].value])                    
                    # valueToFilter => numbers here are not unique on our cell
                    unique = unique.difference(valueToFilter) # All common are not unique => del them
        if len(unique) == 1: # If only one value is unique -> should be the value
            uniqueValue = list(unique)[0]
            if uniqueValue in cell.getPosVal(): # if this value is a possible one, make it the value of the cell (This should always be true)
                cell.addData(["unique 3 by 3", uniqueValue])
                cell.setValue(uniqueValue)
                break
            else:
                print("ERROR at unique 3 by 3")


    # response = input("Continue?")
    response = ""
    if response == "exit":
        gameRunning = False
    elif "viewData" in response: 
        while True:
            response = input("Cell?")
            if "e" in response: # exit, e, ex
                break
            else: # 58 => view data on the cell (5,8)
                print(*grid[int(response[0])][int(response[1])].data, sep="\n")
                print(*grid[int(response[0])][int(response[1])].posVal, sep=", ")
                print(grid[int(response[0])][int(response[1])].value)



#     //***************************    actual algorithm    ***************************
      
#       //if posVal.length == 1 -> show value
#       if (setS.length > 0 && setS[i].posVal.length == 1) { //if posVal.length == 1 -> show value
#         // if(printCoords(setS[i]) == "(7, 8)") console.log(printCoords(setS[i], setS[i].posVal[0]) + " with setS[i].posVal.length in " + i + " index");
        
#         setS = setValueInArray(setS, i, setS[i].posVal[0]);
#         i = (i == 0) ? i : i - 1; //if I remove nº element, all >n elements shift
#       }
      
      
#       //debug
#       if (setS.length > 0) setS[i].show(color(0, 200, 100)); //debug
#     }


#     //++++++++++++++++++++  analyze  ++++++++++++++++++++
#     //when all checked and trivial moves done,

#     //console.log("ANALYZE");

#     //get pairs
#     //also if 3 or more like 13 34 14-> 2 pairs

#     //~~~~~~~~~~~~~~~~~~~~ get Pairs V2 ~~~~~~~~~~~~~~~~~~~~
#     /*
#     What i know about pairs:
#       - have unique values in sector
#       - have unique values in row if pair in row
#       - have unique values in col if pair in col
#       - Pair can be at max 12 23 34 45 56 67 78 89 19
#         [12, 78, 23]
#         [19, 89, 34]
#         [56, 67, 45]
        
#       - if i search for each number in sector and only 2 spots with that value -> new candidate
#       - if candidate is in row && also candidate in row -> new pair
#     */
    
    
#     let pairs = [];//to store candidates (2D -> [[spot, spot], [spot, spot]...])
    
#     //all 3by3s
#     for(let w = 0; w < 9; w++){//for all 9 sectors
#       //console.log("in sector " + w);
#       let candidates = [];
#       for(let i = 0; i < 9; i++){//index
#         let spotsIn3b3 = []; //store in i index the spot with i val in posVal
#         for (let j = 0; j < 3; j++) {
#           for (let k = 0; k < 3; k++) {
#             let x = (w % 3) * 3 + j;//works
#             let y = Math.floor(w / 3) * 3 + k;//works
#             //console.log(printCoord(x,y, grid[x][y].posVal + " => " + grid[x][y].posVal.indexOf(i)));
#             if(grid[x][y].value == undefined &&
#                grid[x][y].posVal.indexOf(i) != -1){
#               spotsIn3b3.push(grid[x][y]);//add it to possible candidates
#             }
#           }
#         }
        
#         if(spotsIn3b3.length == 2){//if candidate (2 spots)
#           candidates.push(spotsIn3b3);
#         }
#       }
#       if(candidates.length > 1){//if new candidates
#         for(let i = 0; i < candidates.length; i++){//remove duplicates
#           if(i + 1 < candidates.length &&
#              candidates[i][0].equals(candidates[i + 1][0]) &&
#              candidates[i][1].equals(candidates[i + 1][1])){
#             //if duplicated => remove next because they are in order
#             candidates.splice(i + 1, 1);
#           }
#         }
#         pairs.push(...candidates);//add them to pairs
#       }
#     }
    
#     for(let i = 0; i < pairs.length; i++){//remove unwanted values from pair and remove good values from the rest
#       //if not useful value in posVal -> Remove it (ej: pair: [123, 12] -> [12, 12])
#       let changeProduced = false;
#       let intersection = [filterArray(pairs[i][0].posVal, pairs[i][1].posVal), filterArray(pairs[i][1].posVal, pairs[i][0].posVal)];
#       //let inter1U2 = filterArray(pairs[i][0].posVal, pairs[i][1].posVal);
#       //let inter2U1 = filterArray(pairs[i][1].posVal, pairs[i][0].posVal);
#       for(let j = 0; j < 2; j++){
#         if(pairs[i][j].posVal.length == 2){
#            //if(pairs[i][j].posVal.length - intersection[j].length == 2){//if intersection = 0
#            if(intersection[j].length == 0){//if intersection = 0 => perfect pair
#             pairs[i][(j + 1) % 2].posVal = pairs[i][j].posVal;
#             //changeProduced = true;  
#             removeFromPairs(pairs[i], pairs[i][0].posVal);
#           // if(debugS(pairs[i][(j + 1) % 2].x, pairs[i][(j + 1) % 2].y)){  console.log("Perf pair 3b3 " + printCoord(pairs[i][(j + 1) % 2].x, pairs[i][(j + 1) % 2].y, printArray(grid[pairs[i][(j + 1) % 2].x][pairs[i][(j + 1) % 2].y].posVal)))}
            
#           }
#           else if(intersection[j].length == 1){//if 1 value only
#             let value = filterArray(pairs[i][j].posVal, intersection[j]);
#             removeFromPairs(pairs[i], value);
#             // if(debugS(pairs[i][(j + 1) % 2].x, pairs[i][(j + 1) % 2].y)){  console.log("1val pair 3b3 " + printCoord(pairs[i][(j + 1) % 2].x, pairs[i][(j + 1) % 2].y, printArray(grid[pairs[i][(j + 1) % 2].x][pairs[i][(j + 1) % 2].y].posVal)))}
            
#           }
#         }
#       } 
#       if(false){
#         let c = color(Math.floor(Math.random() * 255), Math.floor(Math.random() * 255), Math.floor(Math.random() * 255));
#         pairs[i][0].show(c);
#         pairs[i][1].show(c);
#         let f = pairs[i][0];
#         let s = pairs[i][1];
#         console.log(printCoords(f) + " --- " + printCoords(s) + " --> " + f.posVal + " -- " + s.posVal);
#       }
#     }
    
#     pairs = [];
        
    
    
    
    
    
    
    
    
    
    
#     //all rows and cols (debuged)
#     for(let w = 0; w < 9; w++){//for each row & col
#       let candidates = [];
#       for(let i = 1; i <= 9; i++){//for each index (possible value in posVal)
#         let spotsInRow = [];//store the spot with i val in posVal
#         let spotsInCol = [];//store the spot with i val in posVal
        
#         for(let j = 0; j < 9; j++){//for each row if doing cols and viceversa
#           if(grid[j][w].value == undefined &&
#              grid[j][w].posVal.indexOf(i) != -1){//if it has that value
#             spotsInRow.push(grid[j][w]);//add it to possible candidates with that value
#           }
          
#           if(grid[w][j].value == undefined &&
#              grid[w][j].posVal.indexOf(i) != -1){//if it has that value
#             spotsInCol.push(grid[w][j]);//add it to possible candidates with that value
#           }
#         }
#         //console.log(spotsInCol);
        
#         if(spotsInRow.length == 2){//if candidate (2 spots only)
#           candidates.push(spotsInRow);
#           console.log("new candidate in Row: " + printArraySpots(spotsInRow));
#         }
#         if(spotsInCol.length == 2){//if candidate (2 spots only)
#           candidates.push(spotsInCol);
#           console.log("new candidate in Col: " + printArraySpots(spotsInCol));
          
#         }  
#       }
#       //console.log(candidates);
#       if(candidates.length > 1){//if new candidates (type row or col)
#         for(let i = 0; i < candidates.length; i++){//remove duplicates
#           //console.log(printCoords(candidates[i][0]) + " --- " + printCoords(candidates[i][1]));
#           if(i + 1 < candidates.length &&
#              candidates[i][0].equals(candidates[i + 1][0]) &&
#              candidates[i][1].equals(candidates[i + 1][1])){
#             //if duplicated => remove next because they are in order
#             //console.log("duplicated");
#             candidates.splice(i + 1, 1);
#           }
#         }
#         pairs.push(...candidates);//add them to pairs
        
#       }
      
#     }
    
    
    
    
    
#     console.log(printCoords(grid[xDebug][yDebug], printArray(grid[xDebug][yDebug].posVal)));//debug
    
    
#     for(let i = 0; i < pairs.length; i++){//remove unwanted values from pair and remove good values from the rest
#       //if not useful value in posVal -> Remove it (ej: pair: [123, 12] -> [12, 12])
#       let intersection = [filterArray(pairs[i][0].posVal, pairs[i][1].posVal), filterArray(pairs[i][1].posVal, pairs[i][0].posVal)];
#       for(let j = 0; j < 2; j++){
#         if(pairs[i][j].posVal.length == 2){
#           if(intersection[j].length == 0){//if intersection = 0 => perfect pair
#            pairs[i][(j + 1) % 2].posVal = pairs[i][j].posVal;
#            removeFromPairs(pairs[i], pairs[i][0].posVal);
            
#            //if(debugS(pairs[i][(j + 1) % 2].x, pairs[i][(j + 1) % 2].y)){  console.log("1 " + printCoords(pairs[i][(j+1)%2], printArray(pairs[i][(j+1)%2].posVal)));}
           
#           }
#           else if(intersection[j].length == 1){//if 1 value only
#             let value = filterArray(pairs[i][j].posVal, intersection[j]);
#             removeFromPairs(pairs[i], value);
            
#             //if(debugS(pairs[i][0].x, pairs[i][0].y) || debugS(pairs[i][1].x, pairs[i][1].y)){  console.log("2" + printCoords(pairs[i][j], printArray(pairs[i][j].posVal)));}
            
#           }
#         }        
#       }
#       //ERROR MAKING PAIRS!!
      
#       console.log(printCoord(pairs[i][0].x, pairs[i][0].y) + " & " + printCoord(pairs[i][1].x, pairs[i][1].y) +" iteration -> "+ printArray(grid[xDebug][yDebug].posVal));//debug
#     }
    
    
    
#     console.log(printCoords(grid[xDebug][yDebug]) + " with posVal: " + printArray(grid[xDebug][yDebug].posVal));//debug
    
    
    
    
    
    
    
    
    
    
    



#     //check if finnised
#     if (setS.length == 0) {
#       console.log("Done!");
#       noLoop();
#       return;
#     }

#     //draw 3 by 3 grid
#     for (let i = 0; i < 3; i++) {
#       for (let j = 0; j < 3; j++) {
#         stroke(0);
#         strokeWeight(5);
#         noFill();
#         rect(i * 3 * w, j * 3 * h, 3 * w, 3 * h);
#       }
#     }
    

#     //let x = 5, y = 7;
#     //grid[x][y].show(color(0));//debug
#     // console.log(printCoords(grid[xDebug][yDebug]) + " with posVal: " + printArray(grid[xDebug][yDebug].posVal));//debug
#   } //debug
#   noLoop();
#   checkSolution();
# }

# function removeFromPairs(pair, values){//pair, valuesToRemove
#   //detect if row or col and remove values in pairs (1.4)
#   let dx = (pair[0].x - pair[1].x != 0) ? 1 : 0;
#   let dy = (dx != 0) ? 0 : 1;
#   let x = (dx == 0) ? pair[0].x : 0;
#   let y = (dy == 0) ? pair[0].y : 0;
  
#   let deb = (x == xDebug || y == yDebug);//debug
#   if(deb){console.log("Pair " + printCoords(pair[0]) + " & " + printCoords(pair[1]) + " in direction " + printCoord(dx, dy) + " with posVal " + printArray(pair[0].posVal)); console.log();}
  
  
#   for(let j = 0; j < 9; j++){//rows and cols
#     if(pair.indexOf(grid[x][y]) == -1 && grid[x][y].value == undefined){
#       grid[x][y].posVal = filterArray(grid[x][y].posVal, values);
#       //grid[x][y].show(color(0));
#     }
#     x += dx;
#     y += dy;
#   }
#   let sectorX = Math.floor(pair[0].x / 3);
#   let sectorY = Math.floor(pair[0].y / 3)
#   for(let j = 0; j < 3; j++){
#     for(let k = 0; k < 3; k++){
#       let x = sectorX * 3 + j;
#       let y = sectorY * 3 + k;
#       if(pair.indexOf(grid[x][y]) == -1 && grid[x][y].value == undefined){
#         grid[x][y].posVal = filterArray(grid[x][y].posVal, values);
#       }
#     }
#   }
# }

# function setValueInArray(array, index, value) { //also removes from array
#   //console.log(printCoords(array[index]) + " to value " + value);
#   array[index].setValue(value); //set value
#   array.splice(index, 1);
#   return array;
# }
# function filterArray(array1, array2){
#   //console.log("filter: ");
#   //console.log(array1);
#   //console.log(array2); 
#   array1 = array1.filter(function(val) {
#     return array2.indexOf(val) == -1;
#   });
#   return array1;
# }

# function checkSolution(){
#   let error = false;
#   for(let i = 0; i < 9; i++){
#     for(let j = 0; j < 9; j++){
#       if(grid[i][j].value != undefined && grid[i][j].value != solDebug[i][j].value){
#         //console.log(grid[i][j].value + " --- " + solDebug[i][j].value);
#         grid[i][j].show(color(255, 0, 0));
#         error = true;
#       }
#     }
#   }
#   if(error){
#     //console.log("ERROR SOLVING");
#   }
# }

# function printCoords(spot, value){
#   if(value) return printCoord(spot.x, spot.y, value);
#   else{ return printCoord(spot.x, spot.y);}
# }
# function printCoord(x, y, value){
#   if(value){
#     return ("(" + x + ", " + y + ") -> " + value);
#   }
#   else{
#     return ("(" + x + ", " + y + ")");
#   }
# }
# function printArray(array){
#   let str = "[";
#   for(let i = 0; i < array.length; i++){
#     if(Array.isArray(array[i])){
#       str += printArray(array[i]);
#     }
#     else{
#       str += array[i];
#     }
#     str += ((i + 1 < array.length) ? ", " : "");
#   }
#   str += "]";
#   return str;
# }

# function printArraySpots(array){
#   let str = "[";
#   for(let i = 0; i < array.length; i++){
#     if(Array.isArray(array[i])){
#       str += printArray(array[i]);
#     }
#     else{
#       str += printArray([array[i].x, array[i].y]);
#     }
#     str += ((i + 1 < array.length) ? ", " : "");
#   }
#   str += "]";
#   return str;
# }