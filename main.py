import json

print("=== Team Directory ===")

with open("team.json", "r") as file:
    team_members = json.load(file)
