def solve(n, w):
    acc = [0 for _ in range(n + 1)]
    for i in range(n):
        acc[i + 1] = acc[i] + len(w[i])
    for i in range(n + 1):
        seq = []
        seq_ok = [5, 12, 17, 24, 31]
        for j in range(i + 1, n + 1):
            for k in seq_ok:
                if acc[j] - acc[i] == k:
                    seq.append(k)
        if seq == seq_ok:
            print(i + 1)
            return


while True:
    n = int(input())
    if n == 0:
        exit()
    w = [input() for _ in range(n)]
    solve(n, w)
