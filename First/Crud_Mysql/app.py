import tkinter as tk
from tkinter import ttk
import mysql.connector

class TelaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tabela de Usuários")

        # Conexão com o banco de dados (MySQL neste caso)
        self.conexao = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='bdpython'
        )
        self.criar_tabela()

        # Variáveis para armazenar os dados da entrada
        self.id_var = tk.StringVar()
        self.nome_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.senha_var = tk.StringVar()
        self.celular_var = tk.StringVar()
        self.morada_var = tk.StringVar()

        # Labels e Entradas para inserir dados
        tk.Label(root, text="ID:").grid(row=0, column=0, padx=5, pady=5)
        tk.Entry(root, textvariable=self.id_var, state="readonly").grid(row=0, column=1, padx=5, pady=5)

        tk.Label(root, text="Nome:").grid(row=1, column=0, padx=5, pady=5)
        tk.Entry(root, textvariable=self.nome_var).grid(row=1, column=1, padx=5, pady=5)

        tk.Label(root, text="Email:").grid(row=2, column=0, padx=5, pady=5)
        tk.Entry(root, textvariable=self.email_var).grid(row=2, column=1, padx=5, pady=5)

        tk.Label(root, text="Senha:").grid(row=3, column=0, padx=5, pady=5)
        tk.Entry(root, textvariable=self.senha_var).grid(row=3, column=1, padx=5, pady=5)

        tk.Label(root, text="Celular:").grid(row=4, column=0, padx=5, pady=5)
        tk.Entry(root, textvariable=self.celular_var).grid(row=4, column=1, padx=5, pady=5)

        tk.Label(root, text="Morada:").grid(row=5, column=0, padx=5, pady=5)
        tk.Entry(root, textvariable=self.morada_var).grid(row=5, column=1, padx=5, pady=5)

        # Botões
        tk.Button(root, text="Carregar", command=self.carregar_dados).grid(row=0, column=2, padx=5, pady=5)
        tk.Button(root, text="Editar", command=self.editar_dados).grid(row=1, column=2, padx=5, pady=5)
        tk.Button(root, text="Gravar", command=self.gravar_dados).grid(row=2, column=2, padx=5, pady=5)
        tk.Button(root, text="Remover", command=self.remover_registro).grid(row=3, column=2, padx=5, pady=5)

        # Tabela
        self.tree = ttk.Treeview(root, columns=("ID", "Nome", "Email", "Senha", "Celular", "Morada"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nome", text="Nome")
        self.tree.heading("Email", text="Email")
        self.tree.heading("Senha", text="Senha")
        self.tree.heading("Celular", text="Celular")
        self.tree.heading("Morada", text="Morada")
        self.tree.grid(row=6, column=0, columnspan=3, padx=5, pady=5)

        # Carregar dados iniciais
        self.carregar_dados()

    def criar_tabela(self):
        cursor = self.conexao.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            nome VARCHAR(255),
                            email VARCHAR(255),
                            senha VARCHAR(255),
                            celular VARCHAR(20),
                            morada VARCHAR(255))''')
        self.conexao.commit()

    def carregar_dados(self):
        cursor = self.conexao.cursor()
        cursor.execute("SELECT * FROM usuarios")
        dados = cursor.fetchall()

        # Limpar a tabela
        for row in self.tree.get_children():
            self.tree.delete(row)

        # Preencher a tabela
        for dado in dados:
            self.tree.insert("", "end", values=dado)

    def editar_dados(self):
        selected_item = self.tree.selection()
        if selected_item:
            # Obter os dados da linha selecionada
            item = self.tree.item(selected_item)
            data = item["values"]

            # Preencher as variáveis de entrada com os dados selecionados
            self.id_var.set(data[0])
            self.nome_var.set(data[1])
            self.email_var.set(data[2])
            self.senha_var.set(data[3])
            self.celular_var.set(data[4])
            self.morada_var.set(data[5])

    def gravar_dados(self):
        # Obter os valores das variáveis de entrada
        nome = self.nome_var.get()
        email = self.email_var.get()
        senha = self.senha_var.get()
        celular = self.celular_var.get()
        morada = self.morada_var.get()

        if nome and email and senha and celular and morada:
            # Se o ID já estiver preenchido, atualizar o registro
            if self.id_var.get():
                cursor = self.conexao.cursor()
                cursor.execute("UPDATE usuarios SET nome=%s, email=%s, senha=%s, celular=%s, morada=%s WHERE id=%s",
                               (nome, email, senha, celular, morada, self.id_var.get()))
                self.conexao.commit()
            else:
                # Inserir um novo registro
                cursor = self.conexao.cursor()
                cursor.execute("INSERT INTO usuarios (nome, email, senha, celular, morada) VALUES (%s, %s, %s, %s, %s)",
                               (nome, email, senha, celular, morada))
                self.conexao.commit()

            # Limpar as variáveis de entrada
            self.id_var.set("")
            self.nome_var.set("")
            self.email_var.set("")
            self.senha_var.set("")
            self.celular_var.set("")
            self.morada_var.set("")

            # Atualizar a tabela
            self.carregar_dados()
        else:
            print("Preencha todos os campos antes de gravar.")

    def remover_registro(self):
        selected_item = self.tree.selection()
        if selected_item:
            # Obter o ID do registro selecionado
            item = self.tree.item(selected_item)
            id_selecionado = item["values"][0]

            # Remover o registro do banco de dados
            cursor = self.conexao.cursor()
            cursor.execute("DELETE FROM usuarios WHERE id=%s", (id_selecionado,))
            self.conexao.commit()

            # Limpar as variáveis de entrada
            self.id_var.set("")
            self.nome_var.set("")
            self.email_var.set("")
            self.senha_var.set("")
            self.celular_var.set("")
            self.morada_var.set("")

            # Atualizar a tabela
            self.carregar_dados()
        else:
            print("Selecione um registro para remover.")


root = tk.Tk()
app = TelaApp(root)
root.mainloop()
