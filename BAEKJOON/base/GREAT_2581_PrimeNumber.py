m = int(input())
n = int(input())

primeNum_list=[]

for num in range(m, n+1): # 60부터 100까지
    count = 0 
    for i in range(2, num+1):
        if num % i == 0:
            count += 1
    if count == 1:
        primeNum_list.append(num)
        
if primeNum_list:
    print(sum(primeNum_list), min(primeNum_list),sep ="\n")
    
else:
    print(-1)