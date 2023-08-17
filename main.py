def main():
    n = int(input("Введите размер массива: "))
    arr = []

    for i in range(n):
        element = float(input(f"Введите элемент {i+1}: "))
        arr.append(element)

    negative_sum = 0
    for num in arr:
        if num < 0:
            negative_sum += num
    max_index = arr.index(max(arr))
    min_index = arr.index(min(arr))
    start_index = min(max_index, min_index) + 1
    end_index = max(max_index, min_index)

    product_between = 1
    for i in range(start_index, end_index):
        product_between *= arr[i]

    arr.sort()  # Сортировка элементов массива по возрастанию

    print("Сумма отрицательных элементов:", negative_sum)
    print("Произведение элементов между максимальным и минимальным:", product_between)
    print("Массив после сортировки:", arr)

if __name__ == "__main__":
    main()
