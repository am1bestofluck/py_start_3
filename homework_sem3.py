"""
scenario - увязывает все 5 задач в последовательность  

t1 - находит сумму значений нечётных позиций в списке.  

    sum_positions_by_index - ядро t1.  

t2 - перемножает края списка, двигаясь к центру.  
    eedge_to_center_action - ядро t2.

t3 - вычитает предельные отклонения значений списка от целых чисел.  

t4 - преобразовывает десятичное число в двоичное.  

t5 - выводит числа Фибоначчи с базой от -N до N.  
    
    winged_fib - ядро t5.

сопроводительные:
    fib - считаем одно число Фибоначи
"""

__all__ = ['fib', 'input_int']
__version__ = "#3"
__author__ = "anton6733@gmail.com"

# standart imports
import math
import random
import sys
from copy import deepcopy
from typing import Dict, List

# local imports
from homework_sem1 import Break
from binary_subfunctions import normalize, exract_fraction

def input_int(invite: str = '') -> int:
    """Ловим инт пока получается %).  """
    while not isinstance(invite, int):
        try:
            invite = int(input(invite))
        except ValueError:
            pass
        except EOFError:
            pass
        except KeyboardInterrupt:
            print()
    return invite


# def exract_fraction(number: float) -> float:
#         """возвращает дробную часть числа"""
#         positive = number > 0
#         return (number - math.floor(number) if positive
#                 else number - math.ceil(number))


def fib(seed: int) -> int:
    """считаем число ряда Фибоначи seed- порядка.  """
    a, b = 0, 1
    seed_modified = 0
    while seed > seed_modified:
        seed_modified += 1
        a, b = b, a+b  # такое решение прямо на сайте python :( :D
    return a


def sum_positions_by_index(
    list_: List[int | float],
    sum_odd: bool = True, round_to: int = 2
) -> int | float:
    """Возвращаем сумму значений в зависимости от чётности индексов.  

    list_ список к суммированию.  

    sum_odd - если True - прибавляем значения на нечётных индексах; 
    иначе - на нечётных.  
    """
    """round_to - округление для float"""
    output = 0
    for i in range(len(list_)):
        if i % 2 == sum_odd:
            output += list_[i]
    return round(output, round_to) if isinstance(output, float) else output


def winged_fib(limit: int) -> Dict[int, int]:
    """Выводим числа Фибоначи с ключами от -limit до limit включительно

    limit - край последовательности
    """
    """Для этого Мы сначала проходимся по положительному крылу,
    потом отзеркаливаем негативное крыло, переворачивая значение для
    нечётных индексов
    
    tmp - несортированный вывод
    keys_sorted - упорядочиваем ключи.
    output - ответ в зачёт
    """
    tmp, output = {}, {}
    for iteration_key in range(0, abs(limit) + 1, 1):
        tmp[iteration_key] = fib(seed=iteration_key)
    for key in range(-1, - (abs(limit) + 1), -1):
        tmp[key] = tmp[-key] if key % 2 else - tmp[-key]
    keys_sorted = sorted(list(tmp.keys()))
    for out in keys_sorted:
        output[out] = tmp[out]
    return output


def edge_to_center_action(
        list_i: List[int | float], round_to: int = 2) -> List[int | float]:
    """Движется по индексам с краёв входящего списка к центру, добавляя 
    в выводной список произведения крайних элементов под этими индексами.

    list_i - входящий список

    round_to - если float: округляем до этого знака 
    """

    """
    round_to - если float - округляем до этого разряда

    mult - вынес действие с краями отдельно "на случай расширения" 
    """

    def mult(a: int | float, b: int | float, round_to: int = round_to):
        """возвращает  a * b"""
        return a*b if isinstance(a*b, int) else round(a*b, round_to)

    print(edge_to_center_action.__doc__)
    output = []
    i, j = 0, len(list_i)-1
    while i < j:
        output.append(mult(a=list_i[i], b=list_i[j]))
        i += 1
        j -= 1
    else:
        if i == j:
            output.append(mult(a=list_i[i], b=list_i[j]))
    return output


def add_floating_point(base: int = 0, round_to: int = 3) -> float:
    """рандомим дробную часть числа.

    base - прибавляем дробь к этому

    round_to - округляем до этого знака
    """
    return base + round(random.random(), 3)


def t3(list_i: List[float] = [], round_to: int = 3) -> float:
    """Возвращает разность предельных дробных частей списка.  

    list_i - входящий список

    round_to - вывод округляем до этого знака
    """

    if not list_i:
        list_i = list(map(
            add_floating_point, random.choices(range(1, 11), k=10)))
        print(list_i)
    max_ = exract_fraction(list_i[0])
    min_ = exract_fraction(list_i[0])
    for i in list_i[1:]:
        max_ = max(max_, exract_fraction(i))
        min_ = min(min_, exract_fraction(i))
    print(f'{min_=}', f'{max_=}')
    return round(max_ - min_, round_to)


