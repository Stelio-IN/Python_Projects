
'''
Logical operators (and, or , not)
not is a negation as if it is true it becomes false
'''
temp = int(input("What is the temperature outside?! "))
'''
if not(temp >= 0 and temp <= 18):
    print("The temperature is good today")
    print("go outside")
    '''
if temp >= 0 and temp <= 18:
    print("The temperature is good today")
    print("go outside")
elif temp < 0 or temp > 30:
    print("the temperature is bad today")
    print("stay inside")

print("outOfBounds") #out of if's