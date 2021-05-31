from collections import defaultdict

hash_table = defaultdict(list)


def hash_func(word, m):
    _sum = 0
    p = 1_000_000_007
    x = 263
    for i, c in enumerate(word):
        # print(ord(c))
        _sum += ord(c) * x**i
    _sum %= p
    _sum %= m
    return _sum


def main():
    m = int(input())
    n = int(input())
    for _ in range(n):
        command, entry = input().split()
        if command == 'add':
            key = hash_func(entry, m)
            if entry not in hash_table[key]:
                hash_table[key].insert(0, entry)
        elif command == 'del':
            key = hash_func(entry, m)
            if entry in hash_table[key]:
                hash_table[key].remove(entry)
        elif command == 'find':
            key = hash_func(entry, m)
            if entry in hash_table[key]:
                print('yes')
            else:
                print('no')
        elif command == 'check':
            print(' '.join(hash_table[int(entry)]))


if __name__ == "__main__":
    main()
