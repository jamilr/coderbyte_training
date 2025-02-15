def even_pairs(s: str) -> bool:
    if not s:
        return False
    n = len(s)
    even_count = 0
    for i in range(n):
        if not ('0' <= s[i] <= '9'):
            even_count = 0
            continue
        if (ord(s[i]) - ord('0')) % 2 == 0:
            even_count += 1
        if even_count == 2:
            return True
    return False


if __name__ == '__main__':
    e = ['3gy41d216', 'f09r27i8e67', '7r5gg812', 'f178svg3k19k46']
    for s in e:
        print(f's={s} {even_pairs(s)}')