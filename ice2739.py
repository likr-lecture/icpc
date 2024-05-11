def solve(N, M, T, a):
    ans = 0
    ans += a[0] - M
    ans += max(0, T - a[-1] - M)
    for i in range(1, N):
        ans += max(0, a[i] - a[i - 1] - 2 * M)
    print(ans)


N, M, T = list(map(int, input().split()))
a = list(map(int, input().split()))
solve(N, M, T, a)
