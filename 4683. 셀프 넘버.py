def func():
    import sys
    read = sys.stdin.readline

    li = [0 for i in range(10001)]

    for i in range(1, 10000):
        n = i
        while 0 < n <= 10000:
            li[n] += 1
            if n < 10:
                n += n
            elif 10 <= n < 100:
                n += n % 10 + n // 10
            elif 100 <= n < 1000:
                n += n // 100 + n % 100 // 10 + n % 100 % 10
            elif 1000 <= n < 10000:
                n += n // 1000 + n % 1000 // 100 + n % 1000 % 100 // 10 + n % 1000 % 100 % 10
            else:
                n += n // 10000 + n % 10000 // 1000 + n % 10000 % 1000 // 100 + n % 10000 % 1000 % 100 % 10

    for i in range(1, 10000):
        if li[i] == 1:
            print(i)

if __name__ == '__main__':
    func()