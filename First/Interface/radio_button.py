from tkinter import *

def order():
    if(x.get()==0):
        print("Pizza")
    if(x.get()==1):
        print("Hamburger")
    if(x.get()==2):
        print("Hotdog")
food = ["Pizza","Hamburger","Hotdog"]
window = Tk()

x = IntVar()

image_1 = PhotoImage(file='anchor.png')
image_2 = PhotoImage(file='add.png')
image_3 = PhotoImage(file='accept.png')
images = [image_1,image_2,image_3]
for index in range(len(food)):
    radio_button = Radiobutton(window,
                               text=food[index],
                               variable=x,
                               value=index,
                               padx= 25,
                               font=('impact',30),
                               image=images[index],
                               compound='left',
                             #  indicatoron=0 to remove circle indicato
                               command=order
                               )
    radio_button.config() #

    radio_button.pack(anchor =W)

window.mainloop()