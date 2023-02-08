#숫자 카드 게임 2중 for문 사용
#각 행에 해당하는 카드 중 가장 낮은 숫자 카드를 뽑고
#그 중 가장 큰 수의 숫자 카드를 뽑는 프로그램을 작성하라.

n,m = map(int, input().split())

result = 0
for i in range(n):
    card = list(map(int, input().split()))
    min_value = 10001 #line12의 a와 비교하기 위해 10001로 선언
    for a in card:
        min_value = min(min_value, a)
    result = max(result, min_value)

print(result)