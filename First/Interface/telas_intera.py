from tkinter import *

def create_window():
    #new_window = Toplevel() # new window on top of other windows! Associate window
    new_window = Tk()
    old_window.destroy()

old_window = Tk()

button = Button(text='create new Window', command=create_window).pack()

old_window.mainloop()