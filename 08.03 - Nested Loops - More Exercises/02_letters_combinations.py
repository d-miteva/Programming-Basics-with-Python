start_letter = input()
end_letter = input()
exclusive_letter = input()
combination = 0

start_letter = ord(start_letter)
end_letter = ord(end_letter)
exclusive_letter = ord(exclusive_letter)

for letter_one in range(start_letter, end_letter + 1):
    if letter_one != exclusive_letter:
        for letter_two in range(start_letter, end_letter + 1):
            if letter_two != exclusive_letter:
                for letter_three in range(start_letter, end_letter + 1):
                    if letter_three != exclusive_letter:
                        combination += 1
                        print(chr(letter_one) + chr(letter_two) + chr(letter_three), end=" ")

print(combination)
