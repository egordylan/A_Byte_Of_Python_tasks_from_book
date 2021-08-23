"""Проверка на палиндромы.

Проверка слова или фразы на то, что они являются или не являются
палиндромом.
Задача взята из книги 'A byte of Python', стр 122. """

def reverse(text):
    return text[::-1]
# А роза? упала на лапу Азора!
# арозаупаланалапуазора

def is_palindrome(text):
    return text == reverse(text)

something = input('Введите текст: ')

#  Сначала ищет все символы, которые не являются буквами и удаляет их.
#  С помощью join соединяет список в строку и приводит к нижнему регистру lower()
new_string = "".join(c for c in something if c.isalpha()).lower()

if is_palindrome(new_string):
    print('Да, это палиндром.')
else:
    print('Нет, это не палиндром.')
