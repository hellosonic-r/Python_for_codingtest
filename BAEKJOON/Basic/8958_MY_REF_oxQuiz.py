import sys

t = int(input())

for i in range(t): 
    ans = list(sys.stdin.readline().strip()) #strip() 통해 개행문자 제거

    score = 0 ###위치 중요 ###하위 for문이 끝나면 다시 초기화
    result = 0 ###위치 중요 ###하위 for문이 끝나면 다시 초기화

    for j in range(len(ans)):
        if ans[j] == "O": 
            score = score + 1
            result = result + score
        else:
            score = 0
            
    print(result)

### 될것같은데 안됨.. 솔 실패
# OOXXOXXOOO
# OOXXOOXXOO
# OXOXOXOXOXOXOX
# OOOOOOOOOO
# OOOOXOOOOXOOOOX