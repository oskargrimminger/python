# Define the grid size
GRID_SIZE = 5

# Define the possible directions (N = North, E = East, S = South, W = West)
DIRECTIONS = ['N', 'E', 'S', 'W']

def turn_left(direction):
    # Turn left: Move counterclockwise in the direction list
    return DIRECTIONS[(DIRECTIONS.index(direction) - 1) % 4]

def turn_right(direction):
    # Turn right: Move clockwise in the direction list
    return DIRECTIONS[(DIRECTIONS.index(direction) + 1) % 4]

def move(x, y, direction):
    # Move in the direction the robot is facing
    if direction == 'N':
        y += 1
    elif direction == 'E':
        x += 1
    elif direction == 'S':
        y -= 1
    elif direction == 'W':
        x -= 1
    
    # Ensure the robot stays within the grid boundaries
    x = max(0, min(GRID_SIZE - 1, x))
    y = max(0, min(GRID_SIZE - 1, y))
    
    return x, y

def main():
    # Input: Initial position and direction (e.g., 1 2 N)
    initial_position = input("Enter initial position and direction (e.g., 1 2 N): ").split()
    x, y = int(initial_position[0]), int(initial_position[1])
    direction = initial_position[2]
    
    # Input: Series of instructions (e.g., LMLMLMLMM)
    instructions = input("Enter instructions (e.g., LMLMLMLMM): ")
    
    # Process each instruction
    for instruction in instructions:
        if instruction == 'L':
            direction = turn_left(direction)
        elif instruction == 'R':
            direction = turn_right(direction)
        elif instruction == 'M':
            x, y = move(x, y, direction)
    
    # Output: Final position and direction
    print(f"Final position: {x} {y} {direction}")

if __name__ == "__main__":
    main()
