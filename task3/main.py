import networkx as nx
import heapq
import matplotlib.pyplot as plt


def dijkstra(graph, start):
    # Ініціалізація відстаней та множини невідвіданих вершин
    distances = {vertex: float('infinity') for vertex in graph.nodes}
    distances[start] = 0

    min_heap = [(0, start)]

    while min_heap:
        # Знаходження вершини з найменшою відстанню серед невідвіданих
        current_distance, current_vertex = heapq.heappop(min_heap)

        # Якщо поточна відстань більша ніж вже знайдена, пропускаємо ітерацію
        if current_distance > distances[current_vertex]:
            continue

        # Оновлення відстаней для сусідніх вершин
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight['weight']

            # Якщо нова відстань коротша, то оновлюємо найкоротший шлях
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(min_heap, (distance, neighbor))

    return distances


# Створення зваженого графу
G = nx.Graph()

edges = [
    ('A', 'B', 4),
    ('B', 'C', 1),
    ('C', 'D', 1),
    ('A', 'D', 7),
    ('A', 'C', 8),
    ('E', 'F', 5),
    ('F', 'G', 2),
    ('G', 'H', 3),
    ('H', 'I', 4),
    ('I', 'J', 6),
    ('E', 'J', 7),
    ('E', 'A', 2),
    ('F', 'B', 3),
    ('G', 'C', 5),
    ('H', 'D', 6),
    ('I', 'B', 7),
    ('J', 'D', 4),
    ('A', 'J', 9),
    ('B', 'H', 8),
    ('C', 'F', 2),
]

# Додавання ребер до графа
for edge in edges:
    G.add_edge(edge[0], edge[1], weight=edge[2])

# Візуалізація графу
plt.figure(figsize=(16, 9))
options = {
    "font_size": 15,
    "font_weight": "bold",
    "font_color": "white",
    "node_size": 1500,
    "width": 2,
    "with_labels": True
}
pos = nx.kamada_kawai_layout(G)
# pos = nx.circular_layout(G)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw(G, pos, ** options)

nx.draw_networkx_edge_labels(
    G, pos, edge_labels=edge_labels, font_size=13, font_weight="bold")

plt.show()

# Пошук найкоротших шляхів від початкової вершини 'A'
distances = dijkstra(G, 'A')
print("Найкоротші шляхи від вершини 'A'")
for vertex, distance in distances.items():
    print(f"до вершини {vertex}: {distance}")
