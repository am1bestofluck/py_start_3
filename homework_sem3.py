"""
scenario - увязывает все 5 задач в последовательность

t1 - находит сумму значений нечётных позиций в списке.  

t2 - перемножает края списка, двигаясь к центру.  

t3 - вычитает предельные отклонения значений списка от целых чисел.  

t4 - преобразовывает десятичное число в двоичное.  

t5 - выводит числа Фибоначчи с базой от -N до N.  
"""

__version__ = "#3"
__author__ = "anton6733@gmail.com"

# standart imports
import random
import sys
from copy import deepcopy

# local imports
from homework_sem1 import Break, validate_input


def scenario():
    """
    Список задаём выводом пятой задачи # кеширование???
    Со @Списком решаем первую и вторую задачу
    @ Поэлементно создаём Список2 прибавляя к значениям @Списка дробь
    Решаем третью задачу со @Списком2
    Решаем четвёртую задачу на @Списке2. Проверить на интах.
    """
    print(scenario.__doc__)


def main():
    """
    Запускает все задания, если через консоль не указано иное.  
    аргументы: t1 t2 t3 t4 t5 scenario
    """
    """
    executed- список выполненных команд, вводим чтобы не запускать функции
    по два раза по два раза
    accepted_args - если в аргументах не ЭТО - выходим со справкой :))
    """
    accepted_args = {'t1', 't2', 't3', 't4', 't5', 'scenario'}

    def t1() -> None:  # находит сумму значений нечётных позиций в списке
        # print(float_summarize_signs.__doc__)
        # print(float_summarize_signs(validate_input_float(short_note="float!")))
        Break()
        return None

    def t2() -> None:  # перемножает края списка, двигаясь к центру.
        Break()
        return None

    def t3() -> None:  # вычитает предельные дробные части элеметов списка
        Break()
        return None

    def t4() -> None:  # преобразовывает десятичное число в двоичное.
        Break()
        return None

    def t5() -> None:  # выводит числа Фибоначчи с базой от -N до N.
        Break()
        return None

    if len(sys.argv) > 1:
        if 'scenario' in sys.argv[1:]:
            scenario()
            sys.exit()
        if not set(sys.argv[1:]).issubset(accepted_args):
            print( __doc__)
            sys.exit()
        executed = []
        for arg in sys.argv[1:]:
            if arg in executed:
                continue
            else:
                executed.append(arg)
                match arg:
                    case 't1':
                        t1()
                    case 't2':
                        t2()
                    case 't3':
                        t3()
                    case 't4':
                        t4()
                    case 't5':
                        t5()
                    case _:
                        print(__doc__)
                        sys.exit()

    else:
        scenario()


if __name__ == "__main__":
    main()
