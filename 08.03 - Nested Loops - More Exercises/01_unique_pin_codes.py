number_one = int(input())
number_two = int(input())
number_three = int(input())

for one in range(1, number_one + 1):
    if one % 2 == 0:
        for two in range(1, number_two + 1):
            if two == 2 or two == 3 or two == 5 or two == 7:
                for three in range(1, number_three + 1):
                    if three % 2 == 0:
                        print(one, two, three)
