# n = int(input())
# num = list(map(int, input().split()))
# print(min(num),max(num))


#sorted 함수 사용
n = int(input())
num = list(map(int, input().split()))

num_sorted = sorted(num)

print(num_sorted[0],num_sorted[len(num)-1])