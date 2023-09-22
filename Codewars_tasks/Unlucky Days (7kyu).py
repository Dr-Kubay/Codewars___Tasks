from datetime import date, timedelta

def unlucky_days(year):

    result = 0
    start_year = date(year, 1,1 )
    end_year = date(year, 12, 31)

    day = timedelta(days=1)

    while start_year <= end_year:
        if start_year.strftime('%A %d') == "Friday 13":
            result += 1
        start_year += day

    return result

print(unlucky_days(1634))
