import sys
import time
sys.setrecursionlimit(10000)

def A(m, n):
    if m == 0:
        return n+1
    if m > 0 and n == 0:
        return A(m-1, 1)
    if m > 0 and n > 0:
        return A(m-1, A(m, n-1))
    
def z_time(m, n):
    try:
        start = time.perf_counter()
        a = A(m, n)
        end = time.perf_counter()
        return a, end - start
    except RecursionError:
        return None, None
    
if __name__ == "__main__":
    while True:
        try:
            m = int(input("Введите целое неотрицательное число m: "))
            n = int(input("Введите целое неотрицательное число n: "))
            if m < 0 or n < 0:
                print("Оба числа должны быть неотрицательными, попробуйте снова")
                continue
            a, t = z_time(m, n)
            print(f"A({m}, {n}) = {a}")
            print(f"Время выполнения: {t:.6f} секунд")
            break
        except ValueError:
            print("Введите целые числа: ")
        except RecursionError:
            print("Превышена глубина рекурсии! Попробуйте меньшие значения m и n")
    
    print("\nЭкспериментальные данные временной сложности функции Аккермана:")
    print(f"{'m':^4} | {'n':^4} | {'A(m, n)':^20} | {'Время (с)':^12}")
    test_cases = [(0, 100),
        (0, 1000),
        (1, 100),
        (1, 500),
        (2, 100),
        (2, 200),
        (3, 0),
        (3, 1),
        (3, 2),
        (3, 3),
        (3, 4),
        (3, 5),
        (3, 6),
        (3, 7),
        (3, 8),
        (3, 9),
        (4, 0),
        (4, 1)]
    for m, n in test_cases:
        result, elapsed = z_time(m, n)
        if result is None:
            print(f"{m:^6} | {n:^6} | {'RecursionError':^15} | {'error':^15}")
        else:
            print(f"{m:^6} | {n:^6} | {result:^15} | {elapsed:^15.8f}")