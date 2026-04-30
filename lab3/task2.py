import time
import random
import string
class Stack:
    class Node:
        def __init__(self, value, next_node=None):
            self.value = value
            self.next_node = next_node

    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, value): # добавление элемента в стек
        new_node = self.Node(value, self.top)
        self.top = new_node
        self.size += 1

    def pop(self): # удаление и возврат верхнего элемента
        if self.is_empty():
            return None
        value = self.top.value
        self.top = self.top.next_node
        self.size -= 1
        return value

    def is_empty(self):
        return self.top is None

    def get_size(self):
        return self.size


def is_reverse(s1, s2):
    if len(s1) != len(s2):
        return False

    stack = Stack()
    # 1. Кладём все символы s1 в стек
    for ch in s1:
        stack.push(ch)
    # 2. Сравниваем символы из стека (обратный порядок) с s2
    for ch in s2:
        if stack.pop() != ch:
            return False
    return True

def is_reverse2(s1, s2):
    if len(s1) == len(s2):
        len_s1 = len(s1)
        for i in range(len_s1):
            if s1[i] != s2[-i]:
                return False
    else:
        return False
    return True

def main():
    print("Введите число 1, если хотите автоматически создать строки.\nВведите число 2, если хотите ввести строки.")
    k = input()
    if k == '1':
        characters = string.ascii_uppercase + string.digits
        s1 = ''.join(random.choice(characters) for l in range(100000))
        s2 = ''.join(random.choice(characters) for l in range(100000))

    elif k == '2':
        print("Введите строку s1:")
        s1 = input()
        print("Введите строку s2:")
        s2 = input()
    else:
        print("Ошибка. Нужно ввести 1 или 2.")
        return
    print("Способ без использования стандартных коллекций:")
    start = time.time()
    is_reverse(s1, s2)
    elapsed_time = time.time() - start 
    print(f'Время работы: {elapsed_time}')
    if len(s1) < 101 and len(s2) < 101:
        print(f"'{s1}' и '{s2}': {is_reverse(s1, s2)}")
    else: print(is_reverse(s1, s2))
    print("Способ с использованием стандартных коллекций:")
    start = time.time()
    is_reverse2(s1, s2)
    elapsed_time = time.time() - start 
    print(f'Время работы: {elapsed_time}')
    if len(s1) < 101 and len(s2) < 101:
        print(f"'{s1}' и '{s2}': {is_reverse(s1, s2)}")
    else: print(is_reverse(s1, s2))

if __name__ == "__main__":
    main()
