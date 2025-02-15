import collections


def array_addition(seq) -> str:
    max_val = max(seq)
    n = len(seq)
    q = collections.deque([])
    for i in range(n):
        if seq[i] == max_val:
            continue
        m = len(q)
        for j in range(m):
            q.append(q[j]+seq[i])
        q.append(seq[i])
    i = 0
    while i < len(q) and q[i] != max_val:
        i += 1
    return 'false' if i == len(q) else 'true'


if __name__ == '__main__':
    a = [4, 6, 23, 10, 1, 3]
    print(array_addition(a))

