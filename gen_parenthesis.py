def calc(n: int) -> int:
    count = 0

    def gen(s: str, opened: int, closed: int):
        nonlocal n, count
        if len(s) == n*2:
            count += 1
            return
        if opened < n:
            gen(s+'(', opened+1, closed)
        if closed < opened:
            gen(s+')', opened, closed+1)

    gen('',0, 0)
    return count


if __name__ == '__main__':
    t = [2, 3, 4, 5]
    for x in t:
        print(f'{calc(x)}')
