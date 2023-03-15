n, k = map(int,input().split())
temperture = list(map(int, input().split()))

result_list = [sum(temperture[0:k])]
for i in range(n-k): #ex) 가장 앞의 수열 제외하고 10-5 =5 0~4까지 5번 
    result_list.append(result_list[i] - temperture[i] + temperture[i+k])

  
print(max(result_list))
