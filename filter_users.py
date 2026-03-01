import json

def filter_users_by_name(name):
    # Datei öffnen
    with open("users.json", "r") as file:
        users = json.load(file)

    # Eine leere Liste für die Ergebnisse erstellen
    filtered_users = []

    # Jeden Nutzer einzeln prüfen (Standard-Schleife)
    for user in users:
        if user["name"].lower() == name.lower():
            filtered_users.append(user)

    # Ergebnisse ausgeben
    for user in filtered_users:
        print(user)


if __name__ == "__main__":
    filter_option = input("What would you like to filter by? (Currently, only 'name' is supported): ").strip().lower()

    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        filter_users_by_name(name_to_search)
    else:
        print("Filtering by that option is not yet supported.")