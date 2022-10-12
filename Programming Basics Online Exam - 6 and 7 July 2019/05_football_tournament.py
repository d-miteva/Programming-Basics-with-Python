name_team = input()
game_count = int(input())

w_total = 0
d_total = 0
l_total = 0
win_rate = 0
all_games = game_count

for game in range(1, game_count + 1):
    result = input()
    if result == "W":
        w_total += 1
    elif result == "D":
        d_total += 1
    else:
        l_total += 1

if all_games == 0:
    print(f"{name_team} hasn't played any games during this season.")
else:
    total_points = w_total * 3 + d_total
    win_rate = w_total / all_games * 100
    print(f"{name_team} has won {total_points} points during this season.")
    print("Total stats:")
    print(f"## W: {w_total}")
    print(f"## D: {d_total}")
    print(f"## L: {l_total}")
    print(f"Win rate: {win_rate:.2f}%")
