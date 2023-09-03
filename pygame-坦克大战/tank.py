from pygame.image import load
from pygame.sprite import collide_rect
from bullet import Bullet


class Tank(object):
    def __init__(self, tankImgSrcTuple: tuple, window_size: tuple, x=570, y=370) -> None:
        self.tankImg_U = load(tankImgSrcTuple[0])  # 加载坦克图片
        self.tankImg_D = load(tankImgSrcTuple[1])  # 加载坦克图片
        self.tankImg_L = load(tankImgSrcTuple[2])  # 加载坦克图片
        self.tankImg_R = load(tankImgSrcTuple[3])  # 加载坦克图片
        self.tankImg = self.tankImg_U  # 默认坦克朝上
        self.live = True

        self.direction = 'U'  # 坦克方向
        self.rect = self.tankImg.get_rect()
        self.rect.left = self.rect.left  # 坦克当前的X坐标
        self.rect.top = self.rect.top  # 坦克当前的Y坐标
        self.oldLeft = None  # 未移动前的横坐标
        self.oldTop = None # 未移动前的纵坐标
        self.width = self.tankImg.get_rect().width
        self.height = self.tankImg.get_rect().height
        self.step = 7  # 步长
        self.window_size = window_size  # 窗口大小

        self.bulletImg = load('images/bullet.gif')  # 加载子弹图片
        self.bullet = None  # 坦克发射的子弹
        self.bulletList = []  # 当前屏幕中的子弹
        self.MAX_BULLET_NUMBER = 10  # 最大子弹数量

    def move(self, direction='U'):
        self.direction = direction  # 更新坦克方向
        self.oldTop = self.rect.top  # 更新旧的坐标
        self.oldLeft = self.rect.left  # 更新旧的坐标

        if direction == 'U':
            self.tankImg = self.tankImg_U  # 坦克向上
            if self.rect.top >= 0:  # 坦克在屏幕内
                self.rect.top -= self.step  # 坦克向上移动的步长
        elif direction == 'D':
            self.tankImg = self.tankImg_D
            if self.rect.top <= self.window_size[1] - self.tankImg_D.get_height():
                self.rect.top += self.step
        if direction == 'L':
            self.tankImg = self.tankImg_L
            if self.rect.left >= 0:
                self.rect.left -= self.step
        elif direction == 'R':
            self.tankImg = self.tankImg_R
            if self.rect.left <= self.window_size[0] - self.tankImg_R.get_width():
                self.rect.left += self.step

    def fire(self, screen):
        self.bullet = Bullet(self.bulletImg, self)
        self.bulletList.append(self.bullet)

    def display(self, screen):
        screen.blit(self.tankImg, (self.rect.left, self.rect.top))
