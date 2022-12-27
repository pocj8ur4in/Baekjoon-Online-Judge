def func():
    import sys
    read = sys.stdin.readline

    N = int(read())
    li = [list(map(int, read().split())) for i in range(N)]

    li.sort(key=lambda x: [x[1], x[0]])

    R = 1
    C = li[0][1]

    for i in range(N - 1):
        if C <= li[i + 1][0]:
            C = li[i + 1][1]
            R += 1

    print(R)

if __name__ == '__main__':
    func()