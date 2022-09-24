juniors_count = int(input())
seniors_count = int(input())
track = input()

juniors_price = 0
seniors_price = 0

if track == "trail":
    juniors_price = 5.5
    seniors_price = 7
elif track == "cross-country":
    juniors_price = 8
    seniors_price = 9.5
    if juniors_count + seniors_count >= 50:
        juniors_price = juniors_price * 0.75
        seniors_price = seniors_price * 0.75
elif track == "downhill":
    juniors_price = 12.25
    seniors_price = 13.75
elif track == "road":
    juniors_price = 20
    seniors_price = 21.5

total_sum = (juniors_price * juniors_count + seniors_count * seniors_price) * 0.95

print(f"{total_sum:.2f}")

