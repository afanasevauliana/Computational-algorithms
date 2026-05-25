class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        """Метод деления: берём остаток от деления ключа на размер таблицы"""
        return key % self.size
    
    def insert(self, key, value):
        attempt = 0  # начинаем с первой попытки
        
        # Пробуем найти свободное место (максимум size попыток)
        while attempt < self.size:
            # Вычисляем индекс для текущей попытки
            index = (self.hash_function(key) + attempt * attempt) % self.size
            
            # Если ячейка свободна (None) - кладём сюда
            if self.table[index] is None:
                self.table[index] = value
                print(f"Ключ {key} вставлен в ячейку {index}")
                return True
            
            # Если занято - пробуем следующий attempt
            attempt += 1
        
        # Если все ячейки заняты
        print("Таблица заполнена!")
        return False

    def find_index(self, key, attempt):
        """
        Находит индекс для ключа с учётом попыток
        attempt = 0 - первая попытка
        attempt = 1 - вторая попытка и т.д.
        """
        base_index = self.hash_function(key)
        # Формула: (базовый индекс + attempt^2) % размер
        return (base_index + attempt * attempt) % self.size
        
ht = HashTable(10)

ht.insert(42, "Вася")   # идёт в ячейку 2
ht.insert(52, "Маша")   # 52%10=2 (занято!), идёт в 3 (2+1^2)
ht.insert(62, "Петя")   # 62%10=2 (занято!), 3 занято, идёт в 6 (2+2^2=6)

print(ht.table)
# Результат: [None, None, 'Вася', 'Маша', None, None, 'Петя', None, None, None]