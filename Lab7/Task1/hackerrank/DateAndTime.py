import calendar

m, d, y = map(int, input().split())
day = calendar.day_name[calendar.weekday(y, m, d)]

print(day.upper())