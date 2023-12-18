from tkinter import *

def open():
    print("File was open")
def cut():
    print("you cut some text")

window = Tk()

image1 = PhotoImage(file='add.png')
image2 = PhotoImage(file='anchor.png')
image3 = PhotoImage(file='accept.png')
menubar = Menu(window)
window.config(menu=menubar)

fileMenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='File',
                    menu=fileMenu)
fileMenu.add_command(label='Open',
                     command=open,
                     image=image2,
                     compound='left')
fileMenu.add_command(label='Save',
                     image=image1,
                     compound='left'
                     )
fileMenu.add_separator()
fileMenu.add_command(label='Exit',
                     image=image3,
                     compound='left')


editMenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='edit',menu=editMenu)
editMenu.add_command(label='cut',command=cut)
editMenu.add_command(label='paste')
editMenu.add_command(label='copy')

window.mainloop()