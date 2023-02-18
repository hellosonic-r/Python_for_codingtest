###거스름돈 문제
##500원,100원,50원,10원 동전으로 거스름돈 N원을 거슬러줄 수 있는 동전의 최소 개수는?

n = int(input()) #440원 #1260

coin_list = [500,100,50,10]
count = 0
for coin in coin_list:
    if n >= coin:
        count += n // coin # coin=500, count=2 / coin=100, count=4 / 
                                  # coin=50, count=5 / coin=10, count=6
        n %= coin
    else:
        continue

print(count)