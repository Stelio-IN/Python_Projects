
#break Loop, if is equals stop
while True:
    name = input("Enter your name: ")
    if name != "":
        break


phone = "+258-842-156-451"
#Continue Loop, if is equals continue
for i in phone:
    if i == "-":
        continue
    print(i, end="")

print()
#Pass Loop, do nothing
for i in range(1,21):
    if i == 13:
        pass
    else:
        print(i, end= "  ")