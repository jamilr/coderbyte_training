class Capable(object):
    def __init__(self, name: str):
        self._name = name

    def move(self):
        print(f'{self.__class__} is moving')


class CanWalk(Capable):
    def __init__(self, name: str):
        super().__init__(name)

    def move(self):
        print(f'{self.__class__} is moving')
        super().move()


class CanFly(Capable):
    def __init__(self, name: str):
        super().__init__(name)

    def move(self):
        print(f'{self.__class__} is flying')
        super().move()


class CanWalkAndFly(CanWalk, CanFly):
    def __init__(self, name: str):
        super().__init__(name)

    def move(self):
        print(f'{self.__class__} is walking and flying')
        super().move()


if __name__ == '__main__':
    capable = Capable('A')
    can_walk = CanWalk('B')
    can_fly = CanFly('C')
    walk_and_fly = CanWalkAndFly('D')
    print(f'{CanWalkAndFly.__mro__}')

