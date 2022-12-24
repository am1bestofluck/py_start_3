"""
scenario - увязывает все 5 задач в последовательность

t1 - находит сумму значений нечётных позиций в списке.

t2 - перемножает края списка, двигаясь к центру.

t3 - вычитает предельные отклонения значений списка от целых чисел.

t4 - преобразовывает десятичное число в двоичное.

t5 - выводит числа Фибоначчи с базой от -N до N.
"""

__all__ = ['fib', 'input_int']
__version__ = "#3"
__author__ = "anton6733@gmail.com"

# standart imports
import random
import sys
from copy import deepcopy
from typing import Dict, List

# local imports
from homework_sem1 import Break
from binary_subfunctions import (exract_fraction, add_floating_point,
     parse_int, parse_float)
from array_subfunctions import (edge_to_center_action, fib,
    sum_positions_by_index, winged_fib)


def input_int(invite: str = '') -> int:
    """Ловим инт пока получается %).

    invite - приглашение ко вводу
    """
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


def t1(list_: List[int | float] = []) -> int | float:
    """находит сумму значений нечётных позиций в списке

    list_- обрабатываем этот список, а если его нет- рандомим новый.
    """

    print(sum_positions_by_index.__doc__)
    if not list_:
        list_ = random.choices(range(1, 11), k=10)
        print(list_)
    return sum_positions_by_index(list_=list_, sum_odd=True)


def t2(list_: List[int | float] = []) -> None:
    """двигаемся от краев к центру, перемножая позиции 'под курсором'

    list_- обрабатываем этот список, а если его нет- рандомим новый.
    """

    print(edge_to_center_action.__doc__)
    if not list_:
        list_ = random.choices(range(1, 11), k=3)
        print(list_)
    return edge_to_center_action(list_i=list_)


def t3(list_i: List[float] = [], round_to: int = 3) -> float:
    """Возвращает разность предельных дробных частей списка.

    list_i - входящий список

    round_to - вывод округляем до этого знака
    """
    if not list_i:
        list_i = list(map(
            add_floating_point, random.choices(range(1, 11), k=10)))
        print(list_i)

    list_i = list(map(lambda x: round(x, round_to), list_i))
    max_ = exract_fraction(list_i[0])
    min_ = exract_fraction(list_i[0])
    for i in list_i[1:]:
        max_ = max(max_, exract_fraction(i))
        min_ = min(min_, exract_fraction(i))
    print(f'{min_=}', f'{max_=}')
    return round(max_ - min_, round_to)


def t4(base: int | float, float_precision: int = 3) -> str:
    """переводим десятичное число в двоичное.

    Вызывает TypeError если тип base соответствует аннотации

    Вызывает NotImplementedError для чисел размером больше 32 бит...

    float_precision - точность округления.

    base - предмет конвертации
    """
    # кажется алгоритм конвертации зависит от архитектуры и
    # хотелок инженеров ._.
    """{
        parse_int
        positive_float,
        negative_float
    } - сопроводительные функции в зависимости от типа base
    """

    if not isinstance(base, t4.__annotations__['base']):
        raise TypeError((
            f'type(base) in ({t4.__annotations__["base"]})'
            + f', not {type(base).__name__}!')
        )


    

    return (parse_int(base) if isinstance(base, int)
            else parse_float(base))


def t5() -> List[int]:
    """выводит числа Фибоначчи с базой от -N до N."""

    print(winged_fib.__doc__)
    tmp = winged_fib(
        input_int(invite="предел индекса для fib")
    )
    output = list(tmp.values())
    return output


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

    def scenario():
        """
        Список задаём выводом пятой задачи
        Со @Списком решаем первую и вторую задачу
        Поэлементно создаём Список2 прибавляя к значениям @Списка дробь
        Решаем третью задачу со @Списком2
        Решаем четвёртую задачу на @Списке2. Для флотов тоже.
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
        floats = list(map(add_floating_point, deepcopy(fibs)))
        print(floats)
        print(t3(floats))
        Break()
        some_int = random.choice(fibs)
        some_float = random.choice(floats)
        print(f'binary of {str(some_int)} = {t4(some_int)}')
        print(f'binary of {str(round(some_float,4))} = {t4(some_float)}')

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
                        print(t4(15))
                        print(t4(-15))
                        print(t4(15.47))
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
