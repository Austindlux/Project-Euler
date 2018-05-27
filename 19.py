"""How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?"""

months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']

# Index of what day it was, starting on tuesday Jan 1st, 1901
day = 2
year = 1901
month = 0

def days_in_month(month, year):
    """Returns how many days are in a month, given the month and year"""
    if month in ['jan', 'mar', 'may', 'jul', 'aug', 'oct', 'dec']:
        return 31
    if month in ['apr', 'jun', 'sep', 'nov']:
        return 30
    # Leap year
    if month == 'feb' and year % 4 == 0:
        return 29
    else:
        return 28

def find_day(new_day, month, year):
    """Returns what day the 1st of next month will be on"""
    difference = days_in_month(month, year) % 7
    if new_day + difference > 6:
        new_day = day + difference - 7
        return new_day
    else:
        new_day += difference
        return new_day

total = 0

while True:    
    # Sunday on the 1st of the month
    if day == 0:
        total += 1

    # For december, year +1
    if month == 11:
        day = find_day(day, months[month], year)
        month = 0
        year += 1
        continue

    day = find_day(day, months[month], year)
    month += 1

    if year == 2000 and month == 11:
        print(total)
        break
