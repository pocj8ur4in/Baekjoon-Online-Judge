def func():
    import sys
    read = sys.stdin.readline

    N, K = map(int, read().split())
    O = 0
    C = list([read() for i in range(N)])

    for i in range(N):
        if (K < int(C[N - 1 - i])):
            continue
        else:
            while (K >= int(C[N - 1 - i])):
                K -= int(C[N - 1 - i])
                O += 1

    print(O)


if __name__ == '__main__':
    func()