###Try1
# S = int(input())

# num = 1
# while num <= 100:
#     if num * 0.5 * (num + 1) == S:
#         print(num)
#     else:
#         num += 1


###사이의 수 합
# start, finish = map(int, input().split())
# sum = 0 
# for i in range(start,finish+1):
#     sum = sum + i
# print(sum)


###Try2
# S = int(input())

# num = 1
# n = []

# while True:
#     n.append(num)
#     print(num)
#     num += 1
#     if int(sum(n)) == S:
#         break


###리스트에 1부터 넣고 총 합 구하기
# S = []
# i = 1
# while i<=10:
#     S.append(i)
#     print(i, sum(S))
#     i+=1



###Try3 ###Finally I solved it!
S = int(input())

i = 1
while i * (i+1) // 2 <= S:
    i+=1
print(int(i-1))
