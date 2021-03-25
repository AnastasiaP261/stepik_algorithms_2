from collections import deque


def counting_braces(s):
    stack = deque([])
    braces = {'(': ')', '[': ']', '{': '}'}

    for i, ch in enumerate(s, 1):
        if ch in braces.keys():
            stack.append((ch, i))
        elif ch in braces.values():
            if not stack:
                return i
            elif ch == braces[stack[-1][0]]:
                stack.pop()
            else:
                return i

    if not stack:
        return 0
    return stack[-1][1]


def main():
    s = input()

    answer = counting_braces(s)
    if answer == 0:
        print('Success')
    else:
        print(answer)
    
    
def test():
    assert counting_braces("([](){([])})") == 0
    assert counting_braces("()[]}") == 5
    assert counting_braces("{{[()]]") == 7
    assert counting_braces("{{{[][][]") == 3
    assert counting_braces("{*{{}") == 3
    assert counting_braces("[[*") == 2
    assert counting_braces("{*}") == 0
    assert counting_braces("{{") == 2
    assert counting_braces("{}") == 0
    assert counting_braces("") == 0
    assert counting_braces("}") == 1
    assert counting_braces("*{}") == 0
    assert counting_braces("{{{**[][][]") == 3


if __name__ == '__main__':
    main()