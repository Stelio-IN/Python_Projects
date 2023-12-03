#exception = events detected during execution that interrupt the flow of a program
try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
except ZeroDivisionError as e:
    print(e)
    print("You can divide by zero! idiot!!")
except ValueError as e:
    print(e)
    print("Enter only number please")
except Exception as e:
    print(e)
    print("somthing went wrong")
else:
    print(numerator / denominator)
finally:
    print("this will always execute")