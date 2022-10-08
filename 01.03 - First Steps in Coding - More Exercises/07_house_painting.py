x = float(input())
y = float(input())
h = float(input())

front_wall = (x * x) - (1.2 * 2)
back_wall = x * x
side_wall = (x * y) - (1.5 * 1.5)
side_roof = x * y
front_back_roof = (h * x) / 2

total_wall = (front_wall + back_wall) + (2 * side_wall)
total_roof = (2 * side_roof) + (2 * front_back_roof)

total_green_paint = total_wall / 3.4
total_red_paint = total_roof / 4.3

print(f"{total_green_paint:.2f}")
print(f"{total_red_paint:.2f}")