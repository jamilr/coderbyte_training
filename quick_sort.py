from typing import List


def quick_sort(input_arr: List[int]):
    if not input_arr or len(input_arr) == 1:
        return
    n = len(input_arr)

    def _quick_sort(begin: int, end: int):
        nonlocal input_arr
        if begin >= end:
            return
        left, right = begin, end
        pivot = left + (right - left) // 2
        while left < right:
            while left < right and input_arr[left] < input_arr[pivot]:
                left += 1
            while left < right and input_arr[right] > input_arr[pivot]:
                right -= 1
            if left < right:
                input_arr[left], input_arr[right] = input_arr[right], input_arr[left]
                if input_arr[left] == input_arr[pivot]:
                    left += 1
        _quick_sort(begin, left-1)
        _quick_sort(left+1, end)
    _quick_sort(0, n-1)


if __name__ == '__main__':
    a = [1, 3, 2, 7, 5, 15, 12]
    quick_sort(a)
    print(f'A = {a}')
