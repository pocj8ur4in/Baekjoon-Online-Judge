def func():
    import sys
    read = sys.stdin.readline

    li = read().split('-')
    r = 0

    for i in range(len(li)):
        s = li[i]
        s = s.split('+')
        s = list(map(int, s))
        s = sum(s)
        if (i == 0):
            r = s
        else:
            r -= s

    print(r)

if __name__ == '__main__':
    func()