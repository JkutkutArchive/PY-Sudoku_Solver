import tkinter as tk
import tkinter.font as TkFont

from Classes.sudoku import Sudoku
import input

class SudokuSolverGUI():
    # ******* Constructor *******
    
    def __init__(self) -> None:
        # Variables:
        self.COLORS = {
            "BtnNormal": "#ffffff",
            "BtnData": "#ffffff",
            "BtnFocus": "#e0e0e0",
            "BtnSelected": "#b8b8b8",
            "BtnText": "black"
        }
        # self.FONTS = {
        #     "NORMAL": TkFont.Font(
        #     # "NORMAL": tk.font.Font(
        #         size=10
        #     ),
        #     # "DATA": tk.font.Font(
        #     "DATA": TkFont.Font(
        #         # size = 20,
        #         weight = "bold"
        #     )
        # }

        self.mainWidth, self.mainHeight = 500, 500
        self.mouseX, self.mouseY = 0, 0

        self.currentBtn = None


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
        # userControl
        self.root.bind("<KeyPress>", self.keydown)
        self.root.bind("<Shift-KeyPress>", self.keydown)
        self.root.bind('<Up>', self.keydown)
        self.root.bind('<Down>', self.keydown)
        self.root.bind('<Left>', self.keydown)
        self.root.bind('<Right>', self.keydown)

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
        loadSudokuMenu.add_command(label="Easy", command=lambda: self.loadSudoku(input.easy()))
        # loadSudokuMenu.add_command(label="Easy", command=self.loadEasy)
        loadSudokuMenu.add_command(label="Medium", command=self.loadMedium)
        loadSudokuMenu.add_command(label="Hard", command=self.loadHard)

    # ******* GUI manipulation *******
    
    def resize(self, event):
        '''
        When the screen is resized, this function is executed.
        '''
        self.mainWidth, self.mainHeight = event.width, event.height # Store the current window size on global variables

    
    # ******* User input ******* 
    
    def leftMousePressed(self, event):
        '''
        If this method is selected, a cell has been selected by the user
        '''
        if event.widget["state"] == tk.DISABLED: # If cell has the value already selected
            return # do not select it

        if self.currentBtn != event.widget:
            self.changeFocus(event.widget)
    
    def keydown(self, e):
        arrows = ['w', 's', 'a', 'd']
        keys = ["Up", "Down", "Left", "Right"]
        SHIFT = 1

        # print(e)


        if ((e.char.isnumeric() and int(e.char) > 0) or (e.state == SHIFT and e.keycode >= 10 and e.keycode < 19)):
            if self.currentBtn == None:
                return
            
            if (e.char.isnumeric()):
                num = int(e.char)
                draft = False
            else:
                num = e.keycode - 9
                draft = True

            if (self.currentBtn["state"] == tk.NORMAL):
                if draft:
                    self.draft(self.currentBtn, num)
                else:
                    self.setValue(self.currentBtn, num)
                # print("ready to change value (draf: {}) to {}".format(draft, num))
            # else:
            #     print("data cell, value can not change")
        elif (e.char in arrows or e.keysym in keys):
            extraIndex = [
                (-1,  0),
                ( 1,  0),
                ( 0, -1),
                ( 0,  1)
            ]

            if (e.char in arrows):
                indi = arrows.index(e.char)
            else:
                indi = keys.index(e.keysym)
            
            currentIndex = self.getBtnIndex(self.currentBtn)
            index = (currentIndex[0] + extraIndex[indi][0], currentIndex[1] + extraIndex[indi][1])
            
            if (index[0] >= 0 and index[0] < 9 and index[1] >= 0 and index[1] < 9):
                self.changeFocus(self.buttons[index[0]][index[1]])


    # ******* Tools *******
    
    def setBtnState(self, btn, state):
        if btn == None:
            return
        
        if (state == "DATA"):
            btn["state"] = tk.DISABLED
            btn["background"] = self.COLORS["BtnData"]
            # btn["font"] = self.FONTS["DATA"]
        elif (state == "DATAFOCUS"):
            btn["background"] = self.COLORS["BtnFocus"]
        elif (state == "NORMAL"):
            if (btn["state"] == tk.DISABLED):
                self.setBtnState(btn, "DATA")
                return
            btn["background"] = self.COLORS["BtnNormal"]
            # btn["font"] = self.FONTS["NORMAL"]
        if (state == "SELECTED"):
            if (btn["state"] == tk.DISABLED):
                self.setBtnState(btn, "DATAFOCUS")
                return
            btn["background"] = self.COLORS["BtnSelected"]
    
    def changeFocus(self, newBtn):
        self.setBtnState(self.currentBtn, "NORMAL")
        self.setBtnState(newBtn, "SELECTED")
        self.currentBtn = newBtn

    def getBtnIndex(self, btn):
        for i in range(9):
            for j in range(9):
                if btn == self.buttons[i][j]:
                    return (i, j)
        return (0, 0)

    def draft(self, btn, number):
        pass

    def setValue(self, btn, number):
        index = self.getBtnIndex(btn)
        btn["text"] = str(number)
        if self.solution[index[0]][index[1]] == number:
            btn["disabledforeground"] = "blue"
            btn["state"] = tk.DISABLED
        else:
            btn["fg"] = "red"

    # Sudoku logic:
    def loadEasy(self):
        self.loadSudoku(input.easy())
    
    def loadMedium(self):
        self.loadSudoku(input.medium())
    
    def loadHard(self):
        self.loadSudoku(input.hard())

    def loadSudoku(self, sudoku):
        self.sudokuObject = Sudoku(sudoku)
        self.solution = self.sudokuObject.getSolutions()
        if len(self.solution) > 1:
            raise Exception("The current sudoku has more than one solution")
        self.solution = self.solution[0]
        self.fillBoard()

    def fillBoard(self):
        board = self.sudokuObject.toList()

        for r in range(9):
            for c in range(9):
                self.buttons[r][c]["state"] = "normal"
                if board[r][c].getValue() == 0: # If value not given
                    self.buttons[r][c]["text"] = ""
                    self.setBtnState(self.buttons[r][c], "NORMAL")
                else:
                    self.buttons[r][c]["text"] = str(board[r][c].getValue())
                    self.setBtnState(self.buttons[r][c], "DATA")
                


if __name__ == '__main__':
    SudokuSolverGUI()