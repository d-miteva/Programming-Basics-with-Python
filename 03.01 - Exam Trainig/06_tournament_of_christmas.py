days_tournament = int(input())

price = 0
count_win = 0
count_lose = 0
bonus_price = 0
total_price = 0
count_lose_total = 0
count_win_total = 0

for days in range(1, days_tournament + 1):
    name_game = input()
    result = input()
    while name_game != "Finish":
        if result == "win":
            price = price + 20
            count_win = count_win + 1
            count_win_total = count_win_total + 1
        else:
            price = price
            count_lose = count_lose + 1
            count_lose_total = count_lose_total + 1

        name_game = input()

        if name_game == "Finish":
            break
        else:
            result = input()

    if count_win > count_lose:
        bonus_price = price * 1.1
        total_price = total_price + bonus_price
        price = 0
    else:
        total_price = total_price + price
        price = 0

    count_lose = 0
    count_win = 0

if count_win_total > count_lose_total:
    total_price = total_price * 1.2
    print(f"You won the tournament! Total raised money: {total_price:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total_price:.2f}")
