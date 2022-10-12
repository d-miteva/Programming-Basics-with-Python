budget_movie = float(input())
walkon_number = int(input())
clothes_per_walkon_price = float(input())

decor = budget_movie * 0.1
clothes_per_walkon_price_discount = clothes_per_walkon_price * 0.9

if walkon_number > 150:
    clothes_walkon_discount = clothes_per_walkon_price_discount * walkon_number
    total_movie_price = decor + clothes_walkon_discount

else:
    clothes_walkon = clothes_per_walkon_price * walkon_number
    total_movie_price = decor + clothes_walkon

if budget_movie >= total_movie_price:
    more_money = budget_movie - total_movie_price
    print("Action!")
    print(f"Wingard starts filming with {more_money:.2f} leva left.")
else:
    less_money = total_movie_price - budget_movie
    print("Not enough money!")
    print(f"Wingard needs {less_money:.2f} leva more.")
