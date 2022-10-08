students_count = int(input())

with_2 = 0
with_3 = 0
with_4 = 0
with_5 = 0
assess_total = 0

for student in range(1, students_count + 1):
    assess = float(input())
    assess_total = assess_total + assess
    if 2.00 <= assess <= 2.99:
        with_2 = with_2 + 1
    elif 3.00 <= assess <= 3.99:
        with_3 = with_3 + 1
    elif 4.00 <= assess <= 4.99:
        with_4 = with_4 + 1
    elif assess >= 5.00:
        with_5 = with_5 + 1

avr_assess = assess_total / students_count
percent_2 = with_2 / students_count * 100
percent_3 = with_3 / students_count * 100
percent_4 = with_4 / students_count * 100
percent_5 = with_5 / students_count * 100

print(f"Top students: {percent_5:.2f}%")
print(f"Between 4.00 and 4.99: {percent_4:.2f}%")
print(f"Between 3.00 and 3.99: {percent_3:.2f}%")
print(f"Fail: {percent_2:.2f}%")
print(f"Average: {avr_assess:.2f}")
