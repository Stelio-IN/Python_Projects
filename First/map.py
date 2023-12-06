#map() = applies a function to each item in an interable (list,tuple,etc)
#map(function,iterable)

store = [("shirt", 50.00),
         ("pants", 70.00),
         ("jacket",150.00),
         ("socks",15.00),] #Metical

#convert the second element on this list, metical to rand
#
to_rand = lambda data: (data[0],round(data[1]/0.35))
#to_dollar = lambda data: (data[0],round(data[1]/0.89))
store_rand = list(map(to_rand,store))

for i in store_rand:
    print(i, end=" ")