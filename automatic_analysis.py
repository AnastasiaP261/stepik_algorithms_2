def find(i, parent):
    if i != parent[i]:
        parent[i] = find(parent[i], parent)
    return parent[i]


def union(i, j, parent, rank):
    i_parent = find(i, parent)
    j_parent = find(j, parent)

    if i_parent == j_parent:
        return
    if rank[i_parent] > rank[j_parent]:
        parent[j_parent] = i_parent
    else:
        parent[i_parent] = j_parent
        if rank[i_parent] == rank[j_parent]:
            rank[j_parent] += 1


def main():
    n, e, d = map(int, input().split())  # число переменных, кол-во равенств, кол-во неравенств
    parents = [i for i in range(n)]
    rank = [1 for _ in range(n)]

    code = 1
    if e != 0:
        for i in range(e):
            n1, n2 = map(int, input().split())
            union(n1 - 1, n2 - 1, parents, rank)

    if d != 0:
        for i in range(d):
            n1, n2 = map(int, input().split())
            if find(n1 - 1, parents) == find(n2 - 1, parents):
                code = 0

    print(code)


if __name__ == '__main__':
    main()

'''
4 6 1
1 2
1 3
1 4
2 3
2 4
3 4
1 2

'''