from collections import Counter

x = int(input())
n = int(input())

shoes = list(map(int, input().split()))
stock = Counter(shoes)


money = 0

for _ in range(n):
    size, price = map(int, input().split())

    if stock[size] > 0:
        money += price
        stock[size] -= 1

print(money)