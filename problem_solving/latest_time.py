'''Contains algorithm to determine latest time from a list of digits'''


def get_first_digit(digits: list[int]) -> int:

    optional_digits = []
    for digit in digits:
        if digit == 0 or digit == 1 or digit == 2:
            optional_digits.append(digit)

    first_digit = max(optional_digits)
    optional_digits.remove(first_digit)
    return first_digit, optional_digits


def get_second_digit(digits: list[int], first_digit: int) -> int:

    optional_digits = [x for x in digits if x in range(0, 9)]
    print(optional_digits)
    if first_digit == 2:
        optional_digits_two = []
        for digit in optional_digits:
            if digit == 0 or digit == 1 or digit == 2:
                optional_digits_two.append(digit)

        second_digit = max(optional_digits_two)
        optional_digits.remove(second_digit)
        return second_digit, optional_digits

    else:
        second_digit = max(optional_digits)
        optional_digits.remove(second_digit)
        return second_digit, optional_digits


def get_third_digit(digits: list[int]) -> int:

    optional_digits = [x for x in digits if x in range(0, 6)]
    third_digit = max(optional_digits)
    optional_digits.remove(third_digit)

    return third_digit, optional_digits


def get_fourth_digit(digits: list[int]) -> int:
    if len(digits) <= 1:
        fourth_digit = digits[-1]

    return fourth_digit


if (__name__ == "__main__"):

    first, first_list_remaining = get_first_digit([1, 9, 0, 8])

    second, second_list_remaining = get_second_digit(
        first_list_remaining, first)

    third, third_list_remaining = get_third_digit(second_list_remaining)

    fourth = get_fourth_digit(third_list_remaining)

    print(
        "The latest time with the combination given is: {first}{second}:{third}{fourth}")
