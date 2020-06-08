from pylatex import Document, Section, Table, Tabular, MultiColumn, UnsafeCommand
from pylatex.utils import bold 

from pylatex.package import Package

from pylatex.base_classes import CommandBase #Environment, Arguments

doc = Document("basic") #create the document (argument = name of the file)
doc.packages.append(Package('arydshln')) # package to make the custom borders on the table
doc.packages.append(Package('float'))


test1 = Section('Sudoku')
t = Table(position="H")
t.append(UnsafeCommand("centering"))

table = Tabular('l|l:l:l|l:l:l|l:l:l|')
row_cells = ("",\
    MultiColumn(1, align='l|', data=bold('0')),\
    MultiColumn(1, align='l|', data=bold('1')),\
    MultiColumn(1, align='l|', data=bold('2')),\
    MultiColumn(1, align='l|', data=bold('3')),\
    MultiColumn(1, align='l|', data=bold('4')),\
    MultiColumn(1, align='l|', data=bold('5')),\
    MultiColumn(1, align='l|', data=bold('6')),\
    MultiColumn(1, align='l|', data=bold('7')),\
    MultiColumn(1, align='l|', data=bold('8')))
table.add_row(row_cells)
table.add_hline()

for r in range(9):
    table.add_row(tuple([bold(str(r))] + [str(i) for i in range(1,10)]))
    if r == 2 or r == 5 or r == 8:
        table.add_hline()
    else:
        table.append(UnsafeCommand("cline", "1-1"))
        table.append(UnsafeCommand("cdashline", "2-10"))

t.append(table)
test1.append(t)
doc.append(test1)














# ------------------------------------------------------
# test2 = Subsection('MultiRow')
# test3 = Subsection('MultiColumn and MultiRow')
# test4 = Subsection('Vext01')

# table1 = Tabular('|c|c|c|c|')
# table1.add_hline()
# table1.add_row((MultiColumn(4, align='|c|', data='Multicolumn'),))
# table1.add_hline()
# table1.add_row((1, 2, 3, 4))
# table1.add_hline()
# table1.add_row((5, 6, 7, 8))
# table1.add_hline()
# row_cells = ('9', MultiColumn(3, align='|c|', data='Multicolumn not on left'))
# table1.add_row(row_cells)
# table1.add_hline()

# table2 = Tabular('|c|c|c|')
# table2.add_hline()
# table2.add_row((MultiRow(3, data='Multirow'), 1, 2))
# table2.add_hline(2, 3)
# table2.add_row(('', 3, 4))
# table2.add_hline(2, 3)
# table2.add_row(('', 5, 6))
# table2.add_hline()
# table2.add_row((MultiRow(3, data='Multirow2'), '', ''))
# table2.add_empty_row()
# table2.add_empty_row()
# table2.add_hline()

# table3 = Tabular('|c|c|c|')
# table3.add_hline()
# table3.add_row((MultiColumn(2, align='|c|',
#                             data=MultiRow(2, data='multi-col-row')), 'X'))
# table3.add_row((MultiColumn(2, align='|c|', data=''), 'X'))
# table3.add_hline()
# table3.add_row(('X', 'X', 'X'))
# table3.add_hline()

# table4 = Tabular('|c|c|c|')
# table4.add_hline()
# col1_cell = MultiRow(4, data='span-4')
# col2_cell = MultiRow(2, data='span-2')
# table4.add_row((col1_cell, col2_cell, '3a'))
# table4.add_hline(start=3)
# table4.add_row(('', '', '3b'))
# table4.add_hline(start=2)
# table4.add_row(('', col2_cell, '3c'))
# table4.add_hline(start=3)
# table4.add_row(('', '', '3d'))
# table4.add_hline()

# test1.append(table1)
# test2.append(table2)
# test3.append(table3)
# test4.append(table4)

# section.append(test1)
# section.append(test2)
# section.append(test3)
# section.append(test4)

# doc.append(section)
doc.generate_pdf(clean_tex=False)