import tkinter as tk
import tkinter.font as TkFont
from tkinter.ttk import Separator as tkSeparator

from Classes.sudoku import Sudoku
import input

class SudokuSolverGUI():
    # ******* Constructor *******
    
    def __init__(self) -> None:
        # Variables:
        self.COLORS = {
            # Btns
            "BtnNormal": "#ffffff",
            "BtnData": "#ffffff",
            "BtnFocus": "#e0e0e0",
            "BtnSelected": "#b8b8b8",
            "BtnText": "black",
            # Separator = background
            "rootBg": "black"
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
        self.root.configure(background=self.COLORS.get("rootBg"))

        # Menu
        self.menu = tk.Menu(self.root)
        self.initMenu()

        # Setup:
        self.root.geometry(f"{self.mainWidth}x{self.mainHeight}")
        self.root.minsize(self.mainWidth, self.mainHeight)

        # link special events to methods
        # self.root.bind("<Configure>", self.resize)
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
        extraR = 0
        extraC = 0
        # for r in range(11):
        #     extraR = 0
        #     if r >= 3:
        #             extraR = extraR + 1
        #     if r >= 7:
        #         extraR = extraR + 1
        #     trueR = r - extraR
            
        #     if r != 3 and r != 7:
        #         self.buttons.append([])
        #         tk.Grid.rowconfigure(self.root, index=r, weight=3)
        #         tk.Grid.columnconfigure(self.root, index=r, weight=3)
        #     else:
                # tk.Grid.rowconfigure(self.root, index=r, weight=1)
                # tk.Grid.columnconfigure(self.root, index=r, weight=1)
                # continue
            

        #     for c in range(11):
        #         extraC = 0
        #         if c >= 3:
        #             extraC = extraC + 1
        #         if c >= 7:
        #             extraC = extraC + 1
        #         trueC = c - extraC
                
        #         if c != 3 and c != 7:
        #             self.buttons[trueR].append(
        #                 tk.Button(
        #                     self.root,
        #                     background = self.COLORS.get("BtnNormal"),
        #                     activebackground = self.COLORS.get("BtnFocus"),
        #                     disabledforeground = self.COLORS.get("BtnText"),
        #                     bd=3
        #                 )
        #             )
        #             self.buttons[trueR][trueC].grid(row=r, column=c, sticky='nsew')
        #         # else:
        #         #     continue

        # for r in range(21):
        #     if r % 2 == 1: # Small gaps
        #         # print(r)
        #         tk.Grid.rowconfigure(self.root, index=r, weight=1)
        #         tk.Grid.columnconfigure(self.root, index=r, weight=1)
        #         continue
            
        #     if r != 6 and r != 14: # Cell index
        #         self.buttons.append([])
        #         tk.Grid.rowconfigure(self.root, index=r, weight=30)
        #         tk.Grid.columnconfigure(self.root, index=r, weight=30)

        #         trueR = r * 2

        #         if r >= 3:
        #             trueR = trueR + 2
        #         if r >= 6:
        #             trueR = trueR + 2

        #         indexR = r // 2

        #         if r >= 8:
        #             indexR = indexR - 1
        #         if r >= 14:
        #             indexR = indexR - 1
        #         # indexR = indexR * 2           

        #     else: # Big gaps
        #         tk.Grid.rowconfigure(self.root, index=r, weight=8)
        #         tk.Grid.columnconfigure(self.root, index=r, weight=8)
        #         continue

        #     for c in range(9):
        #         trueC = c * 2

        #         if c >= 3:
        #             trueC = trueC + 2
        #         if c >= 6:
        #             trueC = trueC + 2
                
        #         print(str((indexR, c)) + " -> " + str(""))
        #         self.buttons[indexR].append(
        #             tk.Button(
        #                 self.root,
        #                 background = self.COLORS.get("BtnNormal"),
        #                 activebackground = self.COLORS.get("BtnFocus"),
        #                 disabledforeground = self.COLORS.get("BtnText"),
        #                 bd=3
        #             )
        #         )
        #         self.buttons[indexR][c].grid(row=trueR, column=trueC, sticky='nsew')

        for r in range(21):
                if r % 2 == 1: # Small gaps
                    tk.Grid.rowconfigure(self.root, index=r, weight=4)
                    tk.Grid.columnconfigure(self.root, index=r, weight=4)
                    continue
                
                if r != 6 and r != 14: # Cell index
                    self.buttons.append([])
                    tk.Grid.rowconfigure(self.root, index=r, weight=30)
                    tk.Grid.columnconfigure(self.root, index=r, weight=30)
                else: # Big gaps
                    tk.Grid.rowconfigure(self.root, index=r, weight=8)
                    tk.Grid.columnconfigure(self.root, index=r, weight=8)
                    continue


        for r in range(9):
            trueR = r * 2
            if r >= 3:
                trueR = trueR + 2
            if r >= 6:
                trueR = trueR + 2
            
            for c in range(9):
                trueC = c * 2

                if c >= 3:
                    trueC = trueC + 2
                if c >= 6:
                    trueC = trueC + 2
                
                # print(str((r, c)) + " -> " + str(""))
                self.buttons[r].append(
                    tk.Button(
                        self.root,
                        background = self.COLORS.get("BtnNormal"),
                        activebackground = self.COLORS.get("BtnFocus"),
                        disabledforeground = self.COLORS.get("BtnText"),
                        bd=3
                    )
                )
                self.buttons[r][c].grid(row=trueR, column=trueC, sticky='nsew')
            
        

        

        # Fill the board
        self.loadEasy()

        self.root.mainloop()

    def initMenu(self):
        self.root.config(menu = self.menu)
        
        # Create menus
        file_menu= tk.Menu(self.menu)
        loadSudokuMenu= tk.Menu(file_menu)

        window_menu = tk.Menu(self.menu)
        windowSize_menu = tk.Menu(window_menu)
        
        # Configure menus
        # fileMenu
        self.menu.add_cascade(label="File", menu=file_menu) # Name of the menu

        file_menu.add_cascade(label="Load...", menu = loadSudokuMenu)
        file_menu.add_separator()
        file_menu.add_command(label="Exit",command=self.root.quit)

        # loadSudokuMenu
        loadSudokuMenu.add_command(label="Easy", command=lambda: self.loadSudoku(input.easy()))
        loadSudokuMenu.add_command(label="Medium", command=lambda: self.loadSudoku(input.medium()))
        loadSudokuMenu.add_command(label="Hard", command=lambda: self.loadSudoku(input.hard()))

        # windowMenu
        self.menu.add_cascade(label="Window", menu=window_menu)

        window_menu.add_cascade(label="Size", menu=windowSize_menu)

        # windowSizeMenu
        sizes = range(500, 1200, 100)
        format = [f"{n}x{n}" for n in sizes]
        print(format)
        for f in format:
            windowSize_menu.add_command(label=f, command=eval(
                    f"lambda: r(\"{f}\")",
                    # {"r": self.root.geometry, "fo": f}
                    {"r": self.root.geometry}
                    # {"r": print}
                )
            )
        

    # ******* GUI manipulation *******
    
    # def resize(self, event):
    #     '''
    #     When the screen is resized, this function is executed.
    #     '''
        # self.mainWidth, self.mainHeight = event.width, event.height # Store the current window size on global variables

    
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