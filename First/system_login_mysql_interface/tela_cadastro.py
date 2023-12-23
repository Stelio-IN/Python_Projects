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

def cadastrar():
    cursor = conexao.cursor()

    cursor.execute(f'INSERT INTO alunos (nome,email,celular,password,curso) VALUES ("{txt_nome.get()}","{txt_email.get()}",'
                   f'{txt_celular.get()},"{txt_password.get()}","{txt_curso.get()}")')
    conexao.commit()
    cursor.close()

window = customtkinter.CTk()
window.geometry("500x300")

label = customtkinter.CTkLabel(window, text="Tela Cadastro")
label.pack(padx=10, pady=10)

txt_nome = customtkinter.CTkEntry(window, placeholder_text="Nome, ex: stelio", width=170)
txt_nome.pack(padx=10, pady=5)

txt_email = customtkinter.CTkEntry(window, placeholder_text="ex: stelioin@gmail.com", width=170)
txt_email.pack(padx=10, pady=5)

txt_celular = customtkinter.CTkEntry(window, placeholder_text="ex: 842156451", width=170)
txt_celular.pack(padx=10, pady=5)

txt_morada = customtkinter.CTkEntry(window, placeholder_text="morada, ex: magoanine C", width=170)
txt_morada.pack(padx=10, pady=5)

txt_curso = customtkinter.CTkEntry(window, placeholder_text="curso, ex: informatica", width=170)
txt_curso.pack(padx=10, pady=5)

txt_password = customtkinter.CTkEntry(window, show="*", placeholder_text="********", width=170)
txt_password.pack(padx=10, pady=5)

button = customtkinter.CTkButton(window, text="Cadastrar", command=cadastrar)
button.pack(padx=10, pady=10)

window.mainloop()
