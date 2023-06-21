'''
greater >
less < 
greater or equal >=
less or equal <=
equal ==
not equal !=
x and y
x or y
x in [a,b,c] Does x match a or b or c
'''
price = float(input("whats the price?: "))

if price >= 1.00:
    tax = .07
else:
    tax = 0
print(tax)
print()


province = input("What province do you live in? ")
tax = 0

if province == 'Alberta' or province == 'Nunavut' or province == 'Yukon':
	tax = 0.05
elif province == 'Ontario':
	tax = 0.13
else:
	tax = 0.15
print(tax)
print()


country = input("What country do you live in? ")

if country.lower() == 'canada':
	province = input("What province/state do you live in? ")
	if province in('Alberta','Nunavut','Yukon'): #in operetor equal to many 'or's
		tax = 0.05
	elif province == 'Ontario':
		tax = 0.13
	else:
		tax = 0.15
else:
	tax = 0.0
print(tax)
print()


# A student makes honour roll if their average is >=85
# and their lowest grade is not below 70
gpa = float(input('What was your Grade Point Average? '))
lowest_grade = input('What was your lowest grade? ')
lowest_grade = float(lowest_grade)

if gpa >= .85 and lowest_grade >= .70:
	honour_roll = True
else:
	honour_roll = False

if honour_roll:
	print('You made honour roll')