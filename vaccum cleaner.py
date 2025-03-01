import random

def initialize_environment(rows, cols):
    return [[random.choice([0, 1]) for _ in range(cols)] for _ in range(rows)]

def display_environment(environment):
    for row in environment:
        print(row)
    print()

def vacuum_cleaner(environment, start_row, start_col):
    rows, cols = len(environment), len(environment[0])
    row, col = start_row, start_col
    
    print("Initial Environment:")
    display_environment(environment)
    
    for i in range(rows):
        for j in range(cols):
            row, col = i, j  
            if environment[row][col] == 1:
                print(f"Vacuum cleaner cleaning position ({row}, {col})")
                environment[row][col] = 0
            display_environment(environment)
    
    print("Final Cleaned Environment:")
    display_environment(environment)

dimensions = (3, 3)  
environment = initialize_environment(*dimensions)

vacuum_start = (0, 0)

vacuum_cleaner(environment, *vacuum_start)
