n = int(input())

sum_numbers = 0

for i in range(1, n + 1):
    numbers = int(input())

    sum_numbers += numbers

avg_number = sum_numbers / n

print(f"{avg_number:.2f}")
