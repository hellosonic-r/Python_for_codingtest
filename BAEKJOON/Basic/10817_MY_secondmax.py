a, b, c = map(int, input().split())
S = [a,b,c]
S.remove(max(S))
S.remove(min(S))

print(S.pop())
