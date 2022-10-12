height = int(input())
width = int(input())
percent_no_painting = int(input())

wall = (height * width * 4)
wall_painting = wall - wall * percent_no_painting / 100
wall_painting_left = wall_painting

input_line = input()
while input_line != "Tired!":
    paint_lt = int(input_line)

    wall_painting_left -= paint_lt

    if wall_painting_left <= 0:
        break

    input_line = input()

if wall_painting_left < 0:
    print(f"All walls are painted and you have {abs(int(wall_painting_left))} l paint left!")
elif wall_painting_left == 0:
    print(f"All walls are painted! Great job, Pesho!")
else:
    print(f"{int(wall_painting_left)} quadratic m left.")
