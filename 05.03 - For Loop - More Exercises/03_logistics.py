cargo_count = int(input())

price = 0
cargo_total = 0
total_price = 0
bus = 0
truck = 0
train = 0

for cargo in range(1, cargo_count + 1):
    cargo_ton = int(input())
    cargo_total = cargo_ton + cargo_total

    if cargo_ton <= 3:
        price = cargo_ton * 200
        bus = cargo_ton + bus
    elif cargo_ton <= 11:
        price = cargo_ton * 175
        truck = truck + cargo_ton
    else:
        price = cargo_ton * 120
        train = train + cargo_ton

    total_price = price + total_price

avg_price_cargo = total_price / cargo_total

percent_bus = bus / cargo_total * 100
percent_truck = truck / cargo_total * 100
percent_train = train / cargo_total * 100

print(f"{avg_price_cargo:.2f}")
print(f"{percent_bus:.2f}%")
print(f"{percent_truck:.2f}%")
print(f"{percent_train:.2f}%")
