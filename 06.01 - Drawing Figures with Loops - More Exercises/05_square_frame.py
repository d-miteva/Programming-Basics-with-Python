n = int(input())

for i in range(1, n + 1):
    if i == 1:
        print("+" + (n - 2) * " -" + " +")
    elif 1 < i < n:
        print("|" + (n - 2) * " -" + " |")
    else:
        print("+" + (n - 2) * " -" + " +")
