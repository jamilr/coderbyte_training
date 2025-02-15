from typing import List, Any


def calc(seq: List[int]) -> Any:
    if len(seq) < 3:
        return -1

    additive_shift = seq[1]-seq[0]
    multiplicative_shift = seq[1]/seq[0]

    n, arithmetic, geometric, = len(seq), False, False
    for i in range(1, n):
        arithmetic = (seq[i] == seq[i-1] + additive_shift)
        geometric = (seq[i] == seq[i-1]*multiplicative_shift)
        if not arithmetic and not geometric:
            return -1
    return 'airthmetic' if arithmetic else 'geometric'


if __name__ == '__main__':
    seqs = [
        [5, 10, 15],
        [2, 6, 18, 54],
        [2, 6, 9, 11],
        [-2, 2, 6],
        [-2, 4, -8, 16]
    ]
    for seq in seqs:
        print(f'S={seq} seq={calc(seq)}')
