def get_date_based_on_year_and_nr_of_days(year, days):
    days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # Adjust for leap year
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        days_in_months[1] = 29  # February has 29 days in a leap year

    # Determine the month and the day
    month = 0
    while day > days_in_months[month]:
        day -= days_in_months[month]
        month += 1

    return str(day) + "." + str(month + 1) + "." + str(year)