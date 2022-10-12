movie_count = int(input())

high_rating = 0
high_name = ""
low_rating = 11
low_name = ""
avg_rating = 0
total_rating = 0

for movie in range(1, movie_count + 1):
    movie_name = input()
    movie_rating = float(input())

    if high_rating < movie_rating:
        high_rating = movie_rating
        high_name = movie_name

    if low_rating > movie_rating:
        low_rating = movie_rating
        low_name = movie_name

    total_rating = total_rating + movie_rating

avg_rating = total_rating / movie_count

print(f"{high_name} is with highest rating: {high_rating}")
print(f"{low_name} is with lowest rating: {low_rating}")
print(f"Average rating: {avg_rating:.1f}")
