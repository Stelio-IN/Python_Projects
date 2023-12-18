from tkinter import *
from tkinter import ttk

window = Tk()

notebook = ttk.Notebook(window)

tab1 = Frame(notebook)
tab2 = Frame(notebook)

notebook.add(tab1,test="tab1")
notebook.add(tab2,test="tab2")

window.mainloop()