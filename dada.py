import os
import time
import random

# Terminal-Größe (Kann angepasst werden)
WIDTH, HEIGHT = os.get_terminal_size()

# Startposition
x, y = random.randint(0, WIDTH-1), random.randint(0, HEIGHT-1)
dx, dy = 1, 1  # Bewegungsrichtung (1 bedeutet vorwärts, -1 rückwärts)

logo = "DVD"  # Das "Logo", das sich bewegt

# Endlosschleife, um das Logo zu bewegen
while True:
    # Terminal löschen
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Positionen im Terminal überprüfen
    if x + len(logo) >= WIDTH or x < 0:
        dx *= -1  # Richtungsänderung horizontal
    if y >= HEIGHT or y < 0:
        dy *= -1  # Richtungsänderung vertikal

    x += dx
    y += dy

    # Ausgabe auf der neuen Position
    for i in range(HEIGHT):
        if i == y:
            print(" " * x + logo)
        else:
            print()

    # Zeitverzögerung, um die Geschwindigkeit zu kontrollieren
    time.sleep(0.05)
