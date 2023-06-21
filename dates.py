from datetime import datetime, timedelta

# print today's date
current_date = datetime.now()
print(current_date)

# print yesterday's date
one_day = timedelta(days=1)
yesterday = current_date - one_day
print('Yesterday was: ' + str(yesterday))

# ask a user to enter a date
date_entered = input('Please enter a date (dd/mm/yyyy): ')
date_entered = datetime.strptime(date_entered, '%d/%m/%Y')

# print the date one week from the date entered
one_week = timedelta(weeks=1)
one_week_later = date_entered + one_week
print('One week later it will be: ' + str(one_week_later))

today = datetime.now()

# use day, month, year, hour, minute, second functions
# to display only part of the date
# All these functions return integers
# Convert them to strings before concatenating them to another string
print('Day: ' + str(today.day))
print('Month: ' + str(today.month))
print('Year: ' + str(today.year))

print('Hour: ' + str(today.hour))
print('Minute: ' + str(today.minute))
print('Second: ' + str(today.second))