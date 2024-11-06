#
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("spotifydata.xlsx")

temp = df.artist_count.value_counts()
data = [temp.iloc[0], temp.iloc[1], temp.iloc[2], sum(temp.iloc[3:])]
labels = ['1', '2', '3', '3+']

plt.pie(data, labels=labels, autopct='%.0f%%')
plt.legend()
plt.title('Number of artist per chart')
plt.show()
