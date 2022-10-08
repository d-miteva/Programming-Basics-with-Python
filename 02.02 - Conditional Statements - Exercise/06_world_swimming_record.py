from math import floor

record_in_sec = float(input())
distance = float(input())
time_one_m = float(input())

total_time = distance * time_one_m
delay = floor(distance / 15) * 12.5
total_time = total_time + delay

if total_time < record_in_sec:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    diff = total_time - record_in_sec
    print(f"No, he failed! He was {diff:.2f} seconds slower.")
