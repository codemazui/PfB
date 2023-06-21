from array import array

#lists stores anything, any type
names = ['Christopher', 'Susan'] #pre-populatted
scores = [] #empty

scores.append(98) #append add a variable to the list
scores.append(99)

print(names)
print(scores)
print(scores[1])
print()

names = ['Christopher', 'Susan']
print(len(names)) # Get the number of items
names.insert(1, 'Bill') # Insert before index
print(names)
names.sort() #in case of strings, sort by alfabetic
print(names)
print()

names = ['Susan', 'Christopher', 'Bill']
presenters = names[0:2] # Get the first two items
# Starting index and number of items to retrieve

print(names)
print(presenters)
print()


#arrays only store numbers. all must be from the same type within the array
#arrays are objects. need to import library.
scores = array('d') #d is the type double
scores.append(97)
scores.append(98)
print(scores)
print(scores[1])


#dicionaries (keys/value pairs), storege order not guaranteed
person = {'first': 'Christopher'}
person['last'] = 'Harrison'
print(person)
print(person['first'])