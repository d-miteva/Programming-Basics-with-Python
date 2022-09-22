fruit = input()
size_set = input()
number_order_sets = int(input())

price = 0
number_in_set = 0

if size_set == "small":
    number_in_set = 2
    if fruit == "Watermelon":
        price = 56
    elif fruit == "Mango":
        price = 36.66
    elif fruit == "Pineapple":
        price = 42.1
    elif fruit == "Raspberry":
        price = 20
elif size_set == "big":
    number_in_set = 5
    if fruit == "Watermelon":
        price = 28.7
    elif fruit == "Mango":
        price = 19.6
    elif fruit == "Pineapple":
        price = 24.8
    elif fruit == "Raspberry":
        price = 15.2

total_price = number_in_set * price * number_order_sets

if 400 <= total_price <= 1000:
    total_price = total_price * 0.85 # total_price *= 0.85
elif total_price > 1000:
    total_price *= 0.5

print(f"{total_price:.2f} lv.")

