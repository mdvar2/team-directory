import json

print("=== Team Directory ===")

with open("team.json", "r") as file:
    team_members = json.load(file)

print(f'Total team members: {len(team_members)}')

for member in team_members:
    print(f'{member["name"]} - {member["role"]}')

search_name = input("Enter a name to search: ")

for member in team_members:
    if member["name"].lower() == search_name.lower():
        print(f'Found: {member["name"]} - {member["role"]}')

role_search = input("Enter a role to search: ")

for member in team_members:
    if member["role"].lower() == role_search.lower():
        print(f'Found: {member["name"]} - {member["role"]}')