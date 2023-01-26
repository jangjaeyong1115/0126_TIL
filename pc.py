import sys
input = sys.stdin.readline

n = int(input())

list = list(map(int,input().split()))

pc = [0] * 101

result = 0

for i in list :
    if pc[i] == 0: # 자리 값이 0이면 앉히기
        pc[i] = 1

    else : # 자리 값이 0이 아니면 거절하기
        result += 1

print(result)