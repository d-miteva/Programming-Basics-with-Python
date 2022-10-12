name_player = input()

points = 0
points_winner = 0
name_winner = ""

while name_player != "Stop":
    for letter in name_player:
        player_number = int(input())
        if letter == chr(player_number):
            points += 10
        else:
            points += 2

    if points_winner <= points:
        points_winner = points
        name_winner = name_player

    points = 0
    name_player = input()

print(f"The winner is {name_winner} with {points_winner} points!")
