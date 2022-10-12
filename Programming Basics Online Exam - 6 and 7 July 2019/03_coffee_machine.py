drinks = input()
sugar = input()
count = int(input())

total = 0

if drinks == "Espresso":
    if sugar == "Without":
        total = count * 0.9
    elif sugar == "Normal":
        total = count * 1
    else:
        total = count * 1.2

elif drinks == "Cappuccino":
    if sugar == "Without":
        total = count * 1
    elif sugar == "Normal":
        total = count * 1.2
    else:
        total = count * 1.6

else:
    if sugar == "Without":
        total = count * 0.5
    elif sugar == "Normal":
        total = count * 0.6
    else:
        total = count * 0.7

if sugar == "Without":
    total = total * 0.65
if drinks == "Espresso" and count >= 5:
    total = total * 0.75
if total > 15:
    total = total * 0.8

print(f"You bought {count} cups of {drinks} for {total:.2f} lv.")
