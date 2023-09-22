from datetime import date, timedelta

def unlucky_days(year):

    result = 0

    for m in range(1, 13):
        if date(year, m, 13).weekday() == 4:
            result += 1
    return result

# tests:
print(unlucky_days(1634))
print(unlucky_days(1700))
print(unlucky_days(1812))
print(unlucky_days(1907))
print(unlucky_days(1945))
print(unlucky_days(2001))
print(unlucky_days(2020))
print(unlucky_days(2022))