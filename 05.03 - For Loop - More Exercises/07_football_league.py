capacity_stadium = int(input())
fans_count = int(input())

count_a = 0
count_b = 0
count_v = 0
count_g = 0

for fan in range(fans_count):
    sector = input()

    if sector == "A":
        count_a += 1
    elif sector == "B":
        count_b += 1
    elif sector == "V":
        count_v += 1
    elif sector == "G":
        count_g += 1

percent_a = count_a / fans_count * 100
percent_b = count_b / fans_count * 100
percent_v = count_v / fans_count * 100
percent_g = count_g / fans_count * 100
percent_stadium = fans_count / capacity_stadium * 100

print(f"{percent_a:.2f}%")
print(f"{percent_b:.2f}%")
print(f"{percent_v:.2f}%")
print(f"{percent_g:.2f}%")
print(f"{percent_stadium:.2f}%")
