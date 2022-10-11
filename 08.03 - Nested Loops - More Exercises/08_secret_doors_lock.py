hundred_count = int(input())
ten_count = int(input())
singles_count = int(input())

for hundred in range(1, hundred_count + 1):
    if hundred % 2 == 0:
        for ten in range(1, ten_count + 1):
            if ten == 2 or ten == 3 or ten == 5 or ten == 7:
                for single in range(1, singles_count + 1):
                    if single % 2 == 0:
                        print(hundred, ten, single)
