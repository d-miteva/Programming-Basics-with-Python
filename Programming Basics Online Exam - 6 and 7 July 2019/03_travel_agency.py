city = input()
offer = input()
vip = input()
days = int(input())

if days > 0:
    if city == "Bansko" or city == "Borovets" or city == "Varna" or city == "Burgas":
        if offer == "noEquipment" or offer == "withEquipment" or offer == "noBreakfast" or offer == "withBreakfast":
            price = 0
            if city == "Bansko" or city == "Borovets":
                if offer == "noEquipment":
                    price = 80
                    if vip == "yes":
                        price *= 0.95
                else:
                    price = 100
                    if vip == "yes":
                        price *= 0.9
            if city == "Varna" or city == "Burgas":
                if offer == "noBreakfast":
                    price = 100
                    if vip == "yes":
                        price *= 0.93
                else:
                    price = 130
                    if vip == "yes":
                        price *= 0.88

            total_price = price * days
            if days > 7:
                total_price -= price

            print(f"The price is {total_price:.2f}lv! Have a nice time!")

        else:
            print("Invalid input!")

    else:
        print("Invalid input!")

else:
    print("Days must be positive number!")
