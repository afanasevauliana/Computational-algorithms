import time
import random
import string

def rabin_karp_simple(text, s):
    n = len(text) # длина текста
    m = len(s) # длина строки для поиска
    if m == 0 or m > n:
        return []
    s_hash = sum(ord(i) for i in s)
    arr_of_indices = []
    for k in range(n - m + 1):
        substring = text[k:k+m]
        substring_hash = sum(ord(i) for i in substring)
        if s_hash == substring_hash:
            if s == substring:
                arr_of_indices.append(k)
    return arr_of_indices

if __name__ == "__main__":
    text = input("Введите текст: ")
    s = input("Введите строку для поиска: ")
    start = time.perf_counter()
    index_in_text = rabin_karp_simple(text, s)
    end = time.perf_counter()
    print(f'Подстрока для поиска "{s}" начинается с индекса(ов) {index_in_text}')
    print(f"Время выполнения алгоритма: {end-start:.6f} секунд")

    print("\nИССЛЕДОВАНИЕ ВЫЧИСЛИТЕЛЬНОЙ СЛОЖНОСТИ АЛГОРИТМА РАБИНА-КАРПА")
    print("Таблица 1. Зависимость времени от длины текста, m = 10")
    print(f"{'Длина текста n':^20} | {'Время (с)':^15}")
    s = ''.join(random.choices(string.ascii_letters, k=10)) #подстрока, которой нет в тексте (лучший случай)
    for n in range(0, 10001, 1000):
        text = ''.join(random.choices(string.ascii_letters, k=n))
        start = time.perf_counter()
        index_in_text = rabin_karp_simple(text, s)
        end = time.perf_counter()
        print(f"{n:^20} | {(end-start):^15.8f}")

    print("\nТаблица 2. Зависимость времени от длины образца, n = 5000")
    print(f"{'Длина подстроки m':^20} | {'Время (с)':^15}")
    text = ''.join(random.choices(string.ascii_letters, k=5000))
    for m in range(0, 2000, 200):
        s = ''.join(random.choices(string.ascii_letters, k=m))
        start = time.perf_counter()
        index_in_text = rabin_karp_simple(text, s)
        end = time.perf_counter()
        print(f"{m:^20} | {(end-start):^15.8f}")
