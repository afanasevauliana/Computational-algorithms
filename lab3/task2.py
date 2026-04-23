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

if __name__ == "__main__":
    s1 = "qwerty"
    s2 = "zcerty"
    print(f"'{s1}' и '{s2}': {is_reverse(s1, s2)}")

    s1 = "казаки"
    s2 = "иказак"
    print(f"'{s1}' и '{s2}': {is_reverse(s1, s2)}")

    s1 = "abcd"
    s2 = "abc"
    print(f"'{s1}' и '{s2}': {is_reverse(s1, s2)}")
