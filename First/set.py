#set = collection whict is unordered, unindexed. no duplicate values, all type of itens

conjunto = {1, 2, 3, 4, 5,7}
print(conjunto)

conjunto.add(6)
print(conjunto)

conjunto.add(2)
print(conjunto)

conjunto.remove(3)
print(conjunto)

conjunto2 = {3,8,9,10}

#conjunto2.update(conjunto)
for x in conjunto2:
    print(x, end=" ")

#conjunto.clear()
conjunto3 = conjunto.union(conjunto2)
print(conjunto3)

#print(conjunto.difference(conjunto2))
#print(conjunto.intersection(conjunto2))