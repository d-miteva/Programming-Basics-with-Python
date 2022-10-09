import math

n = int(input())

stars = 1
if n % 2 == 0:
    stars += 1

roof_length = math.ceil(n / 2)

for i in range(0, roof_length):
    padding = (n - stars) // 2
    line = "-" * padding + "*" * stars + "-" * padding
    stars += 2
    print(line)

for i in range(n // 2):
    line = "|" + "*" * (n - 2) + "|"
    print(line)
