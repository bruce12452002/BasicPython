class Animal:
    def move(self):
        print("---")


class Dragon(Animal):
    pass


class Snack(Dragon):
    def move(self)
        print("crawl")


def start(a: Animal):
    a.move()


start(Dragon())
start(Snack())

# 父类的方法，子类如果有，就用，没有就一层一层往上找，所以父类一定要有方法
