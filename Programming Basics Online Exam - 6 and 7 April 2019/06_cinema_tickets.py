movie_name = input()

counter = 0
total_movie_tickets = 0
student_ticket = 0
standard_ticket = 0
kid_ticket = 0

while movie_name != "Finish":
    free_seats = int(input())

    for seat in range(1, free_seats + 1):
        type_ticket = input()
        if type_ticket == "student":
            counter += 1
            student_ticket += 1
        elif type_ticket == "standard":
            counter += 1
            standard_ticket += 1
        elif type_ticket == "kid":
            counter += 1
            kid_ticket += 1
        else:
            break

    percent_full_hall_per_movie = counter / free_seats * 100
    total_movie_tickets += counter
    counter = 0

    print(f"{movie_name} - {percent_full_hall_per_movie:.2f}% full.")

    movie_name = input()

percent_student_ticket = student_ticket / total_movie_tickets * 100
percent_standard_ticket = standard_ticket / total_movie_tickets * 100
percent_kid_ticket = kid_ticket / total_movie_tickets * 100

print(f"Total tickets: {total_movie_tickets}")
print(f"{percent_student_ticket:.2f}% student tickets.")
print(f"{percent_standard_ticket:.2f}% standard tickets.")
print(f"{percent_kid_ticket:.2f}% kids tickets.")
