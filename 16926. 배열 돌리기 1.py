def func():
    import sys
    read = sys.stdin.readline

    N, M, R = map(int, read().split())

    B = [list(map(int, read().split())) for i in range(N)]

    C = 0  # 회전의 개수
    if (N / 2) >= (M / 2):
        C = M // 2
    else:
        C = N // 2

    for i in range(R):  # 입력받은 회전만큼
        for j in range(C):  # 동그라미 개수만큼
            n = N - j * 2  # 동그라미의 열의 개수
            m = M - j * 2  # 동그라미의 줄의 개수

            for l in range(m - 1):
                t = B[j][j + l]
                B[j][j + l] = B[j][j + l + 1]
                B[j][j + l + 1] = t

            for l in range(n - 1):
                t = B[j + l][M - 1 - j]
                B[j + l][M - 1 - j] = B[j + l + 1][M - 1 - j]
                B[j + l + 1][M - 1 - j] = t

            for l in range(m - 1):
                t = B[N - 1 - j][M - 1 - j - l]
                B[N - 1 - j][M - 1 - j - l] = B[N - 1 - j][M - 2 - j - l]
                B[N - 1 - j][M - 2 - j - l] = t

            for l in range(n - 2):
                t = B[N - 1 - j - l][j]
                B[N - 1 - j - l][j] = B[N - 2 - j - l][j]
                B[N - 2 - j - l][j] = t

if __name__ == '__main__':
    func()