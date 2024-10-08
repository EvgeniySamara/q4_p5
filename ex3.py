# Задача 3. Генератор последовательности чисел Фибоначчи
# Напишите генераторную функцию fibonacci(n), которая принимает на вход
# одно целое число n и возвращает последовательность первых n чисел
# Фибоначчи. Числа Фибоначчи — это последовательность, в которой каждое
# число является суммой двух предыдущих, начиная с 0 и 1.
# Подсказка № 1
# В последовательности Фибоначчи каждое число является суммой двух предыдущих,
# начиная с 1 и 1. Начальные числа задаются как 1 и 1.

n = 15
def fibonacci(n):
    a = 0
    b = 1
    for i in range(n):
        if a>0:
            yield a
        a,b = a+b,a

for fib in fibonacci(n):
    print(fib, end=' ')