from random import randint


class Person(object):
    def __init__(self, name, score=0):
        self.name = name
        self.score = score

    def guessFist(self):
        personFist = input(f"{self.name}出拳 ==> (1.剪刀 2.石头 3.布)：").strip()
        if personFist == "1":
            return "剪刀"
        elif personFist == "2":
            return "石头"
        elif personFist == "3":
            return "布"
        else:
            return "错误"


if __name__ == "__main__":
    person = Person("Tomboy", 0)
    print(person.guessFist())
