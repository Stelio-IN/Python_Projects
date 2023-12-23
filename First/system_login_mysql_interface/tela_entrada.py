import customtkinter
import mysql.connector

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='bdpython'
)

window = customtkinter.CTk()
window.geometry("500x300")


# -------------------------Function--------------------------------------
def login():
    cursor = conexao.cursor()
    comando = 'select * from alunos'
    cursor.execute(comando)
    resultado = cursor.fetchall()

    for i in resultado:
        if label_email.get() == i[2] and label_senha.get() == i[4]:
            print("Login successful")
            break
    else:
        print("Login failed")


# ---------------------------End-----------------------------------------

label = customtkinter.CTkLabel(window, text="Tela Login")
label.pack(padx=0, pady=10)

label_email = customtkinter.CTkEntry(window, placeholder_text="seu email")
label_email.pack(padx=10, pady=10)

label_senha = customtkinter.CTkEntry(window, show="*", placeholder_text="Digite sua senha")
label_senha.pack(padx=10, pady=10)

checkbox = customtkinter.CTkCheckBox(window, text="lembrar Login")
checkbox.pack(padx=2, pady=2)

botao = customtkinter.CTkButton(window, text="login", command=login)
botao.pack(padx=10, pady=10)

window.mainloop()
