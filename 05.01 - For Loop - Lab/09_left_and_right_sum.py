count_of_numbers = int(input())

left_sum = 0
right_sum = 0

for numbers in range(count_of_numbers * 2):
    current_number = int(input())

    if numbers < count_of_numbers:
        left_sum += current_number
    else:
        right_sum += current_number

if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    diff = abs(left_sum - right_sum)
    print(f"No, diff = {diff}")

# ------------------
# number_count = int(input())
#
# sum_left = 0
# sum_right = 0
#
# for num in range(0, number_count):
#     left_number = int(input())
#     sum_left = sum_left + left_number
#
# for num in range(0, number_count):
#     right_number = int(input())
#     sum_right = sum_right + right_number
#
# if sum_left == sum_right:
#     print(f"Yes, sum = {sum_left}")
# else:
#     diff = abs(sum_left - sum_right)
#     print(f"No, diff = {diff}")
