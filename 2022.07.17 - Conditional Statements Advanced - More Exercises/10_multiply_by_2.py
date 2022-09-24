number = float(input())

while number >= 0:
    number = number * 2
    print(f"Result: {number:.2f}")
    number = float(input())
else:
    print("Negative number!")