def t4(base: int | float,float_precision: int = 3) -> str:
    # кажется алгоритм конвертации зависит от архитектуры и
    # хотелок инженеров ._.
    """переводим десятичное число в двоичное.

    Вызывает TypeError если тип base соответствует аннотации

    Вызывает NotImplementedError для чисел размером больше 32 бит...

    float_precision - точность округления.  

    base - предмет конвертации  
    """
    """{
        parse_int
        positive_float,
        negative_float
    } - сопроводительные функции в зависимости от типа base
    """

    print(base)
    if not isinstance(base, t4.__annotations__['base']):
        raise TypeError((
            f'type(base) in ({t4.__annotations__["base"]})'
            + f', not {type(base).__name__}!')
        )

    def parse_int(base: int) -> str:
        # вообще в интернете минимум два подхода по переводу 
        # отрицательных интов в двоичную систему.
        # вот https://www.instructables.com/Convert-Negative-Numbers-to-Binary/
        # или вот https://cs.calvin.edu/activities/books/rit/chapter5/negative.htm#:~:text=The%20simplest%20is%20to%20simply,would%20be%20written%20as%2011100.
        # по итогу решил наследовать практику bin()
        output = ''
        base_i = abs(base)
        while base_i > 0:
            output = f'{str(base_i % 2)}' + output
            base_i //= 2
        prefix = '0b' if base > 0 else '-0b'
        return f'{prefix}{output}'

    def positive_float(base: float,precision = float_precision) -> str:
        """переводим положительное дробное число в двоичную систему"""
        """дробим число на целую и дробную части. 
        Целую часть считаем как позитив инт.  
        Дробную часть рекурсивно умножаем на два и "целое" от результата
         строково прибавляем к части после запятой, k раз
         k- точность, кол-во знаков после запятой"""
        
        
        base_fractured = [int(base),exract_fraction(base)]
        whole_part = parse_int(base_fractured[0])
        fractured_part = '.'
        base_fractured[1] = round(base_fractured[1],precision)
        tmp = base_fractured[1]
        for i in range( precision, 0, -1):
            tmp = round(tmp*2,precision)
            fractured_part += str (int(tmp))
            tmp = round(tmp - int(tmp),precision)
        output = f'{whole_part}{fractured_part}'
        return output

    def negative_float(base: float) -> str:
        """
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
        # mantissa - само число
        # например: 
        # число 0.41 это (s) 0 (e) -1 (m) 4.1 
        
        # Штош. Сначала "нормализуем мантиссу". Т.е. двигаем разряд пока
        # целая часть не поместится в 10**1.

        sign = '1' if base < 0 else '0'
        exponent_decimal,mantissa_decimal = normalize(base)
        if exponent_decimal > 128:
            raise NotImplementedError('реализовано только для 32-битных' 
            + 'чисел') 
        exponent = parse_int(exponent_decimal + 127)[2:].ljust(8,'0')
        mantissa = ''

        return f'{sign} {exponent} {mantissa}'


    if isinstance(base, int):
        return parse_int(base) 
    return positive_float(base)# if base > 0 else negative_float(base)
    # Должно работать с отрицательными флотами...


def main():
    """
    Запускает все задания, если через консоль не указано иное.  
    аргументы: t1 t2 t3 t4 t5 scenario
    """
    """
    executed- список выполненных команд, вводим чтобы не запускать 
    функции по два раза по два раза
    accepted_args - если в аргументах не ЭТО - выходим со справкой :))
    """
    accepted_args = {'t1', 't2', 't3', 't4', 't5', 'scenario'}

    def t1(list_: List[int | float] = []) -> int | float:  # сумма по признаку
        # print(float_summarize_signs.__doc__)
        # print(float_summarize_signs(validate_input_float(short_note="float!")))
        print(sum_positions_by_index.__doc__)
        if not list_:
            list_ = random.choices(range(1, 11), k=10)
            print(list_)
        return sum_positions_by_index(list_=list_, sum_odd=True)

    def t2(list_: List[int | float] = []) -> None:
        if not list_:
            list_ = random.choices(range(1, 11), k=3)
            print(list_)
        return edge_to_center_action(list_i=list_)

    # вычитает предельные дробные части элеметов списка
    # def t3(list_: List[int | float] = []) -> float:
    #     if not list_:
    #         list_ = random.choices(range(1, 11), k=3)
    #         print(list_)
    #     return None

    # def t4() -> None:  # преобразовывает десятичное число в двоичное.
    #     Break()
    #     return None

    def t5() -> List[int]:  # выводит числа Фибоначчи с базой от -N до N.
        print(winged_fib.__doc__)
        tmp = winged_fib(
            input_int(invite="предел индекса для fib")
        )
        output = list(tmp.values())
        return output

    def scenario():
        """
        Список задаём выводом пятой задачи
        Со @Списком решаем первую и вторую задачу
        Поэлементно создаём Список2 прибавляя к значениям @Списка дробь
        Решаем третью задачу со @Списком2
        Решаем четвёртую задачу на @Списке2. # Проверить на интах.
        """
        print(scenario.__doc__)
        fibs = t5()
        print(fibs)
        Break()
        print(fibs)
        print(t1(fibs))
        Break()
        print(fibs)
        print(t2(fibs))
        Break()
        floats = list(map(add_floating_point,deepcopy(fibs)))
        print(floats)
        print(t3(floats))
        Break()
        some_int = random.choice(fibs)
        some_float = random.choice(floats)
        print(f'binary of {str(some_int)} = {t4(some_int)}')
        print(f'binary of {str(some_float)} = {t4(some_float)}')

         

    if len(sys.argv) > 1:
        if 'scenario' in sys.argv[1:]:
            scenario()
            sys.exit()
        if not set(sys.argv[1:]).issubset(accepted_args):
            print(__doc__)
            sys.exit()
        executed = []
        for arg in sys.argv[1:]:
            if arg in executed:
                continue
            else:
                executed.append(arg)
                match arg:
                    case 't1':
                        print(t1())
                    case 't2':
                        print(t2())
                    case 't3':
                        print(t3())
                    case 't4':
                        print(t4(15.000))
                        print(t4(15.470))
                        print(t4(-15.000))
                        print(t4(1.47))
                        print(t4(1.470))
                        print(t4(-1.0))
                    case 't5':
                        print(t5())
                        Break()

    else:
        scenario()


if __name__ == "__main__":
    main()
