import re


def normalize_phone(phone_number):
    """
    Normalize a phone number to the standard format for SMS sending.

    This function processes a phone number string by removing all characters except digits.
    It ensures that the phone number is in the correct format, specifically for Ukrainian phone numbers.

    Rules:
    - If the number has 9 digits, it assumes it's a local number and prepends '+380'.
    - If the number has 10 digits, it adds the '+38' international code.
    - If the number has 12 digits and starts with '38', it prepends '+'.
    - If the number is not valid (e.g., too short or an unsupported format), it raises a ValueError.

    Args:
        phone_number (str): The phone number in any format.

    Returns:
        str: The normalized phone number in the standard format with the international code.

    Raises:
        ValueError: If the phone number is too short or in an unsupported format.

    Example:
        >>> normalize_phone("067\t123 4567")
        '+380671234567'
        >>> normalize_phone("(095) 234-5678\n")
        '+380952345678'
        >>> normalize_phone("381234567890")
        ValueError: Unsupported country code
    """
    phone_number = re.sub(r"[^\d]", "", phone_number)

    if len(phone_number) < 9:
        raise ValueError("Not enough data for phone normalization")

    elif len(phone_number) == 9:
        phone_number = "+380" + phone_number

    elif len(phone_number) == 10:
        phone_number = "+38" + phone_number

    elif len(phone_number) == 12 and phone_number.startswith("38"):
        phone_number = "+" + phone_number

    else:
        raise ValueError("Incorrect phone number")

    return phone_number


raw_numbers = [
    "067\t123 4567",
    "(095) 234-5678\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
    "381234567890",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Normalized phone numbers for SMS sending:", sanitized_numbers)

try:
    normalize_phone("12345678")
except ValueError:
    print("Not complete phone number")


try:
    normalize_phone("123456789012")
except ValueError:
    print("Unsupported country code")
