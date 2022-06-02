'''
Index Power

Дан массив с положительными числами и число N.
Вы должны найти N-ую степень элемента в массиве с индексом N.
Если N за границами массива, тогда вернуть -1.
Не забывайте, что первый элемент имеет индекс 0.

Давайте посмотрим на несколько примеров:
- массив = [1, 2, 3, 4] и N = 2, тогда результат 3 2 == 9;
- массив = [1, 2, 3] и N = 3, но N за границами массива, так что результат -1.

Входные значения: Два агумента. Массив как список целых и число как целое.

Выходные значения: Целое число.

Пример:

index_power([1, 2, 3, 4], 2) == 9
index_power([1, 3, 10, 100], 3) == 1000000
index_power([0, 1], 0) == 1
index_power([1, 2], 3) == -1

Как это используется:
Эта миссия учит вас как использовать основы массивов и индексов в объединении с простой математикой.

Предусловие: 0 < len(array) ≤ 10
0 ≤ N
all(0 ≤ x ≤ 100 for x in array)
'''


def index_power(array: list, n: int) -> int:
    if len(array) <= n:
        return -1
    else:
        return array[n]**n

if __name__ == '__main__':
    print('Example:')
    print(index_power([1, 2, 3, 4], 2))
    
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert index_power([1, 2, 3, 4], 2) == 9, "Square"
    assert index_power([1, 3, 10, 100], 3) == 1000000, "Cube"
    assert index_power([0, 1], 0) == 1, "Zero power"
    assert index_power([1, 2], 3) == -1, "IndexError"
    print("The task is complete!")


'''
Альтернативные решения:

№ 1
def index_power(array, n):
    return array[n]**n if len(array) > n else -1
    
№ 2
def index_power(array, n):
    try: return array[n] ** n
    except IndexError: return -1
'''