bequest = float(input())
wish_year = int(input())

even_year_money = 0
odd_year_money = 0
age = 17

for year in range(1800, wish_year + 1):
    age = age + 1
    if year % 2 == 0:
        even_year_money = even_year_money + 12000
    else:
        odd_year_money = odd_year_money + 12000 + (50 * age)

total_money = even_year_money + odd_year_money
diff = abs(total_money - bequest)

if bequest >= total_money:
    print(f"Yes! He will live a carefree life and will have {diff:.2f} dollars left.")
else:
    print(f"He will need {diff:.2f} dollars to survive.")
