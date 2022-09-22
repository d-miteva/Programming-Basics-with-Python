time_first = int(input())
time_second = int(input())
time_third = int(input())

total_sec_time = time_first + time_second + time_third

total_min = total_sec_time // 60
total_sec = total_sec_time % 60

if total_sec < 10:
    print(f"{total_min:}:0{total_sec:}")

else:
    print(f"{total_min:}:{total_sec:}")
