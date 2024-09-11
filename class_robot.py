class Directions:
    def __init__(self):
        self.grid_size = 5
        self.directions = ['N', 'W', 'S', 'E']  # 'O' should be 'E' for East

    def turn_left(self, direction):
        return self.directions[(self.directions.index(direction) - 1) % 4]

    def turn_right(self, direction):
        return self.directions[(self.directions.index(direction) + 1) % 4]

    def move(self, x, y, direction):
        if direction == 'N':
            y += 1
        elif direction == 'S':
            y -= 1
        elif direction == 'W':
            x -= 1
        elif direction == 'E':  # Adjusted for East
            x += 1

        # Ensure the robot stays within grid bounds
        x = max(0, min(self.grid_size - 1, x))
        y = max(0, min(self.grid_size - 1, y))

        return x, y


class Game:
    def __init__(self):
        self.directions_handler = Directions()

    def main(self):
        initial_fixed_position = input("Enter position of the robot (e.g., 1 2 N): ").split()
        x, y = int(initial_fixed_position[0]), int(initial_fixed_position[1])
        direction = initial_fixed_position[2]

        instructions = input("Enter instructions (e.g., 'LMLMLMLMM'): ")

        for instruction in instructions:
            if instruction == 'L':
                direction = self.directions_handler.turn_left(direction)
            elif instruction == 'R':
                direction = self.directions_handler.turn_right(direction)
            elif instruction == 'M':
                x, y = self.directions_handler.move(x, y, direction)

        print(f'Final position: {x}, {y}, {direction}')


# Run the game
game = Game()
game.main()
