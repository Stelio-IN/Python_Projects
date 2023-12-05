#sort array list

abc = ["z","s","f","w","b","a",]
abc.sort()
for i in abc:
    print(i, end =" ")
abc.sort(reverse=True)
print()
for i in abc:
    print(i, end =" ")
print()


#for sort a list
nomes = ("Stelio","Involution","Acacio","Mondlane","Paulo",)
sorted_names = sorted(nomes, reverse=True)
#sorted_names = sorted(nomes)
for i in sorted_names:
    print(i, end =" ")

print()

#for sort objecs
carros = [("Mazda","F",700),
          ("BMW","A",850),
          ("Auris","Z",650),
          ("Lexus","L",710),
          ("Xcova","E",500)]
#there python sort a first collun
carros.sort()
for i in carros:
    print(i)

print("<<<<<<<<<<<<<<<<<<S>>>>>>>>>>>>>>>>>>")
preco = lambda precos:precos[2]
carros.sort(key= preco, reverse= True)
for i in carros:
    print(i)

#Listas compostas
coluna_2 = lambda coluna:coluna[2]
students = (("SIN","A",7),
            ("INS","N",2),
            ("ISN","Z",1),
            ("SNI","X",4))
sort_students = sorted(students,key=coluna_2)
for i in sort_students:
    print(i, end=" ")
