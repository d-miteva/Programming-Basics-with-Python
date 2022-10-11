start_left = int(input())
start_right = int(input())
end_left = int(input())
end_right = int(input())

for number_left in range(start_left, start_left + end_left + 1):
    if number_left % 2 == 0:
        continue
    elif number_left % 3 == 0:
        continue
    elif number_left % 5 == 0:
        continue
    elif number_left % 7 == 0:
        continue
    else:
        for number_right in range(start_right, start_right + end_right + 1):
            if number_right % 2 == 0:
                continue
            elif number_right % 3 == 0:
                continue
            elif number_right % 5 == 0:
                continue
            elif number_right % 7 == 0:
                continue
            else:
                print(str(number_left) + str(number_right))
