def merger_method(arr):
    if len(arr) <= 1:
        return arr
    sr = len(arr) // 2
    left_side = merger_method(arr[:sr])
    right_side = merger_method(arr[sr:])

    

with open("text_for_lab4.txt", 'r', encoding='utf-8') as file:
    a = file.readline().split()
    cnt_rows = int(a[0])
    cnt_cols = int(a[1])

    flat_list = []
    for i in range(cnt_rows):
        line = file.readline().split()
        for k in line:
            flat_list.append(int(k))
    print(f"Количество элементов: {cnt_rows * cnt_cols}")
    print(f"Одномерный массив: {flat_list}")
    merger_method(flat_list)
