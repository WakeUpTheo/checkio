'''
First Word (simplified)

You are given a string and you have to find its first word.

This is a simplified version of the First Word mission, which can be solved later.

The input string consists of only English letters and spaces.
There aren’t any spaces at the beginning and the end of the string.
Input: A string.

Output: A string.
'''


# 1 вариант:

# def first_word(text: str) -> str:
#    return text.split()[0]

# 2 вариант:

def first_word(text: str) -> str:
    i = 0
    while i < len(text) and text[i] != ' ':
        i += 1
    return text[:i]

if __name__ == "__main__":
    print("Example:")
    print(first_word("Hello world"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert first_word("Hello world") == "Hello"
    assert first_word("a word") == "a"
    assert first_word("hi") == "hi"
    print("The task complete")