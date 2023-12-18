from tkinter import *
from tkinter import Scale

def submit():
    print("The Temperature is: "+ str(scale.get())+" degrees C")

window = Tk()

window.geometry("300x250")

scale  = Scale(window,
               from_=100,
               to=0,
               length=200,
               orient=VERTICAL, #orientation of scale
               font=('consolas',20),
               tickinterval=10, #this add numeric indicators of value
               resolution=5,     #incriment of slider
               troughcolor='blue',
               fg = 'red',
               bg= 'black'
               )


button = Button(window, text='submit', command=submit)


scale.pack()
button.pack()
window.mainloop()

