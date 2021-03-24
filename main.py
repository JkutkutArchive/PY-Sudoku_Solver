import tkinter as tk

# Variables:
mainWidth, mainHeight = 500, 500
mouseX, mouseY = 0, 0


window = tk.Tk(className='Sudoku solver')
window.geometry("500x500")

greeting = tk.Label(text="Hello, Tkinter")
greeting.pack()


def motion(event):
    '''
    When the mouse is moved over the screen, this function is executed.
    '''
    global mouseX, mouseY
    mouseX, mouseY = event.x, event.y

def resize(event):
    '''
    When the screen is resized, this function is executed.
    '''
    global mainWidth, mainHeight
    mainWidth, mainHeight = event.width, event.height

window.bind('<Motion>', motion)
window.bind("<Configure>", resize)

window.mainloop()