#Importing csv files as pandas dataframe.
from pandas import read_csv, DataFrame

data1 = read_csv("results.csv")
matches = DataFrame(data1)

def result(country):
	filtered = matches[matches['home_team'] == country]

	win = 0
	draw = 0
	lose = 0

	print(filtered.loc['home_score'])

#	for entry in filtered:
#		if matches['home_score'] > matches['away_score']:
#			win = win + 1
#		elif matches['home_score'] < matches['away_score']:
#			lose = lose + 1
#		else:
#			draw = draw + 1

result('Scotland')