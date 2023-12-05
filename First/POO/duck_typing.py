
class Duck:
    def walk(self):
        print("This duck is walking")
    def talk(self):
        print("This duck is qwacking")



class Chicken:
    def walk(self):
        print("This chicken is walking")
    def talk(self):
        print("This chicken is clucking")

    def test(self):
        print("Only for test")

class Person:
    def catch(self,duck):
      #  duck.walk()
        duck.talk()
        duck.test()
        print("You caught the critter")

duck = Duck()
chicken = Chicken()
person = Person()

person.catch(duck)
#this method will return olly the same method between a duck and chicken  because the parrameter is duck
#every method used in the duck class per person that the chicken class must have
person.catch(chicken)