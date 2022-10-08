import math

days = int(input())
food_kg = int(input())
dog_food_kg = float(input())
cat_food_kg = float(input())
turtle_food_gr = float(input())

dog_food_total = dog_food_kg * days
cat_food_total = cat_food_kg * days
turtle_food_total = turtle_food_gr * days / 1000
all_food = dog_food_total + cat_food_total + turtle_food_total

food = abs(food_kg - all_food)

if food_kg >= all_food:
    print(f"{math.floor(food)} kilos of food left.")
else:
    print(f"{math.ceil(food)} more kilos of food are needed.")
