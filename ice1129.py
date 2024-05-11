def solve(n, r, p, c):
    cards = list(range(1, n + 1))
    cards.reverse()
    for pi, ci in zip(p, c):
        tmp = [cards[j] for j in range(pi - 1)]
        for j in range(ci):
            cards[j] = cards[pi - 1 + j]
        for j in range(pi - 1):
            cards[ci + j] = tmp[j]
    print(cards[0])


while True:
    n, r = map(int, input().split())
    if (n, r) == (0, 0):
        exit()
    p, c = list(zip(*[map(int, input().split()) for _ in range(r)]))
    solve(n, r, p, c)
