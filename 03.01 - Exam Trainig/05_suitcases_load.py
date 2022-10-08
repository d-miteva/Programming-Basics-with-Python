lugged_capacity = float(input())

suitcases = 0
lugged = input()

while lugged != "End":
    lugged = float(lugged)
    suitcases = suitcases + 1

    added_lugged_space = 0
    if suitcases % 3 == 0:
        added_lugged_space = lugged * 0.1

    lugged_capacity = lugged_capacity - lugged + added_lugged_space

    if lugged_capacity < 0:
        suitcases = suitcases - 1
        print("No more space!")
        break

    lugged = input()
else:
    print("Congratulations! All suitcases are loaded!")

print(f"Statistic: {suitcases} suitcases loaded.")
