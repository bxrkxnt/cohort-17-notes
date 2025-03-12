'''Contains algorithm to determine latest time from a list of digits'''


def get_first_digit(digits: list[int]) -> int:

    optional_digits = []
    optional_digits_one = []
    for digit in digits:
        optional_digits.append(digit)
        if digit == 0 or digit == 1 or digit == 2:
            optional_digits_one.append(digit)

    first_digit = max(optional_digits_one)
    optional_digits.remove(first_digit)
    return first_digit, optional_digits


def get_second_digit(digits: list[int], first_digit: int) -> int:

    optional_digits = [x for x in digits if x <= 9]
    # print(optional_digits)

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

    optional_digits = [digit for digit in digits]
    optional_digits_third = [x for x in digits if x <= 6]

    # for debugging
    # print(optional_digits)
    # print(optional_digits_third)

    third_digit = max(optional_digits_third)
    optional_digits.remove(third_digit)

    return third_digit, optional_digits


def get_fourth_digit(digits: list[int]) -> int:
    if len(digits) <= 1:
        fourth_digit = digits[0]

    return fourth_digit


if (__name__ == "__main__"):

    first, first_list_remaining = get_first_digit([2, 5, 7, 0])

    second, second_list_remaining = get_second_digit(
        first_list_remaining, first)

    third, third_list_remaining = get_third_digit(second_list_remaining)

    fourth = get_fourth_digit(third_list_remaining)

    print(
        f"The latest time with the combination given is: {first}{second}:{third}{fourth}")
