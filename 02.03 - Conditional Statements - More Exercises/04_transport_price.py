n_km = int(input())
day_night = input()

taxi_day = 0.79 * n_km + 0.7
taxi_night = 0.90 * n_km + 0.7
bus = 0.09 * n_km
train = 0.06 * n_km

if n_km < 20:

    if day_night == "day":
        print(f"{taxi_day:.2f}")
    else:
        print(f"{taxi_night:.2f}")

elif n_km < 100:
    print(f"{bus:.2f}")

else:
    print(f"{train:.2f}")


