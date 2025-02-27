import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
tile_image = pygame.image.load("mahjong_tile.png")  # Load tile image

running = True
while running:
    screen.fill((0, 128, 0))  # Green background like a Mahjong table
    screen.blit(tile_image, (0, 0))  # Draw tile at position
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
