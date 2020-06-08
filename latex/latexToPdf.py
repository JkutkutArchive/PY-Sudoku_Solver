from pylatex import Document, Section, Subsection, Command, Tabular
from pylatex.utils import italic, NoEscape

from pylatex.package import Package

from pylatex import Math, TikZ, Axis, Plot, Figure, Matrix, Alignat

latex_document = '/home/jkutkut/github/PY-Sudoku-Solver/latex/doc4-2.tex'
with open(latex_document) as file:
    tex= file.read()
doc = Document('basic')

# doc.packages.append(Package('arydshln'))
# doc.packages.append(Package('float'))
doc.append(tex)
doc.generate_pdf(clean_tex=True)