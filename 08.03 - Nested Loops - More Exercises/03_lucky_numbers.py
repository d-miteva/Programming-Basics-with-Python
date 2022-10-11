number = int(input())

sum_one_two = 0
sum_three_four = 0

for num_one in range(1, 10):
    sum_one_two = 0
    if num_one < number:
        for num_two in range(1, 10):
            if num_two < number:
                sum_one_two = num_one + num_two
                for num_three in range(1, 10):
                    sum_three_four = 0
                    if num_three < number:
                        for num_four in range(1, 10):
                            if num_four < number:
                                sum_three_four = num_three + num_four
                                if sum_three_four == sum_one_two:
                                    if number % sum_three_four == 0:
                                        print(str(num_one) + str(num_two) + str(num_three) + str(num_four), end=" ")
