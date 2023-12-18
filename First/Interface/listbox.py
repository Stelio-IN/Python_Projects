

from tkinter import *
def submit():
   # print('you have ordered')
    # print(listbox.get(listbox.curselection()))
    food = []
    for i in listbox.curselection():
        food.insert(i,listbox.get(i))


    for i in food:
        print(i)
def add():
    listbox.insert(listbox.size(),entryBox.get())
    listbox.config(height=listbox.size())

def delete():
    for index in reversed(listbox.curselection()):
        listbox.delete(index)

    listbox.config(height=listbox.size())
   # listbox.delete(listbox.curselection())


window = Tk()

listbox = Listbox(window,
                  bg='#f7ffde',
                  font=('Constancia',20),
                  width=12,
                  selectmode= MULTIPLE)

listbox.pack()
listbox.insert(1,'pizza')
listbox.insert(2,'salad')
listbox.insert(3,'soup')
listbox.insert(4,'garlic bread')
listbox.insert(5,'pasta')

entryBox= Entry(window)

listbox.config(height=listbox.size())

submitButton = Button(window,text='submit',command=submit)
addButton = Button(window,text='add',command=add)
deleteButton = Button(window,text='delete',command=delete)


entryBox.pack()
submitButton.pack()
addButton.pack()
deleteButton.pack()
window.mainloop()