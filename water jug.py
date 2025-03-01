from collections import deque

def is_valid_state(x, y, a, b):
    return 0 <= x <= a and 0 <= y <= b
def water_jug_problem(a, b, c):
    visited = set()
    queue = deque([(0, 0)])
    while queue:
`12        x, y = queue.popleft()
        if x == c or y == c:
            return True
        if (x, y) in visited:
            continue
        visited.add((x, y))
        next_states = [
            (a, y),  
            (x, b),  
            (0, y),  
            (x, 0),  
            (x - min(x, b - y), y + min(x, b - y)),  
            (x + min(y, a - x), y - min(y, a - x))
        ]
        for state in next_states:
            if is_valid_state(state[0], state[1], a, b) and state not in visited:
                queue.append(state)
    return False
a = 4  
b = 3  
c = 2
if water_jug_problem(a, b, c):
    print(f"It is possible to measure {c} liters using the jugs.")
else:
    print(f"It is not possible to measure {c} liters using the jugs.")
