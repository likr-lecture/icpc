def solve(h, w, r, s):
    current = (0, 0)
    index = {r[i][j]: (i, j) for i in range(h) for j in range(w)}
    ans = 0
    for c in s:
        i, j = index[c]
        ans += abs(current[0] - i) + abs(current[1] - j) + 1
        current = (i, j)
    print(ans)


while True:
    h, w = list(map(int, input().split()))
    if (h, w) == (0, 0):
        exit()
    r = [input() for _ in range(h)]
    s = input()
    solve(h, w, r, s)
