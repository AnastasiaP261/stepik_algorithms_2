from math import floor
from sys import stdin, stdout
exchanges = []


class Heap:
    def __init__(self, arr):
        self.heap = arr

    def parent(self, i):
        return floor((i - 1) / 2)

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def sift_down(self, i, stack):
        max_i = i
        l = self.left_child(i)
        if l < len(self.heap) and self.heap[l] < self.heap[max_i]:
            max_i = l
        r = self.right_child(i)
        if r < len(self.heap) and self.heap[r] < self.heap[max_i]:
            max_i = r

        if i != max_i:
            exchanges.append([i, max_i])
            self.heap[i], self.heap[max_i] = self.heap[max_i], self.heap[i]
            self.sift_down(max_i, stack)


def build_heap(n, arr):
    arr = Heap(arr)
    for i in range(n // 2 - 1, -1, -1):
        stack = []
        arr.sift_down(i, stack)


def main():
    n = int(stdin.readline())
    arr = list(map(int, stdin.readline().split()))

    build_heap(n, arr)
    stdout.write(str(len(exchanges)) + '\n')
    if exchanges:
        stdout.write('\n'.join(map(lambda x: f'{x[0]} {x[1]}', exchanges)))


if __name__ == '__main__':
    main()