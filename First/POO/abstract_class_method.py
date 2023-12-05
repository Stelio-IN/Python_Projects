from abc import ABC, abstractmethod
class Vehicle(ABC):
    #if you remove the only abstract method this class will be a normal class
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def cor(self):
        pass
class Car(Vehicle):
    def go(self):
        print("You drive te car")

    def cor(self):
        pass


class Motorcycle(Vehicle):
    def go(self):
        print("you ride the motorcycle")

    def cor(self):
        pass


#vehicle = Vehicle()
#vehicle.go()
car = Car()
motorcycle = Motorcycle()

motorcycle.go()
car.go()
