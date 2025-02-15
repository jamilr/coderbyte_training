import collections
from typing import List


def element_merger(seq: List[int]) -> int:
    n = len(seq)
    q = collections.deque([])
    for i in range(1, n):
        q.append(abs(seq[i]-seq[i-1]))
    while len(q) > 1:
        m = len(q)
        for j in range(1, m):
            q.append(abs(q[j-1]-q[j]))
            q.popleft()
        q.popleft()
    return q[0] if q else -1


if __name__ == '__main__':
    seqs = [
        [4, 5, 1, 2, 7],
        [5, 7, 16, 1, 2],
        [1,1,1,2]
    ]
    for seq in seqs:
        print(element_merger(seq))

