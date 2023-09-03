import random
import pygame
from myTank import MyTank
from enemyTank import EnemyTank
from wall import Wall
from gameSound import Sound
import settings

pygame.init()  # 初始化pygame
screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))  # 设置窗口大小
clock = pygame.time.Clock()  # 创建一个时钟对象，用于刷新屏幕显示

pygame.display.set_caption(settings.GAME_TITLE)  # 设置窗口标题
pygame.display.set_icon(pygame.image.load(settings.ICON_PATH))  # 设置窗口图标
"""窗口显示在屏幕正中央"""
"""窗口不允许缩小和放大"""
pygame.display.set_allow_screensaver(True)  # pygame运行时，不允许电脑的屏幕保护程序启动
pygame.mixer.music.set_volume(0.8)  # 设置音量大小

WINDOW_SIZE = pygame.display.get_window_size()  # 获取窗口大小
running = True  # 游戏状态，True表示游戏正在运行，False表示游戏结束
myTankGoUp = False  # 我方坦克是否自动向上移动
myTankGoDown = False  # 我方坦克是否自动向下移动
myTankGoLeft = False  # 我方坦克是否自动向左移动
myTankGoRight = False  # 我方坦克是否自动向右移动
wall_list = []  # 存储当前存在的墙壁
WALL_SPACE = (settings.WIDTH - settings.WALL_NUMBER * settings.WALL_HEIGHT) // (settings.WALL_NUMBER - 1)  # 墙壁之间的间隔
# 第一面墙和第二面墙之间 + 倒数第二面墙和倒数第一面墙之间的间隙：WALL_SPACE + WALL_ROUND
WALL_ROUND = (settings.WIDTH - (settings.WALL_NUMBER - 1) * WALL_SPACE - settings.WALL_NUMBER * settings.WALL_WIDTH) / 2
# 记录游戏音效的播放位置：实现功能：射击音效结束后，游戏音效继续播放而不是重新播放
music_pos = 0.0

sound = Sound()  # 创建游戏声音对象
myTank = MyTank(WINDOW_SIZE)  # 创建我方坦克
enemyTankList = []  # 敌方坦克数量

for i in range(0, settings.WALL_NUMBER):  # 上面的墙体
    wall = Wall(i * (settings.WALL_WIDTH + WALL_SPACE), settings.HEIGHT / 4 - settings.WALL_HEIGHT / 2)
    wall_list.append(wall)

for i in range(0, settings.WALL_NUMBER):  # 下面的墙体
    wall = Wall(i * (settings.WALL_WIDTH + WALL_SPACE), (3 / 4) * settings.HEIGHT - settings.WALL_HEIGHT / 2)
    wall_list.append(wall)

wall_rect_list = []  # 存放墙壁的Rect实例对象
for wall in wall_list:
    wall_rect = pygame.Rect(wall.rect.left, wall.rect.top, wall.width, wall.height)
    wall_rect_list.append(wall_rect)

myTank_rect = pygame.Rect(myTank.rect.left, myTank.rect.top, myTank.width, myTank.height)  # 我方坦克的Rect实例对象

flag = False  # 代表是否需要重新循环生成敌方坦克
"""
此处有BUG，敌方坦克数量足够多时，会出现，敌方坦克压着墙壁，敌方坦克超出屏幕边界，敌方坦克互相重叠的情况
"""
while len(enemyTankList) <= settings.ENEMY_TANK_NUMBER:  # 生成敌方坦克
    enemyTank_x = random.randint(0, WINDOW_SIZE[0] - 60)
    enemyTank_y = random.randint(0, WINDOW_SIZE[1] - 60)
    enemy_rect = pygame.Rect(enemyTank_x, enemyTank_y, settings.ENEMY_TANK_WIDTH, settings.ENEMY_TANK_HEIGHT)
    for wall_rect in wall_rect_list:
        if enemy_rect.colliderect(wall_rect):
            enemyTank_x = random.randint(0, WINDOW_SIZE[0])
            enemyTank_y = random.randint(0, WINDOW_SIZE[1])
            enemy_rect = pygame.Rect(enemyTank_x, enemyTank_y, settings.ENEMY_TANK_WIDTH, settings.ENEMY_TANK_HEIGHT)
            flag = True
            break
    else:
        flag = False

    if flag:
        continue

    for enemyTank in enemyTankList:
        enemyTank_rect = pygame.Rect(enemyTank.rect.top, enemyTank.rect.left, settings.ENEMY_TANK_WIDTH, settings.ENEMY_TANK_HEIGHT)
        if enemy_rect.colliderect(enemyTank_rect):
            enemyTank_x = random.randint(0, WINDOW_SIZE[0])
            enemyTank_y = random.randint(0, WINDOW_SIZE[1])
            enemy_rect = pygame.Rect(enemyTank_x, enemyTank_y, settings.ENEMY_TANK_WIDTH, settings.ENEMY_TANK_HEIGHT)
            flag = True
            break
    else:
        flag = False

    if flag:
        continue

    if enemy_rect.colliderect(myTank_rect):
        enemyTank_x = random.randint(0, WINDOW_SIZE[0])
        enemyTank_y = random.randint(0, WINDOW_SIZE[1])
        enemy_rect = pygame.Rect(enemyTank_x, enemyTank_y, settings.ENEMY_TANK_WIDTH, settings.ENEMY_TANK_HEIGHT)

    enemyTank = EnemyTank(WINDOW_SIZE, enemyTank_x, enemyTank_y)
    enemyTankList.append(enemyTank)


