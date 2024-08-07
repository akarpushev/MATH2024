def bubble_sort(arr):
    n = len(arr)
    # Проходим по всем элементам массива
    for i in range(n):
        # Последние i элементов уже отсортированы
        for j in range(0, n - i - 1):
            # Если текущий элемент больше следующего
            if arr[j] > arr[j + 1]:
                # Меняем их местами
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Пример использования
array = [64, 34, 25, 12, 22, 11, 90, -1]
sorted_array = bubble_sort(array)
print("Отсортированный массив:", sorted_array)
