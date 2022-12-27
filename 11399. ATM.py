def func():
    import sys
    read = sys.stdin.readline

    N = int(read())
    li = list(map(int, read().split()))
    li.sort()

    s = 0

    for i in range(N):
        s += li[i] * (N - i)

    print(s)

if __name__ == '__main__':
    func()