coupon = int(input())

price = 0
total_money = coupon
movie_tickets = 0
other_purchase = 0

input_line = input()
while input_line != "End":
    purchase = len(input_line)

    if purchase > 8:
        price = ord(input_line[0]) + ord(input_line[1])
        total_money -= price
        if total_money < 0:
            break
        movie_tickets += 1
    else:
        price = ord(input_line[0])
        total_money -= price
        if total_money < 0:
            break
        other_purchase += 1

    input_line = input()

print(movie_tickets)
print(other_purchase)
