month = input()
count_nights = int(input())

studio = 0
apartment = 0

if month == "May" or month == "October":
    studio = 50
    apartment = 65
elif month == "June" or month == "September":
    studio = 75.2
    apartment = 68.7
elif month == "July" or month == "August":
    studio = 76
    apartment = 77

if 7 < count_nights <= 14 and (month == "May" or month == "October"):
    studio = studio * 0.95
elif count_nights > 14 and (month == "May" or month == "October"):
    studio = studio * 0.7

if count_nights > 14 and (month == "June" or month == "September"):
    studio = studio * 0.8

if count_nights > 14:
    apartment = apartment * 0.9

print(f"Apartment: {(apartment * count_nights):.2f} lv.")
print(f"Studio: {(studio * count_nights):.2f} lv.")
