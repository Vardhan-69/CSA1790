from collections import deque

# Define the initial state (Missionaries, Cannibals, Boat Position: 1=Left, 0=Right)
initial_state = (3, 3, 1)
goal_state = (0, 0, 0)

# Valid boat moves (1 or 2 people can move at a time)
moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]

def is_valid(state):
    """Check if a state is valid (Missionaries should never be outnumbered)."""
    m, c, _ = state
    if m < 0 or c < 0 or m > 3 or c > 3:
        return False
    if (m < c and m > 0) or (3 - m < 3 - c and (3 - m) > 0):
        return False
    return True

def get_successors(state):
    """Generate all valid next states from the current state."""
    successors = []
    m, c, b = state
    direction = -1 if b == 1 else 1
    for move in moves:
        new_state = (m + direction * move[0], c + direction * move[1], 1 - b)
        if is_valid(new_state):
            successors.append(new_state)
    return successors

def bfs():
    """Perform BFS to find the solution."""
    queue = deque([(initial_state, [])])  # (current_state, path_taken)
    visited = set()
    while queue:
        state, path = queue.popleft()
        if state == goal_state:
            return path + [state]
        if state in visited:
            continue
        visited.add(state)
        for successor in get_successors(state):
            queue.append((successor, path + [state]))
    return None

# Find solution
solution = bfs()
if solution:
    for step in solution:
        print(step)
else:
    print("No solution found!")
