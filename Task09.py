'''Напишіть програму для перетворення градусів Цельсія в градуси Фаренгейта і навпаки.'''
number = float(input("Введіть число: "))
print(f'{number} градусів Цельсія дорівнює {round((number * (9 / 5) + 32), 2)} градусів Фаренгейта')
print(f'{number} градусів Фаренгейта дорівнює {round(((number - 32) * (5 / 9)), 2)} градусів Цельсія')
