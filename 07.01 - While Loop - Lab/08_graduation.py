student_name = input()
current_class = 1
bad_tries = 0
total_grade = 0
is_excluded = False

while current_class <= 12:
    current_grade = float(input())

    if current_grade < 4:
        bad_tries += 1
        if bad_tries > 1:
            is_excluded = True
            break

        continue

    current_class += 1
    total_grade += current_grade

if is_excluded:
    print(f"{student_name} has been excluded at {current_class} grade")
else:
    average_grade = total_grade / 12
    print(f"{student_name} graduated. Average grade: {average_grade:.2f}")

# -----------------------
# name = input()
#
# grades_total = 0
# years_counter = 0
# failed_years = 0
#
# while True:
#     annual_grade = float(input())
#     years_counter += 1
#
#     if annual_grade < 4:
#         failed_years += 1
#
#         if failed_years == 2:
#             print(f"{name} has been excluded at {years_counter} grade")
#             break
#
#         years_counter -= 1
#
#     else:
#         grades_total += annual_grade
#
#     if years_counter == 12:
#         average_grade = grades_total / 12
#         print(f"{name} graduated. Average grade: {average_grade:.2f}")
#         break
# -----------------------
# student_name = input()
# current_class = 1
# bad_tries = 0
# total_grade = 0
# is_excluded = False
#
# while current_class <= 12:
#     current_grade = float(input())
#
#     if current_grade < 4:
#         bad_tries += 1
#         if bad_tries > 1:
#             is_excluded = True
#             break
#
#     else:
#         current_class += 1
#         total_grade += current_grade
#
# if is_excluded:
#     print(f"{student_name} has been excluded at {current_class} grade")
# else:
#     average_grade = total_grade / 12
#     print(f"{student_name} graduated. Average grade: {average_grade:.2f}")

# ----------------
