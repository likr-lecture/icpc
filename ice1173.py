def solve(s):
    stack = []
    for c in s:
        if c == '(' or c == '[':
            stack.append(c)
        for p1, p2 in ['()', '[]']:
            if c == p2:
                if len(stack) == 0 or stack[-1] != p1:
                    print('no')
                    return
                stack.pop()
    if len(stack):
        print('no')
    else:
        print('yes')


while True:
    s = input()
    if s == '.':
        exit()
    solve(s)
