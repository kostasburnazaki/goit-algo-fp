import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Побудова графа та позицій для відображення дерева за допомогою NetworkX
def build_nx_tree(root, G=None, pos=None, x=0, y=0, layer=1):
    if G is None:
        G = nx.DiGraph()
    if pos is None:
        pos = {}
        
    if root:
        G.add_node(id(root), label=root.val)
        pos[id(root)] = (x, y)
        if root.left:
            G.add_edge(id(root), id(root.left))
            build_nx_tree(root.left, G, pos, x - 1 / (1.8 ** layer), y - 1, layer + 1)
        if root.right:
            G.add_edge(id(root), id(root.right))
            build_nx_tree(root.right, G, pos, x + 1 / (1.8 ** layer), y - 1, layer + 1)
    return G, pos

# Алгоритм DFS (Стек) з фіксацією порядку
def dfs_order(root):
    if not root: return []
    stack, order = [root], []
    visited = set()
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            order.append(node)
            if node.right: stack.append(node.right)
            if node.left: stack.append(node.left)
    return order

# Алгоритм BFS (Черга) з фіксацією порядку
def bfs_order(root):
    if not root: return []
    queue, order = [root], []
    while queue:
        node = queue.pop(0)
        order.append(node)
        if node.left: queue.append(node.left)
        if node.right: queue.append(node.right)
    return order

def visualize_tree_traversal(root, traversal_type="DFS"):
    G, pos = build_nx_tree(root)
    order = dfs_order(root) if traversal_type == "DFS" else bfs_order(root)
    
    # Створення градієнта від темного до світлого (Hex кольори)
    # Порядок визначає інтенсивність кольору
    num_nodes = len(order)
    color_map = {}
    for step, node in enumerate(order):
        # Зміна інтенсивності синього кольору: від темного до світлого
        intensity = int(30 + (step / num_nodes) * 200) 
        hex_color = f"#{intensity:02x}85x" # Custom RGB generation
        # Для коректності скористаємося вбудованим лінійним градієнтом плоттера:
        color_map[id(node)] = mcolors.to_hex(plt.cm.Purples(0.4 + 0.6 * (step / num_nodes)))

    node_colors = [color_map[node_id] for node_id in G.nodes()]
    labels = {id(n): n.val for n in order}
    
    plt.figure(figsize=(8, 5))
    nx.draw(G, pos, labels=labels, with_labels=True, node_color=node_colors, 
            node_size=1000, font_weight='bold', font_color='black', edge_color='gray', arrows=False)
    plt.title(f"Обхід дерева в колірному градієнті: {traversal_type}")
    plt.show()

# Демонстрація
def main():
    print("\n--- Завдання 5 (Обходи дерева DFS/BFS) ---")
    # Створюємо бінарне дерево
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(7)
    root.right.left = TreeNode(12)
    root.right.right = TreeNode(18)

    visualize_tree_traversal(root, "DFS")
    visualize_tree_traversal(root, "BFS")


if __name__ == "__main__":
    main()