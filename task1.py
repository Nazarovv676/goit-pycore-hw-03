from datetime import datetime

date_format = "%Y-%m-%d"


class DateFormatError(Exception):
    """
    Custom exception raised when the provided date string does not match the expected format.
    """
    pass


def get_days_from_today(date: str) -> int:
    """
    Calculates the number of days between the given date and today.

    Args:
        date (str): The date string in the format 'YYYY-MM-DD'.

    Returns:
        int: The number of days between the provided date and today. 
             A positive number indicates the date is in the past, 
             while a negative number indicates it is in the future.

    Raises:
        DateFormatError: If the provided date does not match the expected format '%Y-%m-%d'.
    """
    try:
        from_date = datetime.strptime(date, date_format)
    except ValueError:
        # Raise a custom exception if the date format is invalid
        raise DateFormatError

    from_days = from_date.toordinal()

    to_date = datetime.now()
    to_days = to_date.toordinal()

    diff = to_days - from_days

    return diff


# Example usage of the get_days_from_today function
print(get_days_from_today("2024-09-01"))

# Handle invalid date formats
try:
    print(get_days_from_today("trash"))
except DateFormatError:
    print("Invalid date format") 
