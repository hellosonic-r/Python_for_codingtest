l = int(input())
n = int(input())
cake_list = [0 for _ in range(l+1)]

expect = 0 #가장 많은 조각을 받은 방청객이 기대한 케이크 수 
expect_ans = 0 #인덱스

#방청객 수만큼 for문을 수행한다.
for i in range(1,n+1):
    p,k = map(int, input().split())
    #현재 기대 케이크 수가 이전 기대 케이크 수와 같다면 그대로 유지한다.(작은번호 출력)
    if expect == k-p+1:
        expect = expect
    #기대한 케이크 수가 최대라면, expect에 현재 기대 케이크 수를 저장한다.
    elif max(expect, k-p+1) == k-p+1:
        expect = k-p+1
        expect_ans = i
    for j in range(p, k+1):
        if cake_list[j] == 0:
            cake_list[j] = i
        else:
            continue
        
fin = 0
fin_ans = 0
for i in range(1,n+1):
    #현제 실제로 받은 케이크 수가 이전 실제로 받은 케이크 수와 같다면 그대로 유지한다.
    if fin == cake_list.count(i):
        fin = fin
    #실제로 받은 케이크 수가 최대라면, fin에 실제 받은 케이크 수를 저장한다.
    elif max(fin, cake_list.count(i)) == cake_list.count(i):
        fin = cake_list.count(i)
        fin_ans = i #현재 반복문 수행 번호를 저장한다.(방청객 번호)
    else:
        continue
print(expect_ans, fin_ans, sep = "\n")

