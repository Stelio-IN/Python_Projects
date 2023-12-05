

class Retangle:
    def __init__(self,legth,width):
        self.length = legth
        self.width = width


class Square(Retangle):
    def __init__(self,legth,width):
        super().__init__(legth,width)

    def area(self):
        return self.length*self.width
class Cube(Retangle):
    def __init__(self,length,width,heigth):
        super().__init__(length,width)
        self.heigth = heigth
    def volume(self):
        return self.length*self.width*self.heigth


square = Square(3,4)
cube = Cube(3,2,5)
print("Volume cube: "+ str(cube.volume()))
print("Area square: "+ str(square.area()))
