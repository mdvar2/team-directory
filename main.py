import json

print("=== Team Directory ===")

with open("team.json", "r") as file:
    team_members = json.load(file)

for member in team_members:
    print(f'{member["name"]} - {member["role"]}')
