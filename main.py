import tkinter as tk

# Variables:
mainWidth, mainHeight = 500, 500
mouseX, mouseY = 0, 0


window = tk.Tk(className='Sudoku solver')
window.geometry("500x500")

# greeting = tk.Label(text="Hello, Tkinter")
# greeting.pack()


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
    global mainWidth, mainHeight
    mainWidth, mainHeight = event.width, event.height # Store the current window size on global variables

def leftMousePressed(event):
    print("{} {}".format(mouseX, mouseY))

window.bind('<Motion>', motion)
window.bind("<Configure>", resize)
window.bind("<Button-1>", leftMousePressed)


# squareSizeW = mainWidth // 9
squareSizeW = 10
# squareSizeH = mainHeight // 9
squareSizeH = 5

colors = ["red", "blue"]

labels = [[None for __ in range(9)] for _ in range(9)]

for i in range(9):
    for j in range(9):
        # frame1 = tk.Frame(master=window, width=squareSizeW, height=squareSizeH, bg=colors[(9 * i + j) % 2])
        # frame1.pack(x=i*squareSizeW, y=j*squareSizeH)

        frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )
        frame.grid(row=i, column=j)
        labels[i][j] = tk.Label(master=frame, text=f"Row {i}\nColumn {j}", background=colors[(9 * i + j) % 2])
        labels[i][j].config(width=squareSizeW)
        labels[i][j].config(height=squareSizeH)
        labels[i][j].pack()

window.mainloop()