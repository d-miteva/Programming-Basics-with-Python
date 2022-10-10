needed_money = float(input())
init_money = float(input())

all_days_count = 0
count_spend_day = 0

total_money = init_money
while total_money < needed_money:
    if count_spend_day == 5:
        break

    action = input()
    amount = float(input())

    all_days_count += 1

    if action == "spend":
        total_money -= amount
        count_spend_day += 1
        if total_money < 0:
            total_money = 0
    elif action == "save":
        count_spend_day = 0
        total_money += amount

if count_spend_day == 5:
    print(f"You can't save the money.")
    print(f"{all_days_count}")
else:
    print(f"You saved the money for {all_days_count} days.")
