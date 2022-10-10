bottles_detergent = int(input())

all_detergent = bottles_detergent * 750
counter = 1
count_pots = 0
count_dishes = 0

input_line = input()
while input_line != "End":
    dishes = int(input_line)

    if counter % 3 == 0:
        all_detergent -= dishes * 15
        count_pots += dishes
    else:
        all_detergent -= dishes * 5
        count_dishes += dishes

    if all_detergent < 0:
        break

    counter += 1
    input_line = input()

if all_detergent >= 0:
    print(f"Detergent was enough!")
    print(f"{count_dishes} dishes and {count_pots} pots were washed.")
    print(f"Leftover detergent {all_detergent} ml.")
else:
    print(f"Not enough detergent, {abs(all_detergent)} ml. more necessary!")
