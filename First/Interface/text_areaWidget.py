from tkinter import *

def submit():
    input = text.get("1.0",END)
    print(input)

window = Tk()

text = Text(window,
            bg="light yellow",
            font=("Ink Free",15),
            height=8,
            width=20,
            padx=10,
            pady=10,
            fg='purple')
text.pack()
button = Button(text='submit',command=submit)
button.pack()

window.mainloop()