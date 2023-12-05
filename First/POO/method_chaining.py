
class Carro:

    def turn_on(self):
        print("You start the engine")
        return self

    def drive(self):
        print("you drive the car")
        return self
    def brake(self):
        print("you step on the brakes")
        return self
    def turn_off(self):
        print("you turn off the engine")
        return self

car = Carro()
car.turn_on()\
    .drive()\
    .brake()\
    .turn_off()
