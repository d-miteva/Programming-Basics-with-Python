w_m = float(input())
h_m = float(input())

w_cm = w_m * 100
h_cm = (h_m * 100) - 100

offices_h = h_cm // 70
offices_w = w_cm // 120

offices_count = (offices_w * offices_h) - 3

print(int(offices_count))


