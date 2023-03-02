###고정점 찾기
##내풀이(무한재귀함수 에러)
# n = int(input())
# array = list(map(int, input().split()))

# def binary_search(array, start, end):
#     a = find_plus(array,0,n-1)
#     if a == None:
#         return None
#     if start > end:
#         return None
#     mid = (a + end) // 2
#     if array[mid] == mid:
#         return mid
#     elif array[mid] > mid:
#         return binary_search(array,start,mid-1)
#     elif array[mid] < mid:
#         return binary_search(array,mid+1,end)
    
# def find_plus(array, start, end):
#     if start > end:
#         return None
#     mid = (start + end) // 2
#     if array[mid] < 0 and array[mid+1] > 0:
#         return mid+1
#     elif array[mid] == 0 or (array[mid-1] < 0 and array[mid] > 0):
#         return mid
#     else:
#         if array[mid] < 0:
#             return binary_search(array, mid+1, end)
#         elif array[mid] > 0:
#             return binary_search(array, start, mid-1)


# result = binary_search(array, 0, n-1)
# if result == None:
#     print(-1)
# else:
#     print(result)


##교재풀이참고
n = int(input())
array = list(map(int, input().split()))

def binary_search(array, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == mid:
        return mid
    elif array[mid] > mid:
        return binary_search(array, start, mid-1)
    else:
        return binary_search(array, mid+1, end)
    
result = binary_search(array, 0, n-1)
if result == None:
    print(-1)
else:
    print(result)