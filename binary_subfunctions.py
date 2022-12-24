import math


def exract_fraction(number: float) -> float:
        """возвращает дробную часть числа"""
        positive = number > 0
        return (number - math.floor(number) if positive
                else number - math.ceil(number))


def norm(base: int) -> float:
    exp = 0
    if base > 10:
        while base > 10:
            base /= 10
            exp += 1 
    elif base < 1:
        while  base < 1:
            base *= 10
            exp -= 1
    return (base,exp)

def fractial_to_bin(number: float) -> str:
    float_part = exract_fraction(number)
    output = '.'
    precision = norm(number)[1]
    while float_part !=0:
        float_part = float_part*2
        output += str (int(float_part))
        float_part = float_part - int(float_part)
    return output
