'''
Between Markers (simplified)

Вам дана строка и два маркера (начальный и конечный). Вам необходимо найти текст, заключенный между двумя этими маркерами. Но есть несколько важных условий.

Это упрощенная версия миссии Between Markers .

Начальный и конечный маркеры всегда разные.
Начальный и конечный маркеры всегда размером в один символ.
Начальный и конечный маркеры всегда есть в строке и идут один за другим.
Input: Три аргумента. Все строки. Второй и третий аргументы это начальный и конечный маркеры.

Output: Строка.

Пример:

between_markers('What is >apple<', '>', '<') == 'apple'
1
Как это используется: Может использоваться для парсинга небольшой верстки.

Предусловия: Не может быть более одного маркера одного типа.
'''


def between_markers(text: str, begin: str, end: str) -> str:
    begin_marker = text.find(begin)
    end_marker = text.find(end)
    text_between_markers = text[begin_marker+1:end_marker]
    return text_between_markers


if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))

    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple"
    assert between_markers('What is [apple]', '[', ']') == "apple"
    assert between_markers('What is ><', '>', '<') == ""
    assert between_markers('>apple<', '>', '<') == "apple"
    print('Wow, you are doing pretty good. Time to check it!')


'''
Альтернативные решения:

№ 1
def between_markers(text: str, begin: str, end: str) -> str:
    return text[text.index(begin)+1:text.index(end)]
    
№ 2
def between_markers(text, begin, end):
    i = text.find(begin) + 1
    j = text.find(end, i)
    return text[i:j]
'''