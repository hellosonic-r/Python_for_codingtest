'''
배열은 같은 종류의 데이터를 순차적으로 저장하는 자료구조
'''
'''
import queue #파이썬은 queue 라이브러리를 제공한다. 하지만 대부분의 큐와 관련된 자료구조는 list 통해 구현 가능
#1차원 배열 = 리스트
data = [1,2,3,4,5]
string = "Hello World"
print(data[3]) #4 출력
print(string[3]) #l 출력

#2차원 배열
data2 = [[1,2,3],[4,5,6],[7,8,9]]
print(data2[1][0]) #4 출력

#ex) 특정 알파벳의 빈도수 측정 함수
dataset = ["apple","banana","coconut","django"]

def find_alphabet(dataset,alphabet):
    count = 0
    for data in dataset:
        for i in range(len(data)):
            if data[i] == alphabet:
                count += 1
    print(count)

find_alphabet("apple", "p") #2 출력
'''

import queue #파이썬은 queue 라이브러리를 제공한다. 하지만 대부분의 큐와 관련된 자료구조는 list 통해 구현 가능

#Queue() 일반적인 큐 자료구조
data_queue = queue.Queue()
data_queue.put(1) # 1
data_queue.put(2) # 1 - 2
data_queue.put(3) # 1 - 2 - 3
print(data_queue.get()) # 1 출력
print(data_queue.get()) # 2 출력

#LifoQueue() 나중에 입력된 데이터가 먼저 출력 (stack과 동일)
data_lifoqueue = queue.LifoQueue()
data_lifoqueue.put(1) # 1
data_lifoqueue.put(2) # 2 - 1
data_lifoqueue.put(3) # 3 - 2 - 1
print(data_lifoqueue.get()) # 3 출력
print(data_lifoqueue.get()) # 2 출력

#PriorityQueue() 데이터마다 우선순위를 부여하여 정렬된 큐로, 우선순위 높은 순으로 출력하는 자료구조
data_priorityqueue = queue.PriorityQueue()
data_priorityqueue.put((1, "apple")) #(1순위,apple)
data_priorityqueue.put((3, "LG")) #(3순위,lg)
data_priorityqueue.put((2, "samsung")) #(2순위,samsung)
print(data_priorityqueue.get()[1]) # 1순위 apple 출력
print(data_priorityqueue.get()[1]) # 2순위 samsung 출력

