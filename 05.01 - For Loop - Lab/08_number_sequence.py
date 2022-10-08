count_of_numbers = int(input())
current_number = int(input())

max_number = count_of_numbers
min_number = count_of_numbers

for numbers in range(count_of_numbers - 1):
    current_number = int(input())
    if current_number > max_number:
        max_number = current_number
    if current_number < min_number:
        min_number = current_number

print(f"Max number: {max_number}")
print(f"Min number: {min_number}")

# ---------------------
# import sys
#
# number_of_iterations = int(input())
#
# max_number = -sys.maxsize
# min_number = sys.maxsize
#
# for num in range(number_of_iterations):
#     current_number = int(input())
#
#     if current_number > max_number:
#         max_number = current_number
#
#     if current_number < min_number:
#         min_number = current_number
#
# print(f"Max number: {max_number}")
# print(f"Min number: {min_number}")
