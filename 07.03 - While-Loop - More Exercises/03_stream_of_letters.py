input_line = input()

counter_c = 0
counter_n = 0
counter_o = 0
word = ""
last_char = 0
check_input = ""

while input_line != "End":

    char = ord(input_line)

    if 65 <= char <= 90 or 97 <= char <= 122:
        if char != 99 and char != 110 and char != 111:
            word += chr(char)

        if counter_c > 0 and char == 99:
            word += chr(char)
        elif counter_n > 0 and char == 110:
            word += chr(char)
        elif counter_o > 0 and char == 111:
            word += chr(char)

        if char == 99 and counter_c == 0:
            counter_c += 1
        elif char == 110 and counter_n == 0:
            counter_n += 1
        elif char == 111 and counter_o == 0:
            counter_o += 1

        if counter_c == 1 and counter_n == 1 and counter_o == 1:
            word += " "
            counter_c = 0
            counter_n = 0
            counter_o = 0

    check_input = input_line
    input_line = input()

if check_input == "n" or check_input == "o" or check_input == "c":
    print(word)
else:
    word = word.split()
    print(" ".join(word[:-1]))
#
#
# command = input()
# c_counter = 0
# o_counter = 0
# n_counter = 0
# word = ""
# while command != "End":
#     if 65 <= ord(command) <= 90 or 97 <= ord(command) <= 122:
#         if command == "c":
#             if c_counter >= 1:
#                 word += command
#             else:
#                 c_counter += 1
#         elif command == "o":
#             if o_counter >= 1:
#                 word += command
#             else:
#                 o_counter += 1
#         elif command == "n":
#             if n_counter >= 1:
#                 word += command
#             else:
#                 n_counter += 1
#         else:
#             word += command
#         if c_counter >= 1 and o_counter >= 1 and n_counter >= 1:
#             print(f"{word}", end=" ")
#             word = ""
#             c_counter = 0
#             o_counter = 0
#             n_counter = 0
#     command = input()
