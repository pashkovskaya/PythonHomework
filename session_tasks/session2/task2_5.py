from typing import Tuple


def get_digits1(num: int) -> Tuple[int]:
    if num == 0:
        result = [0]
    else:
        num = abs(num)
        divider = 10
        result = []
        while num // divider > 0 or num % divider > 0:
            result.append(num % divider)
            num //= divider
    return tuple(reversed(result))


def get_digits2(num: int) -> Tuple[int]:
    return tuple(int(digit) for digit in str(abs(num)))


number = 1002020
print(get_digits1(number))
print(get_digits1(number))
