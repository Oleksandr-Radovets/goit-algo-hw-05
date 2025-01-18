def binary_search(sorted_array, target):
    """
    Виконує двійковий пошук у відсортованому масиві з дробовими числами.

    Параметри:
    sorted_array (list): Відсортований масив.
    target (float): Число, яке шукаємо.

    Повертає:
    tuple: (кількість ітерацій, верхня межа).
    """
    left, right = 0, len(sorted_array) - 1
    iterations = 0
    upper_bound = None

    while left <= right:
        iterations += 1
        mid = (left + right) // 2

        if sorted_array[mid] == target:
            return (iterations, sorted_array[mid])
        elif sorted_array[mid] < target:
            left = mid + 1
        else:
            upper_bound = sorted_array[mid]
            right = mid - 1

    # Якщо не знайдено точний елемент, повертаємо кількість ітерацій та верхню межу.
    return (iterations, upper_bound)

# Приклад використання:
sorted_array = [1.1, 2.2, 3.3, 4.4, 5.5, 6.6]
target = 3.5
result = binary_search(sorted_array, target)
print(result)  # Виведе: (3, 4.4)