N = int(input()) # 카드받기

card = [i for i in range(1,N+1)] # 리스트 변수 선언하고, 카드리스트 만들기

while len(card) > 1: # 한 장 남을 때까지

    print(card[0]) # 버릴 카드

    del card[0]

    card.append(card[0]) # 뒤로 넘기기

    del card[0]

print(card[0]) # 마지막 남은 카드 출력