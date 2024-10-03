import random

def get_numbers_ticket(min, max, quantity):
    """
    Generate a sorted list of unique 'tickets', where each ticket is represented by a unique number 
    within a specified range.
    
    The function creates a set of 'tickets' by randomly selecting unique numbers from the given range.
    Each ticket corresponds to a single number, and the tickets are returned as a sorted list.

    Args:
        min (int): The minimum value (inclusive) that a ticket number can have.
        max (int): The maximum value (inclusive) that a ticket number can have.
        quantity (int): The number of unique tickets (numbers) to generate.
    
    Returns:
        list: A sorted list of unique 'tickets' (randomly generated numbers) if the inputs are valid.
              Returns an empty list if the inputs are invalid (e.g., if the range is too small for 
              the required quantity of tickets, or if min/max values are negative).
    
    Invalid scenarios (result in an empty list of tickets):
        - Either min or max is less than 0.
        - The min value is greater than the max value.
        - The range between min and max is smaller than the required quantity of tickets.
    
    Example:
        >>> get_numbers_ticket(10, 1000, 200)
        [11, 20, 25, 37, ..., 982, 999, 1000]  # A sorted list of 200 unique tickets.
    """
    if min < 0 or max < 0 or min > max or max - min < quantity:
        return []
    
    random_values = random.sample(range(min, max + 1), quantity)

    return sorted(random_values)

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)
