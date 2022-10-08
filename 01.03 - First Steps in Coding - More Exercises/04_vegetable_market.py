vegetables_price = float(input())
fruits_price = float(input())
vegetables_kg = int(input())
fruits_kg = int(input())

vegetables_price_total = vegetables_price * vegetables_kg
fruits_price_total = fruits_price * fruits_kg

total_price_euro = (vegetables_price_total + fruits_price_total) / 1.94

print(f"{total_price_euro:.2f}")