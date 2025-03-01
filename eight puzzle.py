import heapq
goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def manhattan_distance(state):
    distance = 0
    for r in range(3):
        for c in range(3):
            val = state[r][c]
            if val != 0:
                target_r, target_c = divmod(val - 1, 3)
                distance += abs(r - target_r) + abs(c - target_c)
    return distance
def get_neighbors(state):
    blank_pos = [(r, c) for r in range(3) for c in range(3) if state[r][c] == 0][0]
    r, c = blank_pos
    neighbors = []
    for dr, dc in moves:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            new_state = [row[:] for row in state]
            new_state[r][c], new_state[nr][nc] = new_state[nr][nc], new_state[r][c]
            neighbors.append(new_state)

    return neighbors
def is_goal(state):
    return state == goal_state
def a_star(initial_state):
    open_list = []
    heapq.heappush(open_list, (0, initial_state, [], 0))

    visited = set()

    while open_list:
        f, current_state, path, g = heapq.heappop(open_list)

        if tuple(tuple(row) for row in current_state) in visited:
            continue
        visited.add(tuple(tuple(row) for row in current_state))

        if is_goal(current_state):
            return path

        for neighbor in get_neighbors(current_state):
            if tuple(tuple(row) for row in neighbor) not in visited:
                h = manhattan_distance(neighbor)
                heapq.heappush(open_list, (g + h + 1, neighbor, path + [neighbor], g + 1))

    return None
def print_solution(path):
    for step in path:
        for row in step:
            print(row)
        print()
initial_state = [[2, 0, 3], [1, 4, 5], [7, 8, 6]]

solution = a_star(initial_state)

if solution:
    print("Solution found!")
    print_solution(solution)
else:
    print("No solution found.")
