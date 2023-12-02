
def soma(a,b):
#pass - if you don't know what the function will do
    print(str(a+b))

soma(15,10)

#abs() _ Valor absoluto
#math.ceil() _ Excesso
#math.floor() _ Defeito
#round() _ valor Proximo
def media(a,b):
    print("Sua Media é:"+ str(round((a+b)/2)))

media(float(input("Digite sua nota_1: ")),float(input("Digite sua nota_2: ")))


#return statement
def multiply(number1,number2):
    return number1*number2
print(multiply(2,6))

#Keyword arguments
def status(name,nota_1,nota_2):
    media = round((nota_1+nota_2)/2)
    if media>20 or media<0:
        print(name + ". Situacao: Invalido, Media: " + str(media))
    elif media < 10:
        print(name + ". Situacao: Excluido, Media: "+str(media))
    elif media < 14 and media > 10:
        print(name + ". Situacao: Aprovado, Media: "+str(media))
    elif media >= 14 and media <= 20:
        print(name + ". Situacao: Dispensado, Media: "+str(media))

status(nota_1 = float(input("Digite a Primeira nota: ")),name = input("Nome do aluno: "),nota_2 = float(input("Digite a Segunda nota: ")))


print(round(abs(float(input("Enter a whole Psitive number: ")))))



