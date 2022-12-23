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
import random
import sys
from copy import deepcopy
from typing import Dict, List

# local imports
from homework_sem1 import Break


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
    sum_odd: bool = True
) -> int | float:
    """Возвращаем сумму значений в зависимости от чётности индексов.  

    list_ список к суммированию.  

    sum_odd - если True - прибавляем значения на нечётных индексах; 
    иначе - на нечётных.  
    """
    """round_to - округление для float"""
    output, round_to = 0, 2
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
    
    tmp - расчёт положительного крыла
    output - ответ в зачёт
    keys_sorted - упорядочиваем ключи.
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
    в выводной список суммы крайних элементов под этими индексами.

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
            list_ = random.choices(range(1,11),k=3)
            print(list_)
        return edge_to_center_action(list_i=list_)

    def t3() -> None:  # вычитает предельные дробные части элеметов списка
        Break()
        return None

    def t4() -> None:  # преобразовывает десятичное число в двоичное.
        Break()
        return None

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
                        t3()
                    case 't4':
                        t4()
                    case 't5':
                        print(t5())
                        Break()

    else:
        scenario()


if __name__ == "__main__":
    main()
