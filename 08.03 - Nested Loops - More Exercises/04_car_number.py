start_number = int(input())
end_number = int(input())

sum_two_three = 0

for number_one in range(start_number, end_number + 1):
    for number_two in range(start_number, end_number + 1):
        for number_three in range(start_number, end_number + 1):
            sum_two_three = number_two + number_three
            if sum_two_three % 2 == 0:
                for number_four in range(start_number, end_number + 1):
                    if number_one > number_four:
                        if number_one % 2 == 0 and number_four % 2 != 0:
                            print(str(number_one) + str(number_two) + str(number_three) + str(number_four), end=" ")
                        elif number_one % 2 != 0 and number_four % 2 == 0:
                            print(str(number_one) + str(number_two) + str(number_three) + str(number_four), end=" ")
