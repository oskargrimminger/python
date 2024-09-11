class Directions:
    def __init__(self):
        self.grid_size = 5
        self.directions = ['N','W','S','O']

    def turn_left(self, direction):
        return self.directions[(self.directions.index(direction) - 1) % 4]

    def turn_right(self, direction):
        return self.directions[(self.directions.index(direction) + 1) % 4]

    def move(self,x, y, direction):
        if direction == 'N':
            y += 1
        elif direction == 'S':
            y -= 1
        elif direction == 'W':
            x += 1
        elif direction == 'O':
            x -= 1

        x = max(0, min(self.grid_size - 1, x))
        y = max(0, min(self.grid_size - 1, y))

        return x, y

class Game:
    def __init__(self):
        self.see_directions = Directions()

    def main(self):
        initial_fixed_postion = input("Enter postion of the robot eg 1 2 N: ").split()
        x,y = int(initial_fixed_postion[0]), int(initial_fixed_postion[1])
        direction =initial_fixed_postion[2]

        instructions = input("Enter instructions 'LMLMLMLMM': ")

        for instruction in instructions:
            if instruction == 'L':
                direction = self.see_directions.turn_left(direction)
            elif instruction == 'R':
                direction = self.see_directions.turn_right(direction)
            elif instruction == 'M':
                x, y = self.see_directions.move(x, y, direction)
    
        print(f'final postion: {x},{y}, {direction}')   


game = Game()
game.main()
