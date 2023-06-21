
def get_initial(name, force_uppercase=True):
    if force_uppercase:
        initial = name[0:1].upper()
    else:
        initial = name[0:1]
    return initial

first_name = input('Enter your first name: ')

# not passing a value for force_uppercase so default value is used
first_name_initial = get_initial(first_name) 

print('Your initial is: ' + first_name_initial)


def get_initial(name, force_uppercase):
    if force_uppercase:
        initial = name[0:1].upper()
    else:
        initial = name[0:1]
    return initial

first_name = input('Enter your first name: ')

# When you use named notation, you can specify parameters in any order
first_name_initial = get_initial(force_uppercase=True, name=first_name) 

print('Your initial is: ' + first_name_initial)