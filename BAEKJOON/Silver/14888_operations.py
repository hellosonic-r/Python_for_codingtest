def dfs(count, result):
    if count == len(num_list)-1:
        ans.append(result)
        return

    for i in range(len(op)): #연산을 하나하나 방문하여 돌린다.
        if op[i] != 0: #연산자를 사용할 수 있다면,
            op[i] -= 1 #방문한 연산자의 사용 가능 횟수를 1만큼 줄인다.
            if i == 0:
                dfs(count+1, result + num_list[count+1])
            elif i == 1:
                dfs(count+1, result - num_list[count+1])
            elif i == 2: 
                dfs(count+1, result * num_list[count+1])
            elif i == 3:
                if result < 0: #앞의 값이 음수라면, 문제의 조건에 맞게 양수로 바꿔서 연산 후 음수로 바꿔주기
                    dfs(count+1, -(abs(result) // num_list[count+1]))
                else:
                    dfs(count+1, result // num_list[count+1])
            op[i] += 1 #돌아와서는 방문한 연산자의 사용 가능 횟수를 돌려놓는다.
    

n = int(input())
num_list = list(map(int, input().split()))
op = list(map(int, input().split())) #덧셈, 뺄셈, 곱셈, 나눗셈

ans = []

dfs(0, num_list[0])

print(max(ans))
print(min(ans))