username = input()
password = input()
new_password = input()

while new_password != password:
    new_password = input()
else:
    print(f"Welcome {username}!")

# ------------
# username = input()
# user_password = input()
# data = input()
#
# while user_password != data:
#     data = input()
#
# print(f"Welcome {username}!")
