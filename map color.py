def is_valid_coloring(state, country, color, neighbors):
    for neighbor in neighbors[country]:
        if state.get(neighbor) == color:
            return False
    return True

def backtracking_search(state, countries, colors, neighbors):
    if len(state) == len(countries):
        return state  
    
    uncolored = [c for c in countries if c not in state]
    country = uncolored[0]
    
    for color in colors:
        if is_valid_coloring(state, country, color, neighbors):
            state[country] = color
            result = backtracking_search(state, countries, colors, neighbors)
            if result:
                return result
            state.pop(country) 
    
    return None

def map_coloring(countries, colors, neighbors):
    return backtracking_search({}, countries, colors, neighbors)
countries = ['A', 'B', 'C', 'D']
colors = ['Red', 'Green', 'Blue']
neighbors = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

solution = map_coloring(countries, colors, neighbors)
print("Color Assignment:", solution)
