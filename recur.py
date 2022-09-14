# Даны два целых числа A и В (каждое в отдельной строке). Выведите все числа от A до B включительно, в порядке возрастания,
# если A < B, или в порядке убывания в противном случае.
def num1(x, y):
    if x < y:
        num1(x + 1, y)
        print(x)
    elif x > y:
        num1(x - 1, y)
        print(x)
    else:
        print(x)


num1(1, 3)


# Дано натуральное число N. Вычислите сумму его цифр.

def rec_sum(n, s=0):
    x, y = divmod(n, 10)
    s += y
    if x == 0:
        return print(s)
    else:
        rec_sum(x, s)


rec_sum(int(input()))
