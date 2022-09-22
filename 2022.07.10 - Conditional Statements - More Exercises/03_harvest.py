import math

x_area = int(input())
y_grape = float(input())
z_wine_lt = int(input())
workers = int(input())

harvest_all = x_area * y_grape
wine_lt = harvest_all * 0.4 / 2.5
more = abs(wine_lt - z_wine_lt)

if wine_lt >= z_wine_lt:
    worker_wine = more / workers
    print(f"Good harvest this year! Total wine: {math.floor(wine_lt)} liters.")
    print(f"{math.ceil(more)} liters left -> {math.ceil(worker_wine)} liters per person.")
else:
    print(f"It will be a tough winter! More {math.floor(more)} liters wine needed.")

