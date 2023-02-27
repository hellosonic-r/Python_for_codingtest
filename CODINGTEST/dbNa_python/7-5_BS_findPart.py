###부품찾기
##리스트 풀이 
# n = input()
# n_list = list(map(int, input().split()))

# m = input()
# m_list = list(map(int, input().split()))

# for m_num in m_list:
#     if m_num in n_list:
#         print("yes")
#     else:
#         print("no")


# ##이진탐색 풀이
# def bs(array, target, start, end):
#     while start <= end:
#         mid = (start + end) // 2
#         #찾은 경우 중간값 인덱스 반환
#         if array[mid] == target:
#             return mid
#         #중간 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인 (중간값 포함 오른쪽은 다 날림)
#         elif array[mid] > target:
#             end = mid -1
#         #중간 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인 (중간값 포함 왼쪽은 다 날림)
#         else:
#             start = mid + 1
#     return None

# n = int(input())
# array = list(map(int, input().split()))
# array.sort()

# m = int(input())
# x = list(map(int, input().split()))

# for i in x:
#     result = bs(array, i, 0, n-1)
#     if result != None:
#         print("yes", end = " ")
#     else:
#         print("no", end = " ")


##계수정렬 풀이
n = int(input())
array = [0] * 1000001


for i in input().split():
    array[int(i)] = 1

m = int(input())
x = list(map(int,input().split()))

for i in x:
    if array[i] == 1:
        print("yes",end = " ")
    else:
        print("no",end = " ")