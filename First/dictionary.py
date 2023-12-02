# Criando um dicionário
meu_dicionario = {
    'nome': 'Alice',
    'idade': 30,
    'cidade': 'Wonderland'
}

# Acessando valores através das chaves
print("Nome:", meu_dicionario['nome'])
print("Idade:", meu_dicionario['idade'])
print("Cidade:", meu_dicionario['cidade'])

# Modificando valores
meu_dicionario['idade'] = 31
print("Nova Idade:", meu_dicionario['idade'])

# Adicionando um novo par chave-valor
meu_dicionario['profissao'] = 'Programadora'
print("Profissão:", meu_dicionario['profissao'])

# Removendo um par chave-valor
del meu_dicionario['cidade']

# Verificando a existência de uma chave antes de acessar
if 'cidade' in meu_dicionario:
    print("Cidade:", meu_dicionario['cidade'])
else:
    print("Cidade não está presente no dicionário.")

capitals = {'USA':'Washington',
            'MOZ':'Maputo',
            'Russia':'Moscow'}
#to app new value ou update
capitals.update({'Germany':'Berlin'})
capitals.update({'MOZ':'MPT'})
#capitals.pop('Russia')
#capitals.clear()
for key, value in capitals.items():
    print(key,value)