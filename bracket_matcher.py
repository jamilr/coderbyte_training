def bracket_matcher(s: str) -> int:
    if not s:
        return 0
    count, n = 0, len(s)
    for i in range(n):
        if s[i] not in {'(', ')'}:
            continue
        if s[i] == '(':
            count += 1
        else:
            if count == 0:
                return 0
            count -= 1
    return int(count == 0)


if __name__ == '__main__':
    examples = [
        '(hello (world))',
        '((helo (world))',
        '(good ((morning))',
        'good morning))'
    ]
    for s in examples:
        print(f'{s} = {bracket_matcher(s)}')
