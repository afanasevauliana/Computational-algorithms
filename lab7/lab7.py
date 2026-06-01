class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def build(self, postfix):
        self.root = build_tree(postfix)
    
    def to_infix(self):
        return to_infix(self.root)
    
    def print_tree(self):
        print_tree(self.root)

    def traverse_with_stack(self, node=None):
        if node is None:
            node = self.root
        if node is None:
            print("Дерево пустое")
            return []
        
        stack = []
        current = node
        visited_nodes = []
        steps = []
        
        while stack or current:
            while current:
                steps.append(f"Заходим в узел '{current.value}' (кладём в стек)")
                stack.append(current)
                current = current.left
                if current:
                    steps.append(f"Идём налево от '{stack[-1].value}'")
            
            current = stack.pop()
            steps.append(f"Возврат в узел '{current.value}' (выходим из стека)")
            visited_nodes.append(current.value)
            steps.append(f"ПОСЕЩАЕМ УЗЕЛ: '{current.value}'")
            
            current = current.right
            if current:
                steps.append(f"Идём направо от '{visited_nodes[-1]}'")
        
        print("\n".join(steps))
        print(f"\nРезультат обхода (порядок посещения): {' -> '.join(visited_nodes)}")
        return visited_nodes
    
    def addr(self, value):
        return self._find_node(self.root, value)
    
    def _find_node(self, node, value):
        if node is None:
            return None
        if node.value == value:
            return node
        left_result = self._find_node(node.left, value)
        if left_result:
            return left_result
        return self._find_node(node.right, value)
    
    def value(self, node):
        return node.value if node else None
    
    def left(self, node):
        return node.left if node else None
    
    def right(self, node):
        return node.right if node else None
    
    def father(self, node, current=None, parent=None):
        if current is None:
            current = self.root
        if current is None:
            return None
        if current == node:
            return parent
        if current.left:
            result = self.father(node, current.left, current)
            if result is not None:
                return result
        if current.right:
            result = self.father(node, current.right, current)
            if result is not None:
                return result
        return None
    
    def brother(self, node):
        parent = self.father(node)
        if parent is None:
            return None
        if parent.left == node:
            return parent.right
        elif parent.right == node:
            return parent.left
        return None
    
    def is_left(self, node):
        parent = self.father(node)
        if parent is None:
            return False
        return parent.left == node
    
    def is_right(self, node):
        parent = self.father(node)
        if parent is None:
            return False
        return parent.right == node
    
    def nodes_quantity(self, node=None):
        if node is None:
            node = self.root
        if node is None:
            return 0
        left_count = self.nodes_quantity(node.left) if node.left else 0
        right_count = self.nodes_quantity(node.right) if node.right else 0
        return 1 + left_count + right_count
    
    def clear(self):
        self.root = None

def is_operator(s):
    if s in {'+', '-', '*', '/'}:
        return True
    else: 
        return False

def build_tree(postfix):
    stack = []
    for k in postfix:
        if is_operator(k):
            right = stack.pop()
            left = stack.pop()
            stack.append(Node(k, left, right))
        else:
            stack.append(Node(k))
    return stack.pop()

def to_infix(node):
    if node.left is None and node.right is None:
        return node.value
    else:
        return f"({to_infix(node.left)}{node.value}{to_infix(node.right)})"

def print_tree(node, level=0, is_left=True):
    if node is None:
        return
    
    print_tree(node.right, level + 1, False)
    
    indent = "    " * level
    if level > 0:
        if is_left:
            print(f"{indent}└─── {node.value}")
        else:
            print(f"{indent}┌─── {node.value}")
    else:
        print(f"{node.value}")
    
    print_tree(node.left, level + 1, True)

