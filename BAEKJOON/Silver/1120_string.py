a, b = map(str, input().split())
a_list = list(a)
b_list = list(b)

#두 문자열 길이의 차이+1번 비교하게 될 것이다.
length = len(b_list) - len(a_list)
n = 0
ans = len(b_list)
while n<=length:
    count = 0
    check = b_list[n:n+len(a_list)] #긴 문자열을 짧은 문자열에 맞추어 자른다.
    #각 문자열의 문자를 비교하여 다르면 카운트한다.
    for i in range(len(check)):
        if a_list[i] != check[i]:
            count += 1
    if ans > count:
        ans = count
    n += 1

print(ans)
