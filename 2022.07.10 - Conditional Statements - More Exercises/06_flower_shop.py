import math

magnolia = int(input())
hyacinth = int(input())
rose = int(input())
cactus = int(input())
price_gift = float(input())

price = magnolia * 3.25 + hyacinth * 4 + rose * 3.5 + cactus * 8
total_price = price * 0.95
diff = abs(total_price-price_gift)

if total_price >= price_gift:
    print(f"She is left with {math.floor(diff)} leva.")
else:
    print(f"She will have to borrow {math.ceil(diff)} leva.")