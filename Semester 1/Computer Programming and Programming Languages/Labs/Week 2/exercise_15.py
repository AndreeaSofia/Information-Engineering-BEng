from datetime import datetime


def get_age_of_person_in_number_of_days(birthdate, current_date):
    birthdate_dt = datetime.strptime(birthdate, "%d.%m.%Y")
    current_date_dt = datetime.strptime(current_date, "%d.%m.%Y")
    
    age_in_days = (current_date_dt - birthdate_dt).days
    
    return age_in_days