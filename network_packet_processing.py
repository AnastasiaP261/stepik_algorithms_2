from collections import deque


def processing(buf_size, packets):
    buffer = deque([], maxlen=buf_size)
    answer = []
    for i in range(buf_size):
        buffer.append(0)

    for pack in packets:
        if buffer[0] <= pack[0]:
            answer.append(max(buffer[-1], pack[0]))
            buffer.append(max(buffer[-1], pack[0]) + pack[1])
        else:
            answer.append(-1)

    print(answer)
    return answer


def main():
    buf_size, num_p = map(int, input().split())
    if num_p == 0:
        return
    packets = [list(map(int, input().split())) for _ in range(num_p)]

    print('\n'.join(map(str, processing(buf_size, packets))))


def test():
    format = lambda x1: list(map(lambda x2: list(map(int, x2.split())), x1.split('\n')))

    assert processing(2, format('''0 0
                                    0 0
                                    0 0
                                    1 0
                                    1 0
                                    1 1
                                    1 2
                                    1 3''')) == [0, 0, 0, 1, 1, 1, 2, -1], 'test1'
    assert processing(2, format('''0 0
                                    0 0
                                    0 0
                                    1 1
                                    1 0
                                    1 0
                                    1 2
                                    1 3''')) == [0, 0, 0, 1, 2, -1, -1, -1], 'test2'
    assert processing(1, format('''999999 1
                                    1000000 0
                                    1000000 1
                                    1000000 0
                                    1000000 0''')) == [999999, 1000000, 1000000, -1, -1], 'test3'
    assert processing(2, format('''1 100
                                    1 100 
                                    1 0''')) == [1, 101, -1], 'test5'
    assert processing(3, format('''0 7
                                    0 0
                                    2 0
                                    3 3
                                    4 0
                                    5 0''')) == [0, 7, 7, -1, -1, -1], 'test6'
    assert processing(2, format('''0 2
                                    0 0
                                    2 0
                                    3 0
                                    4 0
                                    5 0''')) == [0, 2, 2, 3, 4, 5], 'test7'
    assert processing(2, format('''2 9
                                    4 8
                                    10 9
                                    15 2
                                    19 1''')) == [2, 11, -1, 19, 21], 'test8'
    assert processing(3, format('''1 1
                                    2 2
                                    3 3
                                    4 4
                                    5 5
                                    6 6
                                    7 7
                                    8 8''')) == [1, 2, 4, 7, 11, -1, 16, -1], 'test9'


if __name__ == '__main__':
    test()
