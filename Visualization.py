#Importing pandas and matplotlib packages
from pandas import read_csv, DataFrame
import matplotlib.pyplot as plt

data1 = read_csv("results.csv")
matches = DataFrame(data1)

#amending date column to just include the year
df_year = (matches['date'].str[:4])

# Plot the histogram
plt.hist(df_year, 30)

# Label the axes
plt.title('Matches played over time')
plt.xlabel('Year')
plt.ylabel('Number of matches')

# Show the figure
plt.show()