while running:
    # for enemyTank in  enemyTankList:
    #     enemyTank.tank_into_wall()
    if not pygame.mixer.music.get_busy():
        sound.playGameSound(play_pos=music_pos)
    for event in pygame.event.get():  # 事件监听，如果有事件发生，获取事件
        if event.type == pygame.QUIT:  # 点击窗口的关闭按钮，窗口关闭
            running = False
        elif event.type == pygame.KEYDOWN:  # 键盘有按下
            if event.key == pygame.K_ESCAPE:  # 按下的是ESC键，游戏结束
                running = False
            if event.key == pygame.K_SPACE:  # 按下的是空格键，发射子弹
                if len(myTank.bulletList) < 10:
                    myTank.fire(screen)
                    music_pos = pygame.mixer.music.get_pos() / 1000
                    sound.playFirSound()
            elif event.key == pygame.K_UP:  # 按下的是上方向键
                myTank.move("U")
                myTankGoUp = True
            elif event.key == pygame.K_DOWN:  # 按下的是下方向键
                myTank.move("D")
                myTankGoDown = True
            elif event.key == pygame.K_LEFT:  # 按下的是左方向键
                myTank.move("L")
                myTankGoLeft = True
            elif event.key == pygame.K_RIGHT:  # 按下的是右方向键
                myTank.move("R")
                myTankGoRight = True
        elif event.type == pygame.KEYUP:  # 键盘有抬起
            if event.key == pygame.K_UP:  # 抬起的是上方向键
                myTankGoUp = False
            elif event.key == pygame.K_DOWN:  # 抬起的是下方向键
                myTankGoDown = False
            elif event.key == pygame.K_LEFT:  # 抬起的是左方向键
                myTankGoLeft = False
            elif event.key == pygame.K_RIGHT:  # 抬起的是右方向键
                myTankGoRight = False

    if myTankGoUp:
        myTank.move("U")
    elif myTankGoDown:
        myTank.move("D")
    elif myTankGoLeft:
        myTank.move("L")
    elif myTankGoRight:
        myTank.move("R")

    screen.fill("#d8c5c5")  # 设置窗口的背景色

    myTank.display(screen)  # 绘制我方坦克

    for wall in wall_list:  # 绘制墙壁
        wall.display(screen)

    for enemyTank in enemyTankList:
        """敌方坦克的移动还不太满意，需要优化"""
        enemyTank.random_move()
        shot_flag = enemyTank.random_shot()
        """敌方坦克的随机射击需要重新设计"""
        if shot_flag and len(enemyTank.bulletList) < enemyTank.MAX_BULLET_NUMBER:
            enemyTank.fire(screen)
            # music_pos = pygame.mixer.music.get_pos() / 1000
            # sound.playHitSound()
            shot_flag = False
        enemyTank.display(screen)

    for bullet in myTank.bulletList:  # 绘制我方坦克子弹
        bullet.move()
        bullet.drop(myTank.bulletList)
        bullet.display(screen)

    for enemyTank in enemyTankList:  # 绘制敌方坦克发射的子弹
        for bullet in enemyTank.bulletList:
            bullet.move()
            bullet.drop(enemyTank.bulletList)
            bullet.display(screen)

    # pygame.display.update()  # 将绘制更新到屏幕上

    pygame.display.flip()  # 将完整显示的 Surface 更新到屏幕

    clock.tick(60)  # limits FPS to 60

pygame.quit()  # 退出pygame
print("游戏结束，谢谢使用！")
