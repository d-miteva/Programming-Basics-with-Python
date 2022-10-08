people_game = int(input())

result = 0
max10 = 0
max20 = 0
max30 = 0
max40 = 0
max50 = 0
invalid = 0

for person in range(people_game):
    number = int(input())

    if 0 <= number <= 9:
        result += number * 20 / 100
        max10 += 1
    elif 10 <= number <= 19:
        result += number * 30 / 100
        max20 += 1
    elif 20 <= number <= 29:
        result += number * 40 / 100
        max30 += 1
    elif 30 <= number <= 39:
        result += 50
        max40 += 1
    elif 40 <= number <= 50:
        result += 100
        max50 += 1

    if number < 0 or number > 50:
        result = result / 2
        invalid += 1

percent_10 = max10 / people_game * 100
percent_20 = max20 / people_game * 100
percent_30 = max30 / people_game * 100
percent_40 = max40 / people_game * 100
percent_50 = max50 / people_game * 100
percent_invalid = invalid / people_game * 100

print(f"{result:.2f}")
print(f"From 0 to 9: {percent_10:.2f}%")
print(f"From 10 to 19: {percent_20:.2f}%")
print(f"From 20 to 29: {percent_30:.2f}%")
print(f"From 30 to 39: {percent_40:.2f}%")
print(f"From 40 to 50: {percent_50:.2f}%")
print(f"Invalid numbers: {percent_invalid:.2f}%")
