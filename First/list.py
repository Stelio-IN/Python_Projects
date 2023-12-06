
food = ["pizza", "Pao", "Salada"]
#print(food[0])
#food.append("feijao")
#food.pop()
#food.insert(0,"Banana")
#food.insert(0,"Laranja")
#food.sort()
#food.clear()

#for it
for i in food:
    print(i, end =" __ ")

print()
drinks = ["Coca","Fanta","Cha"]
dessert = ["cake", "ice cream"]

comida = [food,drinks,dessert]
print(comida[2][1])


students = [1,20,19,16,8,10,5,4,18,8,16]
print(students)
passed_students = list(filter(lambda x:x>=14,students))
print(passed_students)
passed_students = [i for i in students if i>=14]

print(passed_students)
passed_students = [i if i>=14 else "FAILED" for i in students]
print(passed_students)
passed_students = ["PASS" if i>=14 else "FAILED" for i in students]
print(passed_students)
