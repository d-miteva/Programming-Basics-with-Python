mackerel_price = float(input())
sprat_price = float(input())
bonito_kg = float(input())
scad_kg = float(input())
mussel_kg = float(input())

bonito_price = mackerel_price * 1.6
scad_price = sprat_price * 1.8
mussel_price = 7.5

bonito_total_price = bonito_price * bonito_kg
scad_total_price = scad_price * scad_kg
mussel_total_price = mussel_price * mussel_kg

total_price = bonito_total_price + scad_total_price + mussel_total_price

print(f"{total_price:.2f}")