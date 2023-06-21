
name = "GABRIEL"
surname = "sturm"

print("hello " + name.capitalize() + " " + surname.capitalize())
print()
print(name.count("A"), " ", name.count("a")); #note the capitalize only changes the the print, not the variable
print()
output = "Hello, {0} {1}".format(name.capitalize(), surname.capitalize())
print(output)
print()
output = f"Hello, {name.capitalize()} {surname.capitalize()}" #only works in python 3
print(output)
print()
name = name.capitalize() #this is the way to change the variable
print(name)
print()
print(f"Hello, {name.capitalize()} {surname.capitalize()}") #works too
print()