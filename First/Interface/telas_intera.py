from tkinter import *
#
# def create_window():
#     #new_window = Toplevel() # new window on top of other windows! Associate window
#     new_window = Tk()
#     old_window.destroy()
#
# old_window = Tk()
#
# button = Button(text='create new Window', command=create_window).pack()
#
# old_window.mainloop()


def abrir_janela():
    janela2 = Tk()
    janela2.title("Secundaria")
 #   janela.destroy()
    label = Label(janela2,text="Nome:").grid(row=0,column=0)
    txt = Entry(janela2).grid(row=0,column=1)
    label1 = Label(janela2,text="senha:").grid(row=1,column=0)
    txt1 = Entry(janela2).grid(row=1,column=1)
    button = Button(janela2,text="Voltar",command=janela2.destroy).grid(row=2,column=1)

janela = Tk()

button = Button(janela, text="Outra tela",command=abrir_janela)
button.grid(row=0,column=0)
janela.mainloop()