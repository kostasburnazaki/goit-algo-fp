import networkx as nx
import matplotlib.pyplot as plt

def get_heap_positions(heap, index=0, x=0, y=0, layer=1, pos=None):
    if pos is None:
        pos = {}
    if index < len(heap):
        pos[index] = (x, y)
        left = 2 * index + 1
        right = 2 * index + 2
        # Зсув по осі X зменшується з кожним рівнем
        get_heap_positions(heap, left, x - 1 / (1.8 ** layer), y - 1, layer + 1, pos)
        get_heap_positions(heap, right, x + 1 / (1.8 ** layer), y - 1, layer + 1, pos)
    return pos

def visualize_binary_heap(heap):
    G = nx.DiGraph()
    
    # Додавання зв'язків для купи
    for i in range(len(heap)):
        left = 2 * i + 1
        right = 2 * i + 2
        if left < len(heap):
            G.add_edge(i, left)
        if right < len(heap):
            G.add_edge(i, right)
            
    pos = get_heap_positions(heap)
    labels = {i: str(heap[i]) for i in range(len(heap))}
    
    plt.figure(figsize=(8, 5))
    nx.draw(G, pos, labels=labels, with_labels=True, node_color='#FF9800', 
            node_size=1000, font_weight='bold', font_color='white', edge_color='gray', arrows=False)
    plt.title("Візуалізація структури бінарної купи")
    plt.show()

# Демонстрація Завдання 4
print("\n--- Завдання 4 (Візуалізація купи) ---")
min_heap_array = [4, 7, 8, 12, 14, 9, 10, 16, 20, 25]
print(f"Масив купи для візуалізації: {min_heap_array}")
visualize_binary_heap(min_heap_array)