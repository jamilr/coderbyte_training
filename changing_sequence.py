from typing import List


def changing_sequence(seq: List[int]) -> int:
    n = len(seq)
    prev_diff = None
    i = 1
    while i < n:
        diff = 1 if (seq[i] - seq[i-1]) > 0 else -1
        if prev_diff is None:
            prev_diff = diff
        elif diff != prev_diff:
            return i-1
        i += 1
    return -1


if __name__ == '__main__':
    seqs = [
            [1, 2, 4, 6, 4, 3, 1],
            [-4, -2, 9, 10],
            [5, 4, 3, 2, 10, 11]
        ]
    for s in seqs:
        print(changing_sequence(s))


