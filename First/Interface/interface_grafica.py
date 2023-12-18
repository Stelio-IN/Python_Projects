#there you gonna found button input and label

from tkinter import*
from tkinter import PhotoImage

window = Tk() #instantiate an instance of a window

window.geometry("420x420")
window.title("First_GUI_Program")

icon = PhotoImage(file='logo.png')
window.iconphoto(True,icon)
window.config(background="blue")

#Label
label = Label(window,
              text ="Stelio Acacio Mondlane",
              font=('Arial',10,'bold'),
              fg='#00FF00',  #Foreground
              bg='yellow',    #Bacground
              relief=SUNKEN, #Border style
              bd=7,          #Border size
              pady=5,
              padx=5,
              image=icon,    #add Image
              compound='bottom')
#Add image on window
label.pack()
#label.place(x=10,y=50)

window.mainloop() #place window on computer screen, listen for events

window_2 = Tk()
icon: PhotoImage = PhotoImage(file='logo.png')

count =0
def click():
    global  count
    count +=1
    print(count)
  #  print("you clicked the button")
button = Button(window_2,
                text="Clique me",
                command=click,   #Action
                font=("Comic Sans",30),
                fg="#00FF00",
                bg="black",
                activebackground="black",
                activeforeground="#00FF00",
                state=ACTIVE,  #Desable de button
                image=icon,
                compound='bottom'
                )
button.pack()

window_2.mainloop()

def send():
   username=  entry.get()
   print(username)
  # entry.config(state=DISABLED)

def delet():
    entry.delete(0,END)
def backspace():
    entry.delete(len(entry.get())-1,END)

window_3 = Tk()

entry = Entry(window_3,
              font=("Arial",35),
              fg="#00FF00",
              bg="black",
      #        show= "*"
              )
#entry.insert(0,"Stelio IN")

button_submit = Button(window_3,text= "Send",command=send)
button_delet = Button(window_3,text= "delet",command=delet)

button_backspace = Button(window_3,text= "backspace",command=backspace)

entry.pack(side=LEFT)
button_submit.pack(side=LEFT)
button_delet.pack(side=LEFT)
button_backspace.pack(side=LEFT)


window_3.mainloop()

