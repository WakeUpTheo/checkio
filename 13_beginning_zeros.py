'''
Beginning Zeros

You have a string that consist only of digits.
You need to find how many zero digits ("0") are at the beginning of the given string.

Input: A string, that consist of digits.

Output: An Int.

Example:

beginning_zeros('100') == 0
beginning_zeros('001') == 2
beginning_zeros('100100') == 0
beginning_zeros('001001') == 2
beginning_zeros('012345679') == 1
beginning_zeros('0000') == 4

Precondition: 0-9
'''


def beginning_zeros(number: str) -> int:
    if number[0] != '0':
        return 0
    else:
        i = 0
        while i < len(number) and number[i] == '0':
            i += 1
    return len(number[:i])

print(beginning_zeros('0000'))

'''
if __name__ == '__main__':
    print("Example:")
    print(beginning_zeros('100'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert beginning_zeros('100') == 0
    assert beginning_zeros('001') == 2
    assert beginning_zeros('100100') == 0
    assert beginning_zeros('001001') == 2
    assert beginning_zeros('012345679') == 1
    assert beginning_zeros('0000') == 4
    print("The task is complete!")
'''

'''
Альтернативное решение:

def beginning_zeros(number: str) -> int:
    return len(number) - len(number.lstrip('0'))
'''