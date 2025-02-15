import heapq
from typing import List
import heapq


def calc(seq: List[int], k: int) -> int:
    n = len(seq)
    h = []
    for i in range(n):
        if len(h) >= k:
            if h[0] < seq[i]:
                heapq.heappop(h)
        if len(h) < k:
            heapq.heappush(h, seq[i])
    print(f'{len(h)} {h}')
    return sum(h)


if __name__ == '__main__':
    print(hash('abc'))
    print(hash(''.join(sorted(list('abc')))))
    print(hash('bca'))
    print(hash('abc'))
