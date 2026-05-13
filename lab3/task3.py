class Queue: #FIFO
    class Node:
        def __init__(self, data):
            self.data = data # для хранения предложение
            self.next = None
    
    def __init__(self):
        self.front = None  # начало очереди
        self.rear = None   # конец очереди
        self.size = 0
    
    def add_to_the_end_of_the_queue(self, data):
        new_node = self.Node(data)
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1
    
    def del_queue(self): # удаление элемента из начала очереди
        if self.is_empty():
            return None
        
        data = self.front.data
        self.front = self.front.next
        
        if self.front is None: # если очередь опустела
            self.rear = None
        
        self.size -= 1
        return data
    
    def is_empty(self):
        return self.front is None
    
def individual_sentences(text):
    sentences = []
    current_sentence = ""
    
    for char in text:
        current_sentence += char # добавляем текущий символ к накапливаемому предложению
        if char in '.!?':
            sentence = current_sentence.strip() # убираем пробелы на краях
            if sentence:
                sentences.append(sentence)
            current_sentence = ""
    # если остался текст без знака препинания в конце
    if current_sentence.strip():
        sentences.append(current_sentence.strip())
    return sentences


def find_longest_sentence_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
    sentences = individual_sentences(content)
    queue = Queue()
    for sentence in sentences:
        queue.add_to_the_end_of_the_queue(sentence)
    longest_sentence = ""
    max_length = 0
    
    while not queue.is_empty():
        tsentence = queue.del_queue()
        tlenght = len(tsentence)
        if tlenght > max_length:
            max_length = tlenght
            longest_sentence = tsentence
    return longest_sentence, max_length


def print_longest_sentence(filename):
    result = find_longest_sentence_from_file(filename)
    longest_sentence, max_length = result
    print(f"Самое длинное предложение ({max_length} символов):")
    print(longest_sentence)

if __name__ == "__main__":
    print_longest_sentence("text_for_task3.txt")
