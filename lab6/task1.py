class MyHashTable:
    def __init__(self, size=11, c1=0, c2=1):
        self.size = size
        self.c1 = c1 # c1, c2: коэффициенты квадратичной пробы h(k,i) = (h(k) + c1*i + c2*i^2) mod m
        self.c2 = c2
        self.table = [None] * size      # для хранения значений
        self.keys = [None] * size       # для хранения ключей
        self.deleted = [False] * size   # маркер удалённых элементов
        
    def _hash_division(self, key): # метод деления для первичного хеширования
        return key % self.size
    
    def _quadratic_probe(self, key, attempt): # квадратичное исследование
        primary_hash = self._hash_division(key)
        return (primary_hash + self.c1 * attempt + self.c2 * attempt * attempt) % self.size # индекс в таблице для данной попытки
    
    def insert(self, key, value): # вставка пары ключ-значение в хеш-таблицу
        attempt = 0
        while attempt < self.size:
            index = self._quadratic_probe(key, attempt)
            if self.keys[index] is None or self.deleted[index]: # если ячейка свободна или помечена как удалённая
                self.keys[index] = key
                self.table[index] = value
                self.deleted[index] = False
                print(f"Вставка успешна: ключ {key} -> индекс {index}")
                return True
            if self.keys[index] == key and not self.deleted[index]: # если ключ уже существует, обновляем значение
                self.table[index] = value
                print(f"Обновление: ключ {key} уже существует, значение изменено")
                return True
            attempt += 1
        print("Хеш-таблица переполнена")
        return False
    
    def search(self, key): # поиск значения по ключу
        attempt = 0
        while attempt < self.size:
            index = self._quadratic_probe(key, attempt)
            if self.keys[index] is None:
                print(f"Ключ {key} не найден (проверено {attempt} позиций)")
                return None
            if self.keys[index] == key and not self.deleted[index]: # если нашли ключ и ячейка не удалена
                print(f"Ключ {key} найден на индексе {index}")
                return self.table[index]
            attempt += 1
        print(f"Ключ {key} не найден")
        return None
    
    def delete(self, key):
        attempt = 0
        while attempt < self.size:
            index = self._quadratic_probe(key, attempt)
            if self.keys[index] is None:
                print(f"Ключ {key} не найден для удаления")
                return False
            if self.keys[index] == key and not self.deleted[index]:
                self.deleted[index] = True
                self.table[index] = None
                print(f"Ключ {key} удалён из индекса {index} (логическое удаление)")
                return True
            attempt += 1
        print(f"Ключ {key} не найден для удаления")
        return False
    
    def display(self):
        print("\n" + "=" * 60)
        print("          ХЕШ-ТАБЛИЦА С ОТКРЫТОЙ АДРЕСАЦИЕЙ")
        print("=" * 60)
        print(f"{'Индекс':<8} {'Ключ':<12} {'Значение':<20} {'Статус'}")
        print("=" * 60)
        for i in range(self.size):
            if self.keys[i] is None:
                print(f"{i:<8} {'-':<12} {'-':<20} {'свободно'}")
            elif self.deleted[i]:
                print(f"{i:<8} {str(self.keys[i]):<12} {'-':<20} {'удалён'}")
            else:
                print(f"{i:<8} {str(self.keys[i]):<12} {str(self.table[i]):<20} {'занят'}")
        print("=" * 60)
    
    def clear(self):
        self.table = [None] * self.size
        self.keys = [None] * self.size
        self.deleted = [False] * self.size
        print("Таблица полностью очищена")


def print_menu():
    print("\nМеню:")
    print("1. Вставка элемента (ключ + значение)")
    print("2. Поиск элемента по ключу")
    print("3. Удаление элемента по ключу")
    print("4. Показать всю таблицу")
    print("5. Очистить таблицу")
    print("6. Изменить размер таблицы")
    print("7. Показать информацию о таблице")
    print("8. Тестовый пример (автоматическое заполнение)")
    print("0. Выход")


def create_new_table():
    while True:
        try:
            size = int(input("Введите размер таблицы (рекомендуется простое число): "))
            if size <= 0:
                print("Размер должен быть положительным числом!")
                continue
            print("Выберите коэффициенты квадратичного исследования:")
            print("1. Стандартный (c1=0, c2=1) - h(k,i) = (h(k) + i²) mod m")
            print("2. Пользовательский")
            choice = input("Ваш выбор (1/2): ")
            if choice == '1':
                c1, c2 = 0, 1
            else:
                c1 = int(input("Введите c1: "))
                c2 = int(input("Введите c2: "))

            return MyHashTable(size, c1, c2)
        except ValueError:
            print("Ошибка: введите корректное число!")


def demo_auto_fill(ht):
    test_data = [
        (15, "Северенков"), (26, "Романова"), (37, "Рулёв"), 
        (48, "Круглова"), (59, "Сёмин"), (70, "Зарубина")
    ]
    print("\nАвтоматическое заполнение тестовыми данными:")
    for key, value in test_data:
        print(f"  Вставка: ключ={key}, значение='{value}'")
        ht.insert(key, value)
    ht.display()


def main():
    ht = MyHashTable(size=11, c1=0, c2=1)
    while True:
        print_menu()
        choice = input("\nВыберите действие: ")
        if choice == '1':
            try:
                key = int(input("Введите целочисленный ключ: "))
                value = input("Введите значение (строка): ")
                ht.insert(key, value)
            except ValueError:
                print("Ошибка: ключ должен быть целым числом!") 
        elif choice == '2':
            try:
                key = int(input("Введите ключ для поиска: "))
                result = ht.search(key)
                if result is not None:
                    print(f"Значение: {result}")
            except ValueError:
                print("Ошибка: ключ должен быть целым числом!")   
        elif choice == '3':
            try:
                key = int(input("Введите ключ для удаления: "))
                ht.delete(key)
            except ValueError:
                print("Ошибка: ключ должен быть целым числом!")   
        elif choice == '4':
            ht.display()
        elif choice == '5':
            confirm = input("Вы уверены? (y/n): ")
            if confirm.lower() == 'y':
                ht.clear()
        elif choice == '6':
            confirm = input("При изменении размера таблица будет очищена. Продолжить? (y/n): ")
            if confirm.lower() == 'y':
                ht = create_new_table()
                print("Новая таблица создана")
        elif choice == '7':
            print(f"\nИнформация о таблице:")
            print("Параметры: метод деления + квадратичное исследование (c1=0, c2=1)")
            print(f"Размер таблицы: {ht.size}")
            print(f"Коэффициенты: c1={ht.c1}, c2={ht.c2}")
            print(f"Хеш-функция: h(k) = k % {ht.size}")
            print(f"Метод разрешения коллизий: квадратичное исследование")
            print(f"Формула: h(k,i) = ((k mod {ht.size}) + {ht.c1}*i + {ht.c2}*i^2) mod {ht.size}") 
        elif choice == '8':
            demo_auto_fill(ht)
        elif choice == '0':
            print("\nПрограмма завершена")
            break
        else:
            print("Неверный выбор! Пожалуйста, выберите пункт от 0 до 8")

if __name__ == "__main__":
    main()