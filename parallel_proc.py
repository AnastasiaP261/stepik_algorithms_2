import heapq


def main():
    n, m = map(int, input().split())
    processors = []
    for i in range(n):
        heapq.heappush(processors, [0, i])

    for task_time in map(int, input().split()):
        proc = heapq.heappop(processors)
        print(f'{proc[1]} {proc[0]}')
        heapq.heappush(processors, [proc[0] + task_time, proc[1]])


if __name__ == '__main__':
    main()