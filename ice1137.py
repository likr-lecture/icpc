def to_mcxi(v):
    s = ''
    for c in 'ixcm':
        if v % 10 != 0:
            s += c
        if v % 10 > 1:
            s += str(v % 10)
        v //= 10
    return ''.join(list(reversed(s)))


def from_mcxi(s):
    v = 0
    f = 1
    base = {'m': 1000, 'c': 100, 'x': 10, 'i': 1}
    for c in s:
        if c in base:
            v += f * base[c]
            f = 1
        else:
            f = int(c)
    return v


def solve(s1, s2):
    print(to_mcxi(from_mcxi(s1) + from_mcxi(s2)))


n = int(input())
for _ in range(n):
    s1, s2 = input().split()
    solve(s1, s2)
