n_couple = int(input())

n_sum1 = 0
n_sum2 = 0
n_diff = 0
max_diff = 0

for number in range(1, n_couple + 1):
    n1 = int(input())
    n2 = int(input())

    if number % 2 != 0:
        n_sum1 = n1 + n2
    else:
        n_sum2 = n1 + n2

    if number != 1:
        n_diff = abs(n_sum1 - n_sum2)
        if n_diff > max_diff:
            max_diff = n_diff

if max_diff == 0:
    print(f"Yes, value={n_sum1}")
else:
    print(f"No, maxdiff={max_diff}")
