movie = input()
hall = input()
tickets = int(input())

if movie == "A Star Is Born":
    if hall == "normal":
        price = tickets * 7.5
    elif hall == "luxury":
        price = tickets * 10.5
    else:
        price = tickets * 13.5
elif movie == "Bohemian Rhapsody":
    if hall == "normal":
        price = tickets * 7.35
    elif hall == "luxury":
        price = tickets * 9.45
    else:
        price = tickets * 12.75
elif movie == "Green Book":
    if hall == "normal":
        price = tickets * 8.15
    elif hall == "luxury":
        price = tickets * 10.25
    else:
        price = tickets * 13.25
else:
    if hall == "normal":
        price = tickets * 8.75
    elif hall == "luxury":
        price = tickets * 11.55
    else:
        price = tickets * 13.95

print(f"{movie} -> {price:.2f} lv.")
