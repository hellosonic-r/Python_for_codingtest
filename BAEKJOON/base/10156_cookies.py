# K : 과자 한 개의 가격
# N : 사려는 과자의 개수
# M : 현재 동수가 가진 돈
# 부모님께 받아야 하는 돈 출력

import sys

K, N, M = map(int, sys.stdin.readline().split())
print((K * N) - M if (K * N) - M >= 0 else 0)