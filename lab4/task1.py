with open("text_for_lab4.txt", 'r', encoding='utf-8') as file:
    a = file.readline().split()
    cnt_rows = a[0]
    cnt_cols = a[1]
    content = file.read()
    print(cnt_rows, cnt_cols)
    print(content)

