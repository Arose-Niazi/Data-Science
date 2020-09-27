import pandas as pd
from OlympicsCSV import Olympics

olympics = Olympics(pd.read_csv('olympics.csv', delimiter=",", index_col=0, skiprows=1))
print(str.center("Data loaded from file and formatted (Task 1)", 100, " "))
print(olympics.data,"\n")
print(str.center("Series of first object (Task 2)", 100, " "))
print(olympics.getFirstCountry(), "\n")
print("Most Summer Gold Medals (Task 3):", olympics.mostSummerGolds())
print("Most Summer to Winter Medals Difference (Task 4):", olympics.mostGoldDifference())
print("Most Summer to Winter Medals Difference, minimum 1 won and relative to total (Task 5):", olympics.mostRelativeGoldDifference())
print(str.center("Series of weighted points (Task 6)", 100, " "))
print(olympics.calculatePoints())