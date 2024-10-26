def get_age_of_person_based_on_birthdate_and_current_date(day, month, year, person_day, person_month, person_year):
    age = year - person_day

    if (month < person_month) or (month == person_month and day < person_day):
        age = age - 1

    return age