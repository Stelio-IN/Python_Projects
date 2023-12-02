# hierarchy of variable
#L = Local
#E = Enclosing
#G = Global
#B = Built-in



name = "stelio" #global scope

def display_name():
    name = "Invo" # local scope
    print(name)

print(name)
display_name()