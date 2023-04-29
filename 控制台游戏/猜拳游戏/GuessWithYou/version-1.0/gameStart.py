from person import Person
from computer import Computer


class Game(object):
    count = 0

    def __init__(self, person, computer):
        self.person = person
        self.computer = computer

    def welcome(self):
        content = """----------------欢迎来到猜拳游戏---------------
            规则是：1.剪刀 2.石头 3.布
===========================================\n
        """
        print(content)

    def start(self):
        self.welcome()  # 展示欢迎语
        self.gameSetting()  # 做一些游戏的设置

        onGame = input("是否开始游戏？(y/n)").strip()
        while onGame.lower() == "y":
            # 开始游戏
            personFist = self.person.guessFist()  # 用户出拳
            while personFist == "错误":  # 如果用户出拳错误，重新出拳
                print("输入错误，请重新出拳！")
                personFist = self.person.guessFist()

            computerFist = self.computer.guessFist()  # 电脑出拳
            self.count += 1  # 对战次数加1
            self.getResult(personFist, computerFist)  # 获取结果
            onGame = input("是否继续游戏？(y/n)").strip()  # 是否继续游戏

        print(f"\n游戏结束，游戏局数：{self.count}")
        print("happy every day！")

    def gameSetting(self):
        self.person.name = input("请输入您的大名：").strip()
        choose = input("请选择对方角色(1.Tomboy 2.小妹 3.小弟)：").strip()
        if choose == "1":
            self.computer.name = "Tomboy"
        elif choose == "2":
            self.computer.name = "小妹"
        elif choose == "3":
            self.computer.name = "小弟"
        else:
            print("选择错误，已为您选择默认角色：幺叔")
            self.computer.name = "幺叔"

        if choose == "1" or choose == "2" or choose == "3":
            print(f">>> 您选择了{self.computer.name}和你PK！！")

    def getResult(self, personFist, computerFist):
        if personFist == computerFist:
            self.showResult("平局", personFist, computerFist)
        elif (personFist == "剪刀" and computerFist == "石头") or (personFist == "石头" and computerFist == "布") \
                or (personFist == "布" and computerFist == "剪刀"):

            self.computer.score += 1
            self.showResult("失败", personFist, computerFist)
        elif (personFist == '剪刀' and computerFist == "布") or (personFist == "石头" and computerFist == "剪刀") \
                or (personFist == "布" and computerFist == "石头"):

            self.person.score += 1
            self.showResult("胜利", personFist, computerFist)

    def showResult(self, result, personFist, computerFist):
        print("\n==========================对战结果==========================")
        # if result == "平局":
        #     print("==========================平局！==========================")
        # elif result == "胜利":
        #     print(f"=========================={self.person.name}-胜利！==========================")
        # elif result == "失败":
        #     print(f"=========================={self.computer.name}-胜利！==========================")

        print("玩家出拳：", personFist)
        print(f"电脑-{self.computer.name}出拳：", computerFist)
        print(f"{self.person.name} VS {self.computer.name}：<<<{result}>>>")
        print(f"对战次数：{self.count}")
        print(f"比分：{self.person.name}：{self.person.score}，{self.computer.name}：{self.computer.score}\n")
        if self.person.score < self.computer.score:
            print(f"玩家-{self.person.name}落后了，加油哦")
        elif self.person.score == self.computer.score:
            print("暂时平分秋色，玩家加油哦！")
        else:
            print(f"玩家-{self.person.name}处于领先位置，继续保持")
        print(f"<<<<<<<<<<<<<<<<<<<<<<<< {self.person.name}-{result}！ >>>>>>>>>>>>>>>>>>>>>>>>\n")


if __name__ == '__main__':
    person = Person("Tomboy", 0)
    computer = Computer("长空&无名", 0)
    game = Game(person, computer)
    game.start()
