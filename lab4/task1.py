def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    sr = len(arr) // 2
    left_side = merge_sort(arr[:sr])
    right_side = merge_sort(arr[sr:])
    return merge_list(left_side, right_side)
def merge_list(a, b):
    c = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    return c + a[i:] + b[j:]

with open("m2.txt", 'r', encoding='utf-8') as file:
    a = file.readline().split()
    cnt_rows = int(a[0])
    cnt_cols = int(a[1])

    array = []
    for i in range(cnt_rows):
        line = file.readline().split()
        for k in line:
            array.append(int(k))
    print(f"Количество элементов: {cnt_rows * cnt_cols}")
    print(f"Одномерный массив: {array}")
    print(f"Отсортированный массив: {merge_sort(array)}")

