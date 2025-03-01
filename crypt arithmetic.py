from itertools import permutations

def solve_cryptarithmetic():
    # Define unique letters in the problem
    letters = 'SENDMORY'
    
    # Generate all possible digit permutations
    for perm in permutations(range(10), len(letters)):
        # Create a dictionary mapping letters to digits
        mapping = dict(zip(letters, perm))
        
        # Ensure leading digits are not zero
        if mapping['S'] == 0 or mapping['M'] == 0:
            continue
        
        # Convert words to numbers
        send = mapping['S'] * 1000 + mapping['E'] * 100 + mapping['N'] * 10 + mapping['D']
        more = mapping['M'] * 1000 + mapping['O'] * 100 + mapping['R'] * 10 + mapping['E']
        money = mapping['M'] * 10000 + mapping['O'] * 1000 + mapping['N'] * 100 + mapping['E'] * 10 + mapping['Y']
        
        # Check if the equation holds
        if send + more == money:
            print(f"Solution found: {mapping}")
            print(f"{send} + {more} = {money}")
            return
    
    print("No solution found.")

# Run the solver
solve_cryptarithmetic()
