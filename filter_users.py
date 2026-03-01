import json


def filter_users_by_name(name):
    with open("users.json", "r") as file:
        users = json.load(file)
    filtered_users = [user for user in users if user["name"].lower() == name.lower()]
    for user in filtered_users:
        print(user)


def filter_users_by_age(age):
    with open("users.json", "r") as file:
        users = json.load(file)
    filtered_users = []
    for user in users:
        if user["age"] == age:
            filtered_users.append(user)
    for user in filtered_users:
        print(user)


# NEU: Filtern nach E-Mail
def filter_users_by_email(email):
    with open("users.json", "r") as file:
        users = json.load(file)
    filtered_users = []
    for user in users:
        if user["email"].lower() == email.lower():
            filtered_users.append(user)
    for user in filtered_users:
        print(user)


if __name__ == "__main__":
    option = input("Filter by (name/age/email): ").strip().lower()

    if option == "name":
        val = input("Enter name: ").strip()
        filter_users_by_name(val)
    elif option == "age":
        val = int(input("Enter age: "))
        filter_users_by_age(val)
    elif option == "email":
        val = input("Enter email: ").strip()
        filter_users_by_email(val)
    else:
        print("Option not supported.")
