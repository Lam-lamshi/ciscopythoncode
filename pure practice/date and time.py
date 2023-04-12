from datetime import date

def is_magic_date(date, magic_number):
    return sum(int(digit) for digit in str(date.day) + str(date.month) + str(date.year)) == magic_number

def generate_magic_dates(start_year, end_year, magic_number):
    magic_dates = []
    for year in range(start_year, end_year + 1):
        for month in range(1, 13):
            for day in range(1, 32):
                try:
                    if is_magic_date(date(year, month, day), magic_number):
                        magic_dates.append(date(year, month, day))
                except ValueError:
                    pass
    return magic_dates
magic_dates = generate_magic_dates(1900, 2000, 42)
print(magic_dates)
