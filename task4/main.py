import uuid

import networkx as nx
import matplotlib.pyplot as plt
from collections import deque


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        # Унікальний ідентифікатор для кожного вузла
        self.id = str(uuid.uuid4())

    def __lt__(self, other):
        return self.val < other.val


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
    nx.draw(tree, pos=pos, labels=labels, arrows=False,
            node_size=2500, node_color=colors)
    plt.show()


def level_order_traversal(root):
    if not root:
        return []
    queue = deque([root])
    result = []
    while queue:
        node = queue.popleft()
        if node:
            result.append(node)
            queue.append(node.left)
            queue.append(node.right)
    return result


def heapify(node_list, max_heap=False):
    if max_heap:
        node_list.sort(key=lambda x: x.val, reverse=True)
    else:
        node_list.sort(key=lambda x: x.val)
    return node_list


def build_heap_tree(node_list):
    if not node_list:
        return None
    n = len(node_list)
    for i in range(n):
        left_index = 2 * i + 1
        right_index = 2 * i + 2
        if left_index < n:
            node_list[i].left = node_list[left_index]
        else:
            node_list[i].left = None
        if right_index < n:
            node_list[i].right = node_list[right_index]
        else:
            node_list[i].right = None
    return node_list[0]


def convert_to_heap(root, max_heap=False):
    nodes = level_order_traversal(root)
    heapified_nodes = heapify(nodes, max_heap)
    heap_root = build_heap_tree(heapified_nodes)
    return heap_root


# Створення дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)
root.right.right = Node(2)  # Додамо ще один вузол для симетричної візуалізації


# Конвертувати дерево в купу (для наочності використаймо максимальну купу)
heap_root = convert_to_heap(root, True)

# Visualize the heap
draw_tree(heap_root)
