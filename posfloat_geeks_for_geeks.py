# решение с geeksforgeeks 
from binary_subfunctions import exract_fraction
def positive_float(base: float, precision: int) -> str:
    '''переводим положительное дробное число в двоичную систему'''
    '''дробим число на целую и дробную части.
    Целую часть считаем как позитив инт.
    Дробную часть рекурсивно умножаем на два и "целое" от результата
     строково прибавляем к части после запятой, k раз
     k- точность, кол-во знаков после запятой'''

    base_fractured = [int(base), exract_fraction(base)]
    whole_part = parse_int(base_fractured[0])
    fractured_part = '.'
    base_fractured[1] = round(base_fractured[1], precision)
    tmp = base_fractured[1]
    for i in range(precision, 0, -1):
        tmp = round(tmp*2, precision)
        fractured_part += str(int(tmp))
        tmp = round(tmp - int(tmp), precision)
    output = f'{whole_part}{fractured_part}'
    return output