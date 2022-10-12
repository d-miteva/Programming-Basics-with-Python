games_count = int(input())

count_hearthstone = 0
count_fornite = 0
count_overwatch = 0
count_other = 0

for game in range(1, games_count + 1):
    game_name = input()

    if game_name == "Hearthstone":
        count_hearthstone += 1
    elif game_name == "Fornite":
        count_fornite += 1
    elif game_name == "Overwatch":
        count_overwatch += 1
    else:
        count_other += 1

total_hearthstone = count_hearthstone / games_count * 100
total_fornite = count_fornite / games_count * 100
total_overwatch = count_overwatch / games_count * 100
total_other = count_other / games_count * 100

print(f"Hearthstone - {total_hearthstone:.2f}%")
print(f"Fornite - {total_fornite:.2f}%")
print(f"Overwatch - {total_overwatch:.2f}%")
print(f"Others - {total_other:.2f}%")
