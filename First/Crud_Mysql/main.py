import mysql.connector
#Conexao
conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='bdpython'
)
#Criado variavel para ter acesso a conecxao
cursor = conexao.cursor()

#CRUD
# comando = ''
# cursor.execute(comando)
# conexao.commit() # edita o banco de dados
# resultado = cursor.fetchall() # ler do banco de dados



#Create
# nome = "Batatas"
# valor = 18
# comando= f'insert into vendas (nome_produto,valor) values ("{nome}", {valor}) '
# cursor.execute(comando)
# conexao.commit()


#Read
# comando= 'select * from vendas'
# cursor.execute(comando)
# resultado = cursor.fetchall()
# print(resultado)

#Update
# preco = 15
# nome = "Batatas"
# comando = f'update vendas set valor={preco} where nome_produto = "{nome}" '
# cursor.execute(comando)
# conexao.commit()


#Delete
id = 1
comando = f'delete from vendas where idvenda ={1} '
cursor.execute(comando)
conexao.commit()


cursor.close()
conexao.close()