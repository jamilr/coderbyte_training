class Person:
    __slots__ = ['name', 'last_name', 'address']

    def __init__(self, name_val: str, last_name_val: str, address_val: str):
        self.name = name_val
        self.last_name = last_name_val
        self.address = address_val

    def __str__(self):
        return f'Person.name={self.name}, last_name={self.last_name}, address={self.address}'


if __name__ == '__main__':
    p = Person('Alex', 'Max', 'SW1X 9AB')
    delattr(p, 'address')
    print(p)