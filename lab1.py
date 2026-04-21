import time

def find_number():
    suitable_number = 2
    while True:
        m = []
        a = 1
        while True:
            a_cube = a**3
            if a_cube > suitable_number:
                break
            b = a
            while True:
                b_cube = b**3
                s = a_cube + b_cube
                if s == suitable_number:
                    m.append((a, b))
                    break
                elif s > suitable_number:
                    break
                else:
                    b += 1
            a += 1
        if len(m) >= 2:
            return suitable_number, m
        suitable_number += 1

def main():
    start = time.time()
    result, m = find_number()
    elapsed_time = time.time() - start 
    print(f'Время работы: {elapsed_time}')
    print(f"Наименьшее число: {result}")
    print("Способы представления числа в виде суммы кубов двух натуральных чисел:")
    for a, b in m:
        print(f"{a}^3 + {b}^3 = {a**3} + {b**3} = {result}")
if __name__ == "__main__":
    main()