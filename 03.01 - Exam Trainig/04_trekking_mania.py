number_claiming_club = int(input())

musala = 0
monblan = 0
kilimanjaro = 0
k2 = 0
everest = 0

for group in range(number_claiming_club):
    people_in_group = int(input())

    if people_in_group <= 5:
        musala = musala + people_in_group
    elif people_in_group <= 12:
        monblan = monblan + people_in_group
    elif people_in_group <= 25:
        kilimanjaro = kilimanjaro + people_in_group
    elif people_in_group <= 40:
        k2 = k2 + people_in_group
    elif people_in_group >= 41:
        everest = everest + people_in_group

total_people = musala + monblan + kilimanjaro + k2 + everest

precent_musala = musala / total_people * 100
precent_monblan = monblan / total_people * 100
precent_kilimanjaro = kilimanjaro / total_people * 100
precent_k2 = k2 / total_people * 100
precent_everest = everest / total_people * 100

print(f"{precent_musala:.2f}")
print(f"{precent_monblan:.2f}")
print(f"{precent_kilimanjaro:.2f}")
print(f"{precent_k2:.2f}")
print(f"{precent_everest:.2f}")
