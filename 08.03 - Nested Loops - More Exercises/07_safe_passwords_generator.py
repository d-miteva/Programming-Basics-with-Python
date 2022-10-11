number_one = int(input())
number_two = int(input())
max_passwords = int(input())

counter = 0
one = 35
two = 64

for three in range(1, number_one + 1):
    for four in range(1, number_two + 1):
        counter += 1
        if counter > max_passwords:
            break
        print(chr(one) + chr(two) + str(three) + str(four) + chr(two) + chr(one) + "|", end="")
        one += 1
        two += 1
        if one > 55:
            one = 35
        if two > 96:
            two = 64

    if counter > max_passwords:
        break
