from pygame.image import load


class Wall(object):
    def __init__(self, left, top):
        self.wallImg = load('images/wall.gif')
        self.rect = self.wallImg.get_rect()
        self.rect.left = left
        self.rect.top = top
        self.width = self.rect.width
        self.height = self.rect.height
        self.life = 4

    def drop_wall(self):
        pass

    def display(self, screen):
        screen.blit(self.wallImg, self.rect)


if __name__ == '__main__':
    import pygame
    import math

    pygame.init()
    wall_list = []
    WIDTH = 1208
    HEIGHT = 809
    NUM = 5
    WALL_WIDTH = 60
    WALL_HEIGHT = 60
    WALL_SPACE = (WIDTH - NUM * WALL_HEIGHT) // (NUM - 1)
    WALL_ROUND = (WIDTH - (NUM - 1) * WALL_SPACE - NUM * WALL_WIDTH) / 2
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    for i in range(0, NUM):
        wall = Wall(i * (WALL_WIDTH + WALL_SPACE), HEIGHT / 4 - WALL_HEIGHT / 2)
        wall_list.append(wall)

    for i in range(0, NUM):
        wall = Wall(i * (WALL_WIDTH + WALL_SPACE), (3 / 4) * HEIGHT - WALL_HEIGHT / 2)
        wall_list.append(wall)

    for wall in wall_list:
        wall.display(screen)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

