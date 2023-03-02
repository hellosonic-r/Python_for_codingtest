# ###정렬된 배열에서 특정 수의 개수 구하기
##내풀이
# n, x = map(int, input().split())
# array = list(map(int, input().split()))
# ans_end = 0
# ans_start = 0
# def binary_search(array, x, start, end):
#     if start>end:
#         return None
#     mid = (start + end) // 2
#     if array[mid] == x:
#         global ans_start
#         global ans_end
#         ans_start = mid
#         ans_end = mid
#         while array[ans_start] == x: 
#             ans_start -= 1
#         while array[ans_end] == x:
#             ans_end += 1
#         return ans_end - ans_start - 1
#     elif array[mid] > x:
#         return binary_search(array, x, start, mid - 1)
#     elif array[mid] < x:
#         return binary_search(array, x, mid+1, end)
    
# result = binary_search(array, x, 0, n-1)
# if result == None:
#     print(-1)
# else:
#     print(result)


##교재풀이

n, x = map(int, input().split())
array = list(map(int, input().split()))

#처음 위치를 찾는 이진 탐색 메서드
def first(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    #해당 값을 가지는 원소 중에서 가장 왼쪽에 있는 경우에만 인덱스 반환
    if (mid == 0 or target > array[mid - 1]) and array[mid] == target:
        return mid 
    #중간점의 값보다 찾고자 하는 값이 작거나 같은 경우 왼쪽 확인
    elif target <= array[mid]:
        return first(array, target, start, mid-1)
    #중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
        return first(array, target, mid+1, end)

#마지막 위치를 찾는 이진 탐색 메서드
def last(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    #해당 값을 가지는 원소 중에서 가장 오른쪽에 있는 경우에만 인덱스 반환
    if (mid == n - 1 or target < array[mid + 1]) and array[mid] == target: 
        return mid
    #찾고자 하는 값이 중간값보다 크거나 같은 경우(끝을 찾아야되니까) 오른쪽 확인
    elif target >= array[mid]:   
        return last(array, target, mid+1, end)
    #찾고자 하는 값이 중간값보다 작은 경우 왼쪽 확인
    else:
        return last(array, target, start, mid-1)
    
#정렬된 수열에서 값이 x인 원소의 개수를 세는 메서드
def count_by_value(array, x):
    #데이터의 개수
    n = len(array)

    #x가 처음 등장한 인덱스 계산
    a = first(array, x, 0, n-1)
    #수열에 x가 존재하지 않는 경우
    if a == None:
        return 0
    
    #x가 마지막으로 등장한 인덱스 계산
    b = last(array, x, 0, n-1)
    if b == None:
        return 0
    
    #개수를 반환
    return b - a + 1

#값이 x인 데이터의 개수 계산
count = count_by_value(array,x)

#값이 x인 원소가 존재하지 않는다면
if count == 0:
    print(-1)
#값이 x인 원소가 존재한다면
else:
    print(count)
     