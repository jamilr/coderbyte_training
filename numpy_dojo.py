import random

import numpy as np


def gen_synthetic_data():
    a = random.sample(range(pow(2, 9)), k=100)
    b = random.sample(range(pow(10, 9)), k=100)
    for ax, bx in zip(a, b):
        yield ax, bx


if __name__ == '__main__':

    for x, y in gen_synthetic_data():
        print(f'x={x} | y={y}')
