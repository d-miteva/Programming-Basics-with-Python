n = int(input())

print("*" * (2 * n), end="")
print(" " * n, end="")
print("*" * (2 * n))

for i in range(n - 2):
    print("*", end="")
    print("/" * (n * 2 - 2), end="")
    print("*", end="")

    if i == (n - 1) // 2 - 1:
        print("|" * n, end="")
    else:
        print(" " * n, end="")

    print("*", end="")
    print("/" * (n * 2 - 2), end="")
    print("*")

print("*" * (2 * n), end="")
print(" " * n, end="")
print("*" * (2 * n))
