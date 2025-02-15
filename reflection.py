class Calc(object):
    def __init__(self, n):
        self._n = n

    # @property
    # def n(self):
    #     return self._n

    def inc(self):
        self._n += 1

    def double(self):
        self._n *= 2


if __name__ == '__main__':
    calc = Calc(4)
    for m in dir(calc):
        print(f'{m}')
        if 'class' in m:
            continue
        mthd = getattr(calc, m)
        print(f'{mthd}')
        if callable(mthd):
            mthd()

    print(calc)

