#filter(function, iterable)

friends = [("Raquel",22),
           ("Macabeça",19),
           ("Samatha", 15),
           ("Paula",14),
           ("Ana",17)]

age = lambda data:data[1] >=18

drinking_buddies = list(filter(age,friends))

for i in drinking_buddies:
    print(i, end=" ")