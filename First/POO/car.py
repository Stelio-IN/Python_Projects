class Car:

    rodas = 4 #class variable, podemos usar sem necessariamente instaciar um objecto da classe
    def __init__(self,marca,modelo,ano, cor):
        #instance variable, declare inside de construtor
        self.marca = marca
        self.modelo = modelo
        self.ano_fabrico = ano
        self.cor = cor
    def drive(self):
        print("This "+self.marca+"car  is driving")
    def stop(self):
        print("this "+self.marca+" car is stopped")



class Moto:
    color = None

#if you have a superclass you have to use the name of the superclass and this method will be used in all child classes
def change_color(moto,color):
    moto.color = color


moto_1 = Moto()
moto_2 = Moto()
moto_3 = Moto()

change_color(moto_1,"Black")
change_color(moto_2,"Yellow")
change_color(moto_3,"Red")

print(moto_3.color)
print(moto_2.color)
print(moto_1.color)