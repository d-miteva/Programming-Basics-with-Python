import sys

max_number = - sys.maxsize
command = input()

while command != "Stop":

    current_number = int(command)

    if max_number < current_number:
        max_number = current_number

    command = input()

print(max_number)
