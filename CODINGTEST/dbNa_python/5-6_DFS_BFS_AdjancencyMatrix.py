###인접 행렬 방식
#연결이 되어있지 않은 노드끼리는 무한의 비용이라고 작성
INF = 999999999 #무한의 비용 선언

#2차원 리스트를 이용해 인접행렬 표현

graph = [
    [0,7,5],
    [7,0,INF],
    [5,INF,0]
]

print(graph)