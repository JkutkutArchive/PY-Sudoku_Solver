import tkinter as tk
from tkinter.constants import BOTTOM

# Variables:
mainWidth, mainHeight = 500, 500
squareSizeW, squareSizeH = mainWidth // 9, mainHeight // 9
mouseX, mouseY = 0, 0

# Functions:
def motion(event):
    '''
    When the mouse is moved over the screen, this function is executed.
    '''
    global mouseX, mouseY
    mouseX, mouseY = event.x, event.y # Store new values in a global variable

def resize(event):
    '''
    When the screen is resized, this function is executed.
    '''
    global mainWidth, mainHeight, squareSizeW, squareSizeH
    mainWidth, mainHeight = event.width, event.height # Store the current window size on global variables
    squareSizeW, squareSizeH = mainWidth // 9, mainHeight // 9

    # print("resize")

def leftMousePressed(event):
    print("{} {}".format(mouseX, mouseY))


# Setup
root = tk.Tk(className='Sudoku solver')
root.geometry(f"{mainWidth}x{mainHeight}")
root.minsize(mainWidth, mainHeight)


# Map functions to the events
root.bind('<Motion>', motion)
root.bind("<Configure>", resize)
root.bind("<Button-1>", leftMousePressed)


# grid = tk.Frame(root, width=mainWidth-100, height=mainHeight-100)
gridSize = mainHeight
grid = tk.Frame(root, width=gridSize, height=gridSize)
grid.pack(side=BOTTOM)

for i in range(9):
    tk.Grid.rowconfigure(grid, index=i, weight=1)
    tk.Grid.columnconfigure(grid, index=i, weight=1)

buttons = [[tk.Button(grid, text="({}, {})".format(r, c)) for c in range(9)] for r in range(9)]

for i in range(9):
    for j in range(9):
        btn = buttons[i][j]
        btn.grid(row=i, column=j, sticky='nsew')

root.mainloop() 