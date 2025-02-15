import datetime
import sys
from typing import List


class Person(object):
    def __init__(self, first_name: str, last_name: str):
        self._firstname = first_name
        self._lastname = last_name

    def get_full_name(self):
        x = 10
        print(locals())
        return f'{self._firstname} {self._lastname}'


if __name__ == '__main__':
    print(sorted(['19', '2', '21', '18', '24']))


