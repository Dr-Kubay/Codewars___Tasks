import calendar as c

def unlucky_days(year):
    return [c.weekday(year, m, 13) for m in range(1, 13)].count(4)


# tests:
print(unlucky_days(1634))
print(unlucky_days(1700))
print(unlucky_days(1812))
print(unlucky_days(1907))
print(unlucky_days(1945))
print(unlucky_days(2001))
print(unlucky_days(2020))
print(unlucky_days(2022))