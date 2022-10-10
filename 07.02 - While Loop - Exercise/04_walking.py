sum_steps = 0
is_reached = False

input_line = input()
while input_line != "Going home":
    steps = int(input_line)

    sum_steps += steps

    if sum_steps >= 10000:
        is_reached = True
        break

    input_line = input()

if input_line == "Going home":
    steps_home = int(input())
    sum_steps += steps_home
    if sum_steps >= 10000:
        is_reached = True

diff = abs(10000 - sum_steps)
if is_reached:
    print("Goal reached! Good job!")
    print(f"{diff} steps over the goal!")
else:
    print(f"{diff} more steps to reach goal.")

# ---------------------------
# sum_steps = 0
#
# input_line = input()
# while input_line != "Going home":
#     steps = int(input_line)
#
#     sum_steps += steps
#
#     if sum_steps >= 10000:
#         break
#
#     input_line = input()
#
# if input_line == "Going home":
#     steps_home = int(input())
#     sum_steps += steps_home
#
# diff = abs(10000 - sum_steps)
# if sum_steps >= 10000:
#     print("Goal reached! Good job!")
#     print(f"{diff} steps over the goal!")
# else:
#     print(f"{diff} more steps to reach goal.")
