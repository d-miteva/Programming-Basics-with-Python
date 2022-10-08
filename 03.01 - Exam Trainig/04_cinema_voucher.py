vouchers = int(input())

movie_ticket_price = 0
items_price = 0
total_money_left = vouchers
movie_tickets_count = 0
items_count = 0

item = input()

while item != "End":
    item_length = len(item)
    if item_length > 8:
        movie_ticket_price = ord(item[0]) + ord(item[1])
        total_money_left = total_money_left - movie_ticket_price
        if total_money_left >= 0:
            movie_tickets_count = movie_tickets_count + 1
    elif item_length <= 8:
        items_price = ord(item[0])
        total_money_left = total_money_left - items_price
        if total_money_left > 0:
            items_count = items_count + 1

    if total_money_left < 0:
        break

    item = input()

print(movie_tickets_count)
print(items_count)
