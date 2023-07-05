def bs(num_list, target, start, end):
    while start <= end:
        mid = (start+end)//2
        if num_list[mid] == target:
            return mid
        elif num_list[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

n, target = map(int, input().split())
num_list = list(map(int, input().split()))

result = bs(num_list, target, 0, n-1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)

