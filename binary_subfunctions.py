"""
test_unique - проверял могут ли выводы кодирования повторяться.
Проверил миллиард флотов, не повторилось :)

parse_int - парсим инты, совпадая с bin()

extract_fraction - выделяем дробную часть числа

normalize - приводим float к одноразрядной целой части домножая на 10**n

fractial_to_bin - переводим "нормальный" float в двоичную систему

add_floating_point - делаем флот из инта

parse_float - переводим "любой" float в двоичную систему
"""


__version__ = "#3"
__author__ = "anton6733@gmail.com"

import math
import random

def parse_int(base: int) -> str:
    # вообще в интернете минимум два подхода по переводу
    # отрицательных интов в двоичную систему.
    # вот https://www.instructables.com/Convert-Negative-Numbers-to-Binary/
    # или вот https://cs.calvin.edu/activities/books/rit/chapter5/negative.htm#:~:text=The%20simplest%20is%20to%20simply,would%20be%20written%20as%2011100.
    # по итогу решил наследовать практику bin() - для интов
    output = ''
    base_i = abs(base)
    while base_i > 0:
        output = f'{str(base_i % 2)}' + output
        base_i //= 2
    prefix = '0b' if base > 0 else '-0b'
    if not output:
        output = '0'
    return f'{prefix}{output}'


def exract_fraction(number: float) -> float:
        """возвращает дробную часть числа"""
        positive = number > 0
        return (number - math.floor(number) if positive
                else number - math.ceil(number))


def normalize(base: float) -> tuple[float, int]:
    absbase = abs( base)
    digits = len(str(base))-1
    exp = 0
    if absbase > 10:
        while absbase > 10:
            absbase /= 10
            exp += 1 
    elif absbase < 1:
        while  absbase < 1:
            absbase *= 10
            exp -= 1
    return (round(absbase,digits),exp)


def fractial_to_bin(number: float,breakpoint: int = 64) -> str:
    """число должно быть нормализовано до входа сюда хммм :\ """
    whole_part = parse_int(int(number))
    whole_part = whole_part[whole_part.index('b')+1:]
    float_part = exract_fraction(number)
    round_to = len(str(float_part)) -2 # 0.
    output = '.'
    while float_part !=0:
        if not breakpoint: 
            break
        float_part = float_part*2
        output += str (int(float_part))
        float_part = round(float_part - int(float_part),round_to)
        breakpoint -= 1
    return f'{whole_part}{output}'


def test_unique():
    '''проверяем уникальность выводов.'''
    # если округлять q до 32 знаков, то проходят значения до 1/46409
    # а если не округлять - обработало 1/10**9 без прерывания. 
    unique_values = set()
    w = 0
    for i in range(1,100000000):
        q=fractial_to_bin(1/i)
        if q in unique_values:
            print(i, q,'!')
            break
        unique_values.add(q)
        w += 1
        if  not w % 1000 :
            print(w)


def add_floating_point(base: int = 0, round_to: int = 3) -> float:
    """рандомим дробную часть числа.

    base - прибавляем дробь к этому

    round_to - округляем до этого знака
    """
    return base + round(random.random(), 3)


def parse_int(base: int) -> str:
    """переводим base в двоичную систему"""    
    output = ''
    base_i = abs(base)
    while base_i > 0:
        output = f'{str(base_i % 2)}' + output
        base_i //= 2
    prefix = '0b' if base > 0 else '-0b'
    return f'{prefix}{output}'


def parse_float(base: float) -> str:
    """
    флоаты это вообще ховайся.
    # http://cstl-csm.semo.edu/xzhang/Class%20Folder/CS280/Workbook_HTML/FLOATING.htm
    """
    # переводим бинарную дробь в десятичное число
    # .1011 = 1/2 + 0/4 + 1/8 + 1/16 ==
    # 0.5 + 0 + 0.125 + 0. 0625 == 0.6875
    # слева от точки - по интовым правилам.
    # :( чо так сложно то :)
    # будем делать short real - числа в 32 бита ._.
    # Sign - первый бит- 0 для положительных; 1 для отрицательных
    # Exponent - 8 бит - наименьшая степень 10 больше числа. Ну т.е.
    # количество знаков в дроби
    # mantissa - само число, нормализованное, степени базы обрезаем
    # например:
    # число 0.41 это (s) 0 (e) -1 (m) 4.1

    sign = '1' if base < 0 else '0'
    mantissa_decimal, exponent_decimal = normalize(base)
    if exponent_decimal > 128:
        raise NotImplementedError('реализовано только для 32-битных'
                                    + 'чисел')
    exponent = parse_int(exponent_decimal + 127)[2:].rjust(8, '0')
    mantissa = fractial_to_bin( mantissa_decimal) 
    mantissa = (mantissa.replace('.', '')
                .removeprefix('1')  # первую еденичку убирают- тавтология
                .rjust(23, '0'))[:23]
    return f'{sign} {exponent} {mantissa}'