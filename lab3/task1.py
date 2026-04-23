class DbList:
    class Node:
        def __init__(self, element, next_node=None, previous_node=None):
            self.element = element
            self.next_node = next_node
            self.previous_node = previous_node

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    # 1. Добавление элемента в начало списка
    def add_to_beginning(self, element):
        new_node = self.Node(element)
        self.length += 1

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next_node = self.head
            self.head.previous_node = new_node
            self.head = new_node

        return element
    
    # Добавление элемента в конец
    def add(self, element):
        new_node = self.Node(element)
        self.length += 1

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.previous_node = self.tail
            self.tail.next_node = new_node
            self.tail = new_node

        return element

    # 2. Показ всех элементов списка
    def print_elements(self):
        if self.head is None:
            print("[]")
            return
        elements = []
        current = self.head
        while current:
            elements.append(str(current.element))
            current = current.next_node
        print(elements)

    # 3. Определение количества элементов списка
    def size(self):
        return self.length

    # 4. Удаление первого элемента
    def remove_first(self):
        if self.head is None:
            return None
        removed = self.head.element
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next_node
            self.head.previous_node = None
        self.length -= 1
        return removed

    # 5. Поиск данного значения в списке
    def search(self, value):
        current = self.head
        index = 0
        while current:
            if current.element == value:
                return index
            current = current.next_node
            index += 1
        return -1

    # 6. Удаление элемента списка с данным значением (первого вхождения)
    def delete_by_value(self, value):
        current = self.head
        while current:
            if current.element == value:
                if current == self.head: # если удаляем голову
                    self.remove_first()
                elif current == self.tail: # если удаляем хвост
                    self.tail = current.previous_node
                    self.tail.next_node = None
                    self.length -= 1
                else: # если удаляем из середины
                    current.previous_node.next_node = current.next_node
                    current.next_node.previous_node = current.previous_node
                    self.length -= 1
                return True
            current = current.next_node
        return False

    # 7. Изменение всех элементов списка с данным значением на новое
    def replace_all(self, old_value, new_value):
        current = self.head
        found = False
        while current:
            if current.element == old_value:
                current.element = new_value
                found = True
            current = current.next_node
        return found

    # 8. Определение, является ли список симметричным
    def is_symmetric(self):
        if self.length <= 1:
            return True
        
        left = self.head
        right = self.tail
        
        for _ in range(self.length // 2):
            if left.element != right.element:
                return False
            left = left.next_node
            right = right.previous_node
        
        return True

    # 9. Определение, сколько различных значений содержится в списке
    def count_distinct(self):
        if self.head is None:
            return 0
        
        distinct_values = []
        current = self.head
        while current:
            if current.element not in distinct_values:
                distinct_values.append(current.element)
            current = current.next_node
        
        return len(distinct_values)

    # 10. Сортировка элементов списка способом изменения указателей
    def sort_by_pointers(self):
        if self.length <= 1:
            return
        
        swapped = True
        while swapped:
            swapped = False
            current = self.head
            
            while current and current.next_node:
                if current.element > current.next_node.element:
                    current.element, current.next_node.element = current.next_node.element, current.element # меняем значения местами
                    swapped = True
                current = current.next_node

    def remove_last(self): # доп метод: удаление последнего элемента (нужен для delete_by_value)
        if self.tail is None:
            return None
        removed = self.tail.element
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.previous_node
            self.tail.next_node = None
        self.length -= 1
        return removed

    def __iter__(self):
        current = self.head
        while current:
            yield current.element # генератор (для цикла for)
            current = current.next_node


if __name__ == '__main__':
    dbList = DbList()

    dbList.add(0)
    dbList.add(1)
    dbList.add(2)
    dbList.add(2)
    dbList.add(8)
    dbList.add(-3)

    print("Исходный список:")
    dbList.print_elements()
    print(f"Количество элементов: {dbList.size()}")
    print("\n1. Добавление элемента 99 в начало:")
    dbList.add_to_beginning(99)
    dbList.print_elements()
    print(f"\n2. Текущий список:")
    dbList.print_elements()
    print(f"\n3. Количество элементов: {dbList.size()}")
    print("\n4. Удаление первого элемента:")
    dbList.remove_first()
    dbList.print_elements()
    print("\n5. Поиск данного значения:")
index = dbList.search(2)
if index != -1:
    print(f"Элемент 2 найден на индексе {index}")
else:
    print("Элемент 2 не найден")

index = dbList.search(100)
if index != -1:
    print(f"Элемент 100 найден на индексе {index}")
else:
    print("Элемент 100 не найден")
    print("\n6. Удаление элемента со значением 2 (первое вхождение):")
    dbList.delete_by_value(2)
    dbList.print_elements()
    print("\n7. Замена всех элементов со значением 2 на 99:")
    dbList.replace_all(2, 99)
    dbList.print_elements()
    print("\n8. Проверка списка на симметричность:")
    dbList.print_elements()
    print(f"Список симметричен? {dbList.is_symmetric()}")
    print("\nСписок после изменений для проверки:")
    dbList.add(8)
    dbList.add(99)
    dbList.add(1)
    dbList.add(0)
    dbList.print_elements()
    print(f"Симметричен? {dbList.is_symmetric()}")
    print("\n9. Подсчёт различных значений:")
    distinct_list = DbList()
    distinct_list.add(1)
    distinct_list.add(2)
    distinct_list.add(2)
    distinct_list.add(3)
    distinct_list.add(1)
    distinct_list.add(4)
    distinct_list.print_elements()
    print(f"Количество различных значений: {distinct_list.count_distinct()}")
    print("\n10. Сортировка списка:")
    unsorted = DbList()
    unsorted.add(5)
    unsorted.add(1)
    unsorted.add(4)
    unsorted.add(2)
    unsorted.add(8)
    unsorted.add(0)
    unsorted.add(-3)
    print("До сортировки:")
    unsorted.print_elements()
    unsorted.sort_by_pointers()
    print("После сортировки:")
    unsorted.print_elements()
