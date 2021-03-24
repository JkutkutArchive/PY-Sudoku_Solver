import tkinter as tk
import tkinter.font as TkFont

from Classes.sudoku import Sudoku
import input

class SudokuSolverGUI():
    # Variables:
    def __init__(self) -> None:
        # Variables:
        self.COLORS = {
            "BtnNormal": "#ffffff",
            "BtnFocus": "#e0e0e0",
            "BtnSelected": "#b8b8b8",
            "BtnText": "black"
        }
        self.FONTS = {
            "NORMAL": TkFont.Font(
            # "NORMAL": tk.font.Font(
                size=10
            ),
            # "DATA": tk.font.Font(
            "DATA": TkFont.Font(
                # size = 20,
                weight = "bold"
            )
        }

        self.mainWidth, self.mainHeight = 500, 500
        self.mouseX, self.mouseY = 0, 0


        self.root = tk.Tk(className='Sudoku solver')
        self.sudokuObject = None
        

        # Icon
        self.root.iconphoto(False, tk.PhotoImage(file = "Res/icon.png"))

        # Menu
        self.menu = tk.Menu(self.root)
        self.initMenu()

        # Setup:
        self.root.geometry(f"{self.mainWidth}x{self.mainHeight}")
        self.root.minsize(self.mainWidth, self.mainHeight)

        # link special events to methods
        self.root.bind("<Configure>", self.resize)
        self.root.bind("<Button-1>", self.leftMousePressed)
        self.root.bind("<KeyPress>", self.keydown)

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
                        text="{}, {}".format(r, c),
                        background = self.COLORS.get("BtnNormal"),
                        activebackground = self.COLORS.get("BtnFocus"),
                        disabledforeground = self.COLORS.get("BtnText"),
                        bd=3
                    )
                )
                self.buttons[r][c].grid(row=r, column=c, sticky='nsew')
        

        # Fill the board
        self.loadEasy()

        self.root.mainloop()

    def initMenu(self):
        self.root.config(menu = self.menu)
        
        # Create menus
        file_menu= tk.Menu(self.menu)
        loadSudokuMenu= tk.Menu(file_menu)
        
        # Configure menus
        # fileMenu
        self.menu.add_cascade(label="File", menu=file_menu) # Name of the menu

        file_menu.add_cascade(label="Load...", menu = loadSudokuMenu)
        file_menu.add_separator()
        file_menu.add_command(label="Exit",command=self.root.quit)

        # loadSudokuMenu
        loadSudokuMenu.add_command(label="Easy", command=self.loadEasy)
        loadSudokuMenu.add_command(label="Medium", command=self.loadMedium)
        loadSudokuMenu.add_command(label="Hard", command=self.loadHard)

    def resize(self, event):
        '''
        When the screen is resized, this function is executed.
        '''
        self.mainWidth, self.mainHeight = event.width, event.height # Store the current window size on global variables

    # User input
    def leftMousePressed(self, event):
        '''
        If this method is selected, a cell has been selected by the user
        '''
        if event.widget["state"] == tk.DISABLED: # If cell has the value already selected
            return # do not select it
        
        event.widget["background"] = self.COLORS["BtnSelected"]
    
    def keydown(self, e):
        arrows = {'w', 'a', 's', 'd'}
        if (e.char.isnumeric()):
            print("Number")
        elif (e.char in arrows):
            print("Arrow: " + e.char)
        else:
            print(e.char)


    def setBtnState(self, btn, state):
        if (state == "DATA"):
            btn["state"] = tk.DISABLED
            # btn["font"] = self.FONTS["DATA"]
        # elif (state == "NORMAL"):
        #     btn["font"] = self.FONTS["NORMAL"]
    

    # Sudoku logic:
    def loadEasy(self):
        self.loadSudoku(input.easy())
    
    def loadMedium(self):
        self.loadSudoku(input.medium())
    
    def loadHard(self):
        self.loadSudoku(input.hard())

    def loadSudoku(self, sudoku):
        self.sudokuObject = Sudoku(sudoku)
        self.fillBoard()


    def fillBoard(self):
        board = self.sudokuObject.getBoard()

        for r in range(9):
            for c in range(9):
                if board[r][c].getValue() == 0: # If value not given
                    self.setBtnState(self.buttons[r][c], "NORMAL")
                else:
                    self.buttons[r][c]["text"] = str(board[r][c].getValue())
                    self.setBtnState(self.buttons[r][c], "DATA")
                


if __name__ == '__main__':
    SudokuSolverGUI()