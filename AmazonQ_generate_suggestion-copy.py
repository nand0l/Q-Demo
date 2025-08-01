# TODO: place your cursor at the end of line 5 and press Enter to generate a suggestion.
# Tip: press tab to accept the suggestion

fake_users = [{ "name": "User 1", "id": "user1", "city": "San Francisco", "state": "CA" },
              { "name": "User 2", "id": "user2", "city": "New York", "state": "NY" },
              { "name": "User 3", "id": "user3", "city": "Los Angeles", "state": "CA" },
              { "name": "User 4", "id": "user4", "city": "Chicago", "state": "IL" },
              { "name": "User 5", "id": "user5", "city": "Houston", "state": "TX" },
              { "name": "User 6", "id": "user6", "city": "Phoenix", "state": "AZ" },
              { "name": "User 7", "id": "user7", "city": "Philadelphia", "state": "PA" },
              { "name": "User 8", "id": "user8", "city": "San Antonio", "state": "TX" },
              { "name": "User 9", "id": "user9", "city": "San Diego", "state": "CA" },
              { "name": "User 10", "id": "user10", "city": "Dallas", "state": "TX" }]

def listnames(users):
    for user in users:
        print(user["name"])



# Call the function with fake_users list
listnames(fake_users)
def list_name_and_city(users):
    name_city_list = []
    for user in users:
        name_city_list.append((user["name"], user["city"]))
    return name_city_list

# Create the list
name_and_city = list_name_and_city(fake_users)

# Print the list
print(name_and_city)

# Or, if you want to print each pair on a separate line:
for name, city in name_and_city:
    print(f"Name: {name}, City: {city}")
