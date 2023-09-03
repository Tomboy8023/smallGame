from tank import Tank


class MyTank(Tank):
    def __init__(self, window_size):
        self.myTankImgSrcTuple = myTankImgSrcTuple = ('images/p1tankU.gif', 'images/p1tankD.gif',
                                                      'images/p1tankL.gif', 'images/p1tankR.gif')
        super().__init__(self.myTankImgSrcTuple, window_size)

    def move(self, direction='U') -> None:
        self.direction = direction  # 更新坦克方向
        self.oldTop = self.rect.top
        self.oldLeft = self.rect.left

        if direction == 'U':
            self.tankImg = self.tankImg_U  # 坦克向上
            if self.rect.top > 0:  # 坦克在屏幕内
                self.rect.top -= self.step  # 坦克向上移动
                if self.rect.top < 0:
                    self.rect.top = 0
        elif direction == 'D':
            self.tankImg = self.tankImg_D
            if self.rect.top <= self.window_size[1] - self.tankImg_D.get_height() - 4:  # 坦克在屏幕内
                self.rect.top += self.step
        elif direction == 'L':
            self.tankImg = self.tankImg_L
            if self.rect.left >= 0:
                self.rect.left -= self.step
                if self.rect.left < 0:
                    self.rect.left = 0
        elif direction == 'R':
            self.tankImg = self.tankImg_R
            if self.rect.left <= self.window_size[0] - self.tankImg_R.get_width() - 4:
                self.rect.left += self.step

    def myTank_into_enemyTank(self):
        pass
