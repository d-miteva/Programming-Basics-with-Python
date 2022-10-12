word = input()

sum_word = 0
sum_word_power = 0
word_power = ""
check_letter = ""

while word != "End of words":
    for letter in word:
        letter_int = ord(letter)
        sum_word += letter_int

    check_letter = word[0].lower()
    if check_letter == "a" or check_letter == "e" or check_letter == "i" \
            or check_letter == "o" or check_letter == "u" or check_letter == "y":
        sum_word *= len(word)
    else:
        sum_word /= len(word)

    if sum_word_power < sum_word:
        sum_word_power = sum_word
        word_power = word

    sum_word = 0

    word = input()

print(f"The most powerful word is {word_power} - {round(sum_word_power)}")
