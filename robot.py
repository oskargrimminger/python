grid_size = 5



directions = ['N','W','S','O']

def turn_left(direction):
    return directions[(directions.index(direction) - 1) % 4]

def turn_right(direction):
    return directions[(directions.index(direction) + 1) % 4]

def move(x, y, direction):
    if direction == 'N':
        y += 1
    elif direction == 'S':
        y -= 1
    elif direction == 'W':
        x += 1
    elif direction == 'O':
        x -= 1

    x = max(0, min(grid_size - 1, x))
    y = max(0, min(grid_size - 1, y))
    
    return x,y

def main():
    initial_fixed_postion = input("Enter postion of the robot eg 1 2 N: ").split()
    x,y = int(initial_fixed_postion[0]), int(initial_fixed_postion[1])
    direction =initial_fixed_postion[2]

    instructions = input("Enter instructions 'LMLMLMLMM': ")

    for instruction in instructions:
        if instruction == 'L':
            direction = turn_left(direction)
        elif instruction == 'R':
            direction = turn_right(direction)
        elif instruction == 'M':
            x, y = move(x, y, direction)
    
    print(f'final postion: {x},{y}, {direction}')   

main()


