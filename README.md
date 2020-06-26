# PY-Sudoku-Solver:

This proyect makes easy to find the solution of a sudoku, show the steps to follow in order to solve it and even show all possible solutions of a multiple solution sudoku.

## How it works:
### Start:
At the begining, the code checks all the possible solutions of the given sudoku. Acording to the number of solutions:
- One solution: It shows the solution and atempts to find the steps a human would take to get there (see the *steps algorithm*).
- More than one solution: Shows all the possible solutions for the given sudoku.
- No solutions: Ends the code

### Step algorithm:
When a single solution is found, the code can atempt to find the solutions to solve the given sudoku the way a human will do. If founded, all the logic found will be writen into a file using LaTeX (see *LaTeX file using Pylatex*).

### LaTeX file using PyLaTeX:
This code makes use of the file _latexToPDF.py_, a file to easily generate a PDF file using python3 and pylatex. The code contains multiple functions to add new sections, write the steps made to find a solution, print the state of the sudoku and many more. 