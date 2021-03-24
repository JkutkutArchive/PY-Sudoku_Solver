import tkinter as tk
from tkinter.constants import DISABLED
from Classes.sudoku import Sudoku
import input

class SudokuSolver():
    # Variables:
    def __init__(self, root, sudokuObject) -> None:
        # Variables:
        self.COLORS = {
            "BtnNormal": "#ffffff",
            "BtnFocus": "#e0e0e0",
            "BtnSelected": "#b8b8b8",
            "BtnText": "black"
        }

        self.mainWidth, self.mainHeight = 500, 500
        self.mouseX, self.mouseY = 0, 0


        self.root = root
        self.sudokuObject = sudokuObject

        # Setup:
        self.root.geometry(f"{self.mainWidth}x{self.mainHeight}")
        self.root.minsize(self.mainWidth, self.mainHeight)

        # link special events to methods
        self.root.bind("<Configure>", self.resize)
        self.root.bind("<Button-1>", self.leftMousePressed)

        # Create the buttons
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
                        activebackground = self.COLORS.get("BtnFocus"),
                        disabledforeground = self.COLORS.get("BtnText")
                    )
                )
                self.buttons[r][c].grid(row=r, column=c, sticky='nsew')

        # Fill the board
        self.fillBoard()

    def resize(self, event):
        '''
        When the screen is resized, this function is executed.
        '''
        self.mainWidth, self.mainHeight = event.width, event.height # Store the current window size on global variables
        # print("resize")


    def leftMousePressed(self, event):
        '''
        If this method is selected, a cell has been selected by the user
        '''
        if event.widget["state"] == tk.DISABLED:
            return
        event.widget.config(background = self.COLORS.get("BtnSelected"))
        print("{} {}".format(self.mouseX, self.mouseY))

    

    # Sudoku logic:
    def fillBoard(self):
        board = self.sudokuObject.getBoard()

        for r in range(9):
            for c in range(9):
                if board[r][c].getValue() == 0:
                    continue
                self.buttons[r][c]["text"] = str(board[r][c].getValue())
                self.buttons[r][c]["state"] = tk.DISABLED


if __name__ == '__main__':
    window = tk.Tk(className='Sudoku solver')
    sudokuObject = Sudoku(input.easy())
    SudokuSolver(window, sudokuObject)
    window.mainloop()