one_leva_count = int(input())
two_leva_count = int(input())
five_leva_count = int(input())
amount = int(input())

all_total = 0

for one_leva in range(0, one_leva_count + 1):
    for two_leva in range(0, two_leva_count + 1):
        for five_leva in range(0, five_leva_count + 1):
            all_total = one_leva * 1 + two_leva * 2 + five_leva * 5
            if all_total == amount:
                print(f"{one_leva} * 1 lv. + {two_leva} * 2 lv. + {five_leva} * 5 lv. = {amount} lv.")
