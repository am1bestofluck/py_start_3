"""
edge_to_center_action - движемся к центру массива с краёв, перемножая

fib - считаем числа фибоначи

sum_positions_by_index - Возвращаем сумму значений в зависимости от
чётности индексов.

winged_fib - Выводим числа Фибоначи по обе стороны нуля
"""


from typing import List, Dict

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
    for iteration_key in range(0, abs(limit), 1):
        tmp[iteration_key] = fib(seed=iteration_key)
    for key in range(-1, - (abs(limit)), -1):
        tmp[key] = tmp[-key] if key % 2 else - tmp[-key]
    keys_sorted = sorted(list(tmp.keys()))
    for out in keys_sorted:
        output[out] = tmp[out]
    return output