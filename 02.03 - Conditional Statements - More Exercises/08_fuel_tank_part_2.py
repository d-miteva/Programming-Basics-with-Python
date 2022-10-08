fuel = input()
quantity = float(input())
club_card = input()

total_price = 0

if club_card in "No":
    if fuel in "Gas":
        total_price = quantity * 0.93
    elif fuel in "Gasoline":
        total_price = quantity * 2.22
    else:
        total_price = quantity * 2.33
else:
    if fuel in "Gas":
        total_price = quantity * 0.85
    elif fuel in "Gasoline":
        total_price = quantity * 2.04
    else:
        total_price = quantity * 2.21

if 20 < quantity <= 25:
    total_price = total_price * 0.92
elif 25 < quantity:
    total_price = total_price * 0.9

print(f"{total_price:.2f} lv.")
