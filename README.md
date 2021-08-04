# PY-Sudoku_Solver:

This proyect makes easy to find the solution of a sudoku, show the steps to follow in order to solve it and even show all possible solutions of a multiple solution sudoku.



# Instalation:
sudo apt install python3-tk




## How it works:
In order for this code to work, fill the **input.py file** with the desired sudoku. Keep in mind that it must follow the Python3 syntax as the examples given.
At the begining, the code checks all the possible solutions of the sudoku. Acording to the number of solutions:
- One solution: It shows the solution and atempts to find the steps a human would take to get there (see the *steps algorithm*).
- More than one solution: Shows all the possible solutions for the given sudoku.
- No solutions: Ends the code

### Step algorithm:
When a single solution is found, the code can atempt to find the solutions to solve the given sudoku the way a human will do. If founded, all the logic found will be writen into a file using LaTeX (see *LaTeX file using Pylatex*).

### LaTeX file using PyLaTeX:
This code makes use of the file `latexToPDF.py`, a file to easily generate a PDF file using python3 and pylatex. The code contains multiple functions to add new sections, write the steps made to find a solution, print the state of the sudoku and many more. 
