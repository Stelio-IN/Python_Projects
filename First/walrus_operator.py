#assigns values to variables as part of a larger expression
# status = True
# print(status)
# #print(status = true) erro
# print(status := True)


foods = list()
# while True:
#     food = input("what food you like?: ")
#     if food =="quit":
#         break
#     foods.append(food)

while (food := input("what food do you like?: ")) != "quit":
    foods.append(food)

for i in foods:
    print(i)

#assignment methods

def print_you_name():
    print(input("Enter your name: "))

name = print_you_name
name()

say = print
say("Involution is more than you sksksk! it's a joke :)")