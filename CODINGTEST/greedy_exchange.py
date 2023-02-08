#거스름돈
'''
500원, 100원, 50원, 10원
1260원을 모두 거슬러주는 동전의 개수 구하기
'''
n = 1260
count = 0
coin_type = [500,100,50,10]
for coin in coin_type:
    count = count + n // coin
    n = n % coin

print(count)