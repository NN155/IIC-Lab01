'''Створіть програму для перевірки, чи є слово паліндромом (читається однаково зліва направо і справа наліво).'''
word = input("Введіть слово: ")
print(f'{word} - {("не паліндром", "паліндром")[word.lower() == word.lower()[::-1]]}')
