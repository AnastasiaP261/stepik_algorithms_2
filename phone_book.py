phone_book = dict()


def add_in_book(entry):
    phone_num, name = entry.split()
    phone_book[phone_num] = name


def del_from_book(phone_num):
    phone_book.pop(phone_num, '')


def main():
    n = int(input())
    for i in range(n):
        request, entry = input().split(maxsplit=1)
        if request == 'add':
            add_in_book(entry)
        elif request == 'del':
            del_from_book(entry)
        elif request == 'find':
            print(phone_book.get(entry, 'not found'))


if __name__ == "__main__":
    main()
