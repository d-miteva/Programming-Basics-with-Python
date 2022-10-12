budget = float(input())
night_numbers = int(input())
night_price = float(input())
discount_percent = int(input())

other_outcoming = budget * discount_percent / 100

if night_numbers > 7:
    price_discount_per_night = night_price * 0.95
    total_nights_price_discount = price_discount_per_night * night_numbers
    total_sum = total_nights_price_discount + other_outcoming

else:
    total_nights_price = night_price * night_numbers
    total_sum = total_nights_price + other_outcoming

if total_sum <= budget:
    more_lv = budget - total_sum
    print(f"Ivanovi will be left with {more_lv:.2f} leva after vacation.")
else:
    needs_lv = total_sum - budget
    print(f"{needs_lv:.2f} leva needed.")
