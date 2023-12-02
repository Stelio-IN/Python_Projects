
name = "Stelio Acacio Mondlane"
if(name[0].islower()):
    #First to upcase
    name = name.capitalize()
else:
    name = name.upper()
print(name)

#Create subString
#name[0:6]
first_name = name[:6].upper()
last_name = name[7:].lower()
print(first_name)
print(last_name)

#penultimo name[-2]
last_caracter = name[-1]

print(last_caracter)