from typing import List


def calc(seq: List[int]) -> int:
    n = len(seq)
    i = 0
    while i < n and seq[i] != 1:
        i += 1
    if i == n:
        return -1
    j = i-1
    while j >= 0 and seq[j] != 2:
        j -= 1
    left_dist = abs(j-i)
    j = i + 1
    while j < n and seq[j] != 2:
        j += 1
    right_dist = abs(j-i)
    return min(left_dist, right_dist)


if __name__ == '__main__':
    a = [0, 0, 1, 0, 0, 2, 0, 2]
    print(f'enemy distance = {calc(a)}')