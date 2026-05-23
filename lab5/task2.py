import time

def rabin_karp_simple(text, s):
    n = len(text) # длина текста
    m = len(s) # длина строки для поиска
    if m == 0 or m > n:
        return []
    s_hash = sum(ord(i) for i in s)

    for k in range(n - m + 1):
        substring = text[k:k+m]
        substring_hash = sum(ord(i) for i in substring)
        if s_hash == substring_hash:
            if s == substring:
                return k
    return -1

text = input("Введите текст: ")
s = input("Введите строку для поиска: ")
start = time.perf_counter()
index_in_text = rabin_karp_simple(text, s)
end = time.perf_counter()
print(f'Подстрока для поиска "{s}" начинается с индекса {index_in_text}')
print(f"Время выполнения алгоритма: {end-start:.6f} секунд")

