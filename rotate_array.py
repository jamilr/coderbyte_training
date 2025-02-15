from typing import List


def rotate(seq: List[int]):
    n = len(seq)
    k = seq[0]
    for i in range(k):
        seq.append(seq[i])
    return ''.join([str(el) for el in seq[k:]])


if __name__ == '__main__':
    a = [4,3,4,3,1,2]
    print(a)
    print(rotate(a))