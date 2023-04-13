import pygame

pygame.init()
sc = pygame.display.set_mode((800, 600))
RED = (255, 0, 0)
x = 387.5
y = 287.5
pos = (x, y)
pygame.display.set_caption("Circle")
clock = pygame.time.Clock()
done = True
FPS = 30

while done:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if x > 25:
            x -= 25
    if keys[pygame.K_RIGHT]:
        if x < 775:
            x += 25
    if keys[pygame.K_UP]:
        if y > 25:
            y -= 25
    if keys[pygame.K_DOWN]:
        if y < 575:
            y += 25
    pos = (x, y)

    sc.fill((255, 255, 255))
    pygame.draw.circle(sc, RED, pos, 25)
    pygame.display.flip()