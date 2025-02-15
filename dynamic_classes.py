class Fruit(object):
    def __init__(self):
        pass

    def __str__(self):
        return 'Fruit'


class Apple(Fruit):
    def __init__(self):
        pass


if __name__ == '__main__':
    redapple = type('RedApple', (Apple, ), {"size": 'big'})
    print(redapple)
