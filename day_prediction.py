# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar

m, d, y = map(int, input('Enter the Date: ').split())

dow = calendar.weekday(y, m, d)

day = calendar.day_name[dow].upper()

print(day)