days = int(input())
type_room = input()
rating = input()

price = 0

if type_room == "room for one person":
    price = (days - 1) * 18
elif type_room == "apartment":
    if days < 10:
        price = (days - 1) * 25 * 0.7
    elif 10 <= days <= 15:
        price = (days - 1) * 25 * 0.65
    else:
        price = (days - 1) * 25 * 0.5
elif type_room == "president apartment":
    if days < 10:
        price = (days - 1) * 35 * 0.9
    elif 10 <= days <= 15:
        price = (days - 1) * 35 * 0.85
    else:
        price = (days - 1) * 35 * 0.8

if rating == "positive":
    price = price * 1.25
else:
    price = price * 0.9

print(f"{price:.2f}")

