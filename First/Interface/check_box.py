from tkinter import *


def display():
    if(x.get()==1):
        print("You agree :)")
    else:
        print("you don't agree :(")
def display_1():
    if(x.get()):
        print("You agree :)")
    else:
        print("you don't agree :(")
def display_2():
    if(x.get()=="yes"):
        print("You agree :)")
    else:
        print("you don't agree :(")
window = Tk()
window.geometry("200x200")
x = IntVar()
y = BooleanVar()
z = StringVar()
image = PhotoImage(file='anchor.png')

check_button = Checkbutton(window,
                           text="Do you like a thing",
                           variable=x,
                           onvalue=1,
                           offvalue=0,
                           command=display,
                           font=('Arial',10),
                           fg="#00FF00",
                           background="black",
                           activeforeground="#00FF00",
                           activebackground="black",
                           image=image,
                           compound='left',
                           )


check_button_1 = Checkbutton(window,
                           text="Do you like a thing",
                           variable=y,
                           onvalue=True,
                           offvalue=False,
                           command=display,
                           font=('Arial',10),
                           fg="#00FF00",
                           background="yellow",
                           activeforeground="#00FF00",
                           activebackground="yellow",
                           image=image,
                           compound='left',
                           )

check_button_2 = Checkbutton(window,
                           text="Do you like a thing",
                           variable=z,
                           onvalue="yes",
                           offvalue="no",
                           command=display,
                           font=('Arial',10),
                           fg="#00FF00",
                           background="red",
                           activeforeground="#00FF00",
                           activebackground="red",
                           image=image,
                           compound='left',
                           )
check_button_2.pack()
check_button_1.pack()
check_button.pack()
window.mainloop()