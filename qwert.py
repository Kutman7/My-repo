import tkinter as tk


def onLeave(event):
    b.config(bg='yellow')


def onEnter(event):
    b.config(bg='red')


root = tk.Tk()
root.minsize(100, 100)

b = tk.Button(root)
b.pack()
b.bind('<Leave>', onLeave)
b.bind('<Enter>', onEnter)

root.mainloop()