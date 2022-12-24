




__version__ = "#3"
__author__ = "anton6733@gmail.com"
import math
import random
from typing import List

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
    # precision = normalize(number)[1]
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
        
        output = ''
        base_i = abs(base)
        while base_i > 0:
            output = f'{str(base_i % 2)}' + output
            base_i //= 2
        prefix = '0b' if base > 0 else '-0b'
        return f'{prefix}{output}'
