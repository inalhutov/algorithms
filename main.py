# глава  1 бинарный поиск

def binary_search(ls, item):
    low = 0
    high = len(ls) - 1

    while low <= high:
        mid = int((low + high) / 2)
        guess = ls[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 3))
print(binary_search(my_list, -1))

