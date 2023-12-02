
#args = parameter that will pack all arguments into a tuple

def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum
print(add(1,2,3,4,5,6))
def mul(*sin):
    mult =1;
    for i in sin:
        mult*=i
    aux = list(sin)
    aux[0] = 0;
    multaux = 1;
    for i in aux:
        multaux *= i;
    print(multaux)
    return mult
print(mul(1,2,3,4,5,6))

#kwargs = parameter that will pack all arguments into a dicionary

#def hello(**name):
def hello(**kwargs):
    print("Hello "+kwargs['first'] + " "+ kwargs['last'])
    print("hello ", end = "")
    for key,value in kwargs.items():
        print(value,end="")

hello(title = "Mr.",first = "Stelio", middle ="Acacio", last= "Mondlane")
