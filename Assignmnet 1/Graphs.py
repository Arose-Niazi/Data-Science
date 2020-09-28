# Import libraries
import pandas as pd
from matplotlib import pyplot as plt
from OlympicsCSV import Olympics
import numpy as np

olympics = Olympics(pd.read_csv('olympics.csv', delimiter=",", index_col=0, skiprows=1))
dataset = olympics.data.where(olympics.data['Gold.2'] > 10).dropna()

series = dataset.dropna().index
headers = series.values

series = dataset['Gold.2']
print(series.values)
data = series.values

# Wedge properties
wp = {'linewidth': 1, 'edgecolor': "green"}


# Creating autocpt arguments
def func(pct, allvalues):
    absolute = int(pct / 100. * np.sum(allvalues))
    return "{:.1f}%\n({:d} Gold Medals)".format(pct, absolute)

# Creating plot
fig, ax = plt.subplots(figsize=(17, 17))
wedges, texts, autotexts = ax.pie(data,
                                  autopct=lambda pct: func(pct, data),
                                  labels=headers,
                                  wedgeprops=wp,
                                  textprops=dict(color="black"))

# Adding legend
ax.legend(wedges, headers,
          title="Countries",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))

plt.setp(autotexts, size=8, weight="bold")
ax.set_title("Customizing pie chart")

# show plot
plt.show()