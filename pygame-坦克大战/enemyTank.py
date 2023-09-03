from tank import Tank
from random import randint


class EnemyTank(Tank):
    def __init__(self, window_size, x, y):
        self.enemyTankImgSrcTuple = enemyTankImgSrcTuple = ('images/enemy1U.gif', 'images/enemy1D.gif',
                                                            'images/enemy1L.gif', 'images/enemy1R.gif')
        super().__init__(self.enemyTankImgSrcTuple, window_size, x, y)
        self.steps = 100
        self.step = 3
        self.enemyTank_direction = self.random_direction()
        self.bulletList = []
        self.MAX_BULLET_NUMBER = 5  # 最大子弹数量

    def random_direction(self):
        randomNum = randint(1, 4)
        if randomNum == 1:
            return 'U'
        elif randomNum == 2:
            return 'D'
        elif randomNum == 3:
            return 'L'
        elif randomNum == 4:
            return 'R'

    def random_move(self):
        if self.steps < 0:
            self.steps = randint(60, 80)
            self.enemyTank_direction = self.random_direction()
        elif self.rect.left <= 0 or self.rect.left >= self.window_size[0] - 60 or self.rect.top <= 0 or self.rect.top >= self.window_size[1] - 60:
            self.steps = randint(60, 80)
            self.enemyTank_direction = self.random_direction()
        self.steps -= 1
        self.move(self.enemyTank_direction)

    def random_shot(self):
        randomNum = randint(0, 100)
        if randomNum < 2:
            return True
