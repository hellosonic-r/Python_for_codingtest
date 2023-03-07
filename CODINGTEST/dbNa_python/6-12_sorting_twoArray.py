###두 배열의 원소 교체
##내 풀이
# n, k = map(int, input().split())
# A_list = list(map(int,input().split()))
# B_list = list(map(int,input().split()))

# for i in range(k):
#     A_list.append(max(B_list))
#     B_list.append(min(A_list))
#     A_list.pop(A_list.index(min(A_list)))
#     B_list.pop(B_list.index(max(B_list)))

# print(A_list,B_list,sep = "\n")
# print(sum(A_list))

##교재 풀이
n, k = map(int,input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i] < b[i]:
        a[i],b[i] = b[i],a[i]
    else:
        break
print(sum(a))
