def transformation(parents_list, n):
    adj_list = [[] for _ in range(n)]
    root_index = -1

    for child, parent in enumerate(parents_list, 1):
        if parent != -1:
            adj_list[parent].append(child - 1)
        else:
            root_index = child - 1

    return adj_list, root_index


def calc(_list):
    _list, root = transformation(_list, len(_list))
    height = 1
    queue = []

    queue.extend(_list[root])
    if len(queue) == 0:
        return height
    else:
        queue.append(-1)                                # ограничитель уровня

    while queue:
        cur_peak = queue.pop(0)
        if cur_peak == -1:
            height += 1
            if queue: queue.append(-1)
        else:
            queue.extend(_list[cur_peak])

    print(height)
    return height


def main():
    n = int(input())
    print(calc(list(map(int, input().split()))))


def test():
    assert calc([5, 6, -1, 5, 5, 2, 0, 6, 2]) == 5
    assert calc([4, -1, 4, 1, 1]) == 3
    assert calc([-1, 0, 4, 0, 3]) == 4
    assert calc([9, 7, 5, 5, 2, 9, 9, 9, 2, -1]) == 4
    assert calc([2, 2, 3, 5, 5, 7, 7, 9, 9, -1]) == 6
    assert calc([-1]) == 1


if __name__ == '__main__':
    test()
