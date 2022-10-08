season = input()
group_type = input()
count_students = int(input())
count_nights = int(input())

price_night = 0
sport = ""

if group_type == "boys" or group_type == "girls":
    if season == "Winter":
        price_night = 9.6
    elif season == "Spring":
        price_night = 7.2
    elif season == "Summer":
        price_night = 15
elif group_type == "mixed":
    if season == "Winter":
        price_night = 10
    elif season == "Spring":
        price_night = 9.5
    elif season == "Summer":
        price_night = 20

price = price_night * count_students * count_nights

if count_students >= 50:
    price = price * 0.5
elif 20 <= count_students < 50:
    price = price * 0.85
elif 10 <= count_students < 20:
    price = price * 0.95

if group_type == "girls":
    if season == "Winter":
        sport = "Gymnastics"
    elif season == "Spring":
        sport = "Athletics"
    elif season == "Summer":
        sport = "Volleyball"
elif group_type == "boys":
    if season == "Winter":
        sport = "Judo"
    elif season == "Spring":
        sport = "Tennis"
    elif season == "Summer":
        sport = "Football"
elif group_type == "mixed":
    if season == "Winter":
        sport = "Ski"
    elif season == "Spring":
        sport = "Cycling"
    elif season == "Summer":
        sport = "Swimming"

print(f"{sport} {price:.2f} lv.")
