from pygame.mixer import music


class Sound(object):
    def __init__(self):
        self.fireSound_path = 'gameSound/fire.wav'
        self.hitSound_path = 'gameSound/hit.wav'
        self.gameSound_path = 'gameSound/gameSound.wav'
        self.type = 'wav'

    def playFirSound(self):
        music.load(filename=self.fireSound_path, namehint=self.type)
        music.play()

    def playHitSound(self):
        music.load(filename=self.hitSound_path, namehint=self.type)
        music.play()

    def playGameSound(self, play_pos):
        music.load(filename=self.gameSound_path, namehint=self.type)
        music.play()
        music.set_pos(play_pos)


if __name__ == "__main__":
    import pygame

    pygame.init()
    screen = pygame.display.set_mode((600, 900))
    sound = Sound()
    running = True
    pygame.mixer.music.set_volume(0.8)
    pos = 0.0

    while running:
        if not pygame.mixer.music.get_busy():
            print(pos)
            sound.playGameSound(play_pos=pos)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # 点击窗口的关闭按钮，窗口关闭
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    pos = pygame.mixer.music.get_pos() / 1000
                    print('--', pos)
                    sound.playFirSound()
                if event.key == pygame.K_2:
                    sound.playHitSound()
