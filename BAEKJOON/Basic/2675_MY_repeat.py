R, S = list(map(str, input().split()))

for i in range(len(S)):
    print(str(int(R) * S[i]), end="")
