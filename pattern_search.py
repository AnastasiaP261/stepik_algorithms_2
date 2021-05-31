x = 29
p = 999_999_000_001


def hash_func(word):
    _sum = 0
    i = 0
    for i, c in enumerate(word):
        _sum += ord(c) * pow(x, i, p)
    _sum %= p
    return _sum, ord(word[-1]) * pow(x, i, p)


def main():
    pattern = input()
    pattern_key = hash_func(pattern)[0]

    text = input()
    win_prev = text[-len(pattern):]
    win_prev_key, monom_prev = hash_func(win_prev)

    answer = []
    i = -1
    pow_p = pow(x, len(pattern) - 1, p)
    for i in range(-2, -(len(text) - len(pattern)) - 2, -1):
        if win_prev_key == pattern_key:
            answer.append(len(text) + i - len(pattern) + 2)

        win_prev_key = ((win_prev_key - monom_prev) * x + ord(text[i - len(pattern) + 1])) % p
        monom_prev = (ord(text[i]) * pow_p) % p
    else:
        if win_prev_key == pattern_key:
            answer.append(len(text) + i - len(pattern) + 1)

    answer.reverse()
    print(' '.join(map(str, list(answer))))


if __name__ == "__main__":
    main()