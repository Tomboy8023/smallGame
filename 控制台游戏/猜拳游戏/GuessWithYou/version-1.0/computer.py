from random import randint


class Computer(object):
    def __init__(self, name, score=0):
        self.name = name
        self.score = score

    def guessFist(self):
        computerFist = randint(1, 3)
        if computerFist == 1:
            return "剪刀"
        elif computerFist == 2:
            return "石头"
        elif computerFist == 3:
            return "布"
        else:
            return "错误"


if __name__ == "__main__":
    computer = Computer("幺叔", 0)
    print(computer.guessFist())
