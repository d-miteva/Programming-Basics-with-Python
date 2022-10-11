number = int(input())

no_password = True
counter = 0
password = ""

for one in range(1, 10):
    for two in range(1, 10):
        if one < two:
            for three in range(1, 10):
                for four in range(1, 10):
                    if three > four:
                        if number == one * two + three * four:
                            no_password = False
                            counter += 1
                            print(str(one) + str(two) + str(three) + str(four), end=" ")
                            if counter == 4:
                                password = str(one) + str(two) + str(three) + str(four)

if no_password or counter < 4:
    print()
    print("No!")
else:
    print()
    print(f"Password: {password}")
