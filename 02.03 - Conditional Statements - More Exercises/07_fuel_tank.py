fuel = input()
fuel_lt = float(input())

if fuel in ['Diesel', 'Gasoline', 'Gas']:

    if fuel_lt >= 25:
        print(f"You have enough {fuel.lower()}.")

    else:
        print(f"Fill your tank with {fuel.lower()}!")

else:
    print("Invalid fuel!")
