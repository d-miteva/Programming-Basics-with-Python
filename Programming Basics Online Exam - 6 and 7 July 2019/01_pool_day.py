from math import ceil

people = int(input())
tax_entry = float(input())
sunbed_price = float(input())
umbrella_price = float(input())

tax_entry_total = people * tax_entry
sunbed_price_total = ceil(people * 0.75) * sunbed_price
umbrella_price_total = ceil(people * 0.5) * umbrella_price
total_price = tax_entry_total + sunbed_price_total + umbrella_price_total

print(f"{total_price:.2f} lv.")
