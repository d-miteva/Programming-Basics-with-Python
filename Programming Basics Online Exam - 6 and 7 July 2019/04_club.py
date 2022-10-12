wish_income = float(input())

price = 0
total_sum = 0
is_enough_money = False

input_line = input()
while input_line != "Party!":
    cocktail = len(input_line)
    count_cocktail = int(input())

    price = cocktail * count_cocktail

    if price % 2 != 0:
        price *= 0.75

    total_sum += price

    if wish_income <= total_sum:
        is_enough_money = True
        break

    input_line = input()

if is_enough_money:
    print("Target acquired.")
    print(f"Club income - {total_sum:.2f} leva.")
else:
    diff = wish_income - total_sum
    print(f"We need {diff:.2f} leva more.")
    print(f"Club income - {total_sum:.2f} leva.")
