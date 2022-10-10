command = input()
total_sum = 0

while command != "NoMoreMoney":
    current_sum = float(command)

    if current_sum < 0:
        print("Invalid operation!")
        break

    print(f"Increase: {current_sum:.2f}")

    total_sum += current_sum
    command = input()

print(f"Total: {total_sum:.2f}")
# ------------------------
# available_sum = 0
#
# while True:
#     current_sum = input()
#
#     if current_sum == "NoMoreMoney":
#         break
#
#     current_sum = float(current_sum)
#
#     if current_sum >= 0:
#         available_sum += current_sum
#         print(f"Increase: {current_sum:.2f}")
#     else:
#         print("Invalid operation!")
#         break
#
# print(f"Total: {available_sum:.2f}")
# ------------------------
