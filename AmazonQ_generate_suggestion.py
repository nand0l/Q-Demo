# TODO: place your cursor at the end of line 5 and press Enter to generate a suggestion.
# Tip: press tab to accept the suggestion


fake_users = [
    { "name": "User 1", "id": "user1", "city": "San Francisco", "state": "CA" },
    { "name": "User 2", "id": "user2", "city": "Seattle", "state": "WA" },
    { "name": "User 3", "id": "user3", "city": "Portland", "state": "OR" },
    { "name": "User 4", "id": "user4", "city": "Los Angeles", "state": "CA" },
    { "name": "User 5", "id": "user5", "city": "Denver", "state": "CO" },
    { "name": "User 6", "id": "user6", "city": "Chicago", "state": "IL" },
    { "name": "User 7", "id": "user7", "city": "Boston", "state": "MA" },
    { "name": "User 8", "id": "user8", "city": "New York", "state": "NY" },
    { "name": "User 9", "id": "user9", "city": "Miami", "state": "FL" },
    { "name": "User 10", "id": "user10", "city": "Austin", "state": "TX" },
    { "name": "User 11", "id": "user11", "city": "Atlanta", "state": "GA" },
    { "name": "User 12", "id": "user12", "city": "San Diego", "state": "CA" },
    { "name": "User 13", "id": "user13", "city": "San Jose", "state": "CA" },
    { "name": "User 14", "id": "user14", "city": "Phoenix", "state": "AZ" }]




def listnames(users):
    for user in users:
        print(user["name"])



# Add this to make sure the function is called when the script is run
if __name__ == "__main__":
    listnames(fake_users)