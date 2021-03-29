import re
from sys import stdin, stdout


def proc_stack_command(com, stack):
    if re.match(r'push', com):
        v1 = int(com.split()[-1])
        if len(stack) == 0 or v1 > stack[-1][1]:
            v2 = v1
        else:
            v2 = stack[-1][1]
        stack.append([v1, v2])
    elif re.match(r'pop$', com):
        if stack:
            stack.pop()
    elif re.match(r'max$', com):
        if stack:
            return stack[-1][1]
        return 0


def main():
    n = int(stdin.readline())

    stack = []
    for _ in range(n):
        answ = proc_stack_command(stdin.readline(), stack)
        if type(answ) == int:
            stdout.write(str(answ) + '\n')


if __name__ == '__main__':
    main()