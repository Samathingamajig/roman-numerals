roman_decimal_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
roman_place_values = (
    "I II III IV V VI VII VIII IX".split(" "),
    "X XX XXX XL L LX LXX LXXX XC".split(" "),
    "C CC CCC CD D DC DCC DCCC CM".split(" "),
    "M MM MMM".split(" "),
)


def roman_to_decimal(roman: str) -> int:
    output = 0
    for i, c in enumerate(roman):
        val = roman_decimal_dict[c]
        if i < len(roman) - 1 and val < roman_decimal_dict[roman[i + 1]]:
            output -= val
        else:
            output += val

    return output


def decimal_to_roman(decimal: int) -> str:
    num = decimal
    i = 0
    output = ""
    while num > 0:
        if num % 10 > 0:
            output = roman_place_values[i][num % 10 - 1] + output
        i += 1
        num //= 10

    return output
