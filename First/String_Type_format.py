text = "stelio mondlane"

print(len(text)) #length
print(text.find("o")) #busca caractere
print(text.capitalize()) #first caractere upper
print(text.upper()) #upperCase
print(text.lower()) #lowerCase
print(text.isdigit()) #boolean verificar se e digito
print(text.isalpha()) #boolean verificar se contem espaco
print(text.count("e")) #quantidade de um caractere
print(text.replace("e","w")) #trocar caracter selecionado em toda String
print(text*4) #Imprimir uma String numero de vezes


print()
print()

#dividindo String
name = "Stelio Mondlane"

first_name = name[0:6] #[:6]
last_name  = name[7:16] #[7:]
#subString pulando de dois em dois
teste = name[0:15:2] #[::2]
#invertendo String
reversed_name = name[::-1]

print(first_name)
print(last_name)
print(teste)
print(reversed_name)

#Cortar uma String mesmo formato
website1 = "http://google.com"
website2 = "http://youtube.com"
substring = slice(7,-4)
print(website1[substring])
print(website2[substring])


#str.format()
animal = "cow"
item = "moon"
#print("the {} jumped over the {}".format("cow","moon"))
print("the {} jumped over the {}".format(animal,item))

name = "stelio"

print("Hello, my name is {}".format(name))
print("Hello, my name is {:10}. Nice to meet you".format(name))
print("Hello, my name is {:1<0}. Nice to meet you".format(name))
print("Hello, my name is {:>10}. Nice to meet you".format(name))
print("Hello, my name is {:^10}. Nice to meet you".format(name))

number = 3.14159
print("Te number pi is {:.2f}".format(number))

n = 1000
print("The number is: {:b}".format(n)) #Convert to binary
print("The number is: {:o}".format(n)) #Convert to octal
print("The number is: {:x}".format(n)) #Convert to hexa
print("The number is: {:E}".format(n)) #Convert to notacao cientifi