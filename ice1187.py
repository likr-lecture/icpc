import itertools

while True:
    M, T, P, R = map(int, input().split())
    if (M, T, P, R) == (0, 0, 0, 0):
        exit()
    if R == 0:
        print('='.join(reversed([f'{i + 1}' for i in range(T)])))
        continue
    m, t, p, j = list(zip(*[map(int, input().split()) for _ in range(R)]))
    problems = [[0 for _ in range(P)] for _ in range(T)]
    time = [[0 for _ in range(P)] for _ in range(T)]
    penalty = [[0 for _ in range(P)] for _ in range(T)]
    for i in range(R):
        if j[i] == 0:
            problems[t[i] - 1][p[i] - 1] = 1
            time[t[i] - 1][p[i] - 1] = m[i] + penalty[t[i] - 1][p[i] - 1]
        else:
            penalty[t[i] - 1][p[i] - 1] += 20
    scores = [[0, 0, i + 1] for i in range(T)]
    for i in range(T):
        for j in range(P):
            scores[i][0] += problems[i][j]
            scores[i][1] -= time[i][j]
    scores.sort(reverse=True)
    ans = []
    for _, items in itertools.groupby(scores, key=lambda score: (score[0], score[1])):
        ans.append('='.join(f'{score[2]}' for score in items))
    print(','.join(ans))
