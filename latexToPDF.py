from pylatex import Document, Section, Subsection, Table, Tabular, Tabularx, MultiColumn, UnsafeCommand
from pylatex.basic import TextColor, HugeText, NewLine, NewPage
from pylatex.utils import bold, escape_latex, NoEscape
from pylatex.package import Package # To import custom packages
from pylatex.base_classes import CommandBase #Environment, Arguments
from pylatex.position import Center

doc = None # Create the var

def init(data, *fileName): # Init the var
    global doc
    fileName = fileName if fileName else "aa-solution"
    doc = Document(fileName) #create the document (argument = name of the file)
    doc.packages.append(Package('arydshln')) # package to make the custom borders on the table
    doc.packages.append(Package('float')) # package to handle table position
    doc.packages.append(Package('hyperref')) # package to add links
    
    title = Center()
    title.append(HugeText(bold("Sudoku's step by step solver")))
    doc.append(title)
    intro = Section("Introduction")
    intro.append("On this PDF, the reader will be able to see how to solve the given sudoku:")
    addSudokuOnLaTeX(data, place=intro)
    intro.append("On the following pages, with each iteration of the code, the conclusions madeby the algorithm will be showed next to a representation of the sudoku with allthe discovered values.")
    intro.append(NewLine())
    intro.append("The way to refer to a particular cell will be using coordinates (x, y). This way, the value 'x' represents the row's number and 'y' the column's number. This will be represented every time the sudoku’s representation is generated as you can see.")
    intro.append(NewLine())
    intro.append("To see the code used to generate this file and solve the sudoku, please go to the author of the code’s github: ")
    intro.append(NoEscape(r"\href{https://github.com/Jkutkut/PY-Sudoku-Solver}{Jkutkut's GitHub}"))
    intro.append(NewPage())
    doc.append(intro)
    doc.append(Section("Steps"))


def newIteration(grid, *data):
    doc.append(Subsection("New Iteration"))
    addSudokuOnLaTeX(grid, data[0] if data else None)

def addSudokuOnLaTeX(grid, *data, place=None):
    if doc == None: return
    # print(place)
    place = place if place else doc
    if data: data = data[0]
    
    sudokuTabular = Tabular('l|l:l:l|l:l:l|l:l:l|', pos="t")

    sudokuTabular.add_row(tuple([""] + [MultiColumn(1, align='l|', data=bold(str(i))) for i in range(9)]))
    sudokuTabular.add_hline()

    for r in range(9):
        if data:
            row = []
            for c in range(9):
                if data[r][c] != 0: # Data given, print black
                    row.append(str(data[r][c]))
                else:
                    row.append(TextColor("blue", str(grid[r][c])) if grid[r][c] != 0 else "")
        else:
            row = [str(grid[r][c]) if grid[r][c] != 0 else ""  for c in range(9)]

        sudokuTabular.add_row(tuple([bold(str(r))] + row))
        if r == 2 or r == 5 or r == 8:
            sudokuTabular.add_hline()
        else:
            sudokuTabular.append(UnsafeCommand("cline", "1-1"))
            sudokuTabular.append(UnsafeCommand("cdashline", "2-10"))

    xAxis = Tabular('l')
    xAxis.add_row(tuple([bold("X")]))
    xAxis.add_row(tuple([bold(escape_latex("↓"))]))

    table = Table(position="H")
    table.append(UnsafeCommand("centering"))
    axis = Tabular("ll")
    axis.add_row(("", bold(escape_latex("Y →"))))
    axis.add_row((xAxis, sudokuTabular))
    table.append(axis)
    place.append(table)



def toPDF():
    if doc == None: return
    doc.generate_pdf(clean_tex=False)

if __name__ == "__main__":
    data = [
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
    init(data)
    g = [
        [9, 8, 4, 7, 3, 1, 0, 7, 2],
        [6, 1, 0, 4, 9, 7, 0, 0, 0],
        [2, 5, 7, 2, 4, 9, 8, 0, 0],
        [3, 0, 0, 1, 6, 0, 0, 1, 0],
        [3, 4, 0, 3, 7, 0, 9, 2, 0],
        [1, 0, 9, 0, 0, 5, 0, 0, 0],
        [2, 3, 0, 0, 0, 6, 0, 0, 0],
        [3, 4, 5, 0, 1, 8, 0, 9, 6],
        [1, 9, 6, 7, 0, 0, 2, 8, 0]
    ]
    newIteration(g, data)
    toPDF()
    