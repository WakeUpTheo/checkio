'''
Fizz Buzz

"Fizz buzz" это игра со словами, с помощью которой мы будем учить наших роботов делению. Давайте обучим компьютер.

Вы должны написать функцию, которая принимает положительное целое число и возвращает:
"Fizz Buzz" , если число делится на 3 и 5;
"Fizz" , если число делится на 3;
"Buzz" , если число делится на 5;
Число , как строку для остальных случаев.
Входные данные: Число, как целочисленное (int).

Выходные данные: Ответ, как строка (str).

Примеры:

checkio(15) == "Fizz Buzz"
checkio(6) == "Fizz"
checkio(5) == "Buzz"
checkio(7) == "7"
'''


def checkio(number: int) -> str:
    if number % 3 == 0 and number % 5 == 0:
        return 'Fizz Buzz'
    elif number % 3 == 0:
        return 'Fizz'
    elif number % 5 == 0:
        return 'Buzz'
    else:
        return str(number)


if __name__ == '__main__':
    print('Example:')
    print(checkio(15))

    assert checkio(15) == "Fizz Buzz", "15 is divisible by 3 and 5"
    assert checkio(6) == "Fizz", "6 is divisible by 3"
    assert checkio(5) == "Buzz", "5 is divisible by 5"
    assert checkio(7) == "7", "7 is not divisible by 3 or 5"
    print("The task is complete")

'''
Альтернативное решение
def checkio(number):
    if number % 15 == 0:
        return 'Fizz Buzz'
    if number % 5 == 0:
        return 'Buzz'
    if number % 3 == 0:
        return 'Fizz'
    return str(number)
'''