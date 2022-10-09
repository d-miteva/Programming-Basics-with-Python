n = int(input())

for i in range(1, n + 1):
    a = "*"
    b = " *"
    draw_line = a + b * (n - 1)
    print(draw_line)
