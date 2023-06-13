n, m = map(int, input().split())
a_list = set(map(int, input().split()))
b_list = set(map(int, input().split()))

ans = len(a_list-b_list) + len(b_list-a_list)

print(ans)