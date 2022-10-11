count_days = int(input())
count_hours = int(input())

total_sum_day = 0
total_sum = 0

for day in range(1, count_days + 1):
    if day % 2 == 0:
        total_sum_day = 0
        for hour in range(1, count_hours + 1):
            if hour % 2 != 0:
                total_sum_day += 2.5
            else:
                total_sum_day += 1
    elif day % 2 != 0:
        total_sum_day = 0
        for hour in range(1, count_hours + 1):
            if hour % 2 == 0:
                total_sum_day += 1.25
            else:
                total_sum_day += 1

    total_sum += total_sum_day

    print(f"Day: {day} - {total_sum_day:.2f} leva")
print(f"Total: {total_sum:.2f} leva")
