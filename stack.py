n = int(input())

list = []

for i in range(n):
    money = int(input())
    if money == 0:
        list.pop()

        continue
    list.append(money)

print(sum(list))
