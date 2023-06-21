
#For loops takes each item in an array or collection in order, and assigns it to the variable you define.
names = ['Christopher', 'Susan']
for name in names:
    print(name)

# range creates an array
# First parameter is the starter
# Second indicates the number of numbers to create
# range(0, 2) creates [0, 1]
for index in range(0, 2):
	print(index)



#While loops perform an operation as long as a condition is true.
names = ['Christopher', 'Susan']
index = 0
while index < len(names):
    print(names[index])
    index = index + 1
