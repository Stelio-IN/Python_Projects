class Animal:
    alive = True

    def eat(self):
        print("this animal is eating")

    def sleep(self):
        print("this animal is sleeping")

class Rabbit(Animal):
  #  overwrite
    def eat(self):
        print("this rabbit animal is eating")
    def run(self):
        print("this rabbit is running")
class Fish(Animal):
    def swim(self):
        print("This fish is swimming")
class Hawk(Animal):
    def fly(self):
        print("This hawk is flying")

#Criando instancias das classes filhas
rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

rabbit.run()
fish.swim()
hawk.fly()

#Heranca Multipla
class SerVivo:
    alive = True

class Pessoa:
    genero = None

class Teste(SerVivo,Pessoa):
    nome = None

teste = Teste()
teste.nome = "Stelio"

print(teste.alive)
