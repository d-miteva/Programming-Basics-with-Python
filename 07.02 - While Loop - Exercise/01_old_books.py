looking_book = input()

books_count = 0
is_book_found = False

input_line = input()
while input_line != "No More Books":

    if looking_book == input_line:
        is_book_found = True
        break

    books_count += 1

    input_line = input()

if is_book_found:
    print(f"You checked {books_count} books and found it.")
else:
    print(f"The book you search is not here!")
    print(f"You checked {books_count} books.")
