v = int(input())
p1 = int(input())
p2 = int(input())
h = float(input())

p1_now = p1 * h
p2_now = p2 * h
v_now = p1_now + p2_now
percentage_v = v_now * 100 / v
percentage_p1 = p1_now * 100 / v_now
percentage_p2 = p2_now * 100 / v_now

if v_now <= v:
    print(f"The pool is {percentage_v:.2f}% full. Pipe 1: {percentage_p1:.2f}%. Pipe 2: {percentage_p2:.2f}%.")
else:
    more_water = v_now - v
    print(f"For {h:.2f} hours the pool overflows with {more_water:.2f} liters.")
