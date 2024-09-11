board = [[" " for _ in range(3)] for _ in range(3)]

for row in board:
    print(" | ".join(row))
    print("-" * 5)