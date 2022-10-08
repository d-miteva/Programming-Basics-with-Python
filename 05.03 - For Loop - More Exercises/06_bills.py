period = int(input())

total_electricity = 0
total_water = 0
total_internet = 0
total_other = 0
water = 20
internet = 15

for month in range(period):
    electricity = float(input())
    total_electricity += electricity
    total_water += water
    total_internet += internet
    total_other += (electricity + water + internet) * 1.2

avg_month = (total_electricity + total_internet + total_water + total_other) / period

print(f"Electricity: {total_electricity:.2f} lv")
print(f"Water: {total_water:.2f} lv")
print(f"Internet: {total_internet:.2f} lv")
print(f"Other: {total_other:.2f} lv")
print(f"Average: {avg_month:.2f} lv")
