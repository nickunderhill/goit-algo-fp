import uuid

import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="#1296F0"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        # Унікальний ідентифікатор для кожного вузла
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        # Використання id та збереження значення вузла
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r,
                          y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(
        data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, font_color="whitesmoke", arrows=False,
            node_size=2500, node_color=colors,)
    plt.show()


def darken_color(color, factor=0.25):
    """Затемнити колір на 25%"""
    color = color.lstrip('#')
    r, g, b = int(color[:2], 16), int(color[2:4], 16), int(color[4:], 16)
    r, g, b = [max(int(comp * (1 - factor)), 0) for comp in (r, g, b)]
    return f"#{r:02x}{g:02x}{b:02x}"


def bfs(root):
    queue = [root]
    color = root.color
    while queue:
        node = queue.pop(0)
        node.color = color
        color = darken_color(color)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


def dfs(node):
    stack = [node]
    current_color = None
    while stack:
        current_node = stack.pop()
        if current_node is not None:
            current_color = current_node.color if not current_color else darken_color(
                current_color)
            current_node.color = current_color
            if current_node.right:
                stack.append((current_node.right))
            if current_node.left:
                stack.append((current_node.left))


# Створення дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)
root.right.right = Node(2)  # Додамо ще один вузол для симетричної візуалізації


# bfs(root)
dfs(root)

# Visualize the heap
draw_tree(root)
