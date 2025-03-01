import heapq

class Node:
    def __init__(self, name, parent=None, g=0, h=0):
        self.name = name
        self.parent = parent
        self.g = g
        self.h = h  
        self.f = g + h  
    
    def __lt__(self, other):
        return self.f < other.f

def a_star(graph, heuristic, start, goal):
    open_list = []
    closed_set = set()
    start_node = Node(start, None, 0, heuristic[start])
    heapq.heappush(open_list, start_node)
    
    while open_list:
        current_node = heapq.heappop(open_list)
        
        if current_node.name == goal:
            path = []
            while current_node:
                path.append(current_node.name)
                current_node = current_node.parent
            return path[::-1]
        
        closed_set.add(current_node.name)
        
        for neighbor, cost in graph[current_node.name].items():
            if neighbor in closed_set:
                continue
            g = current_node.g + cost
            h = heuristic[neighbor]
            neighbor_node = Node(neighbor, current_node, g, h)
            heapq.heappush(open_list, neighbor_node)
    
    return None
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1, 'E': 3},
    'E': {'D': 3}
}

heuristic = {
    'A': 7, 'B': 6, 'C': 2, 'D': 1, 'E': 0
}
start, goal = 'A', 'E'
path = a_star(graph, heuristic, start, goal)
print("Optimal Path:", path)
