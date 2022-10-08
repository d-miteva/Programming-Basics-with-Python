chrysanthemum = int(input())
rose = int(input())
tulip = int(input())
season = input()
holiday = input()

chrysanthemum_price = 0
rose_price = 0
tulip_price = 0
total = 0

if season == "Spring" or season == "Summer":
    chrysanthemum_price = 2
    rose_price = 4.1
    tulip_price = 2.5

elif season == "Autumn" or season == "Winter":
    chrysanthemum_price = 3.75
    rose_price = 4.5
    tulip_price = 4.15

if holiday == "Y":
    chrysanthemum_price = chrysanthemum_price * 1.15
    rose_price = rose_price * 1.15
    tulip_price = tulip_price * 1.15

total = chrysanthemum * chrysanthemum_price + rose_price * rose + tulip_price * tulip

if season == "Spring" and tulip > 7:
    total = total * 0.95

if season == "Winter" and rose >= 10:
    total = total * 0.9

if chrysanthemum + rose + tulip > 20:
    total = total * 0.8

print(f"{(total + 2):.2f}")
