count_tabs = int(input())
salary = int(input())

copy_salary = salary

for i in range(1, count_tabs + 1):
    if copy_salary > 0:
        name_tab = input()
        if name_tab == "Facebook":
            copy_salary = copy_salary - 150
        elif name_tab == "Instagram":
            copy_salary = copy_salary - 100
        elif name_tab == "Reddit":
            copy_salary = copy_salary - 50

if copy_salary <= 0:
    print("You have lost your salary.")
else:
    print(copy_salary)