if __name__ == "__main__":
    tree = BinaryTree()
    examples = [
        ("ab+", ["a", "b", "+"]),
        ("ab+c*", ["a", "b", "+", "c", "*"]),
        ("ab+cd+*", ["a", "b", "+", "c", "d", "+", "*"]),
        ("ab+c*de/-", ["a", "b", "+", "c", "*", "d", "e", "/", "-"]),
    ]
    
    postfix_expr = None
    
    while True:
        print("\nМЕНЮ:")
        print("1. Выбрать пример выражения")
        print("2. Ввести своё выражение")
        print("3. Показать инфиксную запись")
        print("4. Показать дерево")
        print("5. Показать количество узлов")
        print("6. Обход")
        print("7. Демонстрация операций (addr, father, brother, is_left, is_right)")
        print("8. Очистить дерево")
        print("0. Выход")
        print("\n")
        
        choice = input("Выберите действие: ").strip()
        
        if choice == '0':
            print("Программа завершена")
            break
        
        elif choice == '1':
            print("\nПримеры:")
            for i, (expr, _) in enumerate(examples, 1):
                print(f"  {i}. {expr}")
            try:
                ex_choice = input("Выберите пример (1-4): ").strip()
                if ex_choice in ['1', '2', '3', '4']:
                    idx = int(ex_choice) - 1
                    postfix_expr = examples[idx][0]
                    tree.build(postfix_expr)
                    print(f"\nПостроено дерево для: {postfix_expr}")
                else:
                    print("Неверный выбор!")
            except Exception as e:
                print(f"Ошибка: {e}")
        
        elif choice == '2':
            expr = input("Введите постфиксное выражение: ").strip().replace(" ", "")
            if expr:
                postfix_expr = expr
                tree.build(postfix_expr)
                print(f"\nПостроено дерево для: {postfix_expr}")
            else:
                print("Пустое выражение!")
        
        elif choice == '3':
            if tree.root is None:
                print("Дерево пустое! Сначала выберите или введите выражение (пункт 1 или 2).")
            else:
                print(f"\nПостфиксная запись: {postfix_expr}")
                print(f"Полноскобочная инфиксная запись: {tree.to_infix()}")
        
        elif choice == '4':
            if tree.root is None:
                print("Дерево пустое! Сначала выберите или введите выражение (пункт 1 или 2).")
            else:
                print("\nДерево выражения:")
                tree.print_tree()
        
        elif choice == '5':
            if tree.root is None:
                print("Дерево пустое! Сначала выберите или введите выражение (пункт 1 или 2).")
            else:
                print(f"\nКоличество узлов в дереве: {tree.nodes_quantity()}")
        
        elif choice == '6':
            if tree.root is None:
                print("Дерево пустое! Сначала выберите или введите выражение (пункт 1 или 2).")
            else:
                print("\nОбход дерева")
                tree.traverse_with_stack()

        elif choice == '7':
            if tree.root is None:
                print("Дерево пустое! Сначала выберите или введите выражение (пункт 1 или 2).")
            else:
                print("\nДемонстрация примитивных операций:")
                nodes_to_test = []
                for val in ['a', 'b', 'c', 'd', 'e', '+', '-', '*', '/']:
                    node = tree.addr(val)
                    if node and node not in nodes_to_test:
                        nodes_to_test.append(node)
                
                if not nodes_to_test:
                    print("Не найдено узлов для демонстрации!")
                else:
                    for test_node in nodes_to_test[:5]:
                        print(f"\n      Узел со значением '{tree.value(test_node)}'")
                        print(f"  addr('{tree.value(test_node)}') = {test_node}")
                        print(f"  value = {tree.value(test_node)}")
                        print(f"  left = {tree.value(tree.left(test_node)) if tree.left(test_node) else None}")
                        print(f"  right = {tree.value(tree.right(test_node)) if tree.right(test_node) else None}")
                        print(f"  is_left? {tree.is_left(test_node)}")
                        print(f"  is_right? {tree.is_right(test_node)}")
                        
                        father = tree.father(test_node)
                        print(f"  father = {tree.value(father) if father else None}")
                        
                        brother = tree.brother(test_node)
                        print(f"  brother = {tree.value(brother) if brother else None}")
                
        
        elif choice == '8':
            tree.clear()
            postfix_expr = None
            print("Дерево очищено!")
        
        else:
            print("Неверный выбор! Используйте 0-8.")