def solve(n, k, s):
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    char_index = {c: i for i, c in enumerate(chars)}
    ans = []
    for i, c in enumerate(s):
        ans.append(chars[char_index[c] - k[i % n]])
    print(''.join(ans))


while True:
    n = int(input())
    if n == 0:
        exit()
    k = list(map(int, input().split()))
    s = input()
    solve(n, k, s)
