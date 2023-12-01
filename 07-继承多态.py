class Animal:
    def __init__(self, color, cry):
        self.color = color
        self.cry = cry

    def crys(self):
        print("颜色:", self.color)
        print("叫声:", self.cry)


class Fish(Animal):
    def __init__(self, color, cry, fishtail):
        super().__init__(color, cry)
        self.fishtail = fishtail

    def crys(self):
        super().crys()
        print("鱼尾:", self.fishtail)


if __name__ == '__main__':
    Animal = Animal("棕色", "汪汪 ....")
    print("-------拉布拉多------")
    Animal.crys()

    Fish = Fish("灰褐色", "哇哇 .....", "扇子形")
    print("--------娃娃鱼-------")
    Fish.crys()
