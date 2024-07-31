import pygame, sys, random , math
pygame.init()

# Set up the display
width,height = 1000,1000  # Size of the window
screen =  pygame.display.set_mode((width,height))
pygame.display.set_caption("Orbiting Ball")

import random

def return_slices(number, num_slices, min_slice = 1, max_slice = None):
    if max_slice == None: max_slice = number - num_slices
    if num_slices <= 0:
        raise ValueError("Number of slices must be greater than zero.")
    if num_slices > number:
        raise ValueError("Number of slices cannot be greater than the number itself.")
    if min_slice <= 0 or max_slice <= 0:
        raise ValueError("Minimum and maximum slice sizes must be greater than zero.")
    if min_slice > max_slice:
        raise ValueError("Minimum slice size cannot be greater than maximum slice size.")
    if num_slices * min_slice > number or num_slices * max_slice < number:
        raise ValueError("It's impossible to split the number into the specified number of slices with given min and max sizes.")

    slices = []
    remaining = number

    for _ in range(num_slices - 1):
        max_possible = min(max_slice, remaining - (num_slices - len(slices) - 1) * min_slice)
        min_possible = min_slice
        slice_size = random.randint(min_possible, max_possible)
        slices.append(slice_size)
        remaining -= slice_size

    slices.append(remaining)

    return slices

class planet():
    all = []
    def __init__(self, radius, ball_radius):
    # Define the parameters for the orbit
        self.center = (width/2,height/2)  # The fixed point (center of the window)
        self.radius = radius  # Radius of the orbit
        self.ball_radius = ball_radius  # Radius of the ball
        self.angle = 0
        self.speed = random.uniform(0.07 , 0.01)
        self.color = self.color = (random.randint(50 , 200),random.randint(50 , 200),random.randint(50 , 200))
        planet.all.append(self)
    def rotate(self):
        if not paused:
            self.angle += self.speed
        # Calculate the new position of the ball
        x = self.center[0] + self.radius * math.cos(self.angle)
        y = self.center[1] + self.radius * math.sin(self.angle)
        # Draw the ball
        pygame.draw.circle(screen, self.color, (int(x), int(y)), self.ball_radius)

def generate_planets(planetnum):
        radius_list = return_slices(width/4,planetnum,5)
        print(str(radius_list))
        radius = 0#radius_list[0]
        for a in radius_list:
            newplanet = planet(radius + a,a/2)
            radius += a*1.5
def reset():
    planet.all = []
    generate_planets(10)

paused = False

a = planet(100,20)

# Clock object to control the frame rate
clock = pygame.time.Clock()
fps = 60  # Frames per second

# Main loop
running = True
while running:
    # Clear the screen
    screen.fill("black")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                paused = not paused            
            if event.key == pygame.K_r:
                
                    reset()
    #draw center
    pygame.draw.circle(screen,"white", (width/2, height/2), 5)
    for planets in planet.all:
            planets.rotate()

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(fps)

# Quit pygame
pygame.quit()