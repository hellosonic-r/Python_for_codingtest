##내풀이 - 이진탐색
def bs(num_list, target, start, end):
    while start<=end:
        mid = (start + end)//2
        if num_list[mid] == target:
            return True
        elif num_list[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
        
    return False

n = int(input())
num_list = list(map(int, input().split()))

m = int(input())
find = list(map(int, input().split()))

num_list.sort()

for num in find:
    if bs(num_list, num, 0, n-1):
        print("yes", end = " ")
    else:
        print("no", end = " ")

print()



##교재풀이1 - 계수정렬
n = int(input())
arr = [0] * 1000001

for i in input().split():
    arr[int(i)] = 1

m = int(input())
find = list(map(int, input().split()))

for num in find:
    if arr[num] == 1:
        print("yes", end = " ")
    else:
        print("no", end = " ")

print()


##교재풀이2 - 집합자료형 set()
n = int(input())
arr = set(map(int, input().split()))

m = int(input())
find = list(map(int, input().split()))

for num in find:
    if num in arr:
        print("yes", end = " ")
    else:
        print("no", end = " ")