import time
import random
import math

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

def measure_time(arr, iterations=5):
    times = []
    for _ in range(iterations):
        arr_copy = arr.copy()
        start = time.perf_counter()
        merge_sort(arr_copy)
        end = time.perf_counter()
        times.append((end - start) * 1000000)  # микросекунды
    return sum(times) / len(times)

sizes = [100, 200, 400, 800, 1600, 3200, 6400, 12800, 25600]

print("Исследование вычислительной сложности сортировки слиянием:")
print(f"{'n':>8} | {'Время (мкс)':>12} | {'log₂(n)':>9} | {'n*log₂(n)':>12} | {'n²':>15} | {'Время/n':>12} | {'Время/(n*log₂n)':>16}")
print("-" * 100)

results = []

for size in sizes:
    arr = [random.randint(-1000, 1000) for _ in range(size)]
    avg_time = measure_time(arr)
    log2_n = math.log2(size)
    n_log_n = size * log2_n
    n_squared = size * size
    time_per_n = avg_time / size
    time_per_nlogn = avg_time / n_log_n if n_log_n > 0 else 0
    
    results.append({
        'size': size,
        'time': avg_time,
        'log2_n': log2_n,
        'n_log_n': n_log_n,
        'n_squared': n_squared,
        'time_per_n': time_per_n,
        'time_per_nlogn': time_per_nlogn
    })
    
    print(f"{size:8d} | {avg_time:12.2f} | {log2_n:9.4f} | {n_log_n:12.0f} | {n_squared:15.0f} | {time_per_n:12.4f} | {time_per_nlogn:16.6f}")

print("\nАнализ роста времени при увеличении n в 2 раза:")
print(f"{'Диапазон':>12} | {'Рост n':>10} | {'Рост времени':>12} | {'Теоретический рост O(n)':>20} | {'Теоретический рост O(n²)':>20}")
print("-" * 80)

for i in range(1, len(results)):
    prev = results[i-1]
    curr = results[i]
    n_growth = curr['size'] / prev['size']
    time_growth = curr['time'] / prev['time']
    print(f"{prev['size']:4d} → {curr['size']:4d} | {n_growth:10.1f} | {time_growth:12.2f} | {n_growth:20.1f} | {n_growth*n_growth:20.1f}")
