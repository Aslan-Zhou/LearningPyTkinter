import pygame, sys, random
from pygame.color import THECOLORS

pygame.init()
screen = pygame.display.set_mode([640, 480])
screen.fill([random.randint(1, 254), random.randint(1, 254), random.randint(1, 254)])
for i in range(random.randint(5, 1250)):
    whdth = random.randint(0, 250)
    hieght = random.randint(0, 100)
    top = random.randint(0, 400)
    left = random.randint(0, 500)

    color_name = random.choice(list(THECOLORS.keys()))
    color = THECOLORS[color_name]
    line_whdth = random.randint(1, 3)

    pygame.draw.rect(screen, color, [whdth, hieght, top, left], line_whdth)
    pygame.time.delay(30)
    pygame.display.flip()

if __name__ == '__main__':
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

pygame.quit()

