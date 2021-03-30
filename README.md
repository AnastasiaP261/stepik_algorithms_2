# Задачи с курса Stepik "Алгоритмы: Теория и практика. Структуры данных"
[Cсылка на курс](https://stepik.org/course/1547/info)

В этом репозитории я буду продолжать собирать решения задач со второй части курса по алгоритмам.


###  Статусы задач:
- 🟢 - задача решена и прошла все внутренние тесты платформы
- 🟡 - задача решена, но не все тесты платформы пройдены

### Другие обозначения:
- <kbd>file_name</kbd> - имя файла решения данной задачи

###  Содержание:
1. 🟢 [Расстановка скобок в коде](https://github.com/AnastasiaP261/stepik_alghoritms_2#%D1%80%D0%B0%D1%81%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BA%D0%B0-%D1%81%D0%BA%D0%BE%D0%B1%D0%BE%D0%BA-%D0%B2-%D0%BA%D0%BE%D0%B4%D0%B5)
    <kbd>brace_placement.py</kbd>
2. 🟢 [Высота дерева](https://github.com/AnastasiaP261/stepik_alghoritms_2#%D0%B2%D1%8B%D1%81%D0%BE%D1%82%D0%B0-%D0%B4%D0%B5%D1%80%D0%B5%D0%B2%D0%B0)
    <kbd>tree_height.py</kbd>
3. 🟢 [Симуляция обработки сетевых пакетов](https://github.com/AnastasiaP261/stepik_alghoritms_2#%D1%81%D0%B8%D0%BC%D1%83%D0%BB%D1%8F%D1%86%D0%B8%D1%8F-%D0%BE%D0%B1%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%BA%D0%B8-%D1%81%D0%B5%D1%82%D0%B5%D0%B2%D1%8B%D1%85-%D0%BF%D0%B0%D0%BA%D0%B5%D1%82%D0%BE%D0%B2)
    <kbd>network_packet_processing.py</kbd> 
4. 🟢 [Стек с поддержкой максимума](https://github.com/AnastasiaP261/stepik_alghoritms_2#%D1%81%D1%82%D0%B5%D0%BA-%D1%81-%D0%BF%D0%BE%D0%B4%D0%B4%D0%B5%D1%80%D0%B6%D0%BA%D0%BE%D0%B9-%D0%BC%D0%B0%D0%BA%D1%81%D0%B8%D0%BC%D1%83%D0%BC%D0%B0)
    <kbd>stack_with_max.py</kbd>    
   
## Расстановка скобок в коде
Постановка задачи:
>**Формат входа.** Строка _s[1..n]_, состоящая из заглавных и прописных букв латинского алфавита,
> цифр, знаков препинания и скобок из множества []{}().  
> **Формат выхода.** Если скобки в _s_ расставлены правильно, выведите
строку "Success". В противном случае выведите индекс (используя индексацию с единицы) 
> первой закрывающей скобки, для которой нет соответствующей открывающей. Если такой нет, 
> выведите индекс первой открывающей скобки, для которой нет соответствующей закрывающей.

Используем стэк для решения задачи.

Код:
``` python
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
```

## Высота дерева
Постановка задачи:
> **Формат входа.** Первая строка содержит натуральное число _1 ≤ n ≤ 10<sup>5</sup>_. Вторая строка содержит _n_ целых 
> чисел _parent<sub>0</sub>, ..., parent<sub>n−1</sub>_. Для каждого _0 ≤ i ≤ n−1_, _parenti_ — родитель вершины _i_; 
> если _parenti_ = _−1_, то _i_ является корнем. Гарантируется, что корень ровно один. Гарантируется, что данная 
> последовательность задаёт дерево.  
> **Формат выхода.** Высота дерева.

Сначала преобразуем входной массив (который является списком родителей) в список детей (или список смежностей).
Создадим очередь, в которую добавим вершину-корень и ограничитель уровня(благодаря ему мы сможем отслеживать, когда
мы перешли на более низкий уровень дерева). Далее в цикле проходя по очереди извлекаем из нее каждую вершину и 
добавляем ее детей. Если встречаем ограничитель, то увеличиваем счетчик высоты на 1.

Код:
``` python
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
        queue.append(-1)            # ограничитель уровня

    while queue:
        cur_peak = queue.pop(0)
        if cur_peak == -1:
            height += 1
            if queue: queue.append(-1)
        else:
            queue.extend(_list[cur_peak])

    return height


def main():
    n = int(input())
    print(calc(list(map(int, input().split()))))
```

## Симуляция обработки сетевых пакетов
Постановка задачи:
>Ваша цель — реализовать симулятор обработки сетевых пакетов. Для i-го пакета известно время его поступления 
> _arrival<sub>i</sub>_, а также время _duration<sub>i</sub>_, необходимое на его  обработку. В вашем распоряжении
> имеется один процессор, который обрабатывает пакеты в порядке их поступления. Если процессор начинает обрабатывать
> пакет _i_ (что занимает время _duration<sub>i</sub>_), он не прерывается и не останавливается до тех пор, пока не
> обработает пакет.  
> У компьютера, обрабатывающего пакеты, имеется сетевой буфер размера _size_. До начала обработки пакеты хранятся
> в буфере. Если буфер полностью заполнен в момент поступления пакета (есть _size_ пакетов, поступивших ранее, 
> которые до сих пор не обработаны), этот пакет отбрасывается и уже не будет обработан. Если несколько пакетов 
> поступает в одно и то же время, они все будут сперва сохранены в буфер (несколько последних из них могут быть 
> отброшены, если буфер заполнится). Компьютер обрабатывает пакеты в порядке их поступления. Он начинает обрабатывать
> следующий пакет из буфера сразу после того, как обработает текущий пакет. Компьютер может простаивать, если 
> все пакеты уже обработаны и в буфере нет пакетов. Пакет освобождает место в буфере сразу же, как компьютер 
> заканчивает его обработку.
> 
> **Формат входа.** Первая строка входа содержит размер буфера _size_ и число пакетов _n_. Каждая из следующих _n_ 
> строк содержит два числа: время _arrival<sub>i</sub>_ прибытия _i_-го пакета и время _duration<sub>i</sub>_, 
> необходимое на его обработку. 
> Гарантируется, что _arrival<sub>1</sub> ≤ arrival<sub>2</sub> ≤ ··· ≤ arrival<sub>n</sub>_. При этом может 
> оказаться, что _arrival<sub>i - 1</sub> = arrival<sub>i</sub>_.
> В таком случае считаем, что пакет _i − 1_ поступил раньше пакета _i_.  
> **Формат выхода.** Для каждого из _n_ пакетов выведите
> время, когда процессор начал его обрабатывать, или _−1_, если пакет был отброшен.  
> **Ограничения.** Все числа во входе целые. _1 ≤ size ≤ 10<sup>5</sup>_; _0 ≤ n ≤ 10<sup>5</sup>_;
> _0 ≤ arrivali ≤ 10<sup>6</sup>_; _0 ≤ duration<sub>i</sub> ≤ 10<sup>4</sup>_; 
> _arrival<sub>i</sub> ≤ arrival<sub>i + 1</sub>_ для всех _1 ≤ i ≤ n − 1_.

Заведем очередь фиксированного размера, которая будет эмулировать буфер. При поступлении нового пакета проверяем, 
в какой момент времени закончится обработка первого пакета в очереди. Если это число не больше, чем момент времени,
в который поступил текущий пакет(в таком случае в буфере есть свободное место), то добавляем его в 
очередь. Если больше, то пакет будет отброшен. 

Код:
``` python
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

    return answer


def main():
    buf_size, num_p = map(int, input().split())
    if num_p == 0:
        return
    packets = [list(map(int, input().split())) for _ in range(num_p)]

    print('\n'.join(map(str, processing(buf_size, packets))))
```

## Стек с поддержкой максимума
Постановка задачи:
>В данной задаче ваша цель — расширить интерфейс стека так, чтобы он дополнительно поддерживал операцию max 
> и при этом чтобы время работы всех операций по-прежнему было константным.  
> **Формат входа.** Первая строка содержит число запросов _q_. Каждая из 
> последующих _q_ строк задаёт запрос в одном из следующих форматов: push v, pop, or max. 
> **Формат выхода.** Для каждого запроса max выведите (в отдельной строке) текущий максимум на стеке. 
> **Ограничения.** _1 ≤ q ≤ 400 000_, _0 ≤ v ≤ 100 000_.

Код:
``` python
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
```

<!---
## Название
Постановка задачи:
>

Текст

Код:
``` python

```
-->