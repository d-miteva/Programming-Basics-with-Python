n = int(input())

for i in range(0, n + 1):
    stars = "*" * i
    spaces = " " * (n - i)
    print(spaces, end="")
    print(stars, end="")
    print(" | ", end="")
    print(stars, end="")
    print(spaces)

# ------------------
#
# n = int(input())
#
# a = 0
# b = 0
#
# for i in range(0, n + 1):
#     space = " " * (n - a)
#     a += 1
#     star = "*" * (n - (n - b))
#     b += 1
#     print(space, star, "|", star, space)
