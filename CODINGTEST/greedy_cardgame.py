#숫자 카드 게임 min 함수 이용
#각 행에 해당하는 카드 중 가장 낮은 숫자 카드를 뽑고
#그 중 가장 큰 수의 숫자 카드를 뽑는 프로그램을 작성하라.

n, m = map(int, input().split())

result = 0 
for i in range(n):
    card = list(map(int, input().split())) #공백으로 구분하여 숫자 입력
    min_value = min(card) #현재 줄에서 가장 작은 숫자의 카드 찾기
    result = max(result, min_value) #가장 작은 숫자 카드 중에서 가장 큰 수 찾기

print(result)
