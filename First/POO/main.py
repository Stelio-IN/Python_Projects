from car import Car

car_1 = Car("Toyota","Umpla",2022,"Red")
car_2 = Car("Mazda","Dupla",2022,"Black")
print(car_1.cor + " "+ car_1. modelo + " "+str(car_1.ano_fabrico)+ " "+car_1.marca )
car_2.drive()
car_1.stop()

