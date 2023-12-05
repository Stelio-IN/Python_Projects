

# def dobro(x):
#     return x*2
#
# print(dobro(10))

double = lambda x:x *2
print(double(10))
multiply = lambda x, y: x*y
print(multiply(10,2))
add = lambda x,y,z: x+y+z
print(add(10,5,5))
div = lambda x,y: x/y
print(div(40,2))
full_name = lambda first_name, last_name: first_name + " " + last_name
print(full_name("Stelio","Mondlane"))
age_check = lambda age: True if age>=18 else False
print(age_check(15))
age_check = lambda age: "Maior" if age>=18 else "Menor"
print(age_check(15))
