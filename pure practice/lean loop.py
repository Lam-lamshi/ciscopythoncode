from datetime  import datetime

def isMagicDate (day,month,year):
    day = str(input("Enter the day : "))
    month = str(input("Enter the month : "))
    year = str(input("Enter the year : "))

    if day*month == year % 100:
        return True

    return False
def main():
    for year in range (1900,2000,2100):
        for month in range (1,13):
            for day in range (1,datetime(month,year)+1):
                if isMagicDate(day,month,year):
                    print("%02d/%02d/04d is a magic date." % day,month,year)
    main()