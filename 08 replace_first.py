'''
Replace First

В данном списке первый элемент должен стать последним. Пустой список или список из одного элемента не должен измениться.

Входные данные: Список.

Выходные данные: Набор элементов.

Пример:

replace_first([1, 2, 3, 4]) == [2, 3, 4, 1]
replace_first([1]) == [1]
'''


def replace_first(items: list):
    if len(items) == 1 or len(items) == 0:
        return items
    else:
        items.insert(len(items), items.pop(0))
        return items


if __name__ == "__main__":
    print("Example:")
    print(list(replace_first([1, 2, 3, 4])))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(replace_first([1, 2, 3, 4])) == [2, 3, 4, 1]
    assert list(replace_first([1])) == [1]
    assert list(replace_first([])) == []
    print("The task is complete")

'''
Альтернативное решение

from typing import Iterable
import numpy as np

def replace_first(items: list) -> Iterable:
    # your code here
    return np.roll(items,-1)
'''