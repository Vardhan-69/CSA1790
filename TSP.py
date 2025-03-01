from itertools import permutations
def calculate_distance(graph, path):
    """Calculate the total distance of a given path."""
    distance = 0
    for i in range(len(path) - 1):
        distance += graph[path[i]][path[i + 1]]
    distance += graph[path[-1]][path[0]]  
    return distance
def travelling_salesman(graph):
    """Solve the Traveling Salesman Problem using brute force."""
    nodes = list(graph.keys())
    min_distance = float('inf')
    best_path = None
    for perm in permutations(nodes):
        distance = calculate_distance(graph, perm)
        if distance < min_distance:
            min_distance = distance
            best_path = perm
    
    return best_path, min_distance
graph = {
    'A': {'A': 0, 'B': 10, 'C': 15, 'D': 20},
    'B': {'A': 10, 'B': 0, 'C': 35, 'D': 25},
    'C': {'A': 15, 'B': 35, 'C': 0, 'D': 30},
    'D': {'A': 20, 'B': 25, 'C': 30, 'D': 0}
}
best_path, min_distance = travelling_salesman(graph)
print("Optimal Path:", best_path)
print("Minimum Distance:", min_distance)
