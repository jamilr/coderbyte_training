import string
from collections import defaultdict
from typing import Any, Dict
import re
def letter_count(sentence: str) -> Any:

    def hist(s: str) -> Dict[str, int]:
        hist_dict = defaultdict(int)
        n = len(s)
        for i in range(n):
            hist_dict[s[i]] += 1
        print(hist_dict)
        return hist_dict

    max_repeated_letters = 0
    result = None
    pattern = f'[{string.punctuation}]'
    words = re.sub(pattern, "", sentence).split(' ')
    print(f'{words} {type(words)}')
    for word in words:
        word_hist = hist(word)
        reps = 0
        for letter, count in word_hist.items():
            reps += (1 if count > 1 else 0)
        if reps > max_repeated_letters:
            max_repeated_letters = reps
            result = word
    if max_repeated_letters > 1:
        return result
    return -1


if __name__ == '__main__':
    s = "Today, is the greatest day ever!"
    print(letter_count(s))

