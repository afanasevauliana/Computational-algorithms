import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import FancyBboxPatch

# Глобальные переменные
frames = []

def get_depth(arr):
    if len(arr) <= 1:
        return 1
    sr = len(arr) // 2
    return 1 + max(get_depth(arr[:sr]), get_depth(arr[sr:]))

def merge_sort(arr, x=0, y=0, level=0, max_depth=None):
    if max_depth is None:
        max_depth = get_depth(arr)
    
    # Сохраняем узел деления
    frames.append({
        'type': 'divide_node',
        'arr': arr.copy(),
        'x': x,
        'y': y,
        'level': level,
    })
    
    if len(arr) <= 1:
        return arr, level, x, y  # возвращаем также координаты
    
    sr = len(arr) // 2
    left_side = arr[:sr]
    right_side = arr[sr:]
    
    # Координаты детей
    if level == 0:  # корень
        stretch = 1.55
    elif level == 1:  # первый уровень детей
        stretch = 1.43
    else:
        stretch = 1.3

    offset = stretch ** (max_depth - level)
    x_left = x - offset
    x_right = x + offset
    y_child = y - 1.2
    
    # Сохраняем ребра от родителя к детям
    frames.append({
        'type': 'edge',
        'x1': x, 'y1': y - 0.3,
        'x2': x_left, 'y2': y_child + 0.3,
    })
    
    left_result, left_max_level, left_final_x, left_final_y = merge_sort(
        left_side, x_left, y_child, level + 1, max_depth)
    
    frames.append({
        'type': 'edge',
        'x1': x, 'y1': y - 0.3,
        'x2': x_right, 'y2': y_child + 0.3,
    })
    
    right_result, right_max_level, right_final_x, right_final_y = merge_sort(
        right_side, x_right, y_child, level + 1, max_depth)
    
    # Слияние
    result = merge_list(left_result, right_result)
    
    # Узел слияния располагается на уровень ниже самого глубокого из детей
    max_child_level = max(left_max_level, right_max_level)
    y_merge = y_child - 1.2 * (max_child_level - level)
    
    frames.append({
        'type': 'edge',
        'x1': left_final_x, 'y1': left_final_y - 0.3,
        'x2': x, 'y2': y_merge + 0.3,
    })
    frames.append({
        'type': 'edge',
        'x1': right_final_x, 'y1': right_final_y - 0.3,
        'x2': x, 'y2': y_merge + 0.3,
    })

    frames.append({
        'type': 'merge_node',
        'arr': result.copy(),
        'x': x,
        'y': y_merge,
        'level': max_child_level + 1,
    })
    
    return result, max_child_level + 1, x, y_merge  # возвращаем координаты результата

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

def draw_tree_animation():
    fig, ax = plt.subplots(figsize=(16, 14))
    
    nodes = {}
    drawn_edges = []
    
    def update(frame_idx):
        frame = frames[frame_idx]
        
        if frame['type'] == 'divide_node':
            key = (frame['x'], frame['y'], 'divide')
            if key not in nodes:
                box = FancyBboxPatch((frame['x'] - 0.9, frame['y'] - 0.35), 
                                      1.8, 0.7,
                                      boxstyle="round,pad=0.02",
                                      facecolor='lightblue', edgecolor='black', linewidth=1.5)
                ax.add_patch(box)
                txt = ax.text(frame['x'], frame['y'], str(frame['arr']), 
                             ha='center', va='center', fontsize=7)
                nodes[key] = (box, txt)
        
        elif frame['type'] == 'merge_node':
            key = (frame['x'], frame['y'], 'merge')
            if key not in nodes:
                box = FancyBboxPatch((frame['x'] - 0.9, frame['y'] - 0.35), 
                                      1.8, 0.7,
                                      boxstyle="round,pad=0.02",
                                      facecolor='lightgreen', edgecolor='darkgreen', linewidth=2)
                ax.add_patch(box)
                txt = ax.text(frame['x'], frame['y'], str(frame['arr']), 
                             ha='center', va='center', fontsize=7, fontweight='bold')
                nodes[key] = (box, txt)
        
        elif frame['type'] == 'edge':
            edge_key = (frame['x1'], frame['y1'], frame['x2'], frame['y2'])
            if edge_key not in drawn_edges:
                ax.annotate('', xy=(frame['x2'], frame['y2']), xytext=(frame['x1'], frame['y1']),
                           arrowprops=dict(arrowstyle='->', color='gray', lw=1.2, alpha=0.7))
                drawn_edges.append(edge_key)
        
        # Автоматические границы
        all_x = [frame.get('x', 0) for frame in frames if 'x' in frame]
        all_y = [frame.get('y', 0) for frame in frames if 'y' in frame]
        if all_x and all_y:
            ax.set_xlim(min(all_x) - 2, max(all_x) + 2)
            ax.set_ylim(min(all_y) - 1, max(all_y) + 1)
        
        ax.axis('off')
        ax.set_title('Сортировка слиянием', 
                    fontsize=12, fontweight='bold')
        
        plt.tight_layout()
    
    anim = animation.FuncAnimation(fig, update, frames=len(frames), 
                                   interval=800, repeat=False)
    plt.show()
    return anim

with open("m2.txt", 'r', encoding='utf-8') as file:
    a = file.readline().split()
    cnt_rows = int(a[0])
    cnt_cols = int(a[1])

    array = []
    for i in range(cnt_rows):
        line = file.readline().split()
        for k in line:
            array.append(int(k))
    
    print(f"Количество элементов: {cnt_rows * cnt_cols}")
    print(f"Одномерный массив: {array}")

# Очищаем кадры перед сортировкой
frames = []
max_depth = get_depth(array)
sorted_arr, _, _, _ = merge_sort(array, x=0, y=10, max_depth=max_depth)
print(f"Отсортированный массив: {sorted_arr}")

# Запускаем анимацию
draw_tree_animation()