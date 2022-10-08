chicken_menu_count = int(input())
fish_menu_count = int(input())
vegetable_menu_count = int(input())
price_chicken_menu = chicken_menu_count * 10.35
price_fish_menu = fish_menu_count * 12.4
price_vegetable_menu = vegetable_menu_count * 8.15
all_menu_price = price_vegetable_menu + price_fish_menu + price_chicken_menu
dessert = all_menu_price * 0.2
total_sum = all_menu_price + dessert + 2.5
print(total_sum)