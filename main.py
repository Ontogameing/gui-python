from tkinter import *

HOMEBGCOLOR = "black"
color_choice = "white"

root = Tk()
root.config(bg = HOMEBGCOLOR)
root.geometry("500x500")

todoTaskString = StringVar()

def addTask():
    todo = Checkbutton(root, text = todoTaskString.get(), bg = HOMEBGCOLOR, fg = "gray")
    removeTodo = Button(root, text = "X", bg = HOMEBGCOLOR, fg = "white", command = removeTask)
    todo.pack(); removeTodo.pack();

def removeTask():
    pass

todoLabel = Label(root, text = "todo", bg = HOMEBGCOLOR, fg = "white").pack()

todoTask = Entry(root, textvariable = todoTaskString, bg = color_choice, fg = "black").pack()
todoAddTask = Button(root, text = "Add Task", command = addTask).pack()

root.mainloop()