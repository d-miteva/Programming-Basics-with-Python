poor_grades = int(input())

sum_grade = 0
count_grade = 0
last_problem = ""
count_poor_grade = 0

input_line = input()
while input_line != "Enough":
    grade = int(input())

    if grade <= 4:
        count_poor_grade += 1

    if count_poor_grade == poor_grades:
        break

    sum_grade += grade
    count_grade += 1
    last_problem = input_line

    input_line = input()

if count_poor_grade == poor_grades:
    print(f"You need a break, {count_poor_grade} poor grades.")
else:
    avg_grade = sum_grade / count_grade
    print(f"Average score: {avg_grade:.2f}")
    print(f"Number of problems: {count_grade}")
    print(f"Last problem: {last_problem}")
