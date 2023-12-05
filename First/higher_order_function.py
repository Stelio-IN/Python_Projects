

def loud(text):
    return text.upper()
def quiet(text):
    return text.lower()

def hello(func):
    text = func("hello")
    print(text)

hello(loud)
hello(quiet)

#y/x
def divisor(x):
    def dividend(y):
        return y/x
    return dividend

divede = divisor(5)
print(divede(15))