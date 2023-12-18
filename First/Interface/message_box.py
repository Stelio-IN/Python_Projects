from tkinter import *
from tkinter import messagebox


def click():
    # messagebox.showinfo(title='This is an info box',message="you are person")
    # while True:
    #    messagebox.showwarning(title='Warning',message="you have a Virus")
    # messagebox.showerror(title='ERROR',message='Something is wrong')

    # if messagebox.askokcancel(title='ask ok cancel',message='Do you want to do the thing?'):
    #     print("Yes you want")
    # else:
    #     print("No, you don't")

    # if messagebox.askretrycancel(title='ask ok cancel', message='Do you want to retry the thing?'):
    #     print("Yes, i want")
    # else:
    #     print("No, i don't")
    #
    if messagebox.askyesno(title='ask yes or no', message='Do you like cake?', icon='warning'):
        print("Yes, i like")
    else:
        print("No, i don't like")

window = Tk()

button = Button(window,text='clique me', command=click)

button.pack()

window.mainloop()