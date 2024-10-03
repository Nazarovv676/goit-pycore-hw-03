from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    """
    Get a list of upcoming birthdays within the next 7 days, including today.
    
    This function checks the birthdays of users and adjusts the congratulation date 
    to the next working day if the birthday falls on a weekend (Saturday or Sunday).

    Args:
        users (list): A list of dictionaries where each dictionary contains:
                      - 'name': (str) the user's name
                      - 'birthday': (str) the user's birthday in 'YYYY.MM.DD' format.
    
    Returns:
        list: A list of dictionaries containing the user's name and the corresponding
              congratulation date in 'YYYY.MM.DD' format.
    """
    date_format = '%Y.%m.%d'
    today = datetime.today().date()
    upcoming_birthdays = []
    
    for user in users:
        birthday = datetime.strptime(user["birthday"], date_format).date()
        
        birthday_this_year = birthday.replace(year=today.year)
        
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        
        if 0 <= (birthday_this_year - today).days <= 7:
            congratulation_date = birthday_this_year
            
            if congratulation_date.weekday() == 5:  # Saturday
                congratulation_date += timedelta(days=2)  # Move to Monday
            elif congratulation_date.weekday() == 6:  # Sunday
                congratulation_date += timedelta(days=1)  # Move to Monday
            
            upcoming_birthdays.append({
                'name': user['name'],
                'congratulation_date': congratulation_date.strftime(date_format)
            })

    return upcoming_birthdays


users = [
    {"name": "John Doe", "birthday": "1985.10.03"}, # Lower bound
    {"name": "Jane Smith", "birthday": "1990.10.10"}, # High bound
    {"name": "Joe Biden", "birthday": "1000.10.11"} # Out of range
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("List of upcoming birthdays this week:", upcoming_birthdays)
