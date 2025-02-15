import math


# Medium difficulty question
# 1: Using the Python language, have the function PrimeTime(num) take the num parameter being passed and return the string true
# if the parameter is a prime number,
# otherwise return the string false.
# The range will be between 1 and 2^16.


def is_prime(x: int) -> str:
    if x <= 1:
        return str(False)
    if x <= 3:
        return str(True)
    if x % 2 == 0 or x % 3 == 0:
        return str(False)
    max_divisor = math.isqrt(x)
    for i in range(5, max_divisor+1, 6):
        if x % i == 0 or x% (i+2) == 0:
            return str(False)
    return str(True)



def is_correct(s: str) -> bool:
    if not s or len(s) == 1:
        return False
    n = len(s)
    left_plus, letter_seen = False, False

    def is_letter(s: str) -> bool:
        return s[i] != '+' and s[i] != '='
    for i in range(n):
        if is_letter(s):
            if not left_plus:
                return False
            letter_seen = True
        if s[i] == '+':
            if letter_seen:
                letter_seen = False
            else:
                left_plus = True
        if s[i] == '=':
            if letter_seen:
                return False
            left_plus = False
    return True if not letter_seen else False


def capitalize_words(s: str) -> str:
    return s.title()

def process(s: str) -> str:
    alpha_map = {
        'c': 'd',
        'z': 'a',
    }
    vowels = {'a', 'e', 'i', 'o', 'u'}
    if not s:
        return s
    n = len(s)
    result = ['']*n
    for i in range(n):
        if s[i] in vowels:
            result[i] = s[i].capitalize()
        elif s[i] in alpha_map:
            result[i] = alpha_map[s[i]]
            if result[i] in vowels:
                result[i] = result[i].capitalize()
        else:
            result[i] = s[i]
    return ''.join(result)


def simple_add(k: int):
    return sum(x for x in range(1, k+1))


if __name__ == '__main__':
    # examples = ['++d+===+c++==a', 'a+', '+a', '+a+', '+a=+a+', '+a+=a', '+vb+===+n+a']
    # for s in examples:
    #     print(is_correct(s))

    nums = [2, 3, 5, 6, 7, 9, 13, 21, 27, 121, 123]
    for n in nums:
        print(f'{n} {is_prime(n)}')

