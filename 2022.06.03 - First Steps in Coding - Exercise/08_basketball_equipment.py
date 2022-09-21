year_tax = int(input())
shoes_price = year_tax * 0.6
suit_price = shoes_price * 0.8
ball_price = suit_price / 4
acc_price = ball_price / 5
total_price = suit_price + shoes_price + ball_price + acc_price + year_tax
print(total_price)
