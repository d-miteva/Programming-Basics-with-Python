number_one = int(input())
number_two = int(input())
magic_number = int(input())

combinations = 0
is_magic_number = False

for current_number_one in range(number_one, number_two + 1):
    for current_number_two in range(number_one, number_two + 1):
        combinations += 1

        if current_number_one + current_number_two == magic_number:
            is_magic_number = True
            break

    if is_magic_number:
        break

if is_magic_number:
    print(f"Combination N:{combinations} ({current_number_one} + {current_number_two} = {magic_number})")
else:
    print(f"{combinations} combinations - neither equals {magic_number}")
