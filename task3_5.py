# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

n = int(input('Введите целое число: '))


def fibonacci(a):

    if a == 1 or a == 2:
        return 1
    else:
        return fibonacci(a-1) + fibonacci(a-2)


def nega_fibonacci(n):
    list_negafibonacci = [0]
    for i in range(1, n + 1):
        list_negafibonacci.append(fibonacci(i))
        list_negafibonacci.insert(0, (fibonacci(i) * (-1) ** (i + 1)))
    return list_negafibonacci


# 1 вариант


print(f"Список чисел (нега)Фибоначчи для {n}: {nega_fibonacci(n)}")

# 2 вариант без в 1 метод
# f_list = [0]
# for i in range(1, n+1):
#     f_list.append(fibonacci(i))
#     f_list.insert(0, fibonacci(i)*((-1)**(i+1)))

# print(f_list)
