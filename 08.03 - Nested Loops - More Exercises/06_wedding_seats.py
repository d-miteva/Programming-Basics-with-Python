sector_count = input()
count_row = int(input())
count_seats_odd = int(input())

sector_count_int = ord(sector_count)
counter = 0

for sector in range(65, sector_count_int + 1):
    count_row += 1
    for row in range(1, count_row):
        if row % 2 == 0:
            for seat in range(97, 97 + 2 + count_seats_odd):
                print(chr(sector) + str(row) + chr(seat))
                counter += 1
        else:
            for seat in range(97, 97 + count_seats_odd):
                print(chr(sector) + str(row) + chr(seat))
                counter += 1
print(counter)
