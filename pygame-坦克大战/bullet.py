from settings import WIDTH, HEIGHT

class Bullet(object):
    def __init__(self, bulletImg, tank):
        self.tank = tank  # 坦克对象
        self.direction = self.tank.direction  # 子弹方向
        self.bulletImg = bulletImg  # 加载子弹图片
        self.width = self.bulletImg.get_rect().width
        self.height = self.bulletImg.get_rect().height
        self.x = None  # 子弹的X坐标
        self.y = None  # 子弹的Y坐标
        self.speed = 5  # 子弹的速度
        self.live = True  # 当前子弹的是否有效（在屏幕中）

        if self.direction == 'U':
            self.x = self.tank.rect.left + self.tank.width / 2 - self.width / 2
            self.y = self.tank.rect.top - self.height
        if self.direction == 'D':
            self.x = self.tank.rect.left + self.tank.width / 2 - self.width / 2
            self.y = self.tank.rect.top + self.tank.height
        if self.direction == 'L':
            self.x = self.tank.rect.left - self.width
            self.y = self.tank.rect.top + self.tank.height / 2 - self.height / 2
        if self.direction == 'R':
            self.x = self.tank.rect.left + self.tank.width
            self.y = self.tank.rect.top + self.tank.height / 2 - self.height / 2

    def move(self):
        if self.direction == 'U':
            self.y -= self.speed
        elif self.direction == 'D':
            self.y += self.speed
        elif self.direction == 'L':
            self.x -= self.speed
        elif self.direction == 'R':
            self.x += self.speed

    def drop(self, bulletList):
        if self.x <= -self.width or self.x >= WIDTH or self.y <= -self.height or self.y >= HEIGHT:
            self.live = False
            bulletList.remove(self)

    def display(self, screen):
        screen.blit(self.bulletImg, (self.x, self.y))
