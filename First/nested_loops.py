#loops internos
from builtins import map
'''
rows = int(input("How many rows: "))
columns = int(input("How many columns: "))
symbol =input("Enter a symbol to use: ")

for i in range(rows):
    for j in range(columns):
        print(symbol,end=" ")
    print()

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# Iterando sobre as linhas da matriz
for i in range(len(matriz)):
    # Iterando sobre os elementos de cada linha
    for j in range(len(matriz[i])):
        print(matriz[i][j], end=" ")
    print()

#Criando Matriz e atribuindo valores 
matriz = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        matriz[i][j] = int(input("Digite o numero na posicao: ["+str(i) +"] [" + str(j)+"]" ))

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(matriz[i][j], end=" ")
    print()
'''
# Digitar numero de linhas e colunas
num_linhas = int(input("Digite o número de linhas da matriz: "))
num_colunas = int(input("Digite o número de colunas da matriz: "))

# Declarar uma matriz vazia com base na entrada do usuário
matriz = [[0 for _ in range(num_colunas)] for _ in range(num_linhas)]

for i in range(num_linhas):
    for j in range(num_colunas):
        valor = int(input(f"Digite o valor para a posição ({i+1}, {j+1}): "))
        matriz[i][j] = valor

# Imprimir a matriz
print("Matriz resultante:")
for linha in matriz:
    print(linha)
