n = int(input())

for row in range(1, n + 1):
    space = " " * (n - row)
    star = "* " * row
    print(f"{space}{star}")
for row_bottom in range(n - 1, 0, -1):
    space = " " * (n - row_bottom)
    star = "* " * row_bottom
    print(f"{space}{star}")
