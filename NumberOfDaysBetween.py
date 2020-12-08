def days(date):
    year = int(date[0:4])
    month = int(date[5:7])
    days = int(date[8:10])
    daysInMonth = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    totalDays = 0

    for y in range(1900, year):
        if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
            # print(y, 'is a leap year')
            totalDays += 366
        else:
            # print(y, 'is not a leap year')
            totalDays += 365

    for m in range(1, month):
        if m == 2 and ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
            totalDays += daysInMonth[m] + 1
        else:
            # print(y, 'is not a leap year')
            totalDays += daysInMonth[m]
    
    return totalDays + days

# print(days("2020-12-07"))

def daysBetweenDates(date1, date2):
    num = days(date1) - days(date2)
    if num < 0:
        num = num * -1
    return num

print(daysBetweenDates("1971-06-29", "2010-09-23"))