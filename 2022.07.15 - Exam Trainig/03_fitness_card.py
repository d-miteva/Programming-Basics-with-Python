budget = float(input())
sex = input()
age = int(input())
type_sport = input()

fitness_card_price = 0

if sex == "f":
    if type_sport == "Gym":
        fitness_card_price = 35
    elif type_sport == "Boxing":
        fitness_card_price = 37
    elif type_sport == "Yoga":
        fitness_card_price = 42
    elif type_sport == "Zumba":
        fitness_card_price = 31
    elif type_sport == "Dances":
        fitness_card_price = 53
    elif type_sport == "Pilates":
        fitness_card_price = 37
elif sex == "m":
    if type_sport == "Gym":
        fitness_card_price = 42
    elif type_sport == "Boxing":
        fitness_card_price = 41
    elif type_sport == "Yoga":
        fitness_card_price = 45
    elif type_sport == "Zumba":
        fitness_card_price = 34
    elif type_sport == "Dances":
        fitness_card_price = 51
    elif type_sport == "Pilates":
        fitness_card_price = 39

if age <= 19:
    fitness_card_price *= 0.8

diff = abs(fitness_card_price - budget)

if budget >= fitness_card_price:
    print(f"You purchased a 1 month pass for {type_sport}.")
else:
    print(f"You don't have enough money! You need ${diff:.2f} more.")