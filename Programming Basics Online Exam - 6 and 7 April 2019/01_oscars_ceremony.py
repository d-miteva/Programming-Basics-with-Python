rent_auditorium = int(input())

statues = rent_auditorium * 0.7
kettering = statues * 0.85
sound = kettering * 0.5

total_price = rent_auditorium + statues + kettering + sound

print(f"{total_price:.2f}")
