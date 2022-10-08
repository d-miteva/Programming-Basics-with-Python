period = int(input())

doctors = 7
total_treated = 0

total_untreated = 0
untreated = 0

for day in range(1, period + 1):
    patients_day = int(input())

    if day % 3 == 0 and total_treated < total_untreated:
        doctors = doctors + 1

    if doctors >= patients_day:
        total_treated = total_treated + patients_day
    else:
        untreated = patients_day - doctors
        total_untreated = total_untreated + untreated
        total_treated = total_treated + doctors

print(f"Treated patients: {total_treated}.")
print(f"Untreated patients: {total_untreated}.")
