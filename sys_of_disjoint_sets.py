_max = 0


def make_set(i, parent, rank):
    parent[i] = i
    rank[i] = 0


def find(i, parent):
    if i != parent[i]:
        parent[i] = find(parent[i], parent)
    return parent[i]


def union(dest, source, parent, rank):
    global _max
    d_parent = find(dest, parent)
    s_parent = find(source, parent)

    if d_parent != s_parent:
        parent[s_parent] = d_parent
        rank[d_parent] += rank[s_parent]
        _max = max(_max, rank[d_parent])
    return _max


def main():
    global _max

    n, m = map(int, input().split())    # число таблиц, число запросов
    parent = [i for i in range(n)]
    rank = list(map(int, input().split()))
    _max = max(rank)

    for _ in range(m):
        dest, source = map(int, input().split())
        print(union(dest - 1, source - 1, parent, rank))


if __name__ == '__main__':
    main()

'''
4 5
1 1 1 1
2 1
4 2
4 1
3 1
4 3

'''