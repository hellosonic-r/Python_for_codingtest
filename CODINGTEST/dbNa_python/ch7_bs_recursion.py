def bs(num_list, target, start, end):
    if start > end:
        return None
    mid = (start + end)//2
    if num_list[mid] == target:
        return mid
    elif num_list[mid] > target:
        return bs(num_list, target, start, mid-1)
    else:
        return bs(num_list, target, mid+1, end)

n, target = map(int, input().split())
num_list = list(map(int, input().split()))

result = bs(num_list, target, 0, n-1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)