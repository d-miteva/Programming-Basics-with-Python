degree = float(input())

if 26.00 <= degree <= 35.00:
    print("Hot")
elif 20.10 <= degree <= 25.90:
    print("Warm")
elif 15.00 <= degree <= 20.00:
    print("Mild")
elif 12.00 <= degree <= 14.90:
    print("Cool")
elif 5.00 <= degree <= 11.90:
    print("Cold")
else:
    print("unknown")
