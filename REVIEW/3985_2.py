l = int(input()) #롤케이크 길이

cake = [0] * (l+1)

n = int(input()) #방청객의 수

expect_num = 0
expect = 0

for i in range(1, n+1):
    start, end = map(int, input().split())
    if end-start+1 > expect:
        expect = end-start+1
        expect_num = i
    for j in range(start, end+1):
        if cake[j] == 0:
            cake[j] = i 

ans = 0
ans_num = 0
for i in range(1, n+1):
    if ans < cake.count(i):
        ans = cake.count(i)
        ans_num = i

print(expect_num, ans_num, sep="\n")