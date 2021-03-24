import tkinter as tk

root = tk.Tk()
root.geometry("500x500")

for i in range(9):
    tk.Grid.rowconfigure(root, index=i, weight=1)
    tk.Grid.columnconfigure(root, index=i, weight=1)

buttons = [[tk.Button(root, text="btn ({}, {})".format(r, c)) for c in range(9)] for r in range(9)]

for i in range(9):
    for j in range(9):
        btn = buttons[i][j]
        btn.grid(row=i, column=j, sticky='nsew')

root.mainloop()

# import tkinter as tk

# # Variables:
# mainWidth, mainHeight = 500, 500
# squareSizeW, squareSizeH = mainWidth // 9, mainHeight // 9
# mouseX, mouseY = 0, 0

# grid = None
# cells = [[None for __ in range(9)] for _ in range(9)]
# labels = [[None for __ in range(9)] for _ in range(9)]



# # Setup

# window = tk.Tk(className='Sudoku solver')
# window.geometry("500x500")


# def motion(event):
#     '''
#     When the mouse is moved over the screen, this function is executed.
#     '''
#     global mouseX, mouseY
#     mouseX, mouseY = event.x, event.y # Store new values in a global variable

# def resize(event):
#     '''
#     When the screen is resized, this function is executed.
#     '''
#     print(event)
#     if event.widget.widgetName == "toplevel":
#         return

    
#     global mainWidth, mainHeight, squareSizeW, squareSizeH, cells, labels
#     mainWidth, mainHeight = event.width, event.height # Store the current window size on global variables
#     squareSizeW, squareSizeH = mainWidth // 9, mainHeight // 9

#     # print("{}, {}".format(squareSizeW, squareSizeH))
#     # if (cells[0][0] == None):
#     #     return
#     # for i in range(9):
#     #     posX = i * squareSizeW
#     #     for j in range(9):
#     #         posY = j * squareSizeH
#     #         cell = cells[i][j]
#     #         # cell.config(width = squareSizeW)
#     #         # cell.config(height = squareSizeH)
#     #         cell.place(
#     #             x = posX,
#     #             y = posY
#     #         )





# def leftMousePressed(event):
#     print("{} {}".format(mouseX, mouseY))

# # squareSizeH = 5

# colors = ["white", "black"]

# # grid = tk.Frame(
# #     window,
# #     width = mainWidth,
# #     height = mainHeight,
# #     bg = "lightblue"
# # )
# # grid.pack_propagate(0) # Stops child widgets of label_frame from resizing it

# for i in range(9):
#     for j in range(9):
#         cells[i][j] = tk.Frame(
#             window,
#             width = squareSizeW,
#             height = squareSizeH,
#             bg = colors[(9 * i + j) % 2]
#         )
#         label = tk.Label(
#             cells[i][j],
#             bg="white",
#             fg="black",
#             text="test",
#             font=("Calibri",10)
#         )
#         label.pack()
#         cells[i][j].place(
#             x = i * squareSizeW,
#             y = j * squareSizeH
#         )

#         cells[i][j].pack_propagate(0) # Stops child widgets of label_frame from resizing it



# window.bind('<Motion>', motion)
# window.bind("<Configure>", resize)
# window.bind("<Button-1>", leftMousePressed)

# print(".")
# window.mainloop()