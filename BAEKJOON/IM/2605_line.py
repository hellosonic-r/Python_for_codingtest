# n = int(input())
# num_list = list(map(int, input().split())) # 0 1 1 3 2
# students = list(range(1,n+1))

# for i in range(len(students)): 
#     # i = 0 / 1 2 3 4 5
#     # i = 1 / 1 1 3 4 5 / 2 1 3 4 5
#     # i = 2 / 2 1 1 4 5 / 2 3 1 4 5
#     # i = 3 / 2 3 1 1 5 / 2 3 3 1 5 / 2 2 3 1 5 / 4 2 3 1 5
#     # i = 4 / 4 2 3 1 1 / 4 2 3 3 1 / 4 2 5 3 1(end)
#     if i == 0:
#         continue
#     for j in range(num_list[i]):
#         students[i-j] = students[i-j-1] 
#     students[i - num_list[i]] = i + 1
    
# for i in range(len(students)):
#     print(students[i], end = " ")
#     if i == len(students) - 1:
#         print()

n = int(input())
arr = list(map(int, input().split()))
li = []
# 0 1 1 3 2
for i in range(n):
    if i == 0:
        li.insert(0, i+1)
    else:
        li.insert(arr[i], i+1)
li.reverse()
for i in range(len(li)):
    print(li[i], end = " ")
    if i == len(li) - 1:
        print()