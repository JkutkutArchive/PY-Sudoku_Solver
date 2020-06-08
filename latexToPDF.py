from pylatex import Document, Section, Table, Tabular, MultiColumn, UnsafeCommand
from pylatex.utils import bold 

from pylatex.package import Package

from pylatex.base_classes import CommandBase #Environment, Arguments


doc = Document("solution") #create the document (argument = name of the file)
doc.packages.append(Package('arydshln')) # package to make the custom borders on the table
doc.packages.append(Package('float'))


def addSudokuOnLaTeX(grid):
    t = Table(position="H")
    t.append(UnsafeCommand("centering"))
    table = Tabular('ll|l:l:l|l:l:l|l:l:l|')

    table.add_row(tuple(["",bold("Y")] + [MultiColumn(1, align='l|', data=bold(str(i))) for i in range(9)])) # Line with indices


    table.add_row(tuple([bold("X")] + [MultiColumn(1, align='l|', data="") for i in range(1,11)]))
    table.add_hline()

    for r in range(9):
        table.add_row(tuple([bold(str(r)), ""] + [str(grid[r][c]) if grid[r][c] != 0 else ""  for c in range(9)]))
        if r == 2 or r == 5 or r == 8:
            table.add_hline()
        else:
            table.append(UnsafeCommand("cline", "1-2"))
            table.append(UnsafeCommand("cdashline", "3-11"))
    #Table ended
    t.append(table)
    doc.append(t)

def toPDF():
    doc.generate_pdf(clean_tex=False)

if __name__ == "__main__":
    data = [ #canonical (solved)
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
    addSudokuOnLaTeX(data)
    toPDF()
    