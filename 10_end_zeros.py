'''
End Zeros

Попробуйте выяснить какое количество нулей содержит данное число в конце.

Входные данные: Положительное целое число (int).

Выходные данные: Целое число (int).

Пример:

end_zeros(0) == 1
end_zeros(1) == 0
end_zeros(10) == 1
end_zeros(101) == 0
'''


# Моё решение:

def end_zeros(num: int):
    if str(num)[-1] != '0':
        return 0
    elif len(str(num)) > 1:
        i = -1
        while str(num)[i] == '0':
            i -= 1
        return len(str(num)[i+1:])
    else:
        return 1


if __name__ == "__main__":
    print("Example:")
    print(end_zeros(0))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert end_zeros(0) == 1
    assert end_zeros(1) == 0
    assert end_zeros(10) == 1
    assert end_zeros(101) == 0
    assert end_zeros(245) == 0
    assert end_zeros(100100) == 2
    print("The task is complete")


'''
Решение 1

def end_zeros(num: int) -> int:
        return len(s := str(num)) - len(s.rstrip('0'))

Решение 2

def end_zeros(num: int) -> int:
    for x in str(num)[::-1]:
        if  x != '0':
            return str(num)[::-1].find(x)
    return len(str(num))

Решение 3

def end_zeros(num: int) -> int:
    # your code here
    if num == 0:
        return 1

    zeros = 0
    while num % 10 == 0:
        num //= 10
        zeros += 1
    return zeros
'''