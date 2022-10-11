numbers_count = int(input())
letters_count = int(input())

for one in range(1, numbers_count):
    for two in range(1, numbers_count):
        for three in range(97, letters_count + 97):
            for four in range(97, letters_count + 97):
                for five in range(1, numbers_count + 1):
                    if five > one and five > two:
                        print(str(one) + str(two) + chr(three) + chr(four) + str(five), end=" ")
