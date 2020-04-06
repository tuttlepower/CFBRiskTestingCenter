import college_football_risk as risk

team_api = risk.TeamsApi()
territory_api = risk.TerritoriesApi()
print(team_api.get_team_strength("Ohio State"))
#print(territory_api.get_territory_history("Ohio State",2))


