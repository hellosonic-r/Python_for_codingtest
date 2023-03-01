l = int(input())
n = int(input())

cake = [0] * (l + 1) # 0 0 0 0 0 0 0 0 0 0 
               # 0 1 1 1 0 3 2 2 3 0
received = [0] * (n + 1)
maxPieces,wantMaxNum = 0, 0

for i in range(1, n+1):
    count = 0
    start, end = map(int, input().split())

    #가장 많은 조각을 받을 것이라고 기대한 방청객 번호
    wantPieces = end - start
    if maxPieces < wantPieces:
        maxPieces = wantPieces
        wantMaxNum = i
    #해당 번호의 롤케이크 있으면 제공
    for j in range(start, end + 1):
        if cake[j] == 0:
            cake[j] = i
            count += 1
    received[i] = count

print(wantMaxNum, received.index(max(received)), end = "\n")