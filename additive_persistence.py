def calc(n: int) -> int:
    if n % 10 == 0:
        return 0
    count = 0
    while n > 0 and n // 10 != 0:
        t = 0
        while n != 0:
            n, d = divmod(n, 10)
            t += d
        count += 1
        n = t
        print(n)
    return count


if __name__ == '__main__':
    e = [2718, 19]
    for x in e:
        print(f'x = {x} calc({x}) = {calc(x)}')