# https://www.gov.pl/web/gov/czym-jest-numer-pesel

import re


def validate_pesel(pesel):
    pesel = str(pesel).strip()
    pattern = re.compile("^\d{4}([0][1-9]|[1-2][0-9]|[3][01])\d{5}$")
    if pattern.match(pesel):

        multiplier = 1
        total = 0
        for number in pesel[:-1]:

            value = int(number) * multiplier

            if multiplier == 1:
                multiplier = 3
            elif multiplier == 3:
                multiplier = 7
            elif multiplier == 7:
                multiplier = 9
            elif multiplier == 9:
                multiplier = 1

            if value > 9:
                total += int(str(value)[1])
            else:
                total += value

        if total > 9:
            control = 10 - int(str(total)[1])
        else:
            control = 10 - total

        if str(control) == pesel[-1]:
            return True

    return False
