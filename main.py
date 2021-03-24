import tkinter as tk
from Classes.sudoku import Sudoku
import input

class SudokuSolver():
    # Variables:
    def __init__(self, root, sudokuObject) -> None:
        # Variables:
        self.COLORS = {
            "BtnNormal": "#ffffff",
            "BtnFocus": "#e0e0e0",
            "BtnSelected": "#b8b8b8"
        }

        self.mainWidth, self.mainHeight = 500, 500
        self.mouseX, self.mouseY = 0, 0


        self.root = root
        self.sudokuObject = sudokuObject

        # Setup:
        self.root.geometry(f"{self.mainWidth}x{self.mainHeight}")
        self.root.minsize(self.mainWidth, self.mainHeight)

        # link special events to methods
        self.root.bind('<Motion>', self.mouseMove)
        self.root.bind("<Configure>", self.resize)
        self.root.bind("<Button-1>", self.leftMousePressed)

        self.buttons = []
        for r in range(9):
            self.buttons.append([])
            tk.Grid.rowconfigure(self.root, index=r, weight=1)
            tk.Grid.columnconfigure(self.root, index=r, weight=1)
            for c in range(9):
                self.buttons[r].append(
                    tk.Button(
                        self.root,
                        text="({}, {})".format(r, c),
                        background = self.COLORS.get("BtnNormal"),
                        activebackground = self.COLORS.get("BtnFocus")
                    )
                )
                self.buttons[r][c].grid(row=r, column=c, sticky='nsew')
    


    def mouseMove(self, event):
        '''
        When the mouse is moved over the screen, this function is executed.
        '''
        self.mouseX, self.mouseY = event.x, event.y # Store new values in a global variable

        # print()
        
        # indexX = self.mouseX / (self.mainWidth  / 9)
        # indexY = self.mouseY / (self.mainHeight / 9)
        # print("({}, {}) => {}, {}".format(self.mouseX, self.mouseY, indexX, indexY))

    def resize(self, event):
        '''
        When the screen is resized, this function is executed.
        '''
        self.mainWidth, self.mainHeight = event.width, event.height # Store the current window size on global variables
        # print("resize")

    def leftMousePressed(self, event):
        event.widget.config(background = self.COLORS.get("BtnSelected"))
        print("{} {}".format(self.mouseX, self.mouseY))


if __name__ == '__main__':
    window = tk.Tk(className='Sudoku solver')
    sudokuObject = Sudoku(input.easy())
    SudokuSolver(window, sudokuObject)
    window.mainloop()