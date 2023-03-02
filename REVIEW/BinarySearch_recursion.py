# ##try1
# n, target = list(map(int, input())) #n:원소의 개수/target:찾으려는 수

# #전체원소 입력 받기
# array = list(map(int, input().split()))

# def binary_search(array, target, start, end):
#     if start > end:
#         return None
#     mid = (start + end) // 2

#     #찾은 경우엔 중간점 인덱스 반환
#     if array[mid] == target:
#         return mid
#     elif array[mid] > target:
#         return binary_search(array, target, start, mid-1)
#     else:
#         return binary_search(array, target, mid+1, end)
    
# result = binary_search(array, target, 0, n - 1)
# if result == None:
#     print("원소가 존재하지 않습니다.")
# else:
#     print(result+1)

##try2
# n, target = map(int, input().split())
# array = list(map(int, input().split()))

# def binary_search(array, target, start, end):
#     if start > end:
#         return None
#     mid = (start+ end) // 2
#     if array[mid] == target:
#         return mid
#     elif array[mid] > target:
#         return binary_search(array, target, start, mid-1 )
#     elif array[mid] < target:
#         return binary_search(array, target, mid+1, end )
    
# result = binary_search(array,target,0, n-1)
# if result == None:
#     print("원소가 없습니다.")
# else:
#     print(result + 1)

##try3
# n, target = map(int, input().split())
# array = list(map(int, input().split()))

# def binary_search(array, target, start, end):
#     if start > end:
#         return None
#     mid = (start + end) // 2
#     if array[mid] == target:
#         return mid
#     elif array[mid] > target:
#         return binary_search(array, target, start, mid -1)
#     elif array[mid] < target:
#         return binary_search(array, target, mid + 1, end )
    
# result = binary_search(array, target, 0, n-1)
# if result == None:
#     print("원소가 없습니다.")
# else:
#     print(result + 1)

##try4
n, target = map(int, input().split())
array = list(map(int, input().split()))

def binary_search(array, target, start, end):
    if start > end :
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    elif array[mid] < target:
        return binary_search(array, target, mid+1,end)
    
result = binary_search(array, target, 0, n-1)

if result == None:
    print("원소가 없습니다,")
else:
    print(result + 1)