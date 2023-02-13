import sys

V = int(input())
x = list(map(str, input())) #각각의 인덱스에 해당하는 원소 리스트 갖도록 저장 : x = list(input())

print("A" if x.count("A") > x.count("B") \
      else("B" if x.count("B") > x.count("A") else "Tie"))