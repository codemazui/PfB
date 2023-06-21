
x = 42
y = 0

#this is for treating errors that are not debugging, like failing to conect to a server
#only use this if you are going to treat the error, or else, leve the error alone

try:
    print(x / y)
except ZeroDivisionError as e:
    # Optionally, log e somewhere
    print('Sorry, something went wrong')
except:
    print('Something really went wrong')
finally:
    print('This always runs on success or failure')