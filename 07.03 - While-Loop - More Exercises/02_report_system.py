needed_amount = int(input())

counter = 1
total_sum_cash = 0
total_sum_card = 0
count_cash = 0
count_card = 0
avg_cash = 0
avg_card = 0
is_done = False

input_line = input()

while input_line != "End":
    price = int(input_line)

    if counter % 2 != 0:
        if price > 100:
            print("Error in transaction!")
        else:
            total_sum_cash += price
            count_cash += 1
            print("Product sold!")
    else:
        if price < 10:
            print("Error in transaction!")
        else:
            total_sum_card += price
            count_card += 1
            print("Product sold!")

    counter += 1

    if (total_sum_cash + total_sum_card) >= needed_amount:
        avg_cash = total_sum_cash / count_cash
        avg_card = total_sum_card / count_card
        is_done = True
        break

    input_line = input()

if is_done:
    print(f"Average CS: {avg_cash:.2f}")
    print(f"Average CC: {avg_card:.2f}")
else:
    print("Failed to collect required money for charity.")
