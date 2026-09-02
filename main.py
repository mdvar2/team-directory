import json

print("=== Team Directory ===")

with open("team.json", "r") as file:
    team_members = json.load(file)

for member in team_members:
    print(f'{member["name"]} - {member["role"]}')

search_name = input("Enter a name to search: ")
