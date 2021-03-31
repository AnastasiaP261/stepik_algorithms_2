def to_put(q, num):
    if not q or q[-1][1] <= num:
        q.append([num, num])
    else:
        q.append([num, q[-1][1]])


def to_shift(q1, q2):
    for i in range(len(q1)):
        to_put(q2, q1.pop()[0])


def search_max_in_win(win_size, nums):
    q1 = []
    q2 = []
    answer = []

    for i in range(len(nums)):
        if len(q1) < win_size:
            to_put(q1, nums[i])

        if len(q1) == win_size:
            to_shift(q1, q2)
            answer.append(q2.pop()[1])
        elif q2:
            answer.append(max(q1[-1][1], q2[-1][1]))
            q2.pop()

    return answer


def main():
    n = int(input())
    nums = list(map(int, input().split()))
    win_size = int(input())

    print(' '.join(map(str, search_max_in_win(win_size, nums))))


def test():
    assert search_max_in_win(4, [2, 7, 3, 1, 5, 2, 6, 2]) == [7, 7, 5, 6, 6], 'test 1'
    assert search_max_in_win(1, [2, 1, 5]) == [2, 1, 5], 'test 2'
    assert search_max_in_win(7, [73, 65, 24, 14, 44, 20, 65, 97, 27, 6, 42, 1, 6, 41, 16]) == [73, 97, 97, 97, 97, 97, 97, 97, 42], 'test 3'
    assert search_max_in_win(12, [28, 7, 64, 40, 68, 86, 80, 93, 4, 53, 32, 56, 68, 18, 59]) == [93, 93, 93, 93], 'test 4'
    assert search_max_in_win(12, [16, 79, 20, 19, 43, 72, 78, 33, 40, 52, 70, 79, 66, 43, 60]) == [79, 79, 79, 79], 'test 5'
    assert search_max_in_win(3, [34, 51, 61, 90, 26, 84, 2, 25, 7, 8, 25, 78, 21, 47, 25]) == [61, 90, 90, 90, 84, 84, 25, 25, 25, 78, 78, 78, 47], 'test 6'
    assert search_max_in_win(5, [27, 83, 29, 77, 6, 3, 48, 2, 16, 72, 46, 38, 55, 2, 58]) == [83, 83, 77, 77, 48, 72, 72, 72, 72, 72, 58], 'test 7'
    assert search_max_in_win(4, [1, 4, 5, 6, 1, 1, 1, 1]) == [6, 6, 6, 6, 1], 'test 8'


if __name__ == '__main__':
    test()