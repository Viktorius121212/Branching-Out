import json


def filter_users_by_name(name):
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["name"].lower() == name.lower()]

    for user in filtered_users:
        print(user)


# NEU: Die Funktion für das Alter
def filter_users_by_age(age):
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = []
    for user in users:
        # Hier vergleichen wir Zahlen (age ist ein Integer)
        if user["age"] == age:
            filtered_users.append(user)

    for user in filtered_users:
        print(user)


if __name__ == "__main__":
    # Menü angepasst auf Name und Alter
    filter_option = input("What would you like to filter by? (name/age): ").strip().lower()

    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        filter_users_by_name(name_to_search)
    elif filter_option == "age":
        age_to_search = int(input("Enter an age to filter users: "))
        filter_users_by_age(age_to_search)
    else:
        print("Filtering by that option is not yet supported.")