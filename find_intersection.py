from typing import List, Any


def find(seqs: List[str]) -> Any:
    def to_list(seq: str) -> List[int]:
        return [int(el) for el in seq.replace(',', '').split(' ')]
    def intersection(seqs: List[str]) -> str:
        int_seqs = [to_list(seqs[i]) for i in range(2)]
        i, j = 0, 0
        common = list()
        while i < len(int_seqs[0]) and j < len(int_seqs[1]):
            if int_seqs[0][i] == int_seqs[1][j]:
                common.append(str(int_seqs[0][i]))
                i += 1
                j += 1
            elif int_seqs[0][i] < int_seqs[1][j]:
                i += 1
            else:
                j += 1
        return ','.join(common)
    res = intersection(seqs)
    return 'false' if not res else res


if __name__ == '__main__':
    seqs = [
        ["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"],
        ["1, 3, 4, 7", "2, 6, 8, 10"]
    ]
    for e in seqs:
        print(find(e))

