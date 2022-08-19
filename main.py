from tkinter import *

HOMEBGCOLOR = "black"

root = Tk()
root.config(bg = HOMEBGCOLOR)

homeLabel = Label(root, text = "Home", bg = HOMEBGCOLOR, fg = "white").pack()

root.mainloop()