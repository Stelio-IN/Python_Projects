from tkinter import *
from tkinter.ttk import *
import time

def start():
    tasks =10
    x=0
    while(x<tasks):
        time.sleep(1)
        bar['value']+=10
        x+=1
        percent.set(str((x/tasks)*100)+'%')
        window.update_idletasks()

window = Tk()
percent = StringVar()

bar = Progressbar(window,orient=HORIZONTAL,length=300)
bar.pack(pady=10)
percenteLabe = Label(window,textvariable=percent).pack()

button = Button(window,text='download',command=start).pack()


window.mainloop()