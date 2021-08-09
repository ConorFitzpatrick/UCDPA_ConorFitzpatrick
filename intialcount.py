#Importing csv files as pandas dataframes. Print can be un-commented to display raw data
from pandas import read_csv, DataFrame

data1 = read_csv("results.csv")
matches = DataFrame(data1)
#print(matches.head)

data2 = read_csv("shootouts.csv")
shootouts = DataFrame(data2)
#print(shootouts.head)

#Initialize dictionary to count total international games played
game_count = {}

games_home = matches['home_team']
games_away = matches['away_team']

for entry in games_home:
	if entry in game_count.keys():
		game_count[entry] = game_count[entry] + 1
	else:
		game_count[entry] = 1

for entry in games_away:
	if entry in game_count.keys():
		game_count[entry] = game_count[entry] + 1
	else:
		game_count[entry] = 1

sort_game_count = sorted(game_count.items(), key=lambda x: x[1], reverse=True)

for i in sort_game_count:
	print(i[0], i[1])
