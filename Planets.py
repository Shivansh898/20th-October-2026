import pgzrun
import random
from time import time

start = time()
end_time = 0
finished = False

WIDTH = 1000
HEIGHT = 600

planets = []
lines = []
next_planet = 0

planet_names = ["Mercury","Venus","Earth","Mars","Jupiter","Saturn","Uranus","Neptune"]
# Create planets
for name in planet_names:
    planet = Actor(name.lower())  
    planet.x = random.randint(100, 900)
    planet.y = random.randint(100, 500)
    planets.append(planet)

rocket = Actor("rocket")
rocket.pos = (50, 300)

def draw():
    screen.blit("space", (0, 0))

    # Draw planets
    for i, planet in enumerate(planets):
        planet.draw()
        screen.draw.text(str(i + 1),(planet.x, planet.y + 40),color="white")

    # Draw lines
    for line in lines:
        screen.draw.line(line[0], line[1], "yellow")

    rocket.draw()

    # Timer
    if not finished:
        total = time() - start
    else:
        total = end_time

    screen.draw.text("Time: " + str(round(total, 2)),(20, 20),color="white")

    # Instructions
    screen.draw.text("Connect planets from Mercury to Neptune",center=(WIDTH // 2, 30),color="cyan",fontsize=40)

    if next_planet == len(planets):
        screen.draw.text("SOLAR SYSTEM COMPLETE!",center=(WIDTH // 2, HEIGHT // 2),color="yellow",fontsize=60)

def update():
    pass

def on_mouse_down(pos):
    global next_planet
    global lines
    global finished
    global end_time

    if next_planet < len(planets):

        if planets[next_planet].collidepoint(pos):

            rocket.pos = planets[next_planet].pos

            if next_planet > 0:
                lines.append((planets[next_planet - 1].pos,planets[next_planet].pos))

            next_planet += 1

            if next_planet == len(planets):
                end_time = time() - start
                finished = True

        else:
            lines = []
            next_planet = 0
            rocket.pos = (50, 300)

pgzrun.go()