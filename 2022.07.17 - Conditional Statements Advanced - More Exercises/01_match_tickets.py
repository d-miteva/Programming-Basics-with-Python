budget = float(input())
category = input()
people = int(input())

ticket_price = 0
transport_outcome = 0

if category == "VIP":
    ticket_price = 499.99

elif category == "Normal":
    ticket_price = 249.99


if people <= 4:
    transport_outcome = budget * 0.75
elif 5 <= people <= 9:
    transport_outcome = budget * 0.60
elif 10 <= people <= 24:
    transport_outcome = budget * 0.50
elif 25 <= people <= 49:
    transport_outcome = budget * 0.40
else:
    transport_outcome = budget * 0.25

diff = abs(budget - transport_outcome)
total = abs(diff - (people * ticket_price))

if budget > transport_outcome and diff >= ticket_price * people:
    total = diff - (people * ticket_price)
    print(f"Yes! You have {total:.2f} leva left.")
else:
    print(f"Not enough money! You need {total:.2f} leva.")