T = int(input())

for i in range(T):
    bracket = input()

    cnt = 0  # 초기화
    for i in bracket:
        if i == '(':
            cnt += 1

        else:
            cnt -= 1

        if cnt < 0:
           break
           
    if cnt == 0:
        print('YES')

    elif cnt > 0:
        print('NO')

    