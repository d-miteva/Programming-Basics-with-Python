relax_days = int(input())

work_days = 365 - relax_days

play_time = work_days * 63 + relax_days * 127

time = abs(play_time - 30000)
h = time // 60
m = time % 60

if play_time > 30000:
    print("Tom will run away")
    print(f"{h} hours and {m} minutes more for play")
else:
    print("Tom sleeps well")
    print(f"{h} hours and {m} minutes less for play")
