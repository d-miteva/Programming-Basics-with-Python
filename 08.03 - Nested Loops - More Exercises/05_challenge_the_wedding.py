men_total = int(input())
women_total = int(input())
table_total = int(input())

table_counter = 1

for man in range(1, men_total + 1):
    for woman in range(1, women_total + 1):
        print(f"({man} <-> {woman})", end=" ")
        table_counter += 1

        if table_counter > table_total:
            break

    if table_counter > table_total:
        break
