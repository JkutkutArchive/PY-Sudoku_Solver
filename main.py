import tkinter as tk

class SudokuSolver():
    # Variables:
    def __init__(self, root) -> None:
        # Variables:
        self.mainWidth, self.mainHeight = 500, 500
        self.mouseX, self.mouseY = 0, 0


        self.root = root

        # Setup:
        # self.root.geometry(f"{self.mainWidth}x{self.mainHeight}")
        self.root.minsize(self.mainWidth, self.mainHeight)

        # link special events to methods
        self.root.bind('<Motion>', self.mouseMove)
        self.root.bind("<Configure>", self.resize)
        self.root.bind("<Button-1>", self.leftMousePressed)

        # self.grid = tk.Frame(root)
        # self.grid = tk.Frame(root, width=self.mainWidth, height=self.mainHeight)
        # self.grid.pack(side=tk.BOTTOM)


        self.buttons = [[tk.Button(self.root, text="({}, {})".format(r, c)) for c in range(9)] for r in range(9)]

        for i in range(9):
            tk.Grid.rowconfigure(self.root, index=i, weight=1)
            tk.Grid.columnconfigure(self.root, index=i, weight=1)
            for j in range(9):
                btn = self.buttons[i][j]
                btn.grid(row=i, column=j, sticky='nsew')
    


    def mouseMove(self, event):
        '''
        When the mouse is moved over the screen, this function is executed.
        '''
        self.mouseX, self.mouseY = event.x, event.y # Store new values in a global variable

        indexX = self.mouseX // (self.mainWidth // 9)
        indexY = self.mouseY // (self.mainHeight // 9)
        print("{}, {}".format(indexX, indexY))

    def resize(self, event):
        '''
        When the screen is resized, this function is executed.
        '''
        self.mainWidth, self.mainHeight = event.width, event.height # Store the current window size on global variables

        # print("resize")

    def leftMousePressed(self, event):
        print("{} {}".format(self.mouseX, self.mouseY))


if __name__ == '__main__':
    window = tk.Tk(className='Sudoku solver')
    SudokuSolver(window)
    window.mainloop()