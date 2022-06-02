'''
Best Stock

Вам даны текущие цены на акции. Вам необходимо выяснить за какие акции дают большую цену.

Input: Словарь (dict), в котором ключи - это рыночный код, а значение - это цена за акцию(float)

Output: Строка, рыночный код

Example:

best_stock({"CAC": 10.0, "ATX": 390.2, "WIG": 1.2}) == "ATX"
best_stock({"CAC": 91.1, "ATX": 1.01, "TASI": 120.9}) == "TASI"
'''


def best_stock(data: dict) -> str:
    max_price = max(data.values())
    new_data = {}
    for key, value in data.items():
        new_data[value] = key
    return new_data.get(max_price)


if __name__ == '__main__':
    print("Example:")
    print(best_stock({"CAC": 10.0, "ATX": 390.2, "WIG": 1.2}))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert best_stock({"CAC": 10.0, "ATX": 390.2, "WIG": 1.2}) == "ATX"
    assert best_stock({"CAC": 91.1, "ATX": 1.01, "TASI": 120.9}) == "TASI"
    print("Coding complete? Click 'Check' to earn cool rewards!")

'''
Альтернативные решения:

№ 1
def best_stock(data):
    return max(data, key=data.__getitem__)

№ 2
best_stock = lambda d: next(x for x in d if d[x] == max(d.values()))

№ 3
def best_stock(data):
    return max(data, key=data.get)
'''
