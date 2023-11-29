#Normal loop 0 until range_Limit
import time

for i in range(10):
    print(i+1)
#loop between two numbers
for i in range(50,100):
    print(i)

#loop between two numbers and the jump
for i in range(0,10,2):
    print(i)

#loop for String
for i in "Stelio":
    print(i)


for seconds in range(10,0,-1):
    print(seconds)
    time.sleep(1)
print("Happy new year")