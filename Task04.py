'''Реалізуйте програму, яка перевіряє, чи є число парним чи непарним.'''
print(("Не парне", "Парне")[int(input("Введіть число: ")) % 2 == 0])