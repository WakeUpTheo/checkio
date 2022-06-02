'''
Correct Sentence

На вход Вашей функции будет передано одно предложение. Необходимо вернуть его исправленную копию так, чтобы оно всегда начиналось с большой буквы и заканчивалось точкой.

Обратите внимание на то, что не все исправления необходимы. Если предложение уже заканчивается на точку, то добавлять еще одну не нужно, это будет ошибкой

Входные аргументы: Строка (A string).

Выходные аргументы: Строка (A string).

Пример:

correct_sentence("greetings, friends") == "Greetings, friends."
correct_sentence("Greetings, friends") == "Greetings, friends."
correct_sentence("Greetings, friends.") == "Greetings, friends."

Предусловия: В начале и конце нет пробелов, текст состоит только из пробелов, a-z A-Z , и .
'''


def correct_sentence(text: str):
    if text[0].islower() == True and text[len(text)-1] != '.':
        return text[0].capitalize() + text[1:] + '.'
    elif text[0].islower() == True and text[len(text)-1] == '.':
        return text[0].capitalize() + text[1:]
    elif text[0].isupper() == True and text[len(text)-1] != '.':
        return text + '.'
    else:
        return text



if __name__ == '__main__':
    print("Example:")
    print(correct_sentence("greetings, friends"))


    # These "asserts" are used for self-checking and not for an auto-testing
    assert correct_sentence("greetings, friends") == "Greetings, friends."
    assert correct_sentence("Greetings, friends") == "Greetings, friends."
    assert correct_sentence("Greetings, friends.") == "Greetings, friends."
    assert correct_sentence("hi") == "Hi."
    assert correct_sentence("welcome to New York") == "Welcome to New York."

    print("Coding complete? Click 'Check' to earn cool rewards!")

'''
Альтернативные решения:

№ 1
def correct_sentence(text: str) -> str:   
    return text[0].upper() + text[1:] + ("." if text[-1] != "." else "")

№ 2
correct_sentence = lambda t: t[0].upper() + t[1:] + '.'*(t[-1] != '.')
'''