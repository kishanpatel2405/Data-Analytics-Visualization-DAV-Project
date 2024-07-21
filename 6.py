#songs per years in pie chart
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("spotifydata.xlsx")

filtered_df = df[(df['released_year'] >= 2010) & (df['released_year'] <= 2023)]

years_counts = filtered_df['released_year'].value_counts()

plt.figure(figsize=(8, 8))
plt.pie(years_counts, labels=years_counts.index, autopct='%1.1f%%')
plt.title('Distribution of Years (2010-2023)')
plt.axis('equal')
plt.show()
